import sqlite3
class databaes:
    def __init__(self,data):
        self.con = sqlite3.connect(data)
        self.cur = self.con.cursor()


        sql = """
        
        CREATE TABLE IF NOT EXISTS employee(
               id Integer Primary Key,
               name text,
               job text,
               age text,
               email text,
               mobile text,
               gender text,
               address text
        )
        
        """

        self.cur.execute(sql)
        self.con.commit()


    def insert(self,name,job,age,email,mobile,gender,address):

        self.cur.execute("insert into employee values(NULL,?,?,?,?,?,?,?)",
                   (name,job,age,email,mobile,gender,address))
        self.con.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM employee ")

        rows = self.cur.fetchall()
        return rows



    def remove(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()


    def update(self,id,name,job,age,email,mobile,gender,address):

        self.cur.execute("update employee set name=?,job=?,age=?,email=?,mobile=?,gender=?,address=? where id=?",
                         (name, job, age, email, mobile, gender ,address,id))

        self.con.commit()

