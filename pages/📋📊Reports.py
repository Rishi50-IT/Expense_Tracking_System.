import streamlit as st
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie 


#live server connection
conn=pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124%40@cluster0.dod06ln.mongodb.net/?appName=Cluster0")

#conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")

mydb = conn["expensedb"]
transactions = mydb["transactions"]

st.title("📊 Reports & Analytics")
com.iframe("https://lottie.host/embed/a48fea96-bcae-4f62-aee8-e1c07e4f1e59/A5QzK0qPFf.json")

if "Email" not in st.session_state:
    st.error("Please login to view your reports.")
    st.stop()


records=list(transactions.find({"email":st.session_state["Email"]},{"_id": 0}))



if not records:
    st.warning("No Transactions Available")

else:
    data=pd.DataFrame(records)

    st.subheader("📋 Transaction Table")

    st.dataframe(data, use_container_width=True)

    income = data[data["Type"] == "Income"]["Amount"].sum()
    expense = data[data["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense

    c1, c2, c3 = st.columns(3)

    c1.metric("💵 Total Income", f"₹{income}","100%")
    c2.metric("💸 Total Expense", f"₹{expense}","-9%")
    c3.metric("💰 Balance", f"₹{balance}","91%")

    st.markdown("---")
    expense_data = data[data["Type"] == "Expense"]
if not expense_data.empty:
        
        st.subheader("📊 Category Wise Expenses")

        category_data = expense_data.groupby("Category")["Amount"].sum()
 
        fig, ax = plt.subplots()

        ax.bar(category_data.index, category_data.values)

        plt.xticks(rotation=45)

        st.pyplot(fig)

    
   

st.subheader("🥧 Expense Distribution")

fig2, ax2 = plt.subplots()

ax2.pie(
        category_data.values,
        labels=category_data.index,
        autopct="%1.1f%%"
    )

st.pyplot(fig2)


st.subheader("📈 Monthly Transactions")

monthly = data.groupby("Month")["Amount"].sum()

st.line_chart(monthly)


st.subheader("💹 Income vs Expense")

compare = data.groupby("Type")["Amount"].sum()

st.bar_chart(compare)
