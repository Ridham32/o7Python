import streamlit as st
import sqlite3

def create_connection():
    conn = sqlite3.connect("pythonO7.db",check_same_thread=False)
    return conn

conn = create_connection()
cursor = conn.cursor()


def reg(data):
    try:
        cursor.execute('''INSERT INTO user (name, email, password,gender,age) VALUES (?, ?, ?, ?, ?)''', data)
        conn.commit()
        st.success("Hurray:tada:! You Have Registered Successfully:white_check_mark:")
    except sqlite3.Error as e:
        st.error(e)
    except:
        print("Something went wrong")  



def login(data):
    try:
        cursor.execute('''SELECT * FROM user WHERE email=? AND password=?''',data)
        return cursor.fetchone()
    except:
        st.error("Something went wrong")

def all_data():
    try:
        cursor.execute("SELECT * FROM user")
        return cursor.fetchall()
    except:
        st.error("Something Went wrong")

def update(data):
    try:
        cursor.execute("UPDATE user SET name =?,email=?,password=?,gender=?,age=? WHERE id = ?",data)
        conn.commit()
        return True
    except:
        st.error("Something wnet wrong")
    

def readone(id):
    try:
        cursor.execute("SELECT * FROM user WHERE id =?",(id,))
        return cursor.fetchone()
    except:
        st.error("Something is wrong")

def delete(id):
    try:
        cursor.execute("DELETE FROM user WHERE id =?",(id,))
        conn.commit()
        if cursor.rowcount>0:
            st.success("Deleted Succesfully")
            return True
        else:
            st.error("ID not found")
            return False
    except sqlite3.Error as e:
        print("Database error",e)
        return False
    except Exception as e:
        st.error("Something wrong",e)
        return False

