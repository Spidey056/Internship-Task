txt = input("Enter the text to be inserted:")

f = open("output.txt","a")

f.write(txt)

print("The text is successfully inserted.")

f.close()


