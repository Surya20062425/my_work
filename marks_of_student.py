data ={"shiva":44,"ram":100,"sita":1000,"laxman":500,"ravan":0}
name =input("Enter your name:")\

if name in data:
    print(f"Your name is :{name} your marks: {data[name]}")