import sqlite3
from sqlite3 import Error


year=[2011,2012,2013,2014,2015]

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('database') #':memory:'
        print(sqlite3.version)
    except Error as e:
        print(e)
    return connection



def create_db(cursor,connection):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS year
            (   id integer PRIMARY KEY,
                total integer 
            );''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS top
            (   id INTEGER PRIMARY KEY,
                first TEXT ,
                second TEXT ,
                third TEXT ,
                fourth TEXT ,
                fifth TEXT ,
                FOREIGN KEY (id) REFERENCES year(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            );''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS trans
            (   id INTEGER PRIMARY KEY ,
                air INTEGER ,
                railway	INTEGER ,
                sea INTEGER,
                road INTEGER,
                FOREIGN KEY (id) REFERENCES year(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE            
            );''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS month
            (   id INTEGER PRIMARY KEY,
                march TEXT ,
                june TEXT ,
                sept TEXT ,
                dec TEXT ,
                FOREIGN KEY (id) REFERENCES year(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            );''')
        connection.commit()

    except Error as e:
            print(e)


def table_key(cursor,connnection):
    try:
        for i in range(5):
            temp=year[i]
            cursor.execute("INSERT INTO year (id) VALUES (?)",(temp,))
            cursor.execute("INSERT INTO top (id) VALUES (?)",(temp,))
            cursor.execute("INSERT INTO trans (id) VALUES (?)",(temp,))
            cursor.execute("INSERT INTO month (id) VALUES (?)",(temp,))
        connnection.commit()
    except Error as e:
        print(e)


def select_from(cursor,table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    cursor.execute("SELECT * FROM {}".format(table))

    print("The content of",table,"table:")

    rows = cursor.fetchall()

    for row in rows:
        print(row)



def select_all(cursor):
    select_from(cursor,'year')
    select_from(cursor,'top')
    select_from(cursor,'trans')
    select_from(cursor,'month')


def update_year(connection,cursor,total,b):

    sql='''UPDATE year
                SET total= ?
                WHERE id = ?'''

    cursor.execute(sql,(total,year[b]))
    connection.commit()

def update_top(connection,cursor,countries,b):

    sql='''     UPDATE top
                    SET first= ?,
                        second=?,
                        third=?,
                        fourth=?,
                        fifth=?
                    WHERE id = ?   '''

    cursor.execute(sql,(countries[0],countries[1],countries[2],countries[3],countries[4],year[b]))
    connection.commit()


def update_trans(connection,cursor,trans,b):

    sql='''     UPDATE trans
                    SET air= ?,
                        railway=?,
                        sea=?,
                        road=?
                    WHERE id = ?   '''

    cursor.execute(sql,(trans[0],trans[1],trans[2],trans[3],year[b]))
    connection.commit()

def update_month(connection,cursor,month,b):

    sql='''     UPDATE month
                    SET march= ?,
                        june=?,
                        sept=?,
                        dec=?
                    WHERE id = ?   '''

    cursor.execute(sql,(month[0],month[1],month[2],month[3],year[b]))
    connection.commit()
