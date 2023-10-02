import tkinter as tk
import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "hospital"
    
app=tk.Tk()
app.title("Hospital")
app.geometry("300x300")
app.config(bg='#c2c2d6')

def add_data():
    username=name.get()
    userdate=date.get()
    userdis=disease.get()
    nme.destroy()
    name.destroy()
    dte.destroy()
    date.destroy()
    dis.destroy()
    disease.destroy()
    submit1.destroy()
    mess=username+" on "+userdate+" for "+userdis
    
    info.grid(row=2,column=0)
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
        cursor = connection.cursor()
        if connection.is_connected():
            print("Connected to MySQL")
        else:
            print("Failed to connect to MySQL")
    finally:
        print()
    cursor = connection.cursor()
    insert_query = "INSERT INTO detail (name, date_of_add, disease) VALUES (%s, %s, %s)"
    values = (username, userdate, userdis)
    cursor.execute(insert_query, values)
    connection.commit()
    select_query = "SELECT reference_id FROM detail WHERE name = %s AND date_of_add = %s AND disease = %s"
    values = (username, userdate, userdis)
    cursor.execute(select_query, values)
    result = cursor.fetchall()
    if result:
            choice1.destroy()
            choice2.destroy()
            info.config(text=mess+" your refernce id is "+str(result[0][0]))
    
def add():
    print("Added")
    nme.grid(row=2,column=0)
    name.grid(row=2,column=1)
    dte.grid(row=3,column=0)
    date.grid(row=3,column=1)
    dis.grid(row=4,column=0)
    disease.grid(row=4,column=1)
    submit1.grid(row=5,column=0)

def del_data():
    print("deleting")
    refer=refe.get()
    refer=int(refer)
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
        cursor = connection.cursor()
        if connection.is_connected():
            print("Connected to MySQL")
        else:
            print("Failed to connect to MySQL")
    finally:
        print()
    cursor = connection.cursor()
    delete_query = "DELETE FROM detail WHERE reference_id = %s"
    values = (refer,)  # Create a tuple with a comma
    cursor.execute(delete_query, values)
    connection.commit()
    print("Deleted successfully")
    info.config(text="Successfully deleted")
    choice1.destroy()
    choice2.destroy()
    ref.destroy()
    refe.destroy()
    info.grid(row=0,column=0)
    choice.destroy()
    submit2.destroy()
def delete():
    ref.grid(row=2,column=0)
    refe.grid(row=2,column=1)
    submit2.grid(row=3,column=0)
    
choice=tk.Label(app,text="Enter your choice")
choice.grid(row=0,column=0)
choice1=tk.Button(app,text="Add appointment",command=add)
choice1.grid(row=1,column=0)
choice2=tk.Button(app,text="Delete appointment",command=delete)
choice2.grid(row=1,column=1)
nme=tk.Label(app,text="Enter name")
name=tk.Entry(app)
dte=tk.Label(app,text="Enter date (seprated by dots)")
date=tk.Entry(app)
dis=tk.Label(app,text="Enter disease")
disease=tk.Entry(app)
submit1=tk.Button(app,text="Add",command=add_data)
info=tk.Label(app)
ref=tk.Label(app,text="Enter reference id")
refe=tk.Entry(app)
submit2=tk.Button(app,text="Delete",command=del_data)
