from Objects import draka,Monstr

#p1_1 = лево
#p2_1 = право
gul = Monstr()

gul.randompower = 30
gul.critpower = 80
gul.critchance = 19
gul.power = 60
gul.HP = 200
gul.superpower = 0




def Brick (hero):
    print("Добро Пожаловать в Кирпичную деревню")
    print("К вам подошёл местный житель С квестом и предлогает:")
    print("Найти 1 железо")
    print("1 - принять, 2 отказаться:")
    if input()=="1":
        print(" Вы Приняли Квест")
    else:
        print("Вы Отказались")
    print("Куда пойти: \n 1 - Пещера 2 - Таверна")
    if input()=="1":
        print("Вы выбрали пещеру")
        Peshera(hero)
    else:
        print("Вы выбрали Тавену")
        Taverna(hero)
def Taverna(hero):
    pass

def Peshera(hero):
    print("Куда пойдёшь \n 1 - На право 2 - на лево ")
    if input() == "1":
        print("Вы выбрали на право")

        print("Эпичная Музычка")
        isPererojdenie = draka(hero,gul)
        if isPererojdenie == True:
            Brick(hero)

    else:
        print("Вы выбрали на лево")
        print("Перед вами золото: \n 1 - Добыть 2 - Оставить")
        if input()=="1":
            print("Вы Добыли золото")
            #todo Сумка+1
        else:
            print("Вы отказались")

        gul = Monstr()

        gul.randompower = 30
        gul.critpower = 80
        gul.critchance = 19
        gul.power = 60
        gul.HP = 200
        gul.superpower = 0
        levo(hero,gul,"zoloto")
        # todo драка
def levo(hero,monstr,item):
    print("Вы выбрали на лево")





    print("Куда пойдёшь \n 1 - Вперёд  2 - на лево ")

def pravo(hero,monstr,item):
    print("Вы выбрали на право")



def pryamo(hero,monstr,item):


    print("Куда пойдёшь \n 1 - Вперёд  2 - на лево ")
    print("Вы выбрали вперед")