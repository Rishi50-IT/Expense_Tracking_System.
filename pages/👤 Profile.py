import streamlit as st
import pymongo
conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
my=mydb["expenseinfo"]

    
st.title("User Profile")
@st.dialog("CHANGE PASSWORD")
def cp():
      op=st.text_input("Enter the old Password :")
      np=st.text_input("Enter the New Password :")
      if st.button("Change Password "):
            reset=my.update_one({"password":op},{'$set':{"password":np}})
            st.success("password change successfully")


em=st.session_state["email"]
imag=st.session_state["image"]
user=my.find({"email":email,"imag":imag})

if user:
  st.write(f"Welcome {data['email']} 👋")
    
c1,c2,c3=st.columns(3)
if c1.button("see profile",use_container_width=True):
             str1=st.session_state["email"]
             str2=st.session_state["password"]
             str3=st.session_state["image"]
             user=my.find({"email":str1,"password":str2,"image":str3})
             st.success("user profile")
             for data in user:
                    with st.form("User Profile"):
                           st.text_input("Username",data["username"])  
                           st.text_input("Mobile No",data["mobileno"])  
                           st.text_input("Date of Birth",data["DOB"])                             
                           st.text_input("Address",data["address"])                             
                           st.text_input("Email",data["email"])                             
                           st.text_input("Password",data["password"])                             
                           st.text_input("Live Photo",data["live photo"])                             


if c2.button("change password ",use_container_width=True):
      cp()
if c3.button("Logout",use_container_width=True):
         st.session_state.data = False
         st.session_state.email = ""
         st.session_state.image = ""
         st.success("You have been logged out")
         st.switch_page("login.py")
