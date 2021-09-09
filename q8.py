import json
d=["neelam","programer","24","2400",]
e=["komal","trainer","24","20000"]
f=["anuradha","HR","25","40000"]
g=["Abhishek","nager","29","63000"] 
h=["name","designation","age","salary"]
a={}
b={}
c={}
p={}
k={"emp1":a,"emp2":b,"emp3":c,"emp4":p}
for i in range(len(d)):
    a.update({h[i]:d[i]})
for i in range (len(e)):
    b.update({h[i]:e[i]})
for i in range(len(f)):
    c.update({h[i]:f[i]})
for i in range(len(g)):
    p.update({h[i]:g[i]})
    t=open("manisha.json","w")
    json.dump(k,t,indent=3)



