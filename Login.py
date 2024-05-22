from tkinter import *
from tkinter import messagebox
import sqlite3

class Login:

    """
    Clase para la realización del login del usuario

    Parámetros
    -----------
    Ninguno

    Atributos
    -------
    user : str
        Nombre de usuario
    password : str
        Contraseña del usuario
        
    """
    #Método constructor de la clase "login" que crea la ventana
    def __init__(self):
        
        #Creación de la ventana de login con sus dimensiones y posición
        self.window = Tk()

        #Posiciono la ventana en el centro de la pantalla
        hwindow: int = 400
        wwindow: int = 400
        x_window: int = self.window.winfo_screenwidth() // 2 - wwindow // 2
        y_window: int = self.window.winfo_screenheight() // 2 - hwindow // 2
        position: str = str(wwindow) + "x" + str(hwindow) + "+" + str(x_window) + "+" +str(y_window)
        self.window.geometry(position)
        self.window.resizable(0, 0)


        #self.window.geometry("400x400+100+50")
        self.window.title("Login")

        #Divido la ventana en dos fremes: superior e inferior
        self.top_frame = Frame(self.window)
        self.top_frame.pack(fill="both", expand=True)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack(fill="both", expand=True)

        #Añado la etiqueta con el texto "Login" en negrita en el frame superior
        self.title = Label(self.top_frame, text="Login", font="Arial 20 bold")
        self.title.pack(side="top", pady=20)

        #Añado la etiqueta "Usuario" y el cuadro de entrada del usuario al frame inferior
        self.label_user = Label(self.bottom_frame, text="Usuario", font=("Arial", 18))
        self.label_user.grid(row=0, column=0, padx=20, sticky="e")
        self.user = Entry(self.bottom_frame, bd=0, width=14, font=("Arial", 18))
        self.user.grid(row=0, column=1, padx=5, sticky="w")

        #Añado la etiqueta "Contraseña" y el cuadro de entrada de la contraseña al frame inferior
        self.label_password = Label(self.bottom_frame, text="Contraseña", font=("Arial", 18))
        self.label_password.grid(row=1, column=0, padx=20, sticky="e")
        self.password = Entry(self.bottom_frame, bd=0, width=14, font=("Arial", 18), show="*")
        self.password.grid(row=1, column=1, padx=5, sticky="w")

        #Añado el botón "Entrar" al frame inferior, que ejecutará el método "input"
        self.button_ingress = Button(self.bottom_frame, text="Entrar", width=10, font=("Arial", 18), command=self.input)
        self.button_ingress.grid(row=2, column=0, columnspan=2, pady=35)

        #Muestro la ventana
        mainloop()

    #Método de tratamiento del usuario y contraseña introducidos
    def input(self):
        """
        Comprueba que el usuario está registrado

        Parámetros
        -----------
        Ninguno. Los obtiene del formulario

        Retorna
        -------
        Nada. Almacena el usuario activo en la base de datos
        
        """

        #obtengo el usuario y contraseña introducidos
        name: str = self.user.get()
        passwd: str = self.password.get()
        
        #compruebo si el usuario introducido está registrado en la base de datos
        try:
            conexion = sqlite3.connect("ProyectoP2.db")
            cursor = conexion.execute("select user_name, email from Users where user_name=? and password=?", (name, passwd))
            fila = cursor.fetchone()
            
            #Añado al usuario como el usuario activo
            if fila != None:
                conexion.execute("DELETE FROM UserActive")
                conexion.execute("INSERT INTO UserActive (user_name, email) VALUES (?, ?)", (name, fila[1]))
                conexion.commit()
                messagebox.showinfo(message="User correcto", title="Mensaje login")
            else:
                messagebox.showerror(message="User incorrecto", title="Mensaje login")
            conexion.close()

        except Exception as ex:
            messagebox.showerror(message=ex, title="Mensaje login")
     
        self.window.destroy()

#Login()

