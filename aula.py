import pyautogui as pg
import time


class media:
    def open_sites(self):
        pg.hotkey(['win', 'r'])
        time.sleep(2)
        # Abrir Chorme
        pg.write('chrome')
        pg.hotkey('Enter')

        # Ventana das Contas
        tab = 8
        while tab > 0:
            pg.hotkey('tab')
            tab -= 1
            print(f'Tab número {tab}')
        pg.hotkey('Enter')

        # Abrir um site
        pg.write('totidiversidade.com.br')
        pg.hotkey('Enter')

        # Abrir outro site em uma nova aba
        pg.hotkey(['ctrl', 't'])
        pg.write('linkedin.com')
        pg.hotkey('Enter')

    def my_position(self):
        time.sleep(4)
        print(pg.position())
        # A posição muda pedendedo da tela, ver no terminal o valor de X e Y
        pg.click(x=149, y=747, button='left', clicks=1)


media.open_sites(self='')
media.my_position(self='')
