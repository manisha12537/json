import json 
a= {"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
q=open("q1.json","w")
json.dump(a,q,indent=3)
