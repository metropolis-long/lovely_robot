import pandas as pd
import pymysql

# sql 命令
sql_cmd = "SELECT * FROM diary left join user_info on user_info.user_id = diary.user_id"

# 用DBAPI构建数据库链接engine
con = pymysql.connect(host='127.0.0.1', user='root', password='12345678', database='daily', charset='utf8', use_unicode=True)
df = pd.read_sql(sql_cmd, con)
fp = r'C:\Users\Administrator\Desktop\try3.xls'
df.to_excel(fp,sheet_name='日记',)