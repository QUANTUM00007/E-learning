import sqlite3 as sql

def insertuser(username,password):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT count(*) from users where username='{}".format(username))
    user = cur.fetchone()
    if user[0] != 0:
        return { "message": "user already exist"}
    cur.execute("INSERT INTO users(username, password)) VAlUES(?,?)", (username,password))
    con.commit()
    con.close()
    return {"message":"You have successfully registered"}

def retrieveuser():
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT username,password from users")
    con.commit()
    con.close()
    return insertuser

def login_check(username,password):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT count(*) from users where username='{}' AND password='{}'".format(username,password))
    user = cur.fetchone()
    con.commit()
    con.close()
    print(username[0])

    if user[0] != 0:
        return {"message": "User Successfully login"}
    else:
        return {"message": "Please check username or password"}
    
def delete(username,password):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT count(*) from users where username='{}' AND password='{}'".format(username,password))
    user = cur.fetchone()
    con.commit()
    con.close()
    return {"message": "User successfully deleted"}    
    

