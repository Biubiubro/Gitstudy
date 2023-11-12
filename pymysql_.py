import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                             password='139391', db='multi_table', charset='utf8')

print(connection)
cursor = connection.cursor()
print(cursor)
with cursor as cursor:
    sql = 'select * from emp'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)











