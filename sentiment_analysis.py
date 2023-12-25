import transformers
transformers.logging.CRITICAL
from transformers import pipeline

#checking

data = ["tata motors hits 52 week high", 
        "tata motors stocks rise  causing losses to short traders", 
        " i went to watch a movie after making a MILLION in the stock market"]

def numericCheck(data):
    
    for i in range(len(data)):
        flag=False
        L=data[i].split()
        for j in L:
            j=j.lower()
            if (j=="crore" or j=="million" or j=="lakh" or j=="billion" or j.isnumeric()):
                flag=True
                break
        if(flag):
            print ((i+1) , ":" ,  "Numeric value detected")
        else:
            print ((i+1) , ":" ,  "No numeric value detected")    
                        

def predict(data):
    sentiment_pipeline = pipeline(model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis", verbose=False)
    ans=(sentiment_pipeline(data))
    print(ans)


print ('\n','\n','\n','\n',"CHECKING FOR NUMERIC VALUES",'\n')
numericCheck(data)
print ('\n','\n','\n','\n',"PREDICTING SENTIMENT",'\n')


