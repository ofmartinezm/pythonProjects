from peewee import  *
from datetime import date

db = SqliteDatabase("people.db")

class Person(Model):
	name=CharField()
	birthday= DateField()
	is_relative=BooleanField()
	
	class Meta():
		database=db
		
class Pet(Model):
	owner = ForeignKeyField(Person, related_name='pets')
	name = CharField()
	animal_type = CharField()
	
	class Meta:
		database = db
		
def create_and_connect():
			db.connect()
			db.create_tables([Person,Pet],safe=True)


def create_family_members():
			uncle_tommy=Person(name='Tommy', birthday=date(2000, 11, 11), is_relative=True)
			uncle_tommy.save()
			grandma_ana=Person.create(name='Ana', birthday=date(1960, 10, 10), is_relative=True)
			tommys_dog=Pet.create(owner=uncle_tommy, name='Fido', animal_type='perro')
			anas_cat=Pet.create(owner=grandma_ana, name='Peluza', animal_type='gato')
			
			tommys_dog.name="Firulais"
			tommys_dog.save()

			
def get_family_members():			
	for person in Person.select():
		print("Nombre: {} fecha de nacimiento: {}".format(person.name, person.birthday))

def get_family_member(name):			
	#grandma_ana=Person.select().where(Person.name ==name).get()
	grandma_ana=Person.get(Person.name ==name)
	print("la abuelita: {} nacio en : {}".format(name, grandma_ana.birthday))	
	
def delete_pet(name):
	query=Pet.delete().where(Pet.name==name)
	delete_entries= query.execute()
	print ("{} registros borrados".format(delete_entries))

		
create_and_connect()

#create_family_members()

#get_family_members()

delete_pet("Peluza")
