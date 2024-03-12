import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('partyinvites.db')

# Create a new table with the columns: id, name, age
conn.execute('CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

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

'''
Here is what we see in the table:

--------- After inserting names: ---------
(1, 'Andrew', 25)
(2, 'Jad', 35)
(3, 'Warren', 20)
(4, 'Andrew', 10)

Notice the two Andrews are still able to be distinguished due to primary key ID
'''

# For the sake of understanding, let's update Andrew Mao's (ID: 4) name to Andrew M

conn.execute("UPDATE mytable SET name = ? WHERE id = ?", ('Andrew M', 4))
print("--------- After updating Andrew Mao's name: ---------")
printRows()

'''
--------- After updating Andrew Mao's name: ---------
(1, 'Andrew', 25)
(2, 'Jad', 35)
(3, 'Warren', 20)
(4, 'Andrew M', 10)
'''

# Jad had a birthday, let's update his age:
conn.execute("UPDATE mytable SET age = ? WHERE name = ?", (36, 'Jad')) # ALWAYS use the pkey ID for this instead of the name, this is just an example
print("--------- After updating Jad's age: ---------")
printRows()

'''
--------- After updating Jad's age: ---------
(1, 'Beketov', 25)
(2, 'Jad', 36)
(3, 'Warren', 20)
(4, 'Mao', 10)
'''

# What would be a better way of updating his age?
cursor = conn.execute("SELECT age FROM mytable WHERE id = ?", (2,))
# cursor = conn.execute("UPDATE mytable set age WHERE id = ?", (2,))
jadAge = cursor.fetchone() # Dereference the cursor object, without fetchone() we see: Jad age = <sqlite3.Cursor object at 0x0000027C0F1CF640>
# jadAge is now this tuple: (36,)
# print("Jad age =", jadAge[0]) # Use print statements to verify
conn.execute("UPDATE mytable SET age = ? WHERE id = ?", (jadAge[0]+1, 2))
print("--------- After updating Jad's age the better way: ---------")
printRows()
# We now see that we can dynamically update tables WITHOUT hardcoding values... and that Jad had a double bday and is now 2 years older

'''
--------- After updating Jad's age the better way: ---------
(1, 'Andrew', 25)
(2, 'Jad', 37)
(3, 'Warren', 20)
(4, 'Andrew M', 10)
'''

# Ofc, there is an even better way to do this:
# TODO

# Problem statement: I am trying to compile a list of people to invite to my party. The venue only supports people who are 18+ years old. Let's have our database support this restriction:

# Delete data from the table
conn.execute('DELETE FROM mytable WHERE age < ?', (18,)) # Why (18,)?
print("--------- After deleted people under the age of 18: ---------") # Sorry Andrew Mao :(
printRows()

# Commit changes and close the connection
conn.commit()
conn.close()

# Congrats, you now understand the basics of SQL :D