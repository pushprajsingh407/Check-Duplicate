import json
import requests

response = requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")
print(response)
data=json.loads(response.text)


                                #FOR PRINTING IN HUMAN READABLE FORMAT        

i=0   #FOR ACCESSING LIST ELEMENTS
for paid in data['paid']:
    print('{}. Conference on topic : "{}" will start from {} till {} at {}, {}, {}, {}. Entry will be {} '.\
        format(i+1, data['paid'][i]['confName'],data['paid'][i]['confStartDate'],data['paid'][i]['confEndDate'],\
            data['paid'][i]['venue'],data['paid'][i]['city'],data['paid'][i]['state'],data['paid'][i]['country'],\
                data['paid'][i]['entryType']))   
    i+=1
    
i=0
for free in data['free']:
    print('{}. Conference on topic : "{}" will start from {} till {} at {}, {}, {}, {}. Entry will be {} '.\
        format(i+1,data['free'][i]['confName'],data['free'][i]['confStartDate'],data['free'][i]['confEndDate'],\
            data['free'][i]['venue'],data['free'][i]['city'],data['free'][i]['state'],data['free'][i]['country'],\
                data['free'][i]['entryType']))   
    i+=1
'''    

#                FOR DUPLICATES
#CONDITIONS FOR DUPLICACY:
#1 exact duplicates
#2 if have same conference_id
#3 if same name and same (venue longitude latitude start end date)



def duplicate(dct,i):
    flag=0
    exactduplicateentry=[]
    j=i+1
    for element in dct:
        for key in dct:
            try:
                if data['paid'][i][key] == data['paid'][j][key]:
                    if key=='conference_id':
                        print('conference id same here')
                    j+=1
                    count+=1
                else :
                    j+=1
                    flag=1
                    print('now broke')
                    break
            except:
                break 
   
        if flag == 0:
            exactduplicateentry.append(j)
        elif flag == 1:
            flag=0
    
    return exactduplicateentry
   
i=0
exactduplicateentry=[]
for item in data['paid']:
    exactduplicateentry.append(duplicate(data['paid'][i],i))
    i+=1

if len(exactduplicateentry)>0:
    print("Duplicate of entries at {}".format(exactduplicateentry))
else:
    print("No exact duplicates")

'''