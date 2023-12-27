import transformers
transformers.logging.CRITICAL
from transformers import pipeline

from db import getNews2
from db import updateNews

'''
data = ["tata motors hits 52 week high", 
       "tata motors stocks rise  causing losses to short traders", 
       " i went to watch a movie after making a MILLION in the stock market"]
'''


Inputdata,data = getNews2()

def numericCheck(Inputdata):
    
    for i in range(len(Inputdata)):
        flag=False
        L=Inputdata[i].split()
        for j in L:
            j=j.lower()
            if (j=="crore" or j=="million" or j=="lakh" or j=="billion" or j.isnumeric()):
                flag=True
                break
        if(flag):
            print ((i+1) , ":" ,  "Numeric value detected")
        else:
            print ((i+1) , ":" ,  "No numeric value detected")    
                        

def predict(Inputdata,data):
    sentiment_pipeline = pipeline(model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis", verbose=False)
    sentiment=(sentiment_pipeline(Inputdata))

    ans=[]
    for i in sentiment:
        ans.append(i['label'])

    finalAns=data
    for i in range(len(ans)):
        finalAns[i].append(ans[i])
        updateNews(finalAns[i][0], finalAns[i][2])
    
    #print(finalAns)




#print ('\n','\n','\n','\n',"CHECKING FOR NUMERIC VALUES",'\n')
#numericCheck(data)
#print ('\n','\n','\n','\n',"PREDICTING SENTIMENT",'\n')
predict(Inputdata,data)
#print(predict(data))
