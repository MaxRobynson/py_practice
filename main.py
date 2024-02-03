import tkinter
from tkinter import ttk

def enter_data():
    firstname = first_name_entry.get()
    last = last_name_entry.get()
    title = title_combox.get()
    age = age_spinbox.get()
    nationality = nationality_combox.get()
    
    courses = numcourses_spinbox.get()
    semester = numsemesters_spinbox.get()
window = tkinter.Tk()
window.title('data entry')

frame = tkinter.Frame(window, bg='grey')
frame.pack()

# saving user info
user_info_frame = tkinter.LabelFrame(frame,text="User information")
user_info_frame.grid(column=0, row=0,padx=0, pady=20)

first_name_label = tkinter.Label(user_info_frame, text='First Name')
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text='Last Name')
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)


title_label= tkinter.Label(user_info_frame, text="title")
title_combox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combox.grid(row=1, column=2)


age_albel = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_albel.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combox = ttk.Combobox(user_info_frame, values=["American", "Africa", "Asia", "Europe"])
nationality_label.grid(row=2, column=1)
nationality_combox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
#saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

registerd_label = tkinter.Label(courses_frame, text="Regestration status")
registerd_ckeck  = tkinter.Checkbutton(courses_frame, text="Currently Registered")
registerd_label.grid(row=0, column=0)
registerd_ckeck.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
    
    
# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2,column=0, sticky='news', padx=20, pady=20)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions")
terms_check.grid(row=0, column=0)

# button
button = tkinter.Button(frame, text="Enter Data" , background='green', command= enter_data)
button.grid(row=3, column=0, sticky='news', padx=10, pady=10)



window.mainloop()