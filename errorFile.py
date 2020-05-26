
# code to handle IOError
try:
    myfile = open("errorFile.txt", "w+")
    myfile.write("Hello World")
except IOError:
    print("Error occurred: cannot access file")
else:
    print("Data has been written to file")
    myfile.close()