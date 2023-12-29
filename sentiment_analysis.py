from db import getNews2
from db import updateNews


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
                        

from datetime import datetime

def calcuateWeights():

    from datetime import datetime
    from datetime import timedelta

    current_timestamp = datetime.now()
    time=[]
    n=len(data)
    cumulatedWeight=0
    for i in data:
        time.append(i[1])
    # x=(max(time) - min(time)) / (n*2) #requires data to be in ascending order of time
    for i in range(n):
        # multiplier=multiplier + x 
        time_difference = current_timestamp - data[i][1]
        seconds_difference = time_difference.total_seconds()
        multiplier = 100 / (seconds_difference)
        weight = probability[i] * multiplier
        cumulatedWeight = cumulatedWeight + weight
        finalAns[i].append(weight) #appended at 6th index

    print(finalAns)
    print(cumulatedWeight)

    # print("go through all news in for loop for a duration")
    # print("Older the news, lesser is its weight")
    # print("formula - probability/(timenow-datetime)" )
    # print("persist the value of weight back in the table")


def calculateWeightedSentiment(weights):

    #done above and in predict()

    print("calculating wtd average sentiment, that's to be shown to the user")
    print("weights is a list of [weight,sentiment] for an entity")    
    print("iterate over weights - sum(weighted.probabilities)")
    print("POSITVE sentiments are added, NEGATIVE sentiments are subtracted, NEUTRAL are ignored ")
   
    

probability=[]
finalAns=data

def predict(Inputdata,data):

    import transformers
    transformers.logging.CRITICAL
    from transformers import pipeline

    sentiment_pipeline = pipeline(model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis", verbose=False)
    sentiment=(sentiment_pipeline(Inputdata))

    ans=[]
    for i in sentiment:
        ans.append(i['label'])
        if (i['label']=='positive'): probability.append(i['score'])
        elif (i['label']=='negative'): probability.append(i['score']* (-1))
        else: probability.append(0)
    for i in range(len(ans)):
        finalAns[i].append(ans[i]) #appended at 4th index
        finalAns[i].append(probability[i]) #appended at 5th index
        updateNews(finalAns[i][0], finalAns[i][4])
    
    #print(finalAns)
    #print(sentiment)



#print ('\n','\n','\n','\n',"CHECKING FOR NUMERIC VALUES",'\n')
#numericCheck(data)
#print ('\n','\n','\n','\n',"PREDICTING SENTIMENT",'\n')
predict(Inputdata,data)
calcuateWeights()
#print(predict(data))
        

