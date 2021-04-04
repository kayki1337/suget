import random

from termcolor import colored



class Hero:
    randompower=0
    critpower=0
    critchance = 0
    power = 0
    HP = 0
    superpower = 0
    deffense = 0
    lvl = 0
    XP = 0
    dificult = ""
    location = ""
    kolichestvo =0
    sposobnosti = [" Огненный шар ", " дождь из лазера ", " електро удар ", " игловый разрез ",
                   " стену солнечных лучей ", " серьёзный разрез "]

class Monstr:
    randompower = 0
    critpower = 0
    critchance = 0
    power =60
    HP = 600
    superpower =0
    slowa=["И что это было хехехе","Это всё?","Бьёшь как дефка хаххааахаа","Ты не герой ты слабак","Тебе до меня далеко","бу га га х"]




def draka(hero,monstr):
    kolicheastvo=0
    while True:
        if hero.HP <=0:
            print("Поздровляю ты здох")
            return False
        if monstr.HP <=0:
            print("Поздровляю ты его кокнул")
            onePersent = hero.HP /100
            hero.HP += 40*onePersent
            print("После битвы вы отхилились и у вас "+ str(hero.HP ))
            print("было восстановлено "+ str( onePersent*40 ))
            return True

        monstr_zashita = str(random.randint(1, 3))
        monstr_ataka = str(random.randint(1, 3))

        print("Выберите что защитить: 1-тело 2-голову 3-ноги")
        hero_zashita = input()
        if hero_zashita == "1":
            print("вы защетили тело")
        if hero_zashita == "2":
            print("вы защитили голову ")
        if hero_zashita == "3":
            print("вы защитили тело ")

        print("что атаковать?:  1-тело 2-голову 3-ноги ")
        hero_ataka = input()
        if hero_ataka == "1":
            print("вы атаковали тело ")
        if hero_ataka == "2":
            print("вы атаковали головy")

        if hero_ataka == "3":
            print("вы атаковали тело")

        if kolicheastvo ==hero.kolichestvo:
            kolicheastvo=0
            print(hero.kolichestvo)
            yron = random.randint(25, 100)
            monstr.HP -= yron
            print(hero.sposobnosti+" Который снес монстру "+str(yron))



        kolicheastvo+=1

        if hero_zashita==monstr_ataka:
            print("Харош ты защитился")
        else:
            print("По тебе попали!" )
            demage = monstr.power+random.randint(0,monstr.randompower)
            if(random.randint(0,100)<monstr.critchance):
                print (colored('Монстр ударил критом!!!!!!!!!!', 'red'))
                demage += demage/100*monstr.critpower

            print("Тебе снесли "+colored(str(demage),"blue")+" ХП")
            hero.HP-=demage
            print("У вас осталось "+str(hero.HP))
        if monstr_zashita==hero_ataka:
            print("Монстр заблокировал твою атаку")
            print("Монстр:\n\""+monstr.slowa[random.randint(0,5)]+"\"")
        else:
            print("Фига втащил!")
            demage = hero.power + random.randint(0, hero.randompower)
            if (random.randint(0, 100) < hero.critchance):
                print(colored("Ты ударил критом!!!!!!!!!!", 'red'))
                demage += demage / 100 * hero.critpower


            print("ты снес Монстру  "+colored( str(demage),"yellow")+" ХП")
            monstr.HP-=demage
            print("У монстра осталось "+str(monstr.HP)+" ХП")
