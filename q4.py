import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
b=open("q4.json","w")
c=(sorted,a)
json.dump(c,b,indent=4)
