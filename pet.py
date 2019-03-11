class Pet:

    def __init__(self,hunger=0,tiredness=0):
        '''Konstruktor'''
        self.name = input("Podaj imie zwierzaka: ")
        self.hunger = hunger
        self.tiredness = tiredness

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        '''Sprawdzenie czy imie zostalo wpisane poprawnie'''
        if len(name)>=3 and name.isalpha():
            self.__name = name
        elif len(name)<3:
            raise ValueError("Your name is too short!")
        elif not name.isalpha():
            raise ValueError("Name must be a string")

    @property
    def mood(self):
        '''Właściwość określająca nastrój'''
        str = ''
        mood = self.hunger + self.tiredness
        if  mood < 5:
            str = '\033[31m'+'😍'+'\033[0m'
        elif 5 <=  mood <= 10 :
            str = '\033[93m'+'🙂'+'\033[0m'
        elif 11 <=  mood <= 15:
            str = '\033[32m'+'😐'+'\033[0m'
        elif mood > 15:
            str = '\033[35m'+'☹'+'\033[0m'
        return str

    def __passage_of_time(self):
        '''Zwiększanie głodu i znudzenia zwierzaka w zależności od akcji jakie są wykonywane'''
        import sys
        action = sys._getframe().f_back.f_code.co_name
        if  action == 'talk':
            self.hunger += 1
            self.tiredness += 1
        elif action == 'eat':
            self.tiredness += 1
            print(action)
        elif action == 'play':
            self.hunger += 1
            print(action)

    def __str__(self):
        return 'IMIE: {0} | 🍗: {1} | ⚡: {2}'.format(self.name,self.hunger,self.tiredness)

    def talk(self):
        '''Wyświetla informacje o natroju'''
        self.__passage_of_time()
        print('NASTRÓJ: {0}'.format(self.mood))


    def eat(self, food=4):
        '''Zmniejsza glod zwierzaka'''
        if food > 4:
            print("Podano zle wartosci")
        else:
            self.hunger -=food
            if self.hunger < 0:
                self.hunger = 0
            self.__passage_of_time()

    def play(self, val):
        '''Zmniejsza znudzenie zwierzaka'''
        if val > 4:
            print("Podano zle wartosci")
        else:
            self.tiredness -=val
            if self.tiredness < 0:
                self.tiredness = 0
            self.__passage_of_time()

    def main(self):
        '''Obsługa zwierzaka'''
        end = False
        while not end:
            print()
            print('-'*16,'MENU','-'*16)
            print(self)
            print('\n1. Zapytaj o nastrój')
            print('2. Nakarm')
            print('3. Pobaw się')
            print('4. END\n')
            x = int(input('Co chcesz zrobić: '))
            print('\n'*50)

            if x == 1:
                self.talk()
            elif x == 2:
                print("Każdy posiłek regeneruje podaną ilość punktów głodu\n"
                      "1 - 🍅\n"
                      "2 - 🍞\n"
                      "3 - 🍔\n"
                      "4 - 🍕\n"
                      )
                eat = int(input('Wybierz: '))
                self.eat(eat)
            elif x == 3:
                print("Każda zabawa zmniejsza podana liczbe znudzenia\n"
                      "1 - ⚽\n"
                      "2 - 🏐\n"
                      "3 - 🎳\n"
                      "4 - 🏹\n"
                      )
                play = int(input('Wybierz: '))
                self.play(play)
            elif x == 4:
                end = True


if __name__=='__main__':
    obiekt = Pet()
    obiekt.main()
