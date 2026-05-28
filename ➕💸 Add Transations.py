import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Transaction")
if "transactions" not in st.session_state:
    st.session_state.transactions = []
    
t1,t2=st.tabs(["💵Add Income","Add Expense"])
with t1:
    st.title("Add Income ")
    
    
    with st.form("Add Income"):
        st.header("Add Your  Source of Income")

        category= st.selectbox("Select Category" ,["Salary","Business","Invetsment", "Other Source of Income"] )
        amount = st.number_input("Enter Amount",min_value=0,step=50)
        month = st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September", "October","November","December"])
        income_date = st.date_input("Select Date",value=date.today())
        payment_method= st.radio("Payment Method" ,[ "Cash","Upi","Debit Card","Credit Card"])
        description = st.text_area("Description / Notes")     

    
        if st.form_submit_button("Add Income"):          
           income = {"Type":"Income","Category": category,"Amount": amount,"Month": month,"Date": income_date,"Payment": payment_method,"Description": description}

           st.session_state.transactions.append(income)
           st.success("Income Added Successfully ✅ ")

        st.markdown("---")

st.subheader("📊 Income Records")

with t2 :
    st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered")

    st.title("💰 Add Expense")

    with st.form("expense_form"):
        category = st.selectbox( "Expense  Category",["Food","Travel","Shopping",
                                "Bills","Entertainment","E-commerce",
                                "Education","Health","Other"])

        amount = st.number_input(
        "💵 Enter Amount",
        min_value=0,
        step=50,
        key="expense_amount")

        month = st.selectbox("Select Expense Month",["January","February",
                                                 "March","April","May",
                                                 "June","July","August",
                                                 "September", "October",
                                                 "November","December"],key="expense_month")
        expense_date = st.date_input("Expense Date",value=date.today(),key="expense_date")
        payment_method = st.radio("Payment Method",["Cash","UPI","Debit Card","Credit Card"],key="expense_payment")
        description = st.text_area("Expense Description / Notes",key="expense_descriptionn")  


        if st.form_submit_button("Add Expense"):
            expense={"Type": "Expense",
                "Category": category,
                "Amount": amount,
                "Month": month,
                "Date": expense_date,
                "Payment": payment_method,
                "Description": description}
            st.session_state.transactions.append(expense)
            st.success("Expense Added Successfully ✅")
        else:
            st.info("No Expense  added yet.")
        




st.markdown("---")

st.subheader("📋 All Transactions")

if st.session_state.transactions:

    df = pd.DataFrame(st.session_state.transactions)

    st.dataframe(df, use_container_width=True)

else:
    st.info("No Transactions Added Yet")

