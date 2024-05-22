import sqlite3
import assistant
import organizer
import events


def obj_to_dict(obj_list: list) -> list:
    dict_list = []
    for obj in obj_list:
        dict_list.append(obj.return_dict())
    return dict_list


def save_events(event_obj_list: list) -> None:
    connection = sqlite3.connect('ProyectoP2.db')
    cursor = connection.cursor()
    event_list = obj_to_dict(event_obj_list)
    for event in event_list:
        event_values = (event['event_id'], event['tipo'], event['nombre'], event['mas18'], event['start_date'],
                        event['final_date'], event['assistant_number'], event['location'], event['start_hour'],
                        event['final_hour'], event['price'], event['organizer'])
        sentence = f'INSERT INTO Events VALUES {event_values}'
        cursor.execute(sentence)
        for assistant1 in event['assistants']:
            assist_values = (assistant1, event['event_id'])
            sentence = f'INSERT INTO Assist VALUES {assist_values}'
            cursor.execute(sentence)
    connection.close()


def load_events() -> list:
    def evlappend(el, row1):
        el.append({'event_id': row1[0], 'tipo': row1[1], 'nombre': row1[2], 'mas18': row1[3], 'start_date': row1[4],
                   'final_date': row1[5], 'assistant_number': row1[6], 'location': row1[7], 'start_hour': row1[8],
                   'final_hour': row1[9], 'price': row1[10], 'organizer': row1[11],  'assistant_list': [row1[12]]})
        return el

    connection = sqlite3.connect('ProyectoP2.db')
    cursor = connection.cursor()
    sentence = 'SELECT * FROM Events LEFT JOIN Assist ON Events.event_id = Assist.event_id'
    cursor.execute(sentence)
    event_list = []
    event_obj_list = []
    query = cursor.fetchall()
    i = 0
    for row in query:
        if i == 0:
            i += 1
            event_list = evlappend(event_list, row)
        elif row[0] != event_list[i-1]['event_id']:
            event_list = evlappend(event_list, row)
            i += 1
        elif row[0] == event_list[i-1]['event_id']:
            event_list[i-1]['assistant_list'].append(row[12])
    for event in event_list:
        event_obj_list.append(events.Event(event_id=event['event_id'], tipo=event['tipo'], nombre=event['nombre'],
                                           mas18=event['mas18'], start_date=event['start_date'],
                                           final_date=event['final_date'], assistant_number=event['assistant_number'],
                                           location=event['location'], start_hour=event['start_hour'],
                                           final_hour=event['final_hour'], price=event['price'],
                                           organizer=event['organizer'], asistentes=event['assistant_list']))
    return event_obj_list
