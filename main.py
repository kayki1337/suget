from brick import Brick
from Objects import Hero


hero = Hero()
def sg():
  print("выберите героя:")
  print("Маг:Урон-40,Жизни-200,Сбособность: Призывать воинов (жизни-50 Урон-30 способности:нет)")
  print("Воин:Урон-20,Жизни-250,Сбособность: На каждый 5 удар мечём,призывает огромный меч наносящий 300ед.Урона")
  print("Маг:Урон-30,Жизни-150,Сбособность: на каждый 3 стрелой призывает ледяную стрелу наносящая 200ед.Урона")
  print("1-Маг")
  print("2-воин")
  print("3=эльф")
  print("введите цифру:")
  f=input()
  if f=="1":
     print("Поздровляю вы Маг")
     hero.randompower = 60
     hero.critpower = 70
     hero. critchance = 4
     hero.power = 40
     hero. HP = 800
     hero. superpower = 0
     hero.deffense = 0
     hero.  lvl = 0
     hero. XP = 0
     hero. dificult = ""
     hero. location = ""
     hero. kolichestvo = 0
     hero. sposobnosti = [" Огненный шар ", " дождь из лазера ", " електро удар ", " игловый разрез ",
                    " стену солнечных лучей ", " серьёзный разрез "]

  if f=="2":
     print("Поздровляю вы Воин")
     hero.randompower = 30
     hero.  critpower = 60
     hero.critchance = 13
     hero.  power = 20
     hero. HP = 250
     hero. superpower = 0
     hero.  deffense = 0
     hero.lvl = 0
     hero. XP = 0
     hero. dificult = ""
     hero. location = ""
     hero. kolichestvo = 0
     hero.  sposobnosti = [" Огненный шар ", " дождь из лазера ", " електро удар ", " игловый разрез ",
                    " стену солнечных лучей ", " серьёзный разрез "]

  if f=="3":
     hero.print("Поздровляю вы Эльф")
     hero.hero. randompower = 40
     hero.critpower = 30
     hero.critchance = 5
     hero.power = 30
     hero.HP = 150
     hero.superpower = 0
     hero.deffense = 0
     hero.lvl = 0
     hero.XP = 0
     hero.dificult = ""
     hero.location = ""
     hero.kolichestvo = 0
     hero.sposobnosti = [" Огненный шар ", " дождь из лазера ", " електро удар ", " игловый разрез ",
                    " стену солнечных лучей ", " серьёзный разрез "]


def location():

    print("Выберите локацию:")
    print("1 Кирпичная деревня:")
    print("2 золотая ограда:")
    print("3 железная сталь:")
    print("4 бронзовый посёлок :")
    print("введите цифру:")
    g = input()
    if g =="1":
        location="Кирпичная деревня"
        print("Вы выбрали Кирпичную деревню")
        Brick(hero)
    if g == "2":
        location = "Золотая ограда"
        print("Вы выбрали Золотую ограду")

    if g == "3":
        location = "Железная сталь"
        print("Вы выбрали Железную сталь")
    if g == "4":
        location = "Бронзовый посёлок"
        print("Вы выбрали Бронзовый посёлок")

def difficulties():
    print("Выберите сложность(можно поменять)")
    print("1-Легко")
    print("2-Среднее")
    print("3-Сложно")
    print("введите цифру:")
    c = input()
    if c == "1":
        dificult = "Легко"
        print("Вы выбрали сложность Легко")
    if c == "2":
        dificult = "Среднее"
        print("Вы выбрали сложность Среднее")
    if c == "3":
        dificult = "Сложно"
        print("Вы выбрали сложность Сложно")



sg()
difficulties()
location()











