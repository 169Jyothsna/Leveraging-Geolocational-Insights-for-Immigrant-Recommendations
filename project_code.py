from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser

app = tk.Tk()
app.geometry("750x250")
app.title("Geolocational Insights for Immigrant Recommendations")

bg = tk.PhotoImage(file="C:/Users/jyoth/OneDrive/Documents/MCA/Project/image1.png")
myLabel = Label(app, image=bg)
myLabel.place(x=0, y=0)

def open_browser(city):
    file_path = f"C:/Users/jyoth/Downloads/{city}.html"
    webbrowser.open_new(f"file:///{file_path}")

cities = ("Bangalore", "Chennai", "Delhi", "Gurgaon", "Hyderabad", "Kolkata", "Mumbai")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

cb1 = ttk.Combobox(app, values=cities, width=10, font="Verdana 16")
cb1.place(x=280, y=100)

def go():
    selected_city = cb1.get()
    open_browser(selected_city)

b1 = tk.Button(app, text='Go', command=go, font="16")
b1.place(x=445,  y=100)
cb1.set("Select City")

app.mainloop()
