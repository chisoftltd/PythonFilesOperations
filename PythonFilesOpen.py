# Open a File on the Server

myfile = f = open("demofile.txt", "r")
print(f.read())

# Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(25))

# Read Lines
f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()

print("Name of file: " + myfile.name)
print("Is it closed: " + str(myfile.closed))
print("The file mode: " + myfile.mode)
