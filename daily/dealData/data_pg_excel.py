import psycopg2

conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost", port="5432")

print ("Opened database successfully")
curs = conn.cursor()

# 编写Sql，只取前两行数据
sql = 'SELECT * FROM "center"."book" WHERE "id" = 1 LIMIT 1000 OFFSET 0'

# 数据库中执行sql命令
curs.execute(sql)

# 获得数据
data = curs.fetchall()

# 关闭指针和数据库
curs.close()
conn.close()
print(data)