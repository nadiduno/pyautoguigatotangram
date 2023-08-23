import pyautogui
import time
#Abrir Paint
#pyautogui.press('win')
#pyautogui.write('paint')
#pyautogui.press('enter')

time.sleep(3)

#Gato Tangram

#Queixo
pyautogui.moveTo(500, 400)
pyautogui.dragTo(450, 450, duration=0.25)
pyautogui.moveTo(400, 400)
pyautogui.dragTo(450, 450, duration=0.25)
pyautogui.moveTo(400, 300)
#Cara
pyautogui.moveTo(500, 400)
pyautogui.dragTo(500, 300, duration=0.25)
pyautogui.moveTo(400, 300)
pyautogui.dragTo(400, 400, duration=0.25)
#Orelhas
pyautogui.moveTo(400, 300)
pyautogui.dragTo(450, 330, duration=0.25)
pyautogui.moveTo(500, 300)
pyautogui.dragTo(450, 330, duration=0.25)
#Bigotes esquerdos
pyautogui.moveTo(430, 380)
pyautogui.dragTo(380, 330, duration=0.25)
pyautogui.moveTo(410, 380)
pyautogui.dragTo(370, 350, duration=0.25)
#Bigotes direitos
pyautogui.moveTo(470, 380)
pyautogui.dragTo(520, 330, duration=0.25)
pyautogui.moveTo(490, 380)
pyautogui.dragTo(530, 350, duration=0.25)

#Salvar
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('catTangramNadi.png')
time.sleep(1)
pyautogui.press('enter')





