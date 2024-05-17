import sqlite3
import assistant
import organizer


def save():
    connection = sqlite3.connect('ProyectoP2.db')


def obj_to_dict(obj_list):
    dict_list = []
    for obj in obj_list:
        dict_list.append(obj.return_dict())
    return dict_list


def assistant_dict_to_obj(dict_list):
    obj_list = []
    for di in dict_list:
        obj = assistant.Assistant(username=di['username'], password=di['password'], email=di['email'])
        if not di['is_registered']:
            obj_list.append(obj)
        else:
            obj.register(name=di['name'], birth_date=di['birth_date'], id_num=di['id_num'], tlf=di['tlf'],
                         address=di['address'])
        obj.modify_event_list(event_list=di['event_list'])
    return obj_list

