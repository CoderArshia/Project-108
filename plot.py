import random
import csv
import plotly.express as px
import plotly.figure_factory as ff 

average_result=[]
count=[]
for i in range(0,100):
    average1=random.randint(1,6)
    average2=random.randint(1,6)
    average_result.append(average1+average2)
    count.append(i)
    print(average1,average2)
print(average_result)

fig=ff.create_distplot([average_result],["Result"])
fig.show()