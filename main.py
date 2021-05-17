import pymysql
from config import host, user, password, db_name

try:
    # Connect to the database
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected")
    print("#" * 20)

    try:
        # Create a new table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                          "name varchar(32)," \
        #                          "password varchar(32)," \
        #                          "email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        # Insert any data
        # with connection.cursor() as cursor:
        #     data_insert_query = "INSERT INTO `users` (name, password, email) VALUES ('max', 'test123456789', 'test3@test.com');"
        #     cursor.execute(data_insert_query)
        #     # connection is not autocommit by default. So you must commit to save
        #     # your changes.
        #     connection.commit()
        #     print("Record successfully added")

        # Read a record from table
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for rows in result:
                print(rows)
            print("#" * 20)

        # Delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id=3"
        #     cursor.execute(delete_query)
        #     connection.commit() #! Do not forget to commit changes in table
    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...Try again")
    print(ex)