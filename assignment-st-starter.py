# import packages
# show the title
# read csv and show the dataframe
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('train.csv')
st.write(df)

sns.set()
st.title('Titanic App by Tingyu Fu')

fig, ax = plt.subplots(1, 3, figsize=[15, 5])

df_sorted1 = df[df.Pclass == 1]
df_sorted2 = df[df.Pclass == 2]
df_sorted3 = df[df.Pclass == 3]

ax[0].boxplot(df_sorted1.Fare)
ax[0].set_xlabel('paclass=1')
ax[0].set_xticks([1])
ax[0].set_xticklabels(['Fare'])
ax[0].set_ylim(0, 500)  

ax[1].boxplot(df_sorted2.Fare)
ax[1].set_xlabel('paclass=2')
ax[1].set_xticks([1])
ax[1].set_xticklabels(['Fare'])
ax[1].set_ylim(0, 70) 

ax[2].boxplot(df_sorted3.Fare)
ax[2].set_xlabel('paclass=3')
ax[2].set_xticks([1])
ax[2].set_xticklabels(['Fare'])
ax[2].set_ylim(0, 70) 

ax[0].set_ylabel('Fare')
plt.tight_layout()
plt.show()

