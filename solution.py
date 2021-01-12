import random


def main():
    print_header()
    main_loop()


def main_loop():
    enemies = [10, 5, 13, 8, 7]
    print('Du betrittst die Schule und hast noch 12 Minuten bis du bei deinem Klassenraum sein musst.')
    print()

    for lvl in enemies:
        enemy = f'Schüler (Jg. {lvl})'
        print(f'Du siehst einen {enemy}.')
        cmd = input('[S]prichst du ihn an, versuchst du, ihn zu [i]gnorieren oder siehst du dich [u]m? ')
        print()

        if cmd in ['S', 's']:
            print('> Der Schüler ist sehr aggressiv und beleidigt dich.')
            print('> Du würfelst 22')
            print(f'> Der {enemy} würfelt 7')
            print(f'> Deine Antwort war sehr effektiv! Der {enemy} verschwindet.')
            print()

        elif cmd in ['I', 'i']:
            print('> Du ziehst deinen Kopf ein und läufst schnell weiter.')
            print(f'> Der {enemy} bemerkt dich nicht einmal.')
            print()

        elif cmd in ['U', 'u']:
            print('> Du siehst dich um und siehst:')
            random.shuffle(enemies)
            for list_enemy in enemies:
                if random.randint(0, 1) == 0:
                    print(f'  * Einen Schüler (Jg. {list_enemy})')
                else:
                    print(f'  * Eine Schülerin (Jg. {list_enemy})')
            print()


def print_header():
    print('-------------------------------------')
    print('           EGGE QUEST')
    print('-------------------------------------')
    print()


if __name__ == '__main__':
    main()
