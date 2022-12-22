# Sentiment-polarity-identification-in-financial-news

The main file has following funtions
  * reuters news scrapper
    - date range: day, week, month, year
  * nltk news sentiment analyzer
    ```
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    ```
  * Quant Figures  
    - sma
    - ema


to do list:
 * add polarity analysis
 * apply wavelet to find hidden pattern
 * apply spline for smoothing
 * more news sources
