import streamlit as st
import pymongo
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

#for live server data base co
conn=pymongo.MongoClient("mongodb+srv://Rishi_Munda:<db_password>@cluster0.dod06ln.mongodb.net/?appName=Cluster0")

#for local db
#conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
my=mydb["expenseinfo"]

    
st.title("User Profile")

com.iframe("https://lottie.host/embed/cc5b0694-3397-4044-8a59-e72ab8a47e5f/9aZ5nLcu0V.lottie")

@st.dialog("CHANGE PASSWORD")
def cp():
      op=st.text_input("Enter the old Password :")
      np=st.text_input("Enter the New Password :")
      if st.button("Change Password "):
            reset=my.update_one({"password":op},{'$set':{"password":np}})
            st.success("password change successfully")


em=st.session_state["Email"]
imag=st.session_state["image"]
user=my.find({"email":em})

for data in user:
      e=data['email']
      st.write(f"Welcome {e} 👋")
      p=data['photo']
      u=data['Username']
      m=data['Mobileno']
      a=data['Address']
      
      
  
    
c1,c2,c3, c4=st.columns(4)
if c1.button("🪪 see profile",use_container_width=True):
             str1=data["email"]
             str2=st.session_state["password"]
             str3=st.session_state["image"]
             user=my.find({"email":str1,"password":str2,"image":str3})
             st.success("user profile")
             st.image(p)
             st.logo(p)
             st.text_input("Username",u)  
             st.text_input("Mobile No",m)  
             st.text_input("Address",a)                             
             st.text_input("Email",e)                             
                           

if c2.button("🔑change password ",use_container_width=True):
      cp()
if c3.button("➜]Logout",use_container_width=True):
         st.session_state.data = False
         st.session_state.email = ""
         st.session_state.image = ""
         st.success("You have been logged out")
         st.switch_page("login.py")
if c4.button("➕Add Transactions",use_container_width=True):
         st.switch_page("pages/➕💸 Add Transations.py")
