from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from fpdf import FPDF
import sqlite3
import subprocess


class TicketGui:
    """
    Clase que muestra el formulario para seleccionar el evento de la entrada

    Parámetros
    -----------
    Ninguno

    Atributos
    -------
    Ninguno
    """

    #Creación del formulario para la selección del evento a generar la entrada
    def __init__ (self):
        self.window = Tk()

        #Posiciono la ventana en el centro de la pantalla
        hwindow: int = 400
        wwindow: int = 600
        x_window: int = self.window.winfo_screenwidth() // 2 - wwindow // 2
        y_window: int = self.window.winfo_screenheight() // 2 - hwindow // 2
        position: str = str(wwindow) + "x" + str(hwindow) + "+" + str(x_window) + "+" +str(y_window)
        self.window.geometry(position)
        self.window.resizable(0, 0)
        
        self.window.title("Generar entrada de evento")

        #Divido la ventana en dos fremes: superior e inferior
        self.top_frame = Frame(self.window)
        self.top_frame.pack(fill="both", expand=True)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack(fill="both", expand=True)

        #Añado la etiqueta con el texto "Selecciona el evento"
        self.title = Label(self.top_frame, text="Selecciona el evento para generar la entrada", font="Arial 12")
        self.title.grid(row=1, column=3, columnspan=2, padx=125, pady=30)

        
        #Obtengo los eventos de la base de datos y los muestro en un Combobox
        try:
            conexion = sqlite3.connect("ProyectoP2.db")
            cursor = conexion.execute("select event_id, nombre from Events")
            
            options = []
            
            for row in cursor:
                options.append(row)

            self.option = Combobox(self.top_frame, width="50", values=options, state="readonly")
            self.option.grid(row=2, column=3, columnspan=2, pady=30)
            
            conexion.close()

             #Añado el botón "Entrar" al frame inferior, que ejecutará el método "input"
            self.button_ingress = Button(self.bottom_frame, text="Seleccionar", width=10, font=("Arial", 18), command=self.ticket)
            self.button_ingress.grid(row=5, column=1, columnspan=2, padx=220, pady=30)
        except Exception as ex:
            messagebox.showerror(message=ex, title="Error al consultar base de datos")

        #Muestro la ventana
        mainloop()

    def ticket(self):
        """
        Genera entrada para el evento seleccionado y el usuario activo

        Parámetros
        -----------
        Ninguno. Los obtiene del formulario

        Retorna
        -------
        Nada. 
        
        """

        #Obtengo el idenfificador de evento seleccionado
        event: int = self.option.get().split()

        #Obtengo el usuario activo
        try:
            conexion = sqlite3.connect("ProyectoP2.db")
            cursor = conexion.execute("select user_name from UserActive")
            fila = cursor.fetchone()

            if (fila != None) and (event[0] != None):
                tic = Ticket(fila[0], event[0])
                self.window.destroy()
            else:
                messagebox.showerror(message="Es necesario un usuario activo y un evento", title="Mensaje ticket")
            conexion.close()

        except Exception as ex:
            messagebox.showerror(message=ex, title="Mensaje ticket")

class Ticket:
    """
    Clase que genera la entrada del usuario para el evento

    Parámetros
    -----------
    user : str
        Identificador del asistente al evento
    
    event : int
        Identificador del evento

    Atributos
    -------
    Ninguno
    """

    def __init__(self, user: str, event: int):

        #Obtengo los datos del asistente y del evento para generar la entrada
        try:
            conexion = sqlite3.connect("ProyectoP2.db")

            #Compruebo que el usuario está registrado en el evento
            cursor = conexion.execute("select user_name, event_id from Assist where user_name=? and event_id=?", (user, event))
            fila = cursor.fetchone()

            if fila == None:
                messagebox.showinfo(message="El usuario no está registrado en el evento", title="Mensaje ticket")
                conexion.close()
                return

            #Obtengo los datos para generar la entrada
            cursor = conexion.execute("select full_name, DNI from Assistants where user_name=?", (user, ))
            fila = cursor.fetchone()

            cursor = conexion.execute("select nombre, start_date, final_date, location, start_hour, final_hour, price from Events where event_id=?", (event, ))
            fila2 = cursor.fetchone()        

            conexion.close()

            
            
        except Exception as ex:
            messagebox.showerror(message=ex, title="Mensaje ticket")


        #Genero la entrada en PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0,10, 'Evento:            ' + fila2[0], 1, 1)    
        pdf.cell(0,10, 'Asistente:        ' + fila[0], 1, 1)
        pdf.cell(0,10, 'DNI:                  ' + fila[1], 1, 1)
        pdf.cell(0,10, 'Fecha inicio:   ' + fila2[1], 1, 1)
        pdf.cell(0,10, 'Fecha fin:        ' + fila2[2], 1, 1)
        pdf.cell(0,10, 'Localización:  ' + fila2[3], 1, 1)
        pdf.cell(0,10, 'Hora inicio:     ' + fila2[4], 1, 1)
        pdf.cell(0,10, 'Hora fin:          ' + fila2[5], 1, 1)
        pdf.cell(0,10, 'Precio:            ' + fila2[6], 1, 1)

        pdf.output('ticket.pdf', 'F')

        #Muestro la entrada con el visor PDF
        path = 'ticket.pdf'
        subprocess.Popen([path], shell=True)



tick = TicketGui()