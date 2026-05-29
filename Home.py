import streamlit as st
import time
import streamlit.components.v1 as com
from streamlit-lottie import st-lottie



st.header(" 💰 Expense Tracking System")
st.set_page_config(page_title="💰 Expense Tracker")
st.logo("logo.png")
st.write("Welcome to the expense tracking webpage. You can Track Income & Expenses Easily ")
com.iframe("https://lottie.host/embed/872ed4cc-0112-4b2b-a488-d3ec21fa9632/FY2sesenYh.lottie")
st.toast("welcome to Expense Tracke")
with st.spinner("Loading..."):
    time.sleep(3)
st.subheader("Project Description:")
st.image("expense _tracker_image.png")
st.markdown('''Expense Tracker is a smart web application that helps users to  monitor, analyze, manage and improve their financial activities
expenses efficiently.
The system uses AI/ML techniques to provide:

- Expense prediction
- Spending analysis
- Smart recommendations
- Budget alerts

The project is developed using Python and Streamlit.
We use MongoDB as a Backend DataBase.


''')
with st.expander("See  More Details About Project"):
    st.write("""About Us:Begginer Python Developer | Passionate about AI/ML | Building Innovative Projects | Open to Collaborations | Always Learning and Growing
               
             Contact Us:93xxxxxx67

             """)

st.markdown("[👔](https://www.linkedin.com/in/rishi-munda-a88b80224) |"
" [Github](https://github.com/Rishi50-IT)|""[✖️](https://twitter.com/@340Rishi)")
st.caption("@2026 Expense Tracking System website | Made with love ")
