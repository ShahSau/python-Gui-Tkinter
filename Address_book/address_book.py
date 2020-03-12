#importing 
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#####
root=Tk()
root.title('Creating Database')
#root.geometry("500✕500")

#database

#creating database
conn=sqlite3.connect('address_book.db')


#creating cursor
cursor=conn.cursor()

#creating table
#commeting out the table as I dont want to create a new table everytime I run the program.

#cursor.execute(""" 
#CREATE TABLE address(
#first_name text,
#last_name text,
#address text,
#city text,
#state text,
#zipcode integer
#)""")



def update2():
    #creating database
    conn=sqlite3.connect('address_book.db')

    #creating cursor
    cursor=conn.cursor()

    record_id=dele.box.get()

    #
    cursor.execute("""UPDATE address SET
    first_name= :first,
    last_name= :last,
    address= :address,
    city= :city,
    state= :state,
    zipcode= :zipcode
    WHERE oid= :oid""",
    
    {
        'first':f_name_edit.get(),
        'last': l_name_edit.get(),
        'address': address_edit.get(),
        'city': city_edit.get(),
        'state': state_edit.get(),
        'zipcode': zipcode_edit.get(),
        'oid': record_id
    })

    #comminting 
    conn.commit()

    #closing
    conn.close()

    update.destroy()
#creating the update function
def edit():
    global update
    update=Tk()
    update.title('Updating the  Database')

    #creating database
    conn=sqlite3.connect('address_book.db')

    #creating cursor
    cursor=conn.cursor()


    record_id=dele.box.get()

    #showing the details
    cursor.execute("SELECT * FROM address WHERE oid = "+ record_id)
    records = cursor.fetchall()
    
    #creating global variable
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit


    #creating text box
    f_name_edit= Entry(update, width=30)
    f_name_edit.grid(row=0,column=1,padx=20,pady=(20,0))

    l_name_edit= Entry(update, width=30)
    l_name_edit.grid(row=1,column=1)

    address_edit= Entry(update, width=30)
    address_edit.grid(row=2,column=1)

    city_edit= Entry(update, width=30)
    city_edit.grid(row=3,column=1)

    state_edit= Entry(update, width=30)
    state_edit.grid(row=4,column=1)

    zipcode_edit= Entry(update, width=30)
    zipcode_edit.grid(row=5,column=1)

    #create text box label
    f_name_edit.label=Label(update,text="First Name")
    f_name_edit.label.grid(row=0, column=0,pady=(20,0))

    l_name_edit.label=Label(update,text="Last Name")
    l_name_edit.label.grid(row=1, column=0)

    address_edit.label=Label(update,text="Address")
    address_edit.label.grid(row=2, column=0)

    city_edit.label=Label(update,text="City")
    city_edit.label.grid(row=3, column=0)

    state_edit.label=Label(update,text="State")
    state_edit.label.grid(row=4, column=0)

    zipcode_edit.label=Label(update,text="Zipcode")
    zipcode_edit.label.grid(row=5, column=0)

    for recoo in records:
        f_name_edit.insert(0, recoo[0])
        l_name_edit.insert(0, recoo[1])
        address_edit.insert(0, recoo[2])
        city_edit.insert(0, recoo[3])
        state_edit.insert(0, recoo[4])
        zipcode_edit.insert(0, recoo[5])


    #creating a savebutton
    save_btn=Button(update, text="Save the entry",command=update2)
    save_btn.grid(row=6, column=0, columnspan=2,pady=10, padx=10,ipadx=130)



#creating a delete button
def dele():
     #creating database
    conn=sqlite3.connect('address_book.db')

    #creating cursor
    cursor=conn.cursor()

    #delete a record
    cursor.execute("DELETE from address WHERE oid= "+ dele.box.get())

    #comminting 
    conn.commit()

    #closing
    conn.close()


#creating submit button
def submit():
    #creating database
    conn=sqlite3.connect('address_book.db')

    #creating cursor
    cursor=conn.cursor()

    #insert into the table
    cursor.execute("INSERT INTO address VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })


    #comminting 
    conn.commit()

    #closing
    conn.close()


    #cleaning the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)



#creating query button
def query():
    #creating database
    conn=sqlite3.connect('address_book.db')

    #creating cursor
    cursor=conn.cursor()

    #showing entire table
    cursor.execute("SELECT *,oid FROM address")
    records = cursor.fetchall()
    #print(records)

    #printing the records
    print_records=''
    for reco in records:
        print_records += str(reco[0])+" "+ str(reco[1])+"\t"+ str(reco[6]) + "\n"
        
    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    #comminting 
    conn.commit()

    #closing
    conn.close()





#creating text box
f_name= Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20,pady=(20,0))

l_name= Entry(root, width=30)
l_name.grid(row=1,column=1)

address= Entry(root, width=30)
address.grid(row=2,column=1)

city= Entry(root, width=30)
city.grid(row=3,column=1)

state= Entry(root, width=30)
state.grid(row=4,column=1)

zipcode= Entry(root, width=30)
zipcode.grid(row=5,column=1)

dele.box=Entry(root,width=30)
dele.box.grid(row=9,column=1,pady=5)


#create text box label
f_name.label=Label(root,text="First Name")
f_name.label.grid(row=0, column=0,pady=(20,0))

l_name.label=Label(root,text="Last Name")
l_name.label.grid(row=1, column=0)

address.label=Label(root,text="Address")
address.label.grid(row=2, column=0)

city.label=Label(root,text="City")
city.label.grid(row=3, column=0)

state.label=Label(root,text="State")
state.label.grid(row=4, column=0)

zipcode.label=Label(root,text="Zipcode")
zipcode.label.grid(row=5, column=0)

dele.box.label=Label(root,text="oid of the Select query :")
dele.box.label.grid(row=9,column=0,pady=5)



#creating submit button
submit_btn=Button(root,text="Enter the new entry", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#creating query button
query_btn=Button(root, text="Show all the entries",command=query)
query_btn.grid(row=7, column=0, columnspan=2,pady=10, padx=10,ipadx=137)

#creating a delete button
dele_btn=Button(root, text="Delete an entry",command=dele)
dele_btn.grid(row=10, column=0, columnspan=2,pady=10, padx=10,ipadx=130)

#creating a update button
edit_btn=Button(root, text="Update an entry",command=edit)
edit_btn.grid(row=11, column=0, columnspan=2,pady=10, padx=10,ipadx=130)


#comminting 
conn.commit()

#closing
conn.close()

root.mainloop()