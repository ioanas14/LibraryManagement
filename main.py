from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *

mypass = "Soare141225"
mydatabase = "db"  # The database name
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
current = con.cursor()

root = Tk()
root.title("My library")
root.minsize(width=400, height=400)
root.maxsize(width=800, height=800)
root.geometry("800x800")

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

background_image = background_image.resize((imageSizeWidth, imageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=imageSizeWidth, height=imageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#7d3a16", bd=3)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Ioana's Library!", bg='black', fg='white', font=('Times New Roman',20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

addButton = Button(root, text="Add Book Details", bg='black', fg='white', font=('Times New Roman',15), command=addBook)
addButton.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

deleteButton = Button(root, text="Delete Book", bg='black', fg='white', font=('Times New Roman',15))
deleteButton.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

viewButton = Button(root, text="View Book List", bg='black', fg='white', font=('Times New Roman',15), command=viewBooks)
viewButton.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)



def changeOnHover(button, colorOnHover):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background='black'))

changeOnHover(addButton, "#995d32")
changeOnHover(deleteButton, "#995d32")
changeOnHover(viewButton, "#995d32")

root.mainloop()