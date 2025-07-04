import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(host='localhost' , user = 'root' , password = 'Khushi' , port = '3306' , charset = 'utf8')
        print('Database Connected')
    except:
        print('Database connection failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('Database disconnected')
    except:
        print('Database connection Failed')



