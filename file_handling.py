with open("file.txt","at") as file:
    text = input("enter the text to the file:")
    file.write(f"{text}\n")
    print("the data enterd into file succesfully")

with open("file.txt","r+") as file:
      data=file.read()
      print(file.read())


