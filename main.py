import streamlit as st
import pandas as pd
import plotly.express as px


st.title('STREAMLIT WEB APPLICATION')
table=pd.read_csv('sample_pivot.csv').head()
st.text('Sample pivot is the dataset we use to check for exploratoy analysis on clothing brand')
st.write(table)
## add visualization
bar_plot_fig=px.bar(table,x='Region',y='Units',title='Barplot')
st.plotly_chart(bar_plot_fig,use_container_width=True)

pie_chart_fig=px.pie(table,values='Sales',names='Region',title='Distribution of sales in regions')
st.plotly_chart(pie_chart_fig,use_container_width=True)

## import data
st.title('Tips Dataset')
table2=px.data.tips()
button_label=st.button('click to see the data')
hide=st.checkbox('hide/show Dataset')
if not hide:
    st.write(table2)

## create sunburst
sun_fig=px.sunburst(table2,path=['day','time','sex','smoker'],values='tip',title='SUNBURST FOR THE DAY')
st.plotly_chart(sun_fig,use_container_width=True)

