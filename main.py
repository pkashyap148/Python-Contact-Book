from connect import c,con

print("Welcome to Contact Book")
print("Select from given options")
print("1 => Add")
print("2 => Show")
print("3 => Delete")

def show():
    ask = input("Enter Name of Person or just Hit Enter to see all contacts: ")
    if ask != "":
        try:
            c.execute("SELECT * FROM contacts WHERE name = ?", (ask,))
            x = c.fetchall()
            for item in x:
                print("Name: ", item[0], ", Phone: ", item[1])
            input("Hit Enter to Exit")
        except:

            print("Error while retrieving contact")
            input("Hit Enter to Exit")
    else:
        try:
            c.execute("SELECT * FROM contacts")
            x = c.fetchall()
            if len(x) == 0:
                print("There is no contact in list")
                input("Hit Enter to Exit")
            else:
                for item in x:
                    print("Name: ", item[0], ", Phone: ", item[1])
        except:
            print("Error while retrieving contact")
            input("Hit Enter to Exit")

def add():
    name = input("Enter Name: ")
    num = input("Enter Contact Number: ")
    try:
        c.execute("INSERT INTO contacts VALUES (?, ?)", (name, num))
        con.commit()
        print("Contact Saved")
        input("Hit Enter to Exit")
    except:
        print("Error while inserting contact")
        input("Hit Enter to Exit")

def delete():
    ask = input("Enter Name of Person: ")
    if ask != "":
        try:
            c.execute("DELETE FROM contacts WHERE name = ?", (ask,))
            con.commit()
            print("Contact Deleted")
            input("Hit Enter to Exit")
        except:
            print("Error while deleting contact")
            input("Hit Enter to Exit")


cmd = input("Enter the Command: ")

if cmd == "1":
    add()
elif cmd == "2":
    show()
elif cmd == "3":
    delete()

