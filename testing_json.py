import json
import pprint

with open("name_score.json", "r") as json_file:
    data = json.load(json_file)

#if data["users"]["username"]=="player1":
#print(data["users"][0])

#for x in data["users"]:
    #if x["username"]=="player1":
        #print(x["high_score"])
#first = {
    #"username": "player1",
    #"high_score": 0
    #}
#second = {
    #"username": "player2",
    #"high_score": 0
    #}
#third = {
    #"username": "player3",
    #"high_score": 0
    #}


#for x in data["users"]:
    #if x["high_score"] > first["high_score"]:
        #third = second.copy()
        #second = first.copy()
        #first = x
    #elif x["high_score"] > second["high_score"]:
        #third = second.copy()
        #second = x
    #elif x["high_score"] > third["high_score"]:
        #third = x
#positions = [first,second,third]


#for x in positions:
    #print("1.", x["username"],"   ", x["high_score"])

print(len(data))


