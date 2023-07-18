#importing our pop up window from tkinter
import tkinter
from tkinter import messagebox #pop up box appears outside our window
#Import required packages
import hashlib
import urllib.request

window = tkinter.Tk()
window.title("password cracker")
#popup window size in width and height
window.geometry('340x440')
#main frame bg color dark slate gray
window.configure(bg='#2F2F4F')


def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


     
#inner frame color dark slate, placing all our widgets inside a frame for better UI exterience
frame = tkinter.Frame(bg='#2F2F4F') #frame is our tkinter container inside window for responsivness on larger screen size



# Creating widgets using grid (login created using pack above grid)
#Parent is window and text is username followed by another parent window and text password 
#x3 labels as static text on our password cracker screen 
#multiple attributes used to style our pop up window bg(background) fg(foreground)
login_label = tkinter.Label(
    frame, text="Login", bg='#52528B', fg="#FFFF14", font=("Arial", 28))
username_label = tkinter.Label(
    frame, text="Username", bg='#52528B', fg="#FFFF14", font=("Arial", 18))
username_entry = tkinter.Entry(frame, font=("Arial", 18))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 18))
password_label = tkinter.Label(
    frame, text="Password", bg='#52528B', fg="#FFFF14", font=("Arial", 18))
login_button = tkinter.Button( #command used to execute when button is clicked
    frame, text="Login", bg='#FFFFEF', fg="#272740", font=("Arial", 20), command=login)

# Placing widgets on the screen using grid which has 4 rows and 2 columns, starting at zero, 1, 2  & 3
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)#Pad(y) adding spaceing on y axis
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30) #spacing of login button on y axis

#using pack to make our pop up window responsive when you change the sizing to larger screen to look centralised
frame.pack()

#window.mainloop allows Tkinter to run and display our pop up window. Placed at the end of our password cracker code
window.mainloop()