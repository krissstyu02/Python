import sqlite3
from sqlite3 import Error
def sql_connection():
   try:
      con = sqlite3.connect('database.db')
      return con
   except Error:
      print(Error)

def sql_table(con):
   cursorObj = con.cursor()

   cursorObj.execute(
       "CREATE TABLE party(id_party integer PRIMARY KEY, ideology text, charter_program text, attitude_power text)")

   cursorObj.execute(
      "CREATE TABLE party_members(id_certificate integer PRIMARY KEY, full_name text, position_code real, id_party integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE)")

   cursorObj.execute(
       "CREATE TABLE regional_office(id_regional integer PRIMARY KEY, company text)")

   cursorObj.execute(
       "CREATE TABLE main_plot(id_plot integer PRIMARY KEY, title text, id_party integer, id_regional integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE ,FOREIGN KEY (id_regional) REFERENCES regional_office (id_regional) ON DELETE CASCADE)")

   cursorObj.execute(
       "CREATE TABLE city(id_city integer PRIMARY KEY, city_name text, id_regional integer, size real,FOREIGN KEY (id_regional) REFERENCES regional_office (id_regional) ON DELETE CASCADE)")

   cursorObj.execute(
       "CREATE TABLE event(id_event integer PRIMARY KEY, date_event date, id_party integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE)")

   con.commit()

def sql_insert(con):
   cursorObj = con.cursor()

   cursorObj.execute("INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(1,'Алексеева Оксана Михайловна ', 12, 1)")
   cursorObj.execute(
       "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(2,'Иванов Петр Геннадьевич', 14, 1)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(4,'Осадченко Ирина Валерьяновна', 5, 3)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(3,'Болат Серкан Капибарович', 6, 2)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(5,'Петров Антон Васильевич', 2, 2)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(6,'Захарова Ульяна Сергеевна', 3, 3)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(7,'Кульченко Алексей Юрьевич', 3, 3)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(8,'Рудик Дарья Геннадьевна', 14, 2)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(9,'Дубровин Петр Васильевич', 6, 1)")
   cursorObj.execute(
      "INSERT INTO party_members(id_certificate , full_name , position_code , id_party ) VALUES(10,'Западный Михаил Романович', 5, 2)")

   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(1,'Либерализм','Основные сферы жизни:Медицина.Образование.', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(2,'Консерватизм','Основные сферы жизни:Медицина.Развитие туризма.', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(3,'Либерализм','Основные сферы жизни:Медицина.Наука.', 'Оппозиционная')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(4,'Консерватизм','Основные сферы жизни:Медицина.Развитие инфраструктуры.', 'Оппозиционная')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(5,'Либерализм','Основные сферы жизни:Медицина.Поддержка молодым семьям', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(6,'Консерватизм','Основные сферы жизни:Наука.Бесплатное образование.', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(7,'Либерализм','Основные сферы жизни:Обеспечение работы.Военное обеспечение.', 'Оппозиционная')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(8,'Консерватизм','Основные сферы жизни:Медицина.Здравоохранение.', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(9,'Либерализм','Основные сферы жизни:Наука.Религия.', 'Правящая')")
   cursorObj.execute(
      "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(10,'Либерализм','Основные сферы жизни:Социальная помощь.Градостроительство.', 'Оппозиционная')")

   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(1,'11.09.2021',1)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(2,'10.09.2021',1)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(3,'11.09.2000',2)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(4,'11.09.2020',3)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(5,'11.10.2021',4)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(6,'11.11.2021',5)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(7,'11.12.2021',6)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(8,'11.01.2021',7)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(9,'11.02.2021',8)")
   cursorObj.execute(
      "INSERT INTO event(id_event,date_event, id_party) VALUES(10,'11.03.2021',9)")

   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(1,'Краснодарский край')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(2,'Московская область')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(3,'Ленинградская область')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(4,'Ростовская область')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(5,'Ставропольский край')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(6,'Чеченская республика')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(7,'Республика Дагестан')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(8,'Воронежская область')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(9,'Республика Адыгея')")
   cursorObj.execute(
      "INSERT INTO regional_office(id_regional , company) VALUES(10,'Республика Якутия')")

   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(1,'Краснодар',1,294)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(2,'Усть-Лабинск',1,37)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(3,'Якутск',10,122)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(4,'Москва',2,2511)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(5,'Санкт-Петербург',3,1439)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(6,'Ростов-на-Дону',4,348)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(7,'Ставрополь',5,244)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(8,'Грозный',6,324)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(9,'Махачкала',7,468)")
   cursorObj.execute(
      "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(10,'Майкоп',9,58)")

   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(1,'Центральный Федеральный округ',1, 2)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(2,'Южный Федеральный округ',2, 1)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(3,'Северно-Западный Федеральный округ',3, 3)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(4,'Южный Федеральный округ',4, 4)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(5,'Северо_Кавказский Федеральный округ',5, 5)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(6,'Северо_Кавказский Федеральный округ',6, 6)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(7,'Северо_Кавказский Федеральный округ',7, 7)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(8,'Центральный Федеральный округ',8, 8)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(9,'Южный Федеральный округ',9, 9)")
   cursorObj.execute(
      "INSERT INTO main_plot(id_plot,title ,id_party ,id_regional) VALUES(10,'Дальневосточный Федеральный округ',10, 10)")
   con.commit()

#города 1 региона
def select1(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select city_name,company
    from city inner join regional_office on city.id_regional=regional_office.id_regional where city.id_regional==1   ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('Города Краснодарского края')
   for row in rows:
      print(row)


def select2(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select city_name,size from city order by city.size   ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print()
   print('Сортировка городов по площади(в порядке возрастания)')
   for row in rows:
      print(row)


def select3(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select full_name,attitude_power from party_members inner join party on party_members.id_party=party.id_party 
   where party.attitude_power=='Оппозиционная'   ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print()
   print('Члены оппозиционных партий ')
   for row in rows:
      print(row)

def select4(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select title,company
    from  main_plot inner join regional_office on main_plot.id_regional=regional_office.id_regional where main_plot.title=='Северо_Кавказский Федеральный округ'   ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('Количество регионов Северо-Кавказского округа=',len(rows))


def sql_update(con):
   cursorObj = con.cursor()
   cursorObj.execute('UPDATE party_members SET full_name = "Григорьев Влад Александрович" where position_code == 12')
   cursorObj.execute('UPDATE event SET date_event = "10.05.2021" where id_event == 1')
   cursorObj.execute('UPDATE party SET ideology = "Либерализм" where id_party == 2')
   con.commit()


def sql_delete(con):
   cursorObj = con.cursor()
   cursorObj.execute('DELETE FROM party_members  where position_code == 14')
   cursorObj.execute('DELETE FROM event  where id_event == 3')
   cursorObj.execute('DELETE FROM party_members  where position_code == 14')
   con.commit()




con = sql_connection()
#sql_table(con)
#sql_insert(con)
select1(con)
select2(con)
select3(con)
select4(con)
sql_update(con)
sql_delete(con)

