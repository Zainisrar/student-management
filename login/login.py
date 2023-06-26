
from tkinter import *
import time
import pymysql
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Treeview
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkcalendar import DateEntry




def open_text_box():
    root_login.destroy()
    global count,text_empty
    # import tkinter.print as tkprint
    ################################  functions  ##############################
    def title_movers():
        global count,text_empty
        if count>=len(text):
            count=0
            text_empty=" "
            Title_lable.config(text=text_empty)
        else:
            text_empty=text_empty+text[count]
            Title_lable.config(text=text_empty)
            count+=1
        Title_lable.after(200,title_movers)
    def timer():
        times=time.strftime("%H:%M:%S")
        dates=time.strftime("%d-%m-%Y")
        timer_lable.config(text="Time:"+times+"\n"+"Date:"+dates)
        timer_lable.after(200,timer)
    ####################################################################  IF we connect with MYSQL server then it will use ############################################
    # def connect_db():
    #     windowdb = tk.Toplevel()
    #     windowdb.resizable(False, False)
    #     windowdb.title("Student Management System")
    #     windowdb.iconbitmap("studentmanagement/icons.ico")
    #     windowdb.geometry('500x220+500+300')
    
    #     # label frame
    #     label_frame = ttk.LabelFrame(windowdb, text='Database Detail')
    #     label_frame.grid(row=0, column=0, padx=70, pady=20)
        
    #     # entry box variable
    #     host_var = tk.StringVar()
    #     user_var = tk.StringVar()
    #     password_var = tk.StringVar()
        
    #     # labels
    #     labels_host = ttk.Label(label_frame, text="Enter your Host:")
    #     labels_user = ttk.Label(label_frame, text="Enter your Username:")
    #     labels_password = ttk.Label(label_frame, text="Enter your Password:")
        
    #     # entry boxes
    #     host_entry = ttk.Entry(label_frame, width=36, textvariable=host_var)
    #     user_entry = ttk.Entry(label_frame, width=36, textvariable=user_var)
    #     password_entry = ttk.Entry(label_frame, width=36, textvariable=password_var)
        
    #     # Grid
    #     labels_host.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    #     labels_user.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    #     labels_password.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        
    #     host_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    #     user_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    #     password_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
    #     def submit():
    #         global con, mycursor
    #         # Do something with the entered data
    #         host = host_var.get()
    #         user = user_var.get()
    #         password = password_var.get()
    #         try:
    #             con = pymysql.connect(host=host, user=user, password=password)
    #             mycursor = con.cursor()
    #             # Close the window after processing the data
    #             windowdb.destroy()
    #         except:
    #             messagebox.showerror("Notification", "Incorrect, Try Again")
    #             return
    #         try:
    #             create_database = "CREATE DATABASE mystudentmanagement"
    #             mycursor.execute(create_database)
    #             use_database = "USE mystudentmanagement"
    #             mycursor.execute(use_database)
    #             create_table = """CREATE TABLE student (
    #                 id INT AUTO_INCREMENT PRIMARY KEY,
    #                 name VARCHAR(50),
    #                 mbl VARCHAR(20),
    #                 email VARCHAR(50),
    #                 address VARCHAR(100),
    #                 gender ENUM('Male', 'Female', 'Other'),
    #                 dob DATE,
    #                 date DATE,
    #                 time TIME)
    #             """
    #             mycursor.execute(create_table)
    #         except:
    #             use_database = "USE mystudentmanagement"
    #             mycursor.execute(use_database)
            
    #     # button
    #     submit_button = ttk.Button(windowdb, text='Submit', command=submit)
    #     submit_button.grid(row=3, columnspan=5, padx=40)
        
    #     windowdb.grab_set()
    #     windowdb.mainloop()
    conn = sqlite3.connect("student.db")

    # Create a cursor object
    cursor = conn.cursor()

    ####################################################################################################################################################





    def func_addbtn():
        window = tk.Toplevel()
        window.resizable(False, False)
        window.title("Student Management System")
        window.iconbitmap("studentmanagement\icons.ico")
        window.geometry('500x320+500+300')

        conn = sqlite3.connect("student.db")  # Connect to SQLite database
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY,
                name TEXT,
                mbl TEXT,
                email TEXT,
                address TEXT,
                gender TEXT,
                dob TEXT,
                times TEXT,
                dates TEXT
            )
            """
        )

        label_frame = ttk.LabelFrame(window, text='Student Details')
        label_frame.grid(row=0, column=0, padx=70, pady=20)

        id_var = tk.StringVar()
        name_var = tk.StringVar()
        mbl_var = tk.StringVar()
        email_var = tk.StringVar()
        Address_var = tk.StringVar()
        Gender_var = tk.StringVar()
        DOB_var = tk.StringVar()

        labels_id = ttk.Label(label_frame, text="Enter ID :")
        labels_name = ttk.Label(label_frame, text="Enter Name :")
        labels_mbl = ttk.Label(label_frame, text="Enter Mobile No :")
        labels_email = ttk.Label(label_frame, text="Enter Email :")
        labels_Address = ttk.Label(label_frame, text="Enter Address :")
        labels_Gender = ttk.Label(label_frame, text="Enter Gender :")
        labels_DOB = ttk.Label(label_frame, text="Enter DOB :")

        id_entry = ttk.Entry(label_frame, width=36, textvariable=id_var)
        name_entry = ttk.Entry(label_frame, width=36, textvariable=name_var)
        mbl_entry = ttk.Entry(label_frame, width=36, textvariable=mbl_var)
        email_entry = ttk.Entry(label_frame, width=36, textvariable=email_var)
        Address_entry = ttk.Entry(label_frame, width=36, textvariable=Address_var)
        Gender_entry = ttk.Entry(label_frame, width=36, textvariable=Gender_var)
        DOB_entry = DateEntry(label_frame, width=36, textvariable=DOB_var)  # Use DateEntry widget

        labels_id.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        labels_name.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        labels_mbl.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        labels_email.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        labels_Address.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        labels_Gender.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        labels_DOB.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        mbl_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        Address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        Gender_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        DOB_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        def Submitted():
            id_val = id_var.get()
            name_val = name_var.get()
            mbl_val = mbl_var.get()
            email_val = email_var.get()
            address_val = Address_var.get()
            gender_val = Gender_var.get()
            dob_val = DOB_entry.get_date().strftime("%d-%m-%Y")  # Get the selected date from DateEntry widget
            times = time.strftime("%H:%M:%S")
            dates = time.strftime("%d-%m-%Y")
            # if name_val=='' or id_val=='' or (int(mbl_val)<11 or int(mbl_val)>=11):
            #     messagebox.showerror('error','Enter correct form')
            # else:
            #     try:
            #         id_val=int(id_val)
            #     except ValueError:
            #         messagebox.showerror('error','Age must be Digits')


            try:
                cursor.execute(
                    "INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (id_val, name_val, mbl_val, email_val, address_val, gender_val, dob_val, times, dates)
                )
                conn.commit()

                notification = messagebox.askyesnocancel(
                    "Notification",
                    "ID {}, Name {} added successfully. Do you want to clear the form?".format(id_val, name_val),
                    parent=window
                )
                if notification:
                    id_var.set("")
                    name_var.set("")
                    mbl_var.set("")
                    email_var.set("")
                    Address_var.set("")
                    Gender_var.set("")
                    DOB_var.set("")
            except sqlite3.IntegrityError:
                messagebox.showerror("Notification", "ID already exists")

            cursor.execute("SELECT * FROM student")
            data = cursor.fetchall()
            student_view.delete(*student_view.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_view.insert("", tk.END, values=vv)

        submit_button = ttk.Button(window, text="Submit", command=Submitted)
        submit_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        window.mainloop()


    # func_addbtn()

    #######################################################################################################################################################
    def func_Searchbtn():
        window = tk.Toplevel()
        window.resizable(False,False)
        # window.grab_set()
        window.title("Student Search")
        window.iconbitmap("studentmanagement\icons.ico")
        window.geometry('500x220+500+300')
        # window.minsize(400,150)
        #label frame
        label_frame=ttk.LabelFrame(window,text='Student Details')
        label_frame.grid(row=0,column=0,padx=70,pady=20)
        #entry box variable
        id_var=tk.StringVar()
        name_var=tk.StringVar()
        # mbl_var=tk.StringVar()
        # email_var=tk.StringVar()
        # Address_var=tk.StringVar()
        # Gender_var=tk.StringVar()
        # DOB_var=tk.StringVar()
        # date_var=tk.StringVar()
    
        #labels
        labels_id=ttk.Label(label_frame,text="Enter ID :")
        labels_name=ttk.Label(label_frame,text="Enter Name :")
        # labels_mbl=ttk.Label(label_frame,text="Enter Mobile No :")
        # labels_email=ttk.Label(label_frame,text="Enter Email :")
        # labels_Address=ttk.Label(label_frame,text="Enter Address :")
        # labels_Gender=ttk.Label(label_frame,text="Enter Gender :")
        # labels_DOB=ttk.Label(label_frame,text="Enter DOB :")
        # labels_date=ttk.Label(label_frame,text="Enter Date :")
        #entry boxes
        id_entry=ttk.Entry(label_frame,width=36,textvariable=id_var)
        name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
        # mbl_entry=ttk.Entry(label_frame,width=36,textvariable=mbl_var)
        # email_entry=ttk.Entry(label_frame,width=36,textvariable=email_var)
        # Address_entry=ttk.Entry(label_frame,width=36,textvariable=Address_var)
        # Gender_entry=ttk.Entry(label_frame,width=36,textvariable=Gender_var)
        # DOB_entry=ttk.Entry(label_frame,width=36,textvariable=DOB_var)
        # date_entry=ttk.Entry(label_frame,width=36,textvariable=date_var)
        #Grid
        labels_id.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
        labels_name.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_mbl.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_email.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_Address.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_Gender.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_DOB.grid(row=6,column=0,padx=5,pady=5,sticky=tk.W)
        # labels_date.grid(row=7,column=0,padx=5,pady=5,sticky=tk.W)


        id_entry.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
        name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)
        # mbl_entry.grid(row=2,column=1,padx=5,pady=5,sticky=tk.W)
        # email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)
        # Address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=tk.W)
        # Gender_entry.grid(row=5,column=1,padx=5,pady=5,sticky=tk.W)
        # DOB_entry.grid(row=6,column=1,padx=5,pady=5,sticky=tk.W)
        # date_entry.grid(row=7,column=1,padx=5,pady=5,sticky=tk.W)

        def search():
            id_val = id_var.get()
            name_val = name_var.get()
            # mbl_val = mbl_var.get()
            # email_val = email_var.get()
            # address_val = Address_var.get()
            # gender_val = Gender_var.get()
            # dob_val = DOB_var.get()
            # dates_val = date_var.get()


            query = "SELECT * FROM student WHERE"
            conditions = []
            values = []

            if id_val:
                conditions.append("id=?")
                values.append(id_val)
            if name_val:
                conditions.append("name=?")
                values.append(name_val)
            # if mbl_val:
            #     conditions.append("mbl=?")
            #     values.append(mbl_val)
            # if email_val:
            #     conditions.append("email=?")
            #     values.append(email_val)
            # if address_val:
            #     conditions.append("address=?")
            #     values.append(address_val)
            # if gender_val:
            #     conditions.append("gender=?")
            #     values.append(gender_val)
            # if dob_val:
            #     conditions.append("dob=?")
            #     values.append(dob_val)
            # if dates_val:
            #     conditions.append("dates=?")
            #     values.append(dates_val)

            if conditions:
                query += " " + " AND ".join(conditions)
                cursor.execute(query, tuple(values))
            else:
                cursor.execute("SELECT * FROM student")

            data = cursor.fetchall()
            student_view.delete(*student_view.get_children())
            for row in data:
                student_view.insert("", tk.END, values=row)

        #button
        submit_button=ttk.Button(window,text='Search',command=search)
        submit_button.grid(row=3,columnspan=5,padx=40)
        window.grab_set()
        window.mainloop()
    ###################################################################################################################################################


    def func_Deletebtn():
        # Create the 'deleted_student' table if it doesn't exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS deleted_student (
                id INTEGER PRIMARY KEY,
                name TEXT,
                mbl TEXT,
                email TEXT,
                address TEXT,
                gender TEXT,
                dob TEXT,
                times TEXT,
                dates TEXT
            )
            """
        )
        conn.commit()

        # Get the selected item from the 'student_view' (assuming it's a treeview widget)
        selected_item = student_view.focus()
        if selected_item:
            values = student_view.item(selected_item, "values")
            if values:
                pp = values[0]  # Assuming the ID is stored at index 0 of the 'values' list

                try:
                    # Delete the record from the 'student' table using the ID
                    cursor.execute("DELETE FROM student WHERE id=?", (pp,))
                    conn.commit()
                    messagebox.showinfo("NOTIFICATION", "ID {} is deleted successfully".format(pp))

                    # Insert the deleted record into the 'deleted_student' table
                    cursor.execute(
                        "INSERT INTO deleted_student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        tuple(values)
                    )
                    conn.commit()

                    # Retrieve all records from the 'student' table
                    cursor.execute("SELECT * FROM student")
                    data = cursor.fetchall()

                    # Clear the 'student_view' before repopulating it
                    student_view.delete(*student_view.get_children())

                    # Insert the updated records into the 'student_view'
                    for row in data:
                        student_view.insert("", tk.END, values=row)
                except Exception as e:
                    # Show an error message if an exception occurs during the deletion process
                    messagebox.showerror("ERROR", str(e))
            else:
                messagebox.showerror("ERROR", "No values found for the selected item.")
        else:
            messagebox.showerror("ERROR", "No item selected.")




    ###################################################################################################################################################
    def func_Updatebtn():
        window = tk.Toplevel()
        window.resizable(False,False)
        # window.grab_set()
        window.title("Student Update")
        window.iconbitmap("studentmanagement\icons.ico")
        window.geometry('500x370+500+300')
        # window.minsize(400,150)
        #label frame
        label_frame=ttk.LabelFrame(window,text='Student Details')
        label_frame.grid(row=0,column=0,padx=70,pady=20)
        #entry box variable
        id_var=tk.StringVar()
        name_var=tk.StringVar()
        mbl_var=tk.StringVar()
        email_var=tk.StringVar()
        Address_var=tk.StringVar()
        Gender_var=tk.StringVar()
        DOB_var=tk.StringVar()
        date_var=tk.StringVar()
        time_var=tk.StringVar()
    
        #labels
        labels_id=ttk.Label(label_frame,text="Update by ID :")
        labels_name=ttk.Label(label_frame,text="Update by Name :")
        labels_mbl=ttk.Label(label_frame,text="Update by Mobile No :")
        labels_email=ttk.Label(label_frame,text="Update by Email :")
        labels_Address=ttk.Label(label_frame,text="Update by Address :")
        labels_Gender=ttk.Label(label_frame,text="Update by Gender :")
        labels_DOB=ttk.Label(label_frame,text="Update by DOB :")
        labels_date=ttk.Label(label_frame,text="Update by Date :")
        labels_time=ttk.Label(label_frame,text="Update by Time :")
        #entry boxes
        id_entry=ttk.Entry(label_frame,width=36,textvariable=id_var)
        name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
        mbl_entry=ttk.Entry(label_frame,width=36,textvariable=mbl_var)
        email_entry=ttk.Entry(label_frame,width=36,textvariable=email_var)
        Address_entry=ttk.Entry(label_frame,width=36,textvariable=Address_var)
        Gender_entry=ttk.Entry(label_frame,width=36,textvariable=Gender_var)
        DOB_entry=ttk.Entry(label_frame,width=36,textvariable=DOB_var)
        date_entry=ttk.Entry(label_frame,width=36,textvariable=date_var)
        time_entry=ttk.Entry(label_frame,width=36,textvariable=time_var)
        #Grid
        labels_id.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
        labels_name.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
        labels_mbl.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
        labels_email.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)
        labels_Address.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)
        labels_Gender.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)
        labels_DOB.grid(row=6,column=0,padx=5,pady=5,sticky=tk.W)
        labels_date.grid(row=7,column=0,padx=5,pady=5,sticky=tk.W)
        labels_time.grid(row=8,column=0,padx=5,pady=5,sticky=tk.W)


        id_entry.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
        name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)
        mbl_entry.grid(row=2,column=1,padx=5,pady=5,sticky=tk.W)
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)
        Address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=tk.W)
        Gender_entry.grid(row=5,column=1,padx=5,pady=5,sticky=tk.W)
        DOB_entry.grid(row=6,column=1,padx=5,pady=5,sticky=tk.W)
        date_entry.grid(row=7,column=1,padx=5,pady=5,sticky=tk.W)
        time_entry.grid(row=8,column=1,padx=5,pady=5,sticky=tk.W)
    
        cc = student_view.focus()
        content = student_view.item(cc)
        pp = content["values"]
        if(len(pp)!=0):
            id_var.set(pp[0])
            name_var.set(pp[1])
            mbl_var.set(pp[2])
            email_var.set(pp[3])
            Address_var.set(pp[4])
            Gender_var.set(pp[5])
            DOB_var.set(pp[6])
            date_var.set(pp[7])
            time_var.set(pp[8])

        def Update():
                    
            # Get the updated values from the user (assuming you have entry widgets for each field)
            update_id=id_entry.get()
            updated_name =     name_entry.get()
            updated_mbl =mbl_entry.get()
            updated_email = email_entry.get()
            updated_address =     Address_entry.get()
            updated_gender =    Gender_entry.get()
            updated_dob =  DOB_entry.get()
            updated_times =    time_entry.get()
            updated_dates = date_entry.get()
                
            try:
                # Update the database record with the new values
                cursor.execute(
                    """
                    UPDATE student SET name=?, mbl=?, email=?, address=?, gender=?, dob=?, times=?, dates=?
                    WHERE id=?
                    """,
                    (updated_name, updated_mbl, updated_email, updated_address, updated_gender, updated_dob,
                    updated_times, updated_dates, update_id)
                )
                conn.commit()
                messagebox.showinfo("NOTIFICATION", "Data updated successfully!",parent=window)
                window.destroy()
                
                # Update the values in the student_view widget
            
                cursor.execute("SELECT * FROM student")
                data = cursor.fetchall()
                student_view.delete(*student_view.get_children())
                
                for i in data:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    student_view.insert("", tk.END, values=vv)
                
            except Exception as e:
                messagebox.showerror("ERROR", str(e))
    
        #button
        submit_button=ttk.Button(window,text='Update',command=Update)
        submit_button.grid(row=3,columnspan=5,padx=40)
        window.grab_set()
        window.mainloop()
    ##################################################################################################################################################
    def func_Showallbtn():
        try:
            cursor.execute("SELECT * FROM student")
            data = cursor.fetchall()
            student_view.delete(*student_view.get_children())
                    
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_view.insert("", tk.END, values=vv)
                
        except Exception as e:
                messagebox.showerror("ERROR", str(e))
    ############################################################################################################################################
    # Rest of your code...
    def func_Exportbtn():

        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                # Get the data from the student_view widget
                data = []
                for item_id in student_view.get_children():
                    data.append(student_view.item(item_id)["values"])
                
                # Create a DataFrame using the data
                df = pd.DataFrame(data, columns=["ID", "Name", "Mobile", "Email",
                                                "Address", "Gender", "DOB", "Times", "Dates"])
                
                # Export the DataFrame to CSV
                df.to_csv(file_path, index=False)
                
                messagebox.showinfo("NOTIFICATION", "Data exported successfully!")
            
            except Exception as e:
                messagebox.showerror("ERROR", str(e))

    # Rest of your code...

    ################################################################################################################################################

    def func_Existbtn():
        ext=messagebox.askyesnocancel("Notification","Do you want to Exist?")
        if(ext==True):
            root.destroy()

    ###################################################################################################################################################

    def func_RecoverData():
        try:
            # Retrieve deleted data from a backup table or any other source
            cursor.execute("SELECT * FROM deleted_student")
            data = cursor.fetchall()

            # Clear the existing data in the student_view widget
            student_view.delete(*student_view.get_children())

            # Populate the student_view widget with the recovered records
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_view.insert("", tk.END, values=vv)

                # Insert recovered records back into the student table
                cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", vv)
                conn.commit()

            # Delete the recovered records from the deleted_student table
            cursor.execute("DELETE FROM deleted_student")
            conn.commit()

            messagebox.showinfo("NOTIFICATION", "Data recovery successful!")
        except Exception as e:
            messagebox.showerror("ERROR", str(e))


    #############################################################################################################################################


    from tkinter import ttk, messagebox
    import tkinter as tk
    from PIL import Image, ImageTk
    import win32api
    import win32print
    import time
    import tempfile
    import datetime
    from tkinter.messagebox import showinfo

    def func_GenerateChallan():
        def installed_printer():
            printers = win32print.EnumPrinters(2)
            for p in printers:
                return p

        printerdef = ''

        def locprinter():
            pt = tk.Toplevel()
            pt.title("choose printer")
            var1 = tk.StringVar()
            LABEL = tk.Label(pt, text="Select Printer", bg='goldenrod2', fg='black')
            LABEL.pack(fill=tk.X)
            PRCOMBO = ttk.Combobox(pt, width=35)
            print_list = []
            printers = list(win32print.EnumPrinters(2))
            for i in printers:
                print_list.append(i[2])
            print(print_list)
            # Put printers in combobox
            PRCOMBO['values'] = print_list
            defprinter = win32print.GetDefaultPrinter()
            print('Default selected Printer:', defprinter)
            PRCOMBO.set(defprinter)
            PRCOMBO.pack(padx=5, pady=5)

            def select():
                nonlocal printerdef
                printerdef = PRCOMBO.get()
                pt.destroy()
                print_in_default_printer()

            BUTTON = ttk.Button(pt, text="Print", width=30, command=select)
            BUTTON.pack(pady=10)

        def save_data():
            times = time.strftime("%H:%M:%S")
            dates = time.strftime("%d-%m-%Y")
            current_date = datetime.date.today()

            # Add 5 days to the current date
            payment_within_due_date = current_date + datetime.timedelta(days=10)

            # Convert the new date to the desired format ("%d-%m-%Y")
            due_dates = payment_within_due_date.strftime("%d-%m-%Y")

            payment_after_due_date = payment_within_due_date + datetime.timedelta(days=5)

            # Convert the new date to the desired format ("%d-%m-%Y")
            after_due_dates = payment_after_due_date.strftime("%d-%m-%Y")
            challenge_no = challenge_entry.get()
            name = name_entry.get()
            father_name = father_name_entry.get()
            class_ = class_entry.get()
            section = section_entry.get()
            fees = fees_entry.get()
            try:
                new_fees = int(fees) + 100
            except:
                messagebox.showerror("ERROR", "Must be enter data")

            data = f"""
            Excellent Public School
            ------Office Copy----
            Challenge No: {challenge_no}
            Name: {name}
            Father Name: {father_name}
            Class: {class_}
            Section: {section}
            Date: {dates}
            Time: {times}
            Fees: {fees}
            Payment within due Date: {due_dates}
            Payment after due Date: {after_due_dates}
            after due Date Fees: {new_fees}"""
            data1 = f"""
            Excellent Public School
            ------Student Copy----
            Challenge No: {challenge_no}
            Name: {name}
            Father Name: {father_name}
            Class: {class_}
            Section: {section}
            Date: {dates}
            Time: {times}
            Fees: {fees}
            Payment within due Date: {due_dates}
            Payment after due Date: {after_due_dates}"""

            text_display.insert(tk.END, data + "\n")
            text_display.insert(tk.END, data1 + "\n")

            # Clear the entry fields after saving
            challenge_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            father_name_entry.delete(0, tk.END)
            class_entry.delete(0, tk.END)
            section_entry.delete(0, tk.END)
            fees_entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
            payment_within_due_date_entry.delete(0, tk.END)
            payment_after_due_date_entry.delete(0, tk.END)

        root = tk.Tk()
        root.geometry("1500x800")
        challenge_label = tk.Label(root, text="Challenge No:")
        challenge_label.grid(row=0, column=0, padx=5, pady=5)

        challenge_entry = tk.Entry(root)
        challenge_entry.grid(row=0, column=1, padx=5, pady=5)

        name_label = tk.Label(root, text="Name:")
        name_label.grid(row=0, column=2, padx=5, pady=5)

        name_entry = tk.Entry(root)
        name_entry.grid(row=0, column=3, padx=5, pady=5)

        father_name_label = tk.Label(root, text="Father Name:")
        father_name_label.grid(row=0, column=4, padx=5, pady=5)

        father_name_entry = tk.Entry(root)
        father_name_entry.grid(row=0, column=5, padx=5, pady=5)

        class_label = tk.Label(root, text="Class:")
        class_label.grid(row=1, column=0, padx=5, pady=5)

        class_entry = tk.Entry(root)
        class_entry.grid(row=1, column=1, padx=5, pady=5)

        section_label = tk.Label(root, text="Section:")
        section_label.grid(row=1, column=2, padx=5, pady=5)

        section_entry = tk.Entry(root)
        section_entry.grid(row=1, column=3, padx=5, pady=5)

        fees_label = tk.Label(root, text="Fees:")
        fees_label.grid(row=1, column=4, padx=5, pady=5)

        fees_entry = tk.Entry(root)
        fees_entry.grid(row=1, column=5, padx=5, pady=5)

        submit_button = tk.Button(root, text="Submit", command=save_data)
        submit_button.grid(row=11, column=2, columnspan=2, padx=5, pady=10)

        text_display = tk.Text(root, height=120, width=200)
        text_display.grid(row=13, column=0, columnspan=10, padx=0, pady=0)

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="print", command=locprinter)

        def print_in_default_printer():
            printText = text_display.get("1.0", tk.END)
            print(printText)
            print(printerdef)

            win32print.SetDefaultPrinter(printerdef)
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            # Below is a call to print text from T2 textbox
            win32api.ShellExecute(
                0,
                "printto",
                filename,
                '"%s"' % win32print.GetDefaultPrinter(),
                ".",
                0
            )
            showinfo(title='Success', message='Print Successful', detail='Printing is done. Thank you!')

        root.mainloop()




        






    root=Tk()
    root.title("Student Management System")
    root.iconbitmap("./studentmanagement/icons.ico")
    root.geometry('1550x850+10+10')
    root.minsize(1350,800)


    ##############################################################  Frames #############################################################
    #######################################################   Main Menu    #########################################################
    menu_frame=Frame(root,relief=RIDGE,borderwidth=3)
    menu_frame.place(x=30,y=150,width=300,height=650)
    ####### buttons in main menu ###########
    title_menu=Label(menu_frame,text="Main Menu",font=("arial",22),width=25)
    title_menu.pack(side=TOP,expand=True)
    #Add Button
    addbtn=Button(menu_frame,text="Show all Student",command=func_Showallbtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    addbtn.pack(side=TOP,expand=True)
    # Search Student
    Searchbtn=Button(menu_frame,text="Add Student",command=func_addbtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Searchbtn.pack(side=TOP,expand=True)
    # Delete Student
    Deletebtn=Button(menu_frame,text="Search Student",command=func_Searchbtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Deletebtn.pack(side=TOP,expand=True)
    # recover Student
    Deletebtn=Button(menu_frame,text="Delete Student",command=func_Deletebtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Deletebtn.pack(side=TOP,expand=True)
    # Update Student
    Updatebtn=Button(menu_frame,text="Recover Data",command=func_RecoverData,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Updatebtn.pack(side=TOP,expand=True)
    # Showall Student
    Showallbtn=Button(menu_frame,text="Update Student",command=func_Updatebtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Showallbtn.pack(side=TOP,expand=True)
    # Export data
    Exportbtn=Button(menu_frame,text="Export data",command=func_Exportbtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Exportbtn.pack(side=TOP,expand=True)
    # challan data
    challanbtn=Button(menu_frame,text="Fees Challen",command=func_GenerateChallan,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    challanbtn.pack(side=TOP,expand=True)
    # Exist
    Existbtn=Button(menu_frame,text="Exist",command=func_Existbtn,font=("arial",14),borderwidth=5,relief=RIDGE,width=20,activebackground="black",activeforeground="white")
    Existbtn.pack(side=TOP,expand=True)




    ########################################################  show data frame  ##################################################################
    data_frame=Frame(root,relief=RIDGE,borderwidth=3)
    data_frame.place(x=350,y=150,width=1200,height=650)

    sroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
    sroll_y=Scrollbar(data_frame,orient=VERTICAL)

    student_view=Treeview(data_frame,columns=("ID","Name","Gender","Phone No","Email","Address","DOB","Date","Time"),yscrollcommand=sroll_y.set,
                            xscrollcommand=sroll_x.set)
    sroll_x.pack(side=BOTTOM,fill=X)
    sroll_y.pack(side=RIGHT,fill=Y)
    sroll_x.config(command=student_view.xview)
    sroll_y.config(command=student_view.yview)
    student_view.heading("ID",text="ID")
    student_view.heading("Name",text="NAME")
    student_view.heading("Gender",text="GENDER")
    student_view.heading("Phone No",text="PHONE")
    student_view.heading("Email",text="EMAIL")
    student_view.heading("Address",text="ADDRESS")
    student_view.heading("DOB",text="DOB")
    student_view.heading("Date",text="DATE")
    student_view.heading("Time",text="TIME")
    student_view["show"]="headings"
    style=ttk.Style()
    style.configure("Treeview.Heading",font=("Arial",12,"bold"))
    style.configure("Treeview",font=("Arial",10))
    student_view.pack(fill=BOTH,expand=1)





    ############################### Upper Sections ######################################
    ############  Title  ###########
    text="Exelent Public School Bawli"
    count=0
    text_empty=" "
    Title_lable=Label(root,text=text,font=("arial",40),relief=RIDGE,borderwidth=3,width=25)
    Title_lable.place(x=380,y=35)
    title_movers()  #function call

    ############  Timmer  ###########
    timer_lable=Label(root,font=("arial",16),relief=RIDGE,borderwidth=3,width=15)
    timer_lable.place(x=70,y=40)
    timer()

    ############  Database Button  ###########
    # connect_database=Button(root,text="Connecting to Database",font=("arial",16),relief=RIDGE,background="red",borderwidth=3,width=20,
    #                         activebackground="black",activeforeground="white",command=connect_db)
    # connect_database.place(x=1270,y=45)


























    root.mainloop()





def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'zainisrar@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
        open_text_box()
    else:
        messagebox.showerror('Error','Login Failed')


root_login = Tk()

root_login.title('Login Form') #for title
root_login.iconbitmap('./studentmanagement/icons.ico')
# Get the screen width and height
root_login.minsize(1350,800)


root_login.configure(background='white') #for background color change
img = Image.open('./studentmanagement/logoss.jpg')
resized_img = img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root_login,image=img)
img_label.pack(pady=(90,30))    #for handling position

text_label = Label(root_login,text='Welcome to Exellent Public School',fg='black')
text_label.pack()
text_label.config(font=('Times',24))

email_label = Label(root_login,text='Enter Email',fg='black')
email_label.pack(pady=(20,5))
email_label.config(font=('Times',12,'bold'))

email_input = Entry(root_login,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root_login,text='Enter Password',fg='black')
password_label.pack(pady=(10,5))
password_label.config(font=('Times',12,'bold'))

password_input = Entry(root_login,width=50,show="*")
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root_login,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('Times',10,'bold'))



root_login.mainloop()