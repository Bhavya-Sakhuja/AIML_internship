import seaborn as sns 
import matplotlib.pyplot as plt

tip = sns.load_dataset('tips')

# print(tip.head())

# lineplot 

# sns.lineplot(
#     data=tip,
#     x = "time",
#     y = "sex"
# )

# histogram 

# sns.histplot(
#     data=tip,
#     x = "size"
# ) 

# bar chart 

# sns.barplot(
#     data=tip,
#     x = "day",
#     y = "time"
# )

# pair plot

# sns.pairplot(
#     data=tip
# )

# box plot 

# avg -- max -- min 

# sns.boxplot(
#     data=tip,
#     x = "size",
#     y = "tip"
# )

# count plot 

# sns.countplot(
#     data=tip,
#     x = "time"
# )

# sns.countplot(
#     tip['time']
# )

# matplotlib

size = [10,20,40,20,10]

plt.pie(
    x = size,
    labels=['A','B','C','D','E']
)

plt.show()

# heatmaps
