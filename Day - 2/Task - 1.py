f = open("input.txt", "r")
content = f.read();
content = content.capitalize()
f.close()

f = open("output.txt","w")
f.write(content)
if f:
    print("The existing file is written successfully")
f.close()