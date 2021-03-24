#"a" append to the end of file
f=open("file handling/append_a.txt","a")
f.write("appending the new text to the file")
print(f.read)
f.close()

#to read this
f=open("file handling/append_a.txt","r")
print(f.read())
f.close()


#"w" to overwrite the existing content
f=open("file handling/overwrite_w.txt","w")
f.write("the content has been overwritten")
f.close()

#to read this
f=open("file handling/overwrite_w.txt","r")
print(f.read())
f.close()
#the content has been overwritten

#create a new file
f=open("file handling/mycreate.txt","x")
print("file created")
f.close()
