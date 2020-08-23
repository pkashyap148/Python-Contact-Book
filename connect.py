import sqlite3

# Create Connection and database
con = sqlite3.connect('phone')

# create cursor
c = con.cursor()


# create table
#try:
#    c.execute("""
#        CREATE TABLE contacts(
#            name TEXT,
#            number INTEGER
#        )
#    """)
#    print("Table Created")
#
#except:
#    print("Error while creating table")