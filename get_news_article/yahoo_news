import requests, time
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, sent_tokenize

tk = RegexpTokenizer(r'\w+')
nltk.download('stopwords')
stop = stopwords.words('english')

def scrape_yahoo_news(url):
    scraped_data = requests.get(url).content
    parsed_article = BeautifulSoup(scraped_data)

    article_text = ""
    article = parsed_article.find_all("p")
    
    paragraphs = ""
    for paragraph in article:
            paragraphs +=  paragraph.text + " "
            
    paragraph_sents = sent_tokenize(paragraphs)
    sents = []
        
    for ps in paragraph_sents:
        ps = re.sub(r"\s+", " ", ps) # remove \n and \t
        ps = re.sub(r"[^\w\s]", "", ps) # remove punctuations
        ps = re.sub(r"[0-9]+", "", ps) # remove numbers
        ps = " ".join([word for word in tk.tokenize(ps.lower()) if word not in (stop)]) # remove stop words
        sents.append(ps)
            
    return sents
    
    
    
    
