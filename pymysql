import pymysql
conn = pymysql.connect(host="localhost", user="root", password="redhat", db="test")

cursor = conn.cursor()
#cursor.execute('create table user3 (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user3 values (%s,%s)',['1','tony'])
cursor.execute('select * from user')
print cursor.fetchall()

#conn.commit()
cursor.close()
