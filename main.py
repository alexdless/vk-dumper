
import sqlite3


def auth_and_get_data_vk(): #аутентификация vk api и return данных с метода groups.getMembers
	from vklancer import api
	from vklancer.utils import oauth
	access_token = oauth(input("(vk auth) login: "), input("(vk auth) password: "))
	api = api.API(token=access_token)
	public_id = int(input("(vk) public id: "))
	return api.groups.getMembers(group_id=public_id, fields="city")["response"]["items"]



def create_database():
	ul = "vk-dumper%i.sqlite" % public_id
	conn = sqlite3.connect(ul)
	c = conn.cursor()
	c.execute("CREATE TABLE `users` (`id`	INTEGER, `first_name`	TEXT, `last_name`	TEXT,	`city`	TEXT);")



def insert_database(id, first_name, last_name, city): #создание таблицы для данных
	conn = sqlite3.connect('vk-dumper.sqlite')
	c = conn.cursor()
	c.execute("INSERT INTO users (id, first_name, last_name, city) VALUES (?, ?, ?, ?)", (id, first_name, last_name, city))
	conn.commit()


array = auth_and_get_data_vk()
create_database()

for i in array: #
	try: #костыль, так как в респонсе от вк не всегда есть поле city для отдачи в базу данных.
		id, first_name, last_name, city = i["id"], i["first_name"], i["last_name"], i["city"]["title"]
	except KeyError:
		id, first_name, last_name, city = i["id"], i["first_name"], i["last_name"], "Не указан"
	insert_database(id, first_name, last_name, city)

print("finished")