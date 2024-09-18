import streamlit as st

st.title("🎈 My new app")
st.write("my first python app")
st.write("hello")
name = st.text_input("please enter your name")
st.write("welcome",name)
def register():
  surname = st.text_input("please enter your surname")
  forename = st.text_input("please enter your forename")
  date = st.text_input("please enter your date of birth without spaces between the numbers")
  username = st.text_input("please enter a username")
  password = st.text_input("please enter the password")

  st.write('your username is '+username)
  st.write('your password is '+password)
  file=open("users.txt","a")
  file.write("\n"+username+","+password+","+surname+","+forename+","+date+","+"N"+","+"1")
  file.close()
register()
