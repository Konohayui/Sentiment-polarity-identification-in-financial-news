import requests, time
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, sent_tokenize

tk = RegexpTokenizer(r'\w+')
nltk.download('stopwords')
stop = stopwords.words('english')

def get_reuters_news(ticker, date_range = "pastWeek"):
    # date_range can be: pastDay, pastWeek, pastMonth, and pastYear
    print(f"Search {ticker}'s {date_range} news")
    with requests.Session() as s:
        r = s.get(f'https://www.reuters.com/search/news?sortBy=date&dateRange={date_range}&blob={ticker}')
        soup = BeautifulSoup(r.content, 'lxml')
        num_results = soup.select_one('.search-result-count-num').text
        r = s.get(f'https://www.reuters.com/assets/searchArticleLoadMoreJson?blob={ticker}&bigOrSmall=big&articleWithBlog=true&sortBy=relevance&dateRange={date_range}&numResultsToShow={num_results}&pn=&callback=addMoreNewsResults')
        p = re.compile(r'id: "(.*?)"')
        p2 = re.compile(r'headline: "(.*?)"')
        links = [f'https://www.reuters.com/article/id{i}' for i in p.findall(r.text)]
        headlines = [BeautifulSoup(i, 'lxml').get_text() for i in p2.findall(r.text)]
    
    articles = []    
    cleaned_articles = []
    for link in links:
        paragraphs = ""
        scraped_data = urllib.request.urlopen(link)
        scraped_data = scraped_data.read()
        parsed_article = BeautifulSoup(scraped_data, 'lxml')
        article = parsed_article.find_all("p")
        
        for paragraph in article:
            paragraphs +=  paragraph.text + " "

        articles.append(paragraphs)
        paragraph_sents = sent_tokenize(paragraphs)
        sents = []
        
        for ps in paragraph_sents:
            ps = re.sub(r"\s+", " ", ps) # remove \n and \t
            ps = re.sub(r"[^\w\s]", "", ps) # remove punctuations
            ps = re.sub(r"[0-9]+", "", ps) # remove numbers
            ps = " ".join([word for word in tk.tokenize(ps.lower()) if word not in (stop)]) # remove stop words
            sents.append(ps)
            
        cleaned_articles.append(" ".join(sents))
        
    return headlines, articles, cleaned_articles
  
  
  
