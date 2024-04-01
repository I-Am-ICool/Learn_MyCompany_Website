import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add header and other writeups
st.title("The Best Company")
content = """This is the best company website because it is the first I'm designing that actually makes much sense.
I cannot imagine what it will be like to go through this. The journey was what I thought will be easy, However, coding 
ain't for the weak-hearted. We meuve!!!
"""
st.write(content)

# Add subheader
st.subheader("Our Team")

# Set the number of columns by making provision for their spacing
col1, empty_col1, col2, empty_col2, col3 = st.columns([3.0, 0.5, 3.0, 0.5, 3.0])

# Read the csv file using pandas
df = pandas.read_csv("data.csv")

# Code the adding content to first column
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

# Code the adding content to second column
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

# Code the adding content to third column
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

