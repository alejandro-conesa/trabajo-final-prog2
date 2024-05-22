"""
        Crea un nuevo usuario

        Parámetros
        -----------
        Ninguno. Los obtiene del formulario

        Retorna
        -------
        Nada. Almacena un nuevo usuario en la base de datos

        """
#obtengo los datos del registro
user_name: str = self.user.get()
password: str = self.password.get()
email: str = self.email.get()
full_name: str = self.full_name.get()
dni: str = self.dni.get()
telf: str = self.telf.get()
location: str = self.location.get()
cp: str = self.cp.get()
address: str = self.adress.get()

def register_assistant():
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
                "INSERT INTO Assistants (user_name, full_name, DNI, birthdate, telf, location, CP, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (user_name, full_name, dni, birthdate, telf, location, cp, address))

            connection.commit()
            messagebox.showinfo(message="Asistente registrado exitosamente", title="Registro")

        connection.close()

    except Exception as ex:
        messagebox.showerror(message=str(ex), title="Error en el registro")


