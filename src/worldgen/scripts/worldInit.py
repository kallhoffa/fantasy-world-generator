import sqlite3
import yaml

def world_init(world = "default"):
    print(world)

world_init()

conn = sqlite3.connect('test.db')

print ("Opened database successfully");


#
# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print "Table created successfully";
#
# conn.close()