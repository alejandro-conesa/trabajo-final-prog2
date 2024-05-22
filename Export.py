from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
import csv
from fpdf import FPDF
import subprocess
import threading

class ExportGui:
    """
    Clase que muestra el formulario para exportar a CSV y PFD

    Parámetros
    -----------
    Ninguno

    Atributos
    -------
    Ninguno
    """
    def __init__ (self):

        #Creación del formulario para la exportación a CSV o PDF
        self.window = Tk()

        #Posiciono la ventana en el centro de la pantalla
        hwindow: int = 400
        wwindow: int = 600
        x_window: int = self.window.winfo_screenwidth() // 2 - wwindow // 2
        y_window: int = self.window.winfo_screenheight() // 2 - hwindow // 2
        position: str = str(wwindow) + "x" + str(hwindow) + "+" + str(x_window) + "+" +str(y_window)
        self.window.geometry(position)
        self.window.resizable(0, 0)
        
        self.window.title("Exportar a CSV y PDF")

        #Divido la ventana en dos fremes: superior e inferior
        self.top_frame = Frame(self.window)
        self.top_frame.pack(fill="both", expand=True)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack(fill="both", expand=True)

        #Añado la etiqueta con el texto "Selecciona el evento"
        self.title = Label(self.top_frame, text="Selecciona el evento a exportar", font="Arial 12")
        self.title.grid(row=1, column=3, columnspan=2, padx=200, pady=30)
        
        
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
            self.button_ingress = Button(self.bottom_frame, text="Seleccionar", width=10, font=("Arial", 18), command=self.event)
            self.button_ingress.grid(row=3, column=1, columnspan=2, padx=250, pady=30)
            
        except Exception as ex:
            messagebox.showerror(message=ex, title="Error al consultar base de datos")

        #Muestro la ventana
        mainloop()

    def event(self):
        """
        Exporta los asistentes a un evento a los formatos CSV y PDF

        Usa concurrencia para generar los dos formatos al mismo tiempo

        Parámetros
        -----------
        Ninguno. Los obtiene del formulario

        Retorna
        -------
        Nada. 
        
        """

        #Obtengo el idenfificador de evento seleccionado
        event: int = self.option.get().split()

        #Creo objeto de la clase ExportCsv para generar archivo CSV
        x = threading.Thread(target=ExportCsv, args=(event[0], event[1], ))
        
        #Creo objeto de la clase ExportPdf para generar archivo PDF
        y = threading.Thread(target=ExportPdf, args=(event[0], event[1], ))

        #Creamos y ejecutamos las dos clases concurrentemente
        x.start()
        y.start()

        
        
        #Informo de la generación de los listados y muestro el listado de asistentes al evento
        messagebox.showinfo(message="Generados los archivos EVENT.CSV y EVENT.PDF", title="Mensaje exportar")
        path = 'event.pdf'
        subprocess.Popen([path], shell=True)

        self.window.destroy()

   
class Export:
    """
    Superclase para exportar a CSV y PDF

    Parámetros
    -----------
    event : int
        Identificador del evento

    Atributos
    -------
    event : int
        Identificador del evento
    """

    event: int = 0

    def __init__(self, event: int):
        self.event: int = event


class ExportCsv(Export):
    """
    Clase para exportar a CSV. Hereda de la superclase Export

    Parámetros
    -----------
    event : int
        Identificador del evento

    name : str
        Nombre del evento

    Atributos
    -------
    Ninguno
        
    """

    def __init__(self, event: int, name: str):
        super().__init__(event)

        #Consulto todos los asistentes al evento y genero un archivo CSV
        with open('event.csv', mode='w', newline='') as event_file:
            fieldnames = ['Asistentes evento', name]
            event_writer = csv.DictWriter(event_file, fieldnames=fieldnames)

            event_writer.writeheader()

            #Consulto los asistentes al evento seleccionado
            conexion = sqlite3.connect("ProyectoP2.db")
            cursor = conexion.execute("select user_name from Assist where event_id=?", event[0])
            filas = cursor.fetchall()
                     
            #Añado los asistentes encontrados al archivo CSV
            for row in filas:
                cursor = conexion.execute("select full_name from assistants where user_name=?", (row[0], ))
                fila = cursor.fetchone()
                event_writer.writerow({'Asistentes evento': fila[0]})
           
            conexion.close()


class ExportPdf(Export):
    """
    Clase para exportar a PDF. Hereda de la superclase Export

    Parámetros
    -----------
    event : int
        Identificador del evento

    name : str
        Nombre del evento

    Atributos
    -------
    Ninguno
        
    """

    def __init__(self, event: int, name: str):
        super().__init__(event)

        ##Consulto los asistentes al evento seleccionado
        conexion = sqlite3.connect("ProyectoP2.db")
        cursor = conexion.execute("select user_name from Assist where event_id=?", event[0])
        filas = cursor.fetchall()

        #Añado los asistentes encontrados al archivo PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0,10, 'Asistentes evento:  ' + name, 1, 1)
        for row in filas:
            cursor = conexion.execute("select full_name from assistants where user_name=?", (row[0], ))
            fila = cursor.fetchone()
            pdf.cell(0,10, str(fila[0]), 0, 1)
        
        pdf.output('event.pdf', 'F')
        conexion.close()

#eg = ExportGui()

