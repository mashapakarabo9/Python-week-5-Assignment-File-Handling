
file = open('my_file.txt',"w")
file.writelines(["My name is karabo","07353278784","I a developer"])
file.close()

file=open("my_file.txt",'r') #Open file in Read mode
file_str= file.read() #Read file content
print(file_str) #Print file content 
file.close()

file = open("my_file.txt","a") # Open file in appending mode
file.writelines(["Kenya","South Africa","Nigeria"]) #appending three lines to the file
file.close()

#Error handling

try:
    file = open("my_file.txt","r+")

except FileNotFoundError :
    print("file name not found ")
except PermissionError:
    print("File access denied")

finally:
    file.close()


