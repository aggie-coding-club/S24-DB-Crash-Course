import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('partyinvitestmpl.db')


# Problem statement: I am trying to compile a list of people to invite to my party. The venue only supports people who are 18+ years old. Create a DB table with a list of all names and ages of people that will come


# TODO: Create a new table called mytable with the columns: id, name, age
conn.execute('')

# Insert into the table some data
conn.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ('Andrew', 25))
conn.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ('Jad', 35))
conn.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ('Warren', 20))
conn.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ('Andrew', 10))


# Now let's verify that everything was inserted correctly; let's use a cursor for this. We'll make this a function so we can call it whenever convenient
def printRows():
    cursor = conn.execute('SELECT * FROM mytable') # * means all. This line can be translated as SELECT ALL FROM mytable
    for row in cursor:
        print(row)
    print()
    
print("--------- After inserting names: ---------")
printRows()

# TODO: Update some data to make it more readable and easily understood, change Andrew at ID 4's name to 'Andrew M'
conn.execute('')

# TODO: Jad had a birthday, increase his age by 1
conn.execute('')

# TODO: Delete data from the table, remove anyone under the age of 18 to adhere to party restrictions (Hint: '... age < ?')
conn.execute('')


# Verify the final party list
print("--------- Final Party List: ---------")
printRows()


# Commit changes and close the connection (Uncomment this when done so that there are no repeating items in the table upon reruns of the program):
# conn.commit()
# conn.close()
