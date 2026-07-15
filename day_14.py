import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]

# # color , linewidth , line design , pointer
# plt.plot(x,y,color="red",marker="o",linestyle="--",linewidth=2)
# # title , xlabel , ylabel , grid

# plt.title("Demo Graph")

# plt.xlabel("X Axis")

# plt.ylabel("Y Axis")

# plt.grid()

# students = ['Ram','Sham',"Kirat"]

Marks = [50,55,52,89,74,90,98,55,52,53]

plt.hist(Marks,bins=3)

# plt.barh(students,Marks)

# scatter plot 

# age = [23,54,65,32,11]
# salary = [10000,34000,45000,22000,18000]

# plt.scatter(age,salary)

# pie chart 

sizes = [30,40,20,10]

labels = ['A','B','C','D']

plt.pie(
    sizes,
    labels = labels,
    autopct='%1.1f%%'
)

plt.savefig("graph.png")
plt.show()

