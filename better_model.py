import transformers
transformers.logging.CRITICAL
from transformers import pipeline


data = ["tata motors hits 52 week high", 
       "tata motors stocks rise  causing losses to short traders", 
       " i went to watch a movie after making a MILLION in the stock market"]


sentiment_pipeline = pipeline(model="RashidNLP/Finance-Sentiment-Classification", verbose=False)
ans=(sentiment_pipeline(data))
print(ans)