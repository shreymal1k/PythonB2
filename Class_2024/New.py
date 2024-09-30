file=open("example.txt","w")

file.write("Hello,this is a test.")

fileContent=file.writelines(dataString)

file.close()


filename="example.yxy"

file=open(filename,"r+")

dataString="SOme \n dummy files"
# write a program to read a csv file and store the data as a 2d list 