import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

from tenacity import _first_set

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)

print("The Mean of sampling distribution : ",mean)
print("standard Deviation of sampling distribution : ",std)

first_stdev_start,first_stdev_end=mean-std,mean+std
second_stdev_start,second_stdev_end=mean-(2*std),mean+(2*std)
third_stdev_start,third_stdev_end=mean-(3*std),mean+(3*std)

df=pd.read_csv("school1.csv")
data=df["Math_score"].tolist()
mean_of_sample1=statistics.mean(data)
print("mean of sample1: ",mean_of_sample1)
fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="Std dev 1 end "))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="Std dev 2 end "))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="Std dev 3 end "))
fig.show()