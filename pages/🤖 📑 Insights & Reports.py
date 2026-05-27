import streamlit as st
import pandas as pd



st.set_page_config(page_title="Expense Reports and Insights")

st.subheader("🤖 AI Insights")

insight1, insight2 = st.columns(2)

with insight1:
        st.success("✅ Your savings increased by 15% this month.")

        st.warning("⚠ Shopping expenses are higher than usual.")
with insight2:
        st.info( "📌 Suggested budget for next month: ₹20,000")
        

        st.error("🚨 Bills spending crossed monthly limit.")
        
st.header("Reports")

st.title("📑 Monthly Reports")

st.subheader("Expense Summary")

if "data" in st.session_state:
        
        df = pd.DataFrame(st.session_state.data)
        st.dataframe(df,use_container_width=True)
        transaction_type=st.radio(
        "💳 Type",
        ["Income", "Expense"])
        if transaction_type !="All":
                filtered_df=df[df["Type"]== transaction_type]
        else:
                 
              filtered_df=df

        st.subheader("📋 Filtered Data")
        st.dataframe(filtered_df)
        csv=filtered_df.to_csv(index=False)
        st.download_button(
          "⬇ Download Report",
          data=csv,
          file_name="expense_report.csv",
          mime="text/csv"
         )
        income = df[df["Type"] == "Income"]["Amount"].sum()

        expense = df[df["Type"] == "Expense"]["Amount"].sum()

        savings = income - expense

        col1, col2, col3 = st.columns(3)

        with col1:
                
                st.metric("💵 Income", f"₹{income}")

        with col2:
                st.metric("💸 Expense", f"₹{expense}")
        with col3:
                st.metric("🏦 Savings", f"₹{savings}")

    # ---------------- CHART ----------------
        st.subheader("📊 Expense Chart")

        expense_df = df[df["Type"] == "Expense"]

        if not expense_df.empty:
                
                chart_data = expense_df.groupby("Category")["Amount"].sum()

                st.bar_chart(chart_data)

        else:
                
            st.warning("⚠ No expense data found")

# ---------------- AI INSIGHTS ----------------
st.markdown( "----AI Insights----")
st.title("🤖 AI Predictions")

st.info(
        "Predicted next month expense: ₹22,000"
    )

st.success(
        "You can save ₹8,000 next month"
    )

st.warning(
        "Reduce shopping expenses by 10%"
    )

