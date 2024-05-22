import bd_proyecto_easygest
import Login
import registro_asistentes
import registro_organizadores
import export
import Ticket
import events

db = bd_proyecto_easygest.CreateDataBase()

def main_menu():
    print("1-Registrarse")
    print("2-Login")
    op = int(input("Introduce la opción que desee: "))
    if op == 1:
        print("1- Asistente")
        print("2- Organizador")
        user_type = int(input("Introduce el tipo de usuario: "))
        if user_type == 1:
            registro_asistentes.register_assistant()
        elif user_type == 2:
            registro_organizadores.register_organizer()
    elif op == 2:
        Login.Login()

def assistant_menu():
    while True:
        print("\nMENÚ ASISTENTE")
        print("1- Descargar entradas de mis eventos")
        print("2- Buscar eventos nuevos")
        print("3- Exportar datos asistentes")
        print("4- Salir")
        op = int(input("Introduce la opción que desee: "))
        if op == 1:
            Ticket.TicketGui()
        elif op == 2:
            # Aquí se llamaría a la funcionalidad para buscar eventos nuevos
            print("Funcionalidad de buscar eventos nuevos aún no implementada.")
        elif op == 3:
            export.ExportGui()
        elif op == 4:
            break

def organizer_menu():
    while True:
        print("\nMENÚ ORGANIZADOR")
        print("1- Crear eventos nuevos")
        print("2- Gestionar mis eventos")
        print("3- Exportar datos asistentes")
        print("4- Salir")
        op = int(input("Introduce la opción que desee: "))
        if op == 1:
            events.create_event()
        elif op == 2:
            # Aquí se llamaría a la funcionalidad para gestionar los eventos del organizador
            print("Funcionalidad de gestionar eventos aún no implementada.")
        elif op == 3:
            export.ExportGui()
        elif op == 4:
            break

if __name__ == "__main__":
    main_menu()
    try:
        # Obtengo el usuario activo
        connection = sqlite3.connect("ProyectoP2.db")
        cursor = connection.execute("SELECT user_name FROM UserActive")
        active_user = cursor.fetchone()
        if active_user:
            cursor = connection.execute("SELECT user_name FROM Assistants WHERE user_name=?", (active_user[0],))
            is_assistant = cursor.fetchone()
            if is_assistant:
                assistant_menu()
            else:
                organizer_menu()
        else:
            print("No hay usuario activo.")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        connection.close()
