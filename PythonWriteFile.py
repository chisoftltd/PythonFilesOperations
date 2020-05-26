# Write to an Existing File
import os

f = open("demofile2.txt", "a")
f.write("Now the file has more content! TXT files are useful for storing information in plain text with no special formatting beyond basic fonts and font styles.")
f.close()

myfile = open("Tutorial2.txt", "w")

myfile.write("Python Programming Tutorials \n")
myfile.write("Coding Challenge \n")
myfile.write("Java Programming Tutorial")


myfile.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content! The file is commonly used for recording notes, directions, and other similar documents that do not need to appear a certain way. If you are looking to create a document with more formatting capabilities, such as a report, newsletter, or resume, you should look to the .DOCX file, which is used by the popular Microsoft Word program.")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

# Create a New File

if os.path.exists("myfile5.txt") or os.path.exists("myfile4.txt"):
    os.remove("myfile4.txt")
    os.remove("myfile5.txt")
else:
  print("The file does not exist")


f = open("myfile4.txt", "x")
f = open("myfile5.txt", "w")
