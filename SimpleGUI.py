from tkinter import *

root = Tk()

# ---Definitions----------------------------------------------------

header = Label(root, text='User Information', bg='blue', fg='white')

f_name = Label(root, text='First Name: ')
l_name = Label(root, text='Last Name: ')
user_age = Label(root, text='Age: ')
user_height = Label(root, text='Height(in): ')
user_weight = Label(root, text='Weight(lbs): ')

f_name_entry = Entry(root)
l_name_entry = Entry(root)
user_age_entry = Entry(root)
user_height_entry = Entry(root)
user_weight_entry = Entry(root)

# ---Layout---------------------------------------------------------------

header.grid(row=0)

f_name.grid(row=1, column=0, sticky=E)
l_name.grid(row=2, column=0, sticky=E)
user_age.grid(row=3, column=0, sticky=E)
user_height.grid(row=4, column=0, sticky=E)
user_weight.grid(row=5, column=0, sticky=E)


f_name_entry.grid(row=1, column=1)
l_name_entry.grid(row=2, column=1)
user_age_entry.grid(row=3, column=1)
user_height_entry.grid(row=4, column=1)
user_weight_entry.grid(row=5, column=1)


# ------------------------------------------------------------------------------------------

root.mainloop()
