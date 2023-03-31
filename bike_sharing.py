import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
st.set_page_config(layout = 'centered',page_title='first app')

st.title('Bike Sharing EDA')
df = pd.read_csv('./newrResultBikeSharing')
st.dataframe(df.head())

option = st.selectbox("Select an option: ",["year","month","weekday"])
if option == 'year':
    st.text("Count of bikes during years")
    fig=px.bar(df,x='year' , y='count')
    st.plotly_chart(fig)
elif option == 'B':
    st.text("Count of bikes during months")
    fig=px.bar(df,x='month' , y='count')
    st.plotly_chart(fig)
elif option == 'weekday':
    st.text("Count of bikes during days")
    fig=px.bar(df,x='weekday' , y='count')
    st.plotly_chart(fig)

st.title("Count of bikes during: ")
radio = st.radio("Select An Option",["year", "season"])
if radio == 'year':
    st.text("Count of bikes during years")
    fig=px.pie(data_frame=df,
      names=df.groupby('year').sum()['count'].index,
     values=df.groupby('year').sum()['count'].values,
      hole=0.3)
    st.plotly_chart(fig)
elif radio == 'season':
    st.text("Count of bikes during seasons")
    fig=px.pie(data_frame=df,
      names=df.groupby('season').sum()['count'].index,
     values=df.groupby('season').sum()['count'].values,
      hole=0.5)
    st.plotly_chart(fig)

st.title("Histogram for numerical data")
option2 = st.selectbox("Select an option for your histogram: ",["temp","atemp","humidity","windspeed"])
if option2 == 'temp':
    st.text("Histogram for temp")
    fig=px.histogram(df['temp'])
    st.plotly_chart(fig)
elif option2 == 'atemp':
    st.text("Histogram for atemp")
    fig=px.histogram(df['atemp'])
    st.plotly_chart(fig)
elif option2 == 'humidity':
    st.text("Histogram for humidity")
    fig=px.histogram(df['humidity'])
    st.plotly_chart(fig)
elif option2 == 'windspeed':
    st.text("Histogram for windspeed")
    fig=px.histogram(df['windspeed'])
    st.plotly_chart(fig)

st.title("corelation between each features")
fig2=plt.figure(figsize=(20,20))
sns.heatmap(df.corr('pearson'),vmin=-1,vmax=1,cmap='coolwarm',annot=True,square=True)
st.pyplot(fig2)

st.title("boxplot between count & each categorical features")
option3 = st.selectbox("Select an option to show a boxplot between count & each categorical features: ",["season","holiday","workingday","weather"])
if option3 == 'season':
    st.text("Boxplot between count & season")
    fig=plt.figure()
    sns.boxplot(data=df,x='season',y='count')
    # fig.set(xlabel='season',ylabel='count')
    st.pyplot(fig)
elif option3 == 'holiday':
    st.text("Boxplot between count & holiday")
    fig=plt.figure()
    sns.boxplot(data=df,x='holiday',y='count')
    # fig.set(xlabel='holiday',ylabel='count')
    st.pyplot(fig)
elif option3 == 'workingday':
    st.text("Boxplot between count & working day")
    fig=plt.figure()
    sns.boxplot(data=df,x='workingday',y='count')
    # fig.set(xlabel='workingday',ylabel='count')
    st.pyplot(fig)
elif option3 == 'weather':
    st.text("Boxplot between count & weather")
    fig=plt.figure()
    sns.boxplot(data=df,x='weather',y='count')
    # fig.set(xlabel='weather',ylabel='count')
    st.pyplot(fig)

fields =[f for f in df]
fields = fields[5:-3]
st.title("Scatter plot between count & each numeric features")
st.text(fields[4:])
fig = plt.figure(figsize=(17,3))

for i,f in enumerate(fields[4:]):
    ax=fig.add_subplot(1,4,i+1)
    ax.scatter(df[f],df['count'])
    ax.set_ylabel('count')
    ax.set_xlabel(f)
st.pyplot(fig)

st.title("Histogram of count before editing")
st.text("from the graph it is shown that the count data is skewed at the left side. the density of values is more between 0 and 200.")
fig4 = plt.figure(figsize=(17,3))
sns.set_style('darkgrid')
sns.distplot(hour['cnt'],bins=100,color='purple')
st.pyplot(fig4)

st.title("Histogram of count after editing")
fig5 = plt.figure(figsize=(17,3))
sns.set_style('darkgrid')
sns.distplot(df['count'],bins=100,color='purple')
st.pyplot(fig5)

st.title('Exploratory Data Analysis')

st.title('Count of bikes during weekdays and weekends')
fig6, ax = plt.subplots(figsize=(20,10))
sns.pointplot(data=hour,x='hr',y='cnt',hue='weekday',ax=ax)
ax.set(title='Count of bikes during weekdays and weekends')
st.pyplot(fig6)

st.title('Count of bikes during weekdays and weekends: unregistered users')
fig7, ax = plt.subplots(figsize=(20,10))
sns.pointplot(data=hour,x='hr',y='casual',hue='weekday',ax=ax)
ax.set(title='Count of bikes during weekdays and weekends: unregistered users')
st.pyplot(fig7)

st.title('Count of bikes during weekdays and weekends: registered users')
fig8, ax = plt.subplots(figsize=(20,10))
sns.pointplot(data=hour,x='hr',y='registered',hue='weekday',ax=ax)
ax.set(title='Count of bikes during weekdays and weekends: registered users')
st.pyplot(fig8)

st.title('Count of bikes during weather')
fig9, ax = plt.subplots(figsize=(20,10))
sns.pointplot(data=hour,x='hr',y='cnt',hue='weathersit',ax=ax)
ax.set(title='Count of bikes during weather')
st.pyplot(fig9)
st.text("=> so here we have 4 different typs of weather at 4:00 pm and 6:00 pm \n=> we have less numbers of users that are most likely in heavy rain weather \n-> green graph is most likely for cloudy or shower rain")

fig11, ax = plt.subplots(figsize=(20,10))
st.title('Count of bikes during seasons')
sns.pointplot(data=hour,x='hr',y='cnt',hue='season',ax=ax)
ax.set(title='Count of bikes during seasons')
st.pyplot(fig11)
st.text('we have here 4 numbers of seasons only one of them is lower at bike counts  \n "blue graph" => might be winter')

fig12,(ax1,ax2)=plt.subplots(ncols=2,figsize=(20,6))
sns.regplot(x=hour['temp'],y=hour['cnt'],ax=ax1)
ax1.set(title='Relation between temp and users')
sns.regplot(x=hour['hum'],y=hour['cnt'],ax=ax2)
ax1.set(title='Relation between humidity and users')
st.pyplot(fig12)
st.text('when humidity increases, users decreases when temp increases, users increases')


st.title("Correlation in the data set")
corr= hour.corr()
fig13=plt.figure(figsize=(20,10))
sns.heatmap(corr,annot=True,annot_kws={'size':15})
st.pyplot(fig13)
