import sqlite3
import assistant
import organizer


def obj_to_dict(obj_list: list) -> list:
    dict_list = []
    for obj in obj_list:
        dict_list.append(obj.return_dict())
    return dict_list


def assistant_dict_to_obj(dict_list: list) -> list:
    obj_list = []
    for di in dict_list:
        obj = assistant.Assistant(username=di['username'], password=di['password'], email=di['email'])
        obj.register(name=di['name'], birth_date=di['birth_date'], id_num=di['id_num'], tlf=di['tlf'],
                     address=di['address'])
        obj.modify_event_list(event_list=di['event_list'])
        obj_list.append(obj)
    return obj_list


def organizer_dict_to_obj(dict_list: list) -> list:
    obj_list = []
    for di in dict_list:
        obj = organizer.Organizer(username=di['username'], password=di['password'], email=di['email'])
        obj.register(type_org=di['type_org'], name=di['name'], id_user=di['id_user'])
        obj.modify_event_list(event_list=di['event_list'])
        obj_list.append(obj)
    return obj_list


def save(org_list: list, assist_list: list) -> None:
    org_dict_list = obj_to_dict(org_list)
    assist_dict_list = obj_to_dict(assist_list)
    connection = sqlite3.connect('ProyectoP2.db')
    cursor = connection.cursor()
    for org in org_dict_list:
        tupla_org = (org['username'], org['name'], org['id_user'], org['type_org'])
        tupla_usr = (org['username'], org['password'], org['email'])
        sentence_usr = f'INSERT INTO Users VALUES {tupla_usr}'
        sentence_org = f'INSERT INTO Organizers VALUES {tupla_org}'
        try:
            cursor.execute(sentence_usr)
            cursor.execute(sentence_org)
        except sqlite3.IntegrityError:
            pass
    for assist in assist_dict_list:
        tupla_assist = (assist['username'], assist['name'], assist['id_num'], assist['birth_date'],
                        assist['tlf'], assist['address']['city'], assist['address']['code'], assist['address']['street'])
        tupla_usr = (assist['username'], assist['password'], assist['email'])
        sentence_usr = f'INSERT INTO Users VALUES {tupla_usr}'
        sentence_assist = f'INSERT INTO Assistants VALUES {tupla_assist}'
        try:
            cursor.execute(sentence_usr)
            cursor.execute(sentence_assist)
        except sqlite3.IntegrityError:
            pass


def load() -> list:
    # obtener de la db una lista de organizers y de asistentes
    org_list = organizer_dict_to_obj()
    assisst_list = assistant_dict_to_obj()
    return org_list, assisst_list


