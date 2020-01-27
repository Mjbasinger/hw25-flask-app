import datetime
from peewee import *
from flask_login import UserMixin
DATABASE = SqliteDatabase('animals.sqlite')


class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()

    class Meta:
        database = DATABASE
# Animal model that takes in multiple parameters. CharField will limit to 255. 
class Animal(Model):
    sci_name = CharField()
    name = CharField()
    animal_type = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta: 
        database = DATABASE
# method to init database and create tables based on array 'Animal'
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Animal], safe=True)
    print('TABLES created')
    DATABASE.close()