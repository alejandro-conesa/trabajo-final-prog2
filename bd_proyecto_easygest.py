import sqlite3
from tkinter import messagebox


class CreateDataBase:

    """
    Clase para la creación de la base de datos del proyecto

    Parámetros
    -----------
    Ninguno

    Atributos
    ---------
    Ninguno
        
    """

    def __init__(self):
        self.create_tables()

    def create_tables(self):

        """
        Crea las distintas tablas que componen el proyecto

        Parámetros
        -----------
        Ninguno.

        Raises
        ------
        Tables already exists

        Retorna
        -------
        Nada.
        
        """
        try:
            connection = sqlite3.connect('ProyectoP2.db')
            #cursor = connection.cursor()
            connection.execute("""CREATE TABLE Users (
                            user_name VARCHAR(50) PRIMARY KEY,
                        password VARCHAR(50),
                        email VARCHAR(50))
            """)

            connection.execute("""CREATE TABLE Assistants (user_name VARCHAR(50) PRIMARY KEY,
                        full_name VARCHAR(50),
                        DNI CHAR(8),
                        birthdate VARCHAR(10),
                        telf CHAR (9),
                        location VARCHAR(50),
                        CP CHAR(5),
                        adress VARCHAR(50),
                        FOREIGN KEY (user_name) REFERENCES Users(user_name))
            """)

            connection.execute("""CREATE TABLE Organizers (user_name VARCHAR(50) PRIMARY KEY,
                        name VARCHAR(50),
                        DNI_CIF VARCHAR(9),
                        type VARCHAR(20),
                        FOREIGN KEY (user_name) REFERENCES Users(user_name) )
            """)

            connection.execute("""CREATE TABLE Events (event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo VARCHAR (50),
                        nombre VARCHAR(50),
                        mas18 INTEGER CHECK (mas18 IN (0, 1)),
                        start_date VARCHAR (10),
                        final_date VARCHAR (10),
                        assistant_number VARCHAR(10),
                        location VARCHAR(50),
                        start_hour VARCHAR(10),
                        final_hour VARCHAR(10),
                        price VARCHAR(30),
                        organizer VARCHAR(50) NOT NULL,
                        FOREIGN KEY (organizer) REFERENCES Organizers (user_name))
            """)

            connection.execute("""CREATE TABLE Assist (user_name VARCHAR(50),
                        event_id INTEGER,
                        PRIMARY KEY (user_name, event_id),
                        FOREIGN KEY (user_name) REFERENCES Assistants(user_name),
                        FOREIGN KEY (event_id) REFERENCES Events(event_id))
            """)

            connection.execute("""CREATE TABLE UserActive (user_name VARCHAR(50),
                               email VARCHAR(50))
            """)

            connection.commit()
            connection.close()

        except Exception as ex:
            messagebox.showerror(message=ex, title="Mensaje creación base de datos")

 
#db = CreateDataBase()


