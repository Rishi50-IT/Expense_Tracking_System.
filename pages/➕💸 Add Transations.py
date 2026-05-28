import streamlit as st
import pandas as pd
from datetime import date

t1,t2=st.tabs(["Add Income","Add Expense"])
with t1:
    st.title("Add Income ")
    if "income_data" not in st.session_state:
       
      st.session_state.income_data=[]
    
    with st.form("Add Income"):
        st.header("Add Your  Source of Income")

        category= st.selectbox("Select Category" ,["Salary","Business","Invetsment", "Other Source of Income"] )

        amount = st.number_input("Enter Amount",min_value=0,step=50)

    
        month = st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September", "October","November","December"])
      
    
        income_date = st.date_input("Select Date",value=date.today())

        payment_method= st.radio("Payment Method" ,[ "Cash","Upi","Debit Card","Credit Card"])


        description = st.text_area("Description / Notes")     

    
        if st.form_submit_button("Add Income"):
            income = {"Category": category,"Amount": amount,"Month": month,"Date": income_date,"Payment": payment_method,"Description": description}

            st.session_state.income_data.append(income)

            st.success("Income Saved Successfully ✅")


st.markdown("---")

st.subheader("📊 Income Records")







with t2 :
    st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered")

    st.title("💰 Add Expense")


    if "data" not in st.session_state:
        st.session_state.data = []


    with st.form("expense_form"):

     st.subheader("Enter Expense Details")

    
     category = st.selectbox( "Select Category",["Food","Travel","Shopping","Bills","Entertainment","Education","Health","Other"])

    
    amount = st.number_input(
        "💵 Enter Amount",
        min_value=0,
        step=50)

    
    month = st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September", "October","November","December"])

    
    expense_date = st.date_input("Select Date",value=date.today())


    payment_method = st.radio("Payment Method",["Cash","UPI","Debit Card","Credit Card"])
    

    
    description = st.text_area("Description / Notes")  

if st.session_state.income_data:

        df = pd.DataFrame(st.session_state.income_data)

        st.dataframe(df)

else:
   st.info("No Income added yet.")

