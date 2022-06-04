import mysql.connector as mariaDB

def connect_db():
    """
    It tries to connect to the database, and if it succeeds, it returns the connection object. If it
    fails, it prints the error and returns None
    :return: The connection object.
    """
    try:
        db = mariaDB.connect(
            host="localhost",
            user="root",
            passwd="2005",
            database="db_biblioteca"
        )
        return db
    except mariaDB.Error as e:
        print(e)
        return None



def get_books():
    """
    It connects to the database, creates a cursor, executes a query, fetches the results, and returns
    them
    :return: A list of tuples.
    """
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM libros")
        books = cursor.fetchall()
        return books
    except mariaDB.Error as e:
        print(e)
        return None

# buscar usuario si el usuario existe retorna True si no existe retorna False
def search_user(cedula, nombre):
    """
    It connects to the database, creates a cursor, executes a query, fetches the results, and returns
    them
    :return: A list of tuples.
    """
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE cedula = %s AND nom_usuario = %s", (cedula, nombre))
        users = cursor.fetchall()
        if users:
            return True
        else:
            return False
    except mariaDB.Error as e:
        print(e)
        return None

def add_user(usuario, cedula):
    """
    It connects to the database, creates a cursor, executes a query, fetches the results, and returns
    them
    :return: A list of tuples.
    """
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (cedula, nom_usuario) VALUES (%s, %s)", (cedula, usuario))
        db.commit()
        return True
    except mariaDB.Error as e:
        print(e)
        return False