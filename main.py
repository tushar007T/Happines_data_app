import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")

x1 = st.selectbox("select the data for the x-axis", ("GDP", "Happiness", "Generosity"))
y1 = st.selectbox("select the data for the y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x1} and {y1}")

df = pd.read_csv("data/happy.csv")
match x1:
    case "GDP":
        x = df["gdp"]
    case "Happiness":
        x = df["happiness"]
    case "Generosity":
        x = df["generosity"]

match y1:
    case "GDP":
        y = df["gdp"]
    case "Happiness":
        y = df["happiness"]
    case "Generosity":
        y = df["generosity"]


figure = px.scatter(x=x, y=y, labels={"x": x1, "y": y1})
st.plotly_chart(figure)
