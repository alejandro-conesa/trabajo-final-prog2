"""
        Crea un nuevo organizador

        Parámetros
        -----------
        Ninguno. Los obtiene del formulario

        Retorna
        -------
        Nada. Almacena un nuevo organizador en la base de datos

        """
#obtengo los datos del registro
user_name: str = self.user.get()
password: str = self.password.get()
email: str = self.email.get()
name: str = self.name.get()
dni_cif: str = self.dni_cif.get()
type: str = self.type.get()

def register_organizer():
    try:
        connection = sqlite3.connect('ProyectoP2.db')
        cursor = connection.cursor()

        # Comprobar si el usuario ya existe en la tabla Users
        cursor.execute("SELECT * FROM Users WHERE user_name = ?", (user_name))
        user_exists = cursor.fetchone()

        if user_exists:
            messagebox.showerror(message="El nombre de usuario ya existe. Por favor, elija otro.",
                                 title="Error en el registro")
        else:
            cursor.execute("INSERT INTO Users (user_name, password, email) VALUES (?, ?, ?)",
                           (user_name, password, email))
            cursor.execute(
                "INSERT INTO Organizers (user_name, name, DNI_CIF, type) VALUES (?, ?, ?, ?)",
                (user_name, name, dni_cif,type))

            connection.commit()
            messagebox.showinfo(message="Organizador registrado exitosamente", title="Registro")

        connection.close()

    except Exception as ex:
        messagebox.showerror(message=str(ex), title="Error en el registro")
