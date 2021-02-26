#!/usr/bin/env python3

import sqlite3


def table_builder(table_name):
    table_name = input("Enter the table name: ")
    conn = sqlite3.connect('challenge.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS {table_name}
    (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
    AGE            INT     NOT NULL,
    ADDRESS        CHAR(50),
    SALARY         REAL);''')
    print("Table created successfully")
    conn.close()
    return table_name



def insert_data(id, employee, age, address, salary):
    id = input("Enter the employee id: ")
    employee = input("Enter the employee name: ")
    age = input("Enter the employee age: ")
    address = input("Enter the employee address: ")
    salary = input("Enter the employee salary: ")
    conn = sqlite3.connect('challenge.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO {table_name} (ID,NAME,AGE,ADDRESS,SALARY) VALUES ({id}, '{name}', {age}, '{address}', {salary})")
    conn.commit()  # you must commit the changes whenever you update a table
    print("Records created successfully")
    conn.close() # always close the table after updating it



def select_data():
    conn = sqlite3.connect('challenge.db')
    id = input("Enter the employee id: ")
    print("Opened database successfully")
    cursor = conn.execute("SELECT {id} from {table_name}") # the Cursor method allows you to fetch data from the database
    row = []
    for row in cursor:
        print(row)
        rows.append(row)
    print("Operation done successfully")
    conn.close()
    return rows



## def update_data(choice):
def udpate_data(employee, age, address, salary):
    conn = sqlite3.connect('challenge.db')
    print("Opened database successfully")
    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()



def delete_data():
    conn = sqlite3.connect('challenge.db')
    print("Opened database successfully")
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()



if __name__ == "__main__":
    table_builder()
    insert_data()
    select_data()
    delete_data()

