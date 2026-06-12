import pymysql

__cnx = None

def get_connection():
    global __cnx
    try:
        # Only establish a connection if one doesn't exist or has been closed
        if __cnx is None or not __cnx.open:
            __cnx = pymysql.connect(
                host='127.0.0.1', 
                user='root', 
                password='balaji@123sql', 
                database='grocery_store',
                port=3306
            )
            #   This must stay INSIDE the try block so it only prints on real success
            print("Connection successful!") 
            
    except pymysql.MySQLError as e:
        print("Error while connecting to database:", e)
        __cnx = None  # Reset to None so it tries again next time called
        
    except Exception as other_e:
        print("General application error:", other_e)
        __cnx = None

    return __cnx

