mycursor.fetchall()
            student_view.delete(*student_view.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_view.insert("", tk.END, values=vv)


    #button
    submit_button=ttk.Button(window,text='Search',command=Search)
    submit_button.grid(row=3,columnspan=5,padx=40)
    window.grab_set()
    window.mainloop()
###################################