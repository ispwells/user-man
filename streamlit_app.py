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
  menu()

def login():
  userenter = st.text_input("please enter your username")
  userpass = st.text_input("please enter your password")
  file=open("users.txt","r")
  for line in file:
    lines = line.split(",")
    username = lines[0]
    password = lines[1]
    surname = lines[2]
    date = lines[4]
    admin = lines[5]
    #print(admin)
    #print(username)
    #active = lines[6]
    if userenter == username and userpass == password:
      firstname = lines[3]
      #print("check")
      if admin == 'N':
        st.write('welcome '+firstname+' ' +surname)
        st.write('your birthdate is '+ date)
        #choice = st.number_input("please chose 1 to draw shapes or 2 to play guessing game")
        #if choice == 1:
          #import shapes as s
        #else:
          #import game as g
      #elif active == "I":
        #print("your account is not active")
      else:
        print("welcome admin")
        #adminf()
      file=open("loginrecord.txt","a")
      file.write("\n"+userenter+","+str(datetime.datetime.now()))
      file.close()

def menu():
  slection = st.text_input("please enter R to register or L to login")
  if slection == 'r' or slection == 'R':
    register()
  elif slection == 'l' or slection == 'L':
    login()
  
  else:
    menu()
menu()
