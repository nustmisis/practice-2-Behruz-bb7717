# -*- coding: utf-8 -*-
"""
Китайский гороскоп делит время на 12-летние циклы, и  каждому году 
соответствует конкретное животное. Один из таких циклов приведен ниже
Год Животное 
2000 Дракон
2001 Змея 
2002 Лошадь 
2003 Коза 
2004 Обезьяна 
2005 Петух 
2006 Собака
2007 Свинья
2008 Крыса
2009 Бык
2010 Тигр
2011 Кролик
Напишите программу, которая будет запрашивать у пользователя год 
рождения и  выводить ассоциированное с  ним название животного по 
китайскому гороскопу. При этом программа не должна ограничиваться 
только годами из приведенной таблицы, а должна корректно обрабатывать все годы нашей эры.
"""

year = input()
animal_number = (year-2000) % 12
  
if animal_number ==0:
    animal= "Дракон"
elif animal_number ==1:
    animal="Змея"
elif animal_number ==2:
    animal="Лощадь"
elif animal_number ==3:
    animal="Коза"
elif animal_number ==4:
    animal="Обезьяна"
elif animal_number ==5:
    animal="Петух"
elif animal_number ==6:
    animal="Собака"
elif animal_number ==7:
    animal="Свиня"
elif animal_number ==8:
    animal="Крыса"
elif animal_number ==9:
    animal="Бык"
elif animal_number ==10:
    animal="тигр"
else:
    animal="Кролик"


print(animal)
