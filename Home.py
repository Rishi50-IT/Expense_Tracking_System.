import streamlit as st
import time
st.header(" 💰 Expense Tracking System")
st.set_page_config(page_title="💰 Expense Tracker")
st.logo("logo.png")
st.write("Welcome to the expense tracking webpage. You can Track Income & Expenses Easily ")
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
    st.write("""About Us:
              Contact Us:

             """)

st.caption("@2026 Expense Tracking System website | Made with love ")
