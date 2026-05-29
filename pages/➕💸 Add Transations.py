import streamlit as st
import pandas as pd
import pymongo
from datetime import date
import streamlit.components.v1 as com
#from streamlit_lottie import st_lottie

#live server connection
conn= pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0")
#conn=pymongo.MongoClient("mongodb+srv://Rishi_Munda:<db_password>@cluster0.dod06ln.mongodb.net/?appName=Cluster0")

#for local db
#conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
transactions=mydb["transactions"]

st.set_page_config(page_title="Transaction")
if "transactions" not in st.session_state:
    st.session_state.transactions = []
st.header("➕ Add New Transaction")
c1,c2=st.columns(2)
with c1:
    com.iframe("https://lottie.host/embed/135ca7d0-9a8e-41e2-9a8b-3985fd3a4530/0FWKtPLPAv.lottie")
with c2:
    com.iframe("https://lottie.host/embed/5aed7e16-d179-449b-80c1-d8ef118f27f0/z7O82KECUH.lottie")
    
t1,t2=st.tabs(["💵Add Income","Add Expense"])
with t1:
    st.title("Add Income ")
    
    
    with st.form("Add Income"):
        st.subheader("Add Your  Source of Income")
        com.iframe("https://lottie.host/embed/bfc96117-3415-4682-8141-5a62ce022119/q2M3kpnaAK.lottie")
        category= st.selectbox("Select Category" ,["Salary","Business","Invetsment", "Other Source of Income"] )
        amount = st.number_input("Enter Amount",min_value=0,step=50)
        month = st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September", "October","November","December"])
        income_date = st.date_input("Select Date",value=date.today())
        payment_method= st.radio("Payment Method" ,[ "Cash","Upi","Debit Card","Credit Card"])
        description = st.text_area("Description / Notes")     

    
        if st.form_submit_button("Add Income"):          
           income = {"email":st.session_state["Email"],
               "Type":"Income","Category": category,"Amount": amount,"Month": month,"Date":str( income_date),"Payment": payment_method,"Description": description}

           transactions.insert_one(income)
           st.success("Income Added Successfully ✅ ")

        st.markdown("---")




with t2:

    st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered")

    st.title("💰 Add Expense")

    with st.form("expense_form"):
        com.iframe("https://lottie.host/embed/cf361bf1-f911-43d0-9d81-7aac48e58483/P85yY7w2Kn.lottie")
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
            expense={"email":st.session_state["Email"],
                "Type": "Expense",
                "Category": category,
                "Amount": amount,
                "Month": month,
                "Date":str( expense_date),
                "Payment": payment_method,
                "Description": description}
            transactions.insert_one(expense)
            st.success("Expense Added Successfully ✅")
        else:
            st.info("No Expense  added yet.")
        




st.markdown("---")

st.subheader("📋 All Transactions")
data=list(transactions.find( { "email": st.session_state["Email"] }, {"_id": 0} ))

if data:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)




else:
    st.info("No Transactions Added Yet")

st.subheader("📑Income Records")
if st.button("📊 Data Visulization"):
    st.switch_page("pages/📋📊Reports.py")
