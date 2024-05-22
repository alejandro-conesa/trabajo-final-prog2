# Define la clase EventsFilter para gestionar y filtrar eventos
class EventsFilter:
    # Método de inicialización, crea una lista vacía de eventos
    def __init__(self):
        self.events = []

    def agregar_evento(self, evento):
        self.events.append(evento)
    # Método para buscar eventos basados en argumentos clave-valor
    def search_events(self, **kwargs):
        # Inicializa la variable resultados con la lista completa de eventos
        resultados = self.events
        # Itera sobre cada clave y valor en los argumentos proporcionados
        for key, value in kwargs.items():
            # Línea de filtro:
            resultados = [event for event in resultados if getattr(event, f'_{key}') == value]
        # Devuelve la lista de eventos que coinciden con los criterios de búsqueda
        return resultados

    # Método para visualizar todos los eventos
    def watch_events(self):
        # Itera sobre cada evento en la lista de eventos
        for event in self.events:
            # Imprime la representación en cadena del evento
            print(event)
