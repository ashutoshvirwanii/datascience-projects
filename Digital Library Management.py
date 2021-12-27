#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc 
con = pyodbc.connect('''Driver={SQL Server};
                      Server=LAPTOP-B5MVUCO8;
                      Database=Books;
                      Trusted_Connection=yes''')


# In[ ]:





# In[2]:


def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    
    
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#7d8eff")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#000e66",bd=5)
    headingFrame1.place(relx=0.10,rely=0.1,relwidth=0.8,relheight=0.11)
        
    headingLabel = Label(headingFrame1, text="VIEW BOOK LIST", bg='black', fg='white', font=('Impact',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=1.0)
    y = 0.25
    
    Label(labelFrame, text="%-15s%-30s%-30s%-20s"%('BID','Title','Author','Status'),
          bg='black',fg='white', font=('Arial', 14)).place(relx=0.10,rely=0.1)
    Label(labelFrame, text="------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.10,rely=0.15)
          
    getBooks = "select * from "+bookTable
   
    try:
        cur.execute(getBooks)
        #con.commit()
        for i in cur:
            Label(labelFrame, text="%-15s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.10,rely=y)
            y += 0.05
    except pyodbc.Error as e:
        messagebox.showinfo("Failed to fetch files from database", e)
    
    quitBtn = Button(root,text="EXIT",bg='#000e66', font = ('poppins',15,'bold'), fg='White', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


# In[ ]:





# In[3]:


# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allBid = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()

    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)
        #con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            #con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except pyodbc.Error as e:
        messagebox.showinfo("Error","Can't fetch Book IDs", e)
    
    
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
  
    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except pyodbc.Error as e:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again", e)
    
    
    allBid.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff8080")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#3d0000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='white', fg='Black', font=('Impact',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ",font = ('Poppins', 12), bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="RETURN",bg='#3d0000', fg='white', font = ('Poppins', 15, 'bold'),command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#3d0000', fg='white', font = ('Poppins', 15, 'bold'), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


# In[4]:


# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        #con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            #con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except pyodbc.Error as e:
        messagebox.showinfo("Error","Can't fetch Book IDs",e)
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#fffa70")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#969100",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue A Book", bg='White', fg='Black', font=('Impact',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ",font = ('Poppins',12),  bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="ISSUE",bg='#969100', fg='white',font = ('Poppins',15, 'bold'), border =0,command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#969100', fg='white', font = ('Poppins',15, 'bold'), border =0, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


# In[5]:


# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    messagebox.showinfo('Delete', 'Deleting book with id :- '+bid)
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        
        cur.execute(deleteIssue)
        con.commit()
        
        cur.execute(deleteSql)
        con.commit()
        
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except pyodbc.Error as e:
        messagebox.showinfo("Please check Book ID",e)
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#63ffe2")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#004538",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete A Book", bg='White', fg='Black', font=('Impact',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", font = ('Poppins',12), bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#004538', font = ('Poppins',15,'bold'), fg='White',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#004538', font = ('Poppins',15,'bold'), fg='White', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


# In[6]:


def bookRegister():
    Book_info = "books" # Book Table
    Book_ID = bookInfo1.get()
    Book_Name = bookInfo2.get()
    Book_author = bookInfo3.get()
    Book_available = bookInfo4.get()
    #Book_available = status.lower()
    
    #con = pyodbc.connect('''Driver={SQL Server};
    #                  Server=tcp:LENOVO-E41-15\GAVRIL;
    #                  Database=test1;
    #                  UID=admin;
    #                  PWD=admin;
    #                  Trusted_Connection=yes''')
    #con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    insertBooks = "insert into "+Book_info+" values('"+Book_ID+"','"+Book_Name+"','"+Book_author+"','"+Book_available+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except pyodbc.Error as e:
        messagebox.showinfo("Can't add data into Database", e)
    #cur.close
    #con.close
    print(Book_ID)
    print(Book_Name)
    print(Book_author)
    print(Book_available)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    #mypass = "root"
    #mydatabase="db"

    con = pyodbc.connect('''Driver={SQL Server};
                      Server=LAPTOP-B5MVUCO8;
                      Database=Books;
                      Trusted_Connection=yes''')
    #con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    Book_info = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#d980ff")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#1e002b", border = 5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

   # addbk = PhotoImage(file = 'C:/Users/Gavril/Pictures/newbook.png')
    headingLabel = Label(headingFrame1,text="Add A New Book", font = ('Poppins', 25), bg='White', fg='Black')
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", font = ('Poppins', 12), bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", font = ('Poppins', 12), bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame, border = 1)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", font = ('Poppins', 12), bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", font = ('Poppins', 11), bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    #submit_btn = PhotoImage(file = 'C:/Users/Gavril/Pictures/nbsubmit.png')
    SubmitBtn = Button(root,text="SUBMIT",font = ('Arial', 15, 'bold'), bg='#1e002b', fg='White', border =0,command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #quit_btn = PhotoImage(file = 'C:/Users/Gavril/Pictures/nbquit.png')
    quitBtn = Button(root,image = quit_btn, border = 0, command=root.destroy)
    quitBtn = Button(root,text="QUIT", font = ('Arial', 15, 'bold'), bg='#1e002b', fg='White', border =0, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


# In[ ]:


root = Tk()
root.title("Library system")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
#background_image =Image.open("C:/Users/Gavril/Downloads/sqlpython project/lib.jpg")
#[imageSizeWidth, imageSizeHeight] = background_image.size

#newImageSizeWidth = int(imageSizeWidth*n)
#if same:
#    newImageSizeHeight = int(imageSizeHeight*n) 
#else:
    #newImageSizeHeight = int(imageSizeHeight/n) 
 #   
#background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
#img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

#Canvas1.create_image(300,340,image = img) 
#imgbg = PhotoImage(file = 'C:/Users/Gavril/Pictures/Design/spd.png')
Canvas1.config(bg = 'white', width = 1000, height = 500)
Canvas1.pack(expand=True,fill=BOTH)



headingFrame1 = Frame(root,bd=0, bg ='White')
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.25)

img = PhotoImage(file = 'D:/Downloads/label.png')
headingLabel = Label(headingFrame1, image = img, bg ='White')
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


#headingLabel = Label(headingFrame1, text="LibrarianM \n by Gavril", fg='#001757', font=('Impact',25))
#headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

view_btn = PhotoImage(file = "D:/Downloads/Viewbook.png")
btn1 = Button(root, image = view_btn, border = 0, bg ='White', command=View)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

add_btn = PhotoImage(file = "D:/Downloads/addbook.png")
btn1 = Button(root, image = add_btn, border = 0, bg ='White', command=addBook)
btn1.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)


issue_btn = PhotoImage(file = "D:/Downloads/issuebook.png")   
btn3 = Button(root,image = issue_btn, border = 0, bg ='White', command=issueBook)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

delete_btn = PhotoImage(file = "D:/Downloads/deletebook.png")
btn4 = Button(root,image = delete_btn, border = 0, bg ='White', command = delete)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

return_btn = PhotoImage(file = "D:/Downloads/returnbook.png")
btn5 = Button(root,image = return_btn, border = 0, bg ='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()


# In[ ]:





# In[ ]:




