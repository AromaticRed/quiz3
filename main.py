import requests
import json
import sqlite3

con = sqlite3.connect("dogs.sqlite")
cursor = con.cursor()
cursor.execute("create table if not exists dogs("
               "id INTEGER primary key autoincrement, link varchar(30))")


res = requests.get("https://dog.ceo/api/breeds/image/random")


if res.status_code == 200:
    print(res.headers)
    dictionary = json.loads(res.text)
    file = open("dogs.json", "w")
    json.dump(dictionary, file, indent=3)
    file.close()
    url = dictionary["message"]
    photo_result = requests.get(url)
    file = open("dog.png", "wb")
    file.write(photo_result.content)
    file.close()
    cursor.execute("insert into dogs(link) values(:message)", dictionary)


else:
    print("ამჟამად მიუწვდომელია")

con.commit()
con.close()
