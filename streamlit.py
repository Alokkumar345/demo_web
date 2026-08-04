import streamlit as st
import pandas as pd

# streamlit run streamlit.py   

# st.title("Hello Alok how are you")

# st.header("Python")

# st.subheader("Java")

# st.markdown("i love india")

# st.code(""" for i in range(1,10):
# print("Hello")""")

# df=pd.read_csv("modified_data.csv")  # add data in streamlit

# st.dataframe(df)

name=st.text_input("enter your name :")
Fname=st.text_input("Enter your Father name")
Adr=st.text_area("Enter text :")

classdata=st.selectbox("Enter your class :",(1,2,3,4,5,6))


button=st.button("Done")
if button:
    st.markdown(f"""Name :{name}
Father Name :{Fname}
address : {Adr}
class :{classdata}""")