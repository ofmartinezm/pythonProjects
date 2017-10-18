from peewee import *

from collections import OrderedDict

import  datetime

import sys

db=SqliteDatabase('diary.db')


class Entry(Model):
    content= TextField()
    timestamp= DateField(default=datetime.datetime.now())
    class Meta():
            database=db

def create_and_connect():
    """Conecion a la base de datos y creación de la tabla"""
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """show menu"""
    choice=None
    while choice!='q':
        print("Ingrese 'q' para salir")
        for key,value in menu.items():
            print("{}) {}".format(key,value.__doc__))
        choice=input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add entry"""
    print("Ingrese su pensamiento.")
    print('Presione ENTER  y luego  ctrl+Z para finalizar')
    data= sys.stdin.read().strip()

    if data:
        if input("Esta seguro de guardar esta entrada? [Y/N]").lower().strip()!='n':
            entrada = Entry.create(content=data)
            print("Su entrada se registro exitosamente!!")


def view_entries(search_query=None):
    """View all entries"""
    entries=Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries=entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp= entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('+'*len(timestamp))
        print('/n')
        print(entry.content)
        print('/n')
        print('+' * len(timestamp))
        print("n) siguiente entrada")
        print("d) borrar entrada")
        print("q) regresar al menu")

        next_action=input("Action: [ndq] ").lower().strip()

        if next_action=='q':
            break
        elif next_action=='d':
            delete_entry(entry)


def search_entry():
    """Buscar una entrada"""
    search_query=input("search query: ").strip()
    view_entries(search_query)

def delete_entry(entry):
    """Delete an entry"""
    action=input("Esta seguro? [Y/N]".lower().strip())

    if action=='y':
        entry.delete_instance()



menu=OrderedDict([
    ('a',add_entry),
    ('v',view_entries),
    ('d',delete_entry),
    ('s',search_entry)
])


def hello_world():
    print("Hola mundo ofmm")

if __name__=='__main__':
    create_and_connect()
    menu_loop()