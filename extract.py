import psycopg2
data=psycopg2.connect(
    database="postgres",
    user='postgres',
    password='surya@2006', 
    host='localhost',
    port= '5432'  
)
cursor=data.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
         (name text,salary int,age int);''')
print("Table created successfully")
data.commit()
data.close()


def data():
    data=psycopg2.connect(
        database="postgres",user='postgres',
        password='surya@2006',host='localhost',port= '5432'  
    )
    
    cursor=data.cursor()
    cursor.execute('''insert into EMPLOYEE (name,salary,age) values ('surya',25000,18)''')
    print("data inserted successfully")
    data.commit()   
    data.close()
    data()
    
def extract():
    data=psycopg2.connect(
        database="postgres",user='postgres',
        password='surya@2006',host='localhost',port= '5432'  
    )
    cursor=data.cursor()
    cursor.execute('''select * from EMPLOYEE''')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    data.commit()
    data.close()
    
extract()