from user import User
from assistant import Assistant

class Evento:
    def __init__(self, event_id: int, tipo: str, nombre: str, mas18: int, start_date: str, final_date: str,
                 location: str, start_hour: str, final_hour: str, price: str, organizer: str,
                 asistentes=None, assistant_number=0):
        if asistentes is None:
            asistentes = []
        self._event_id = event_id
        self._tipo = tipo
        self._nombre = nombre
        self._mas18 = mas18
        self._start_date = start_date
        self._final_date = final_date
        self._location = location
        self._start_hour = start_hour
        self._final_hour = final_hour
        self._price = price
        self._organizer = organizer
        self._asistentes = asistentes
        self._assistant_number = assistant_number

    def return_dict(self) -> dict:
        info_dict = {
            'event_id': self._event_id,
            'tipo': self._tipo,
            'nombre': self._nombre,
            'mas18': self._mas18,
            'start_date': self._start_date,
            'final_date': self._final_date,
            'location': self._location,
            'start_hour': self._start_hour,
            'final_hour': self._final_hour,
            'price': self._price,
            'organizer': self._organizer,
            'assistant_number': self._assistant_number,
            'asistentes': self._asistentes
        }
        return info_dict

    def modificar_asistentes(self, action: str, asistente: Assistant):
        if action == 'añadir' and asistente not in self._asistentes:
            self._asistentes.append(asistente)
        elif action == 'quitar' and asistente in self._asistentes:
            self._asistentes.remove(asistente)
        self._assistant_number = len(self._asistentes)
