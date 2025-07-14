import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(
            host='localhost',
            user="root",
            password="Khushi",
            database='db1',          # Corrected spelling
            port=3306,
            charset="utf8mb4"
        )
        print('Database Connected')
    except Exception as e:
        print('Database Connection Failed:', e)
    return connection

def disconnect_db(connection):
    try:
        if connection:
            connection.close()
            print('DB disconnected')
    except Exception as e:
        print('DB disconnection failed:', e)

# Test the functions
if __name__ == "__main__":
    conn = connect_db()
    disconnect_db(conn)
