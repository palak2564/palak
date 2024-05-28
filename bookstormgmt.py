import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='tiger',database='python')
if con.is_connected():
    print("Successfully established connection to database!")
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS BOOKSHOP")
print("Query executed successfully!")
cur.execute("USE BOOKSHOP")
cur.execute("create table if not exists bookgenres(No integer,Genre_name varchar(50))")
con.commit()
def data_insertion():
    
    #======insert data into genre table===========
    while True:
        no=int(input("Number:"))
        gname=input("Enter name of genre:")
        cur.execute("insert into bookgenres values({},'{}')".format(no,gname))
        con.commit()


    #======Action & Adventure=======
    cur.execute("create table actadv  if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Action & Adventure")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO actadv VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()

    #======Classical Novels=======
    cur.execute("create table cnv  if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Action & Adventure")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO cnv VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()

    #=========Detective & Mystery=========
    cur.execute("create table detmys  if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Detective & Mystery")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO detmys VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()

    #========Fantasy==========
    cur.execute("create table fantasy  if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Fantasy")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO fantasy VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()

    #=======Historical Fiction=======
    cur.execute("create table hisfic if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Historical Fiction")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO hisfic VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()

    #========Horror==========
    cur.execute("create table horror if not exists(Book_No integer,Book_Name varchar(50),Author_Name varchar(50),Book_Price integer,Book_Stock integer)")
    print("TABLE CREATED SUCCESSFULLY!")
    while True:
        print("Horror")
        bookno=int(input("Book no:"))
        bookname=input("Book name:")
        author=input("Author name:")
        bookprice=int(input("Book price:"))
        bookstock=int(input("Book stock available:"))
        cur.execute("INSERT INTO horror VALUES({},'{}','{}',{},{})".format(bookno,bookname,author,bookprice,bookstock))
        con.commit()
def billing_calc():
       

        # setting up the tkinter window
        root = tkinter.Tk()
        root.geometry("450x500+200+200")
        root.resizable(0,0)
        root.title("Calculator")

        val = ""
        A = 0
        operator = ""


        #Hover button
        def entered(event):
            btnc.config(bg="#ff4117")

        def left(event):
            btnc.config(bg="#fc876d")

        def entered_(event):
            btnx.config(bg="#ffd500")

        def left_(event):
            btnx.config(bg="#faed5f")



        # function for numerical button clicked

        def btn_1_isclicked():
            global val
            val = val + "1"
            data.set(val)

        def btn_2_isclicked():
            global val
            val = val + "2"
            data.set(val)

        def btn_3_isclicked():
            global val
            val = val + "3"
            data.set(val)

        def btn_4_isclicked():
            global val
            val = val + "4"
            data.set(val)

        def btn_5_isclicked():
            global val
            val = val + "5"
            data.set(val)

        def btn_6_isclicked():
            global val
            val = val + "6"
            data.set(val)

        def btn_7_isclicked():
            global val
            val = val + "7"
            data.set(val)

        def btn_8_isclicked():
            global val
            val = val + "8"
            data.set(val)

        def btn_9_isclicked():
            global val
            val = val + "9"
            data.set(val)

        def btn_0_isclicked():
            global val
            val = val + "0"
            data.set(val)

        def btn_dot_isclicked():
            global val
            val = val + "."
            data.set(val)


        # functions for the operator button click
        def btn_plus_clicked():
            global A
            global operator,val
            A = float(val)
            operator = "+"
            val = val + "+"
            data.set(val)

        def btn_minus_clicked():
            global A
            global operator,val
            A = float(val)
            operator = "-"
            val = val + "-"
            data.set(val)

        def btn_mult_clicked():
            global A
            global operator,val
            A = float(val)
            operator = "*"
            val = val + "*"
            data.set(val)

        def btn_div_clicked():
            global A
            global operator,val
            A = float(val)
            operator = "/"
            val = val + "/"
            data.set(val)


        def btn_exp_clicked():
            global A
            global operator,val
            A = float(val)
            operator = "^"
            val = val + "^"
            data.set(val)


        def btn_c_pressed():
            global A,operator,val
            val = ""
            A = 0
            operator = ""
            data.set(val)

        def btn_x_pressed():
            global A,operator,val
            v = val[-1]
            val = val[:len(val)-1]
            if v in ['+','-','*','/']:
                operator=""
            operator = ""
            data.set(val)


        # function to find the result
        def result():
            global A,operator,val
            val2 = val
            if operator == "+":
                x = float((val2.split("+")[1]))
                C = A + x
                val = str(C)
                data.set(val)
            elif operator == "-":
                x = float((val2.split("-")[1]))
                C = A - x
                val = str(C)
                data.set(val)
            elif operator == "*":
                x = float((val2.split("*")[1]))
                C = A * x
                val = str(C)
                data.set(val)
            elif operator == "/":
                x = float((val2.split("/")[1]))
                if x == 0:
                    messagebox.showerror("Error", "Division By 0 Not Supported")
                    A = ""
                    val = ""
                    data.set(val)
                else:
                    C = A / x
                    data.set(C)
            elif operator == "^":
                x = float((val2.split("^")[1]))
                C = A ** x
                val = str(C)
                data.set(val)
            else:
                #print(1)
                if '+' in val2 or '-' in val2 or '*' in val2 or '/' in val2 or '^' in val2:
                    return
                #print(2)
                x=float(val2)
                C = x * x
                val = str(C)
                data.set(val)

        # the label that shows the result
        data = StringVar()
        lbl = Label(
            root,
            text = "Label",
            anchor = SE,
            font = ("Verdana", 20),
            textvariable = data,
            background = "#ffffff",
            fg = "#000000",
        )
        lbl.pack(expand = True, fill = "both")

        # the frames section
        btnrow0 = Frame(root)
        btnrow0.pack(expand = True, fill = "both")

        btnrow1 = Frame(root)
        btnrow1.pack(expand = True, fill = "both")

        btnrow2 = Frame(root)
        btnrow2.pack(expand = True, fill = "both")

        btnrow3 = Frame(root)
        btnrow3.pack(expand = True, fill = "both")

        btnrow4 = Frame(root)
        btnrow4.pack(expand = True, fill = "both")


        # The buttons section
        # button for frame 0
        btnc = Button(
            btnrow0,
            text = "C",
            font = ("Verdana", 22),
            bg = "#fc876d",
            relief = GROOVE,
            border = 0,
            command = btn_c_pressed,
        )
        btnc.pack(side = LEFT, expand = True, fill = "both",)
        btnc.bind("<Enter>",entered)
        btnc.bind("<Leave>", left)


        btnx = Button(
            btnrow0,
            text = "Del",
            font = ("Verdana", 22),
            bg="#faed5f",
            relief = GROOVE,
            border = 0,
            command = btn_x_pressed,
        )
        btnx.pack(side = LEFT, expand = True, fill = "both",)
        btnx.bind("<Enter>",entered_)
        btnx.bind("<Leave>", left_)

        btnpower = Button(
            btnrow0,
            text = "exp",
            font = ("Verdana", 22),
            bg = "#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_exp_clicked,
        )
        btnpower.pack(side = LEFT, expand = True, fill = "both",)

        btnsq = Button(
            btnrow0,
            text = "sq",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = result,
        )
        btnsq.pack(side = LEFT, expand = True, fill = "both",)


        # button for frame 1
        btn1 = Button(
            btnrow1,
            text = "1",
            font = ("Verdana", 22),
            bg = "#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_1_isclicked,
        )
        btn1.pack(side = LEFT, expand = True, fill = "both",)

        btn2 = Button(
            btnrow1,
            text = "2",
            font = ("Verdana", 22),
            bg = "#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_2_isclicked,
        )
        btn2.pack(side = LEFT, expand = True, fill = "both",)

        btn3 = Button(
            btnrow1,
            text = "3",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_3_isclicked,
        )
        btn3.pack(side = LEFT, expand = True, fill = "both",)

        btnplus = Button(
            btnrow1,
            text = "+",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_plus_clicked,
        )
        btnplus.pack(side = LEFT, expand = True, fill = "both",)

        # buttons for frame 2

        btn4 = Button(
            btnrow2,
            text = "4",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_4_isclicked,
        )
        btn4.pack(side = LEFT, expand = True, fill = "both",)

        btn5 = Button(
            btnrow2,
            text = "5",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_5_isclicked,
        )
        btn5.pack(side = LEFT, expand = True, fill = "both",)

        btn6 = Button(
            btnrow2,
            text = "6",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_6_isclicked,
        )
        btn6.pack(side = LEFT, expand = True, fill = "both",)

        btnminus = Button(
            btnrow2,
            text = "-",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_minus_clicked,
        )
        btnminus.pack(side = LEFT, expand = True, fill = "both",)

        # button for frame 3

        btn7 = Button(
            btnrow3,
            text = "7",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_7_isclicked,
        )
        btn7.pack(side = LEFT, expand = True, fill = "both",)

        btn8 = Button(
            btnrow3,
            text = "8",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_8_isclicked,
        )
        btn8.pack(side = LEFT, expand = True, fill = "both",)

        btn9 = Button(
            btnrow3,
            text = "9",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_9_isclicked,
        )
        btn9.pack(side = LEFT, expand = True, fill = "both",)

        btnmult = Button(
            btnrow3,
            text = "*",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_mult_clicked,
        )
        btnmult.pack(side = LEFT, expand = True, fill = "both",)

        # button for frame4
        btndot = Button(
            btnrow4,
            text = ".",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_dot_isclicked,
        )
        btndot.pack(side = LEFT, expand = True, fill = "both",)


        btn0 = Button(
            btnrow4,
            text = "0",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_0_isclicked,
        )
        btn0.pack(side = LEFT, expand = True, fill = "both",)

        btnequal = Button(
            btnrow4,
            text = "=",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = result,
        )
        btnequal.pack(side = LEFT, expand = True, fill = "both",)

        btndiv = Button(
            btnrow4,
            text = "/",
            font = ("Verdana", 22),
            bg="#b9ebfa",
            relief = GROOVE,
            border = 0,
            command = btn_div_clicked,
        )
        btndiv.pack(side = LEFT, expand = True, fill = "both",)

        root.mainloop()

    
#Main Menu
while True:
    print("1:Signup")
    print("2:Login")
    ch=int(input("SIGNUP/LOGIN(1,2):"))
    cur.execute("create table if not exists signup(username varchar(20),password varchar(20))")
    if ch==1:
        username=input("USERNAME:")
        pw=input("PASSWORD:")
        
        cur.execute("insert into signup values('"+username+"','"+pw+"')")
        con.commit()

    elif ch==2:
        username=input("USERNAME:")
        cur.execute("select username from signup where username='"+username+"'")
        pot=cur.fetchone()

        if pot is not None:
            print("VALID USERNAME!!!!!!")
            pw=input("PASSWORD:")
            cur.execute("select password from signup where password='"+pw+"'")
            a=cur.fetchone()

            if a is not None:
                print("LOGIN SUCCESSFULL!")
                print("""==============MY BOOK STORE================""")
                print("1.Insert/Edit store data")
                print("2.Make purchase")
                print("3.Billing")
                pv=int(input("Enter your choice(1/2/3):"))
                if pv==1:
                    data_insertion()
                elif pv==2:
                    print("Hello!")
                    print("Welcome!")
                    print("========BOOK GENRES=========")
                    print("1.Action & Adventure")            
                    print("2.Classical Novels")              
                    print("3.Detective & Mystery ")          
                    print("4.Fantasy")                       
                    print("5.Historical Fiction")           
                    print("6.Horror")
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        print("Action & Adventure")
                        cur.execute("select * from actadv")
                        data=cur.fetchall()
                        print(type(data))
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break
                          

                    elif choice==2:
                        print("Classical Novels")
                        cur.execute("select * from cnv")
                        data=cur.fetchall()
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break


                    elif choice==3:
                        print("Detective & Mystery")
                        cur.execute("select * from detmys")
                        data=cur.fetchall()
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break
                            

                    elif choice==4:
                        print("Fantasy")
                        cur.execute("select * from fantasy")
                        data=cur.fetchall()
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break


                    elif choice==5:
                        print("Historical Fiction")
                        cur.execute("select * from hisfic")
                        data=cur.fetchall()
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break  


                    elif choice==6:
                        print("Horror")
                        cur.execute("select * from horror")
                        data=cur.fetchall()
                        for i in data:
                            print(data,sep="<-")
                            cur.execute("USE BOOKSHOP")
                            name=input("Enter your name:")
                            phn_no=int(input("Enter your phone number:"))
                            no=int(input("Enter the number of book you want to buy:"))
                            if no==data[1]:
                                print("ok")
                            price=int(input("Enter the price of the book:"))
                            qty=int(input("Enter the product quantity you want to buy:"))
                            cost=price*qty
                            cur.execute("create table if not exists consumer(name varchar(50),phn_no char(10),no integer,price integer,qty integer,cost integer)")
                            print("Table created successfully!")
                            cur.execute("insert into consumer values('{}','{}',{},{},{},{})".format(name,phn_no,no,price,qty,cost))
                            con.commit()
                            ask=input(("Do you want to continue?"))
                            if ask=='n' or 'no' or 'N' or 'No':
                                break
                    
                elif pv==3:
                    print("============BILLING=========")
                    no=int(input("Enter the phone number of the customer:"))
                    cur.execute("select * from consumer where phn_no='"+str(no)+"'")
                    pov=cur.fetchall()
                    for data in pov:
                        print(data)
                        billing_calc()
            
                else:
                        print("Invalid request!")
                        break
