
# f = open(r'C:\Users\Bhavya\Downloads\Global Ai - Phase - 2\firebase.json','r')

# mode --> r , w , a , w+

# list1 = ['hellloo guysss','Hello Everyone']
f = open('demo.txt','a')
# content = f.read()

# print(content)

# content = f.readline()

# print(content)

# [1line, 2line ]

# content = f.readlines()

# for lines in content:
#     print(lines)

# content = f.read(5)
# print(content)

# f.writelines(list1)

# f.write("Bhavya Sakhuja")

# f.close()

# exception handling 

try:
   with open('demo.txt','r') as f:
      content = f.read()
      print(content)
except FileNotFoundError:
   print("File doesn't exist")
finally:
   print("program executed successfully!!")
   
