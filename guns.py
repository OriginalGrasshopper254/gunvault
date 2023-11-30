import sqlite3
import os.path
import time

path = '/Users/kenyantrapper/Coding/firearms/gunvault.db'
hashtags = '############################################'


def check_database_exists():

    if os.path.isfile(path) == True:
        print('Connected to database!')
        return True
    else:
        try:
            con = sqlite3.connect('gunvault.db')
            cur = con.cursor()
            print("Database doesn't exists. Let me create one.")
            print(hashtags)
            print('Database created!')
            print(hashtags)
            cur.execute("""CREATE TABLE gunvault(brand, model, caliber, serial)""")
            print("Table 'gunvault' created.")
            print('Program will close, Please Re-run')
        except sqlite3.Error as error:
            print(f"Something went wrong, here's what I know. \n>: {error}")

def add_gun(brand, model, caliber, serial):
    con = sqlite3.connect('gunvault.db')
    cur = con.cursor()
    confirm_serial = input('Please confirm serial >: ')
    if confirm_serial == serial:
        try:
            cur.execute("""INSERT INTO gunvault VALUES (?, ?, ?, ?)""", (brand, model, caliber, serial,))
            con.commit()
            con.close()
        except Exception as error:
            print(f'Something went wrong. Here is what I know. \n>: {error}')
    else:
        print("serial doesn't match.")

def delete_gun(serial):
    con = sqlite3.connect('gunvault.db')
    cur = con.cursor()
    try:
        cur.execute(""" DELETE FROM gunvault WHERE serial=(?)""", (serial,))
        con.commit()
        con.close()
    except Exception as error:
        print(f'Something went wrong. This is what I know \n>: {error}')

def show_all():
    con = sqlite3.connect('gunvault.db')
    cur = con.cursor()
    try:
        for row in cur.execute(""" SELECT * FROM gunvault ORDER BY brand """):
            print('\n',row)
            print('\n')
    except Exception as error:
        print(f'Something went wront, what I know is this: \n>: {error}')

var = 5
while var <= 5:

    if check_database_exists() == True:
        print('''What would you like to do ?
        1: Add a new firearm.
        2: Remove a firearm.
        3. Show all firearms.
        4. Close Gunvault. \n''')
        menu_selection = input('>: ')

        if menu_selection == '1':
            brand = input('What is the brand of firearm? >: ')
            model = input(f'What is the model your {brand}? >: ')
            caliber = input(f'What is the caliber of your {brand} {model}? >: ')
            serial = input(f'What is the serial of your {brand} {model} {caliber}? >: ')
            try:
                add_gun(brand, model, caliber, serial)
            except Exception as error:
                print(f'Something obviosly went wrong, {error} \n that is all i know i swear!!')

        elif menu_selection == '2':
            removal_serial = str(input('Enter the serial of the firearm you want removed >: '))
            try:
                delete_gun(removal_serial)
            except Exception as error:
                print(f'Well, {error} happened!')

        elif menu_selection == '3':
            show_all()

        elif menu_selection =='4':
            var = 10

        else:
            pass
    else:
        print('Something went wrong that I am trying to figure out. 🤷🏾‍♂️')
        print("""!! NOTICE !! IF THIS IS THE FIRST TIME YOU RUN THIS SCRIPT, IT IS OKAY TO SEE THIS.
JUST RE RUN THE SCRIPT AND EVERYTHING SHOULD WORK FINE.""")
        var = 10
