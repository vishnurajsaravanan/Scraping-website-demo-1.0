import streamlit as st
import pandas as pd
from raw_data import *

st.write("# blog-scrappy")

dat = st.selectbox("Choose URL",options=('https://blogs.sap.com/','https://unfoundation.org/blog/','https://aws.amazon.com/blogs/aws/'))
try:
    if dat == 'https://blogs.sap.com/':
        d = pd.read_csv("SAP.csv") 
    elif dat == 'https://unfoundation.org/blog/':
        d = pd.read_csv("unfoundation.csv")
    elif dat == "https://aws.amazon.com/blogs/aws/":
        d = pd.read_csv("aws.csv")
except: 
    pass

st.table(d)

data_as_csv = d.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download data as CSV",
    data_as_csv,
    "blog.csv",
    "text/csv",
    key="download-tools-csv",
)
