import psycopg2

def connect():
    """Establish a connection to the PostgreSQL database."""
    connection = None

    try:
        connection = psycopg2.connect(

            database="postgres",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
    except psycopg2.Error as e:

        print(f"Error connecting to the database: {e}")
        return None
    
    return connection

def add_answers(age, gndr, plng, clr):
    connection = connect()

    if connection != None:

        cursor = connection.cursor()
        cursor.execute("INSERT INTO questioned (age, gender, planguage, favcolor) VALUES (%s, %s, %s, %s);" ,[age, gndr, plng, clr])
        connection.commit()
        cursor.close()
        connection.close()

def show_answers():
    connection = connect()
    result = None

    if connection != None:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM questioned ORDER BY id")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
    return result

def clear_answers():
    connection = connect()
    if connection != None:

        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE questioned RESTART IDENTITY;")
        connection.commit()
        cursor.close()
        connection.close()
