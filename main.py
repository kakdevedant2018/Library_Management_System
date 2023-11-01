
# importing the modules
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

#Connecting to the MySql server
#Python MySQL client library it is a Python package that creates an API interface for us to access MySQL relational databases. 

mypass = "password" #use your own password
mydatabase="db" #The database name

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)

#root is the username here


cur = con.cursor() #cur -> cursor


# Designing the Window
# Python with tkinter is the fastest and easiest way to create the GUI applications.

# Creating an object and invoking the constructor
root = Tk()
root.title("Library") # this will set title of the window as Library.
root.minsize(width=400,height=400)
root.geometry("600x500")


# Adding a Background Image

same=True
n=0.25

background_image =Image.open("/home/vedantk/snap/firefox/common/Downloads/stockholm-sweden-april-22-2017-260nw-625928870.webp")  # we are using open method to store the store the image.

[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(600,500,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)




#  Setting up the Head Frame

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)



# Adding the Buttons

#Following code snippet will add the add book button 

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

# Following code snippet will add the Delete book button on page.

btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

#

btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

#

btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

#

btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnn)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

# The root.mainloop() call at the end of the script starts the main event loop, which listens for user interactions and keeps the GUI application running. When you close the main window, the event loop exits, and the application terminates.

root.mainloop()





