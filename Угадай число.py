import random as r
from loguru import logger 
import os

#Переменные
run = True #Отвечает за продолжение цикла
awr = "Утка" #Отвечает за выход из игры
AI_number = 0
player_number = 0


#MAIN LOOP
while run: 
	
	print("Я загадал число от 1 до 100, попробуйте его угадать!")
	print("=" * 40)
	AI_number = r.randint(1, 100)
	logger.debug(AI_number)
	
	#Игра
	while True:
		player_number = int(input("Введите своё число: "))
		if player_number == AI_number:
			print("Вы угадали!")
			
			if input("Хотите сыграть ещё раз? (Да/Нет): ") == "Д" or "Y" or "Да" or "Yes":
				break
			else:
				quit()
		elif player_number > AI_number:
			print("Моё число меньше вашего. Берите меньше")
		else:
			print("Моё число больше вашего. Берите больше")
		print("=" * 40)

	os.console("cls")

input("Выйти")
quit()
