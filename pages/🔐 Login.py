import streamlit as st
import pymongo
import random
import time
from datetime import date

conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
my=mydb["expenseinfo"]

"""progress = st.progress(0)
for i in range(100):
     progress.progress(i + 1)
     time.sleep(0.02)
     progress.empty()  """
tab1,tab2=st.tabs(["SIGNIN" , "SIGNUP"])
with tab1:
     with st.form("tab1"):
           st.subheader("Login Your Account")
           em=st.text_input("Email:")
           pa=st.text_input("Password:" , type="password")
           st.checkbox("Terms &Conditions")
           if st.form_submit_button("SIGNIN"):
                if not em or not pa  :
                     st.error("Fill all fields")
                else :
                     user=my.find({"email":em,"password":pa})
                     v=0
                     for data in user:
                          v=v+1
                          st.session_state["Email"]=data['email']
                          st.session_state["password"]=data["password"]
                          st.session_state["image"]=data['live photo']
                          st.success(f"welcome:{data['email']}")
                          st.switch_page("pages/👤 Profile.py")

                     if v==0 :
                              st.error("Invalid Login Details")
                
              

with tab2:
    with st.form("tab2"):
          
          st.subheader("Create New Account")
          us=st.text_input("Username")
          mn=st.text_input("Mobile no")
          dob=st.date_input("DOB" )#,# value=date.today() , min_value=date(1975,1,1) , max_value=(2050,12,31))
          ad=st.text_area("Address")
          e=st.text_input("Email")
          p=st.text_input("Password:", type="password")
          cp=st.text_input("Conform Password:" , type="password")
          lp=st.camera_input("Click your Picture")
          count=random.randrange(1,100000)
          str1="img"
          str1=str1+str(count)+".jpg"
          if lp:
              with open(str1,"wb") as f:
                    f.write(lp.getvalue())
      
          st.checkbox("Terms &Conditions")
          if st.form_submit_button("SIGNUP"):
               my.insert_one({"Username":us ,"Mobileno":mn,"Address":ad,"email":e,"password":p,"live photo":lp})
               if p==cp :
                 st.success("Thank you for SIGNUP")
                 st.balloons()
               else:
                 st.error(" Your password is not same")
st.markdown("---")
st.caption("@2026 Expense Tracking Systm Login Form")
