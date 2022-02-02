#Dictionary:collection of key values
#dictionary methods:1.items() 2.keys() 3.update()
oxford = {
    "gift": "something willngly given to someone",
    "this": "a keyword in c++",
    "Youtube": "a video sharing platform",
    "instagram": "picture sharing platform",
    "myList": [1,2,4],
    "gift": "hi"
    
}
print(oxford)
print(oxford["this"])

#items():
#print(oxford.items())
for a, b in oxford.items(): #a contain key, b contain value
    print("\n\t", a, ":" ,b)

#keys():
for key in oxford.keys():
    print(key)


#update():
oxford.update({"Ritika":"good girl", "myList":[6, 8]})
print(oxford)

#get():
print(oxford.get("notpresent"))