import tkinter as tk
from datetime import date

def age_calc():
    curdate = date.today()
    birthday = date(int(year_entry.get()),int(month_entry.get()),int(date_entry.get()))
    age = curdate.year-birthday.year
    if curdate.month < birthday.month:
        age -= 1
    elif curdate.month == birthday.month and  curdate.day < birthday.day:
        age -=1
    age_entry.insert(0,age)
    

root = tk.Tk()

root.title("Age Calculator")

date_label = tk.Label(root,text = "Day")
date_entry = tk.Entry(root)

month_label = tk.Label(root, text = "Month")
month_entry = tk.Entry(root)

year_label = tk.Label(root,text = "year")
year_entry = tk.Entry(root)

age_label = tk.Label(root,text="age")
age_entry = tk.Entry(root)

button = tk.Button(root, text = "calculate", command=age_calc)

date_label.pack()
date_entry.pack()
month_label.pack()
month_entry.pack()
year_label.pack()
year_entry.pack()
age_label.pack()
age_entry.pack()
button.pack()

root.mainloop()