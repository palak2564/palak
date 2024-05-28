import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

def establish_connection():
    try:
        con = sql.connect(host='localhost', user='root', password='tiger', database='python')
        if con.is_connected():
            print("Successfully established connection to database!")
        return con
    except sql.Error as err:
        print(f"Error: {err}")
        return None

def create_database_and_tables(cur):
    cur.execute("CREATE DATABASE IF NOT EXISTS BOOKSHOP")
    print("Query executed successfully!")
    cur.execute("USE BOOKSHOP")
    cur.execute("CREATE TABLE IF NOT EXISTS bookgenres(No INTEGER, Genre_name VARCHAR(50))")
    con.commit()
    print("Table bookgenres created successfully!")

def data_insertion(cur, con):
    while True:
        no = int(input("Number:"))
        gname = input("Enter name of genre:")
        cur.execute("INSERT INTO bookgenres VALUES (%s, %s)", (no, gname))
        con.commit()
        if input("Continue inserting genres? (y/n): ").lower() != 'y':
            break

    table_names = {
        "Action & Adventure": "actadv",
        "Classical Novels": "cnv",
        "Detective & Mystery": "detmys",
        "Fantasy": "fantasy",
        "Historical Fiction": "hisfic",
        "Horror": "horror"
    }

    for genre, table in table_names.items():
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table} (Book_No INTEGER, Book_Name VARCHAR(50), Author_Name VARCHAR(50), Book_Price INTEGER, Book_Stock INTEGER)")
        print(f"Table {table} created successfully!")
        while True:
            print(genre)
            bookno = int(input("Book no:"))
            bookname = input("Book name:")
            author = input("Author name:")
            bookprice = int(input("Book price:"))
            bookstock = int(input("Book stock available:"))
            cur.execute(f"INSERT INTO {table} VALUES (%s, %s, %s, %s, %s)", (bookno, bookname, author, bookprice, bookstock))
            con.commit()
            if input(f"Continue inserting books in {genre}? (y/n): ").lower() != 'y':
                break

def billing_calc():
    root = tkinter.Tk()
    root.geometry("450x500+200+200")
    root.resizable(0, 0)
    root.title("Calculator")

    val = ""
    A = 0
    operator = ""

    def entered(event, btn):
        btn.config(bg="#ff4117")

    def left(event, btn):
        btn.config(bg="#fc876d")

    def entered_(event, btn):
        btn.config(bg="#ffd500")

    def left_(event, btn):
        btn.config(bg="#faed5f")

    def num_btn_clicked(number):
        nonlocal val
        val = val + str(number)
        data.set(val)

    def operator_btn_clicked(op):
        nonlocal A, operator, val
        A = float(val)
        operator = op
        val = val + op
        data.set(val)

    def btn_c_pressed():
        nonlocal A, operator, val
        val = ""
        A = 0
        operator = ""
        data.set(val)

    def btn_x_pressed():
        nonlocal operator, val
        val = val[:-1]
        if not any(op in val for op in ['+', '-', '*', '/']):
            operator = ""
        data.set(val)

    def result():
        nonlocal A, operator, val
        try:
            val2 = val.split(operator)
            if operator == "+":
                C = A + float(val2[1])
            elif operator == "-":
                C = A - float(val2[1])
            elif operator == "*":
                C = A * float(val2[1])
            elif operator == "/":
                C = A / float(val2[1]) if float(val2[1]) != 0 else float('inf')
            elif operator == "^":
                C = A ** float(val2[1])
            else:
                C = A * A
            val = str(C)
            data.set(val)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid operation: {e}")
            btn_c_pressed()

    data = StringVar()
    lbl = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable=data, background="#ffffff", fg="#000000")
    lbl.pack(expand=True, fill="both")

    btn_row_frames = [Frame(root) for _ in range(5)]
    for frame in btn_row_frames:
        frame.pack(expand=True, fill="both")

    buttons = [
        {'text': 'C', 'row': 0, 'col': 0, 'bg': "#fc876d", 'cmd': btn_c_pressed, 'hover': (entered, left)},
        {'text': 'Del', 'row': 0, 'col': 1, 'bg': "#faed5f", 'cmd': btn_x_pressed, 'hover': (entered_, left_)},
        {'text': 'exp', 'row': 0, 'col': 2, 'bg': "#b9ebfa", 'cmd': lambda: operator_btn_clicked("^")},
        {'text': 'sq', 'row': 0, 'col': 3, 'bg': "#b9ebfa", 'cmd': result},
        *({'text': str(i), 'row': (i-1)//3+1, 'col': (i-1)%3, 'bg': "#b9ebfa", 'cmd': lambda x=i: num_btn_clicked(x)} for i in range(1, 10)),
        {'text': '+', 'row': 1, 'col': 3, 'bg': "#b9ebfa", 'cmd': lambda: operator_btn_clicked("+")},
        {'text': '-', 'row': 2, 'col': 3, 'bg': "#b9ebfa", 'cmd': lambda: operator_btn_clicked("-")},
        {'text': '*', 'row': 3, 'col': 3, 'bg': "#b9ebfa", 'cmd': lambda: operator_btn_clicked("*")},
        {'text': '.', 'row': 4, 'col': 0, 'bg': "#b9ebfa", 'cmd': lambda: num_btn_clicked(".")},
        {'text': '0', 'row': 4, 'col': 1, 'bg': "#b9ebfa", 'cmd': lambda: num_btn_clicked("0")},
        {'text': '=', 'row': 4, 'col': 2, 'bg': "#b9ebfa", 'cmd': result},
        {'text': '/', 'row': 4, 'col': 3, 'bg': "#b9ebfa", 'cmd': lambda: operator_btn_clicked("/")}
    ]

    for btn_info in buttons:
        btn = Button(btn_row_frames[btn_info['row']], text=btn_info['text'], font=("Verdana", 22), bg=btn_info['bg'],
                     relief=GROOVE, border=0, command=btn_info['cmd'])
        btn.pack(side=LEFT, expand=True, fill="both")
        if 'hover' in btn_info:
            btn.bind("<Enter>", lambda event, b=btn: btn_info['hover'][0](event, b))
            btn.bind("<Leave>", lambda event, b=btn: btn_info['hover'][1](event, b))

    root.mainloop()

def main_menu(cur, con):
    while True:
        print("1: Signup")
        print("2: Login")
        ch = int(input("SIGNUP/LOGIN (1,2): "))
        cur.execute("CREATE TABLE IF NOT EXISTS signup(username VARCHAR(20), password VARCHAR(20))")
        if ch == 1:
            username = input("USERNAME: ")
            pw = input("PASSWORD: ")
            cur.execute("INSERT INTO signup VALUES (%s, %s)", (username, pw))
            con.commit()
        elif ch == 2:
            username = input("USERNAME: ")
            cur.execute("SELECT username FROM signup WHERE username=%s", (username,))
            if cur.fetchone():
                print("VALID USERNAME!")
                pw = input("PASSWORD: ")
                cur.execute("SELECT password FROM signup WHERE password=%s", (pw,))
                if cur.fetchone():
                    print("LOGIN SUCCESSFUL!")
                    print("""==============MY BOOK STORE================""")
                    print("1. Insert/Edit store data")
                    print("2. Make purchase")
                    print("3. Billing")
                    pv = int(input("Enter your choice (1/2/3): "))
                    if pv == 1:
                        data_insertion(cur, con)
                    elif pv == 2:
                        make_purchase(cur, con)
                    elif pv == 3:
                        billing_calc()

def make_purchase(cur, con):
    print("Hello!")
    print("Welcome!")
    print("========BOOK GENRES=========")
    genres = ["Action & Adventure", "Classical Novels", "Detective & Mystery", "Fantasy", "Historical Fiction", "Horror"]
    for idx, genre in enumerate(genres, start=1):
        print(f"{idx}. {genre}")
    choice = int(input("Enter your choice (1/2/3/4/5/6): "))
    genre_table = {
        1: "actadv",
        2: "cnv",
        3: "detmys",
        4: "fantasy",
        5: "hisfic",
        6: "horror"
    }
    selected_table = genre_table.get(choice)
    if selected_table:
        cur.execute(f"SELECT * FROM {selected_table}")
        books = cur.fetchall()
        for book in books:
            print(book)
        print("What would you like to purchase?")
        bookno = int(input("Enter book number: "))
        cur.execute(f"SELECT Book_Name, Book_Price FROM {selected_table} WHERE Book_No = %s", (bookno,))
        book = cur.fetchone()
        if book:
            print(f"Book Name: {book[0]}, Price: {book[1]}")
            print("Thank you for your purchase!")
        else:
            print("Book not found!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    con = establish_connection()
    if con:
        cur = con.cursor()
        create_database_and_tables(cur)
        main_menu(cur, con)
        cur.close()
        con.close()
