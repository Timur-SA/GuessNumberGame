import random as r
from loguru import logger 
from rich.console import Console
import os

#Переменные
console = Console()
run = True #Отвечает за продолжение цикла
awr = "Текст" #Отвечает за выход из игры
AI_number = 0
player_number = 0


#MAIN LOOP
while True: 
	
	run = True
	print("Я загадал число от 1 до 100, попробуйте его угадать!")
	print("=" * 40)
	AI_number = r.randint(1, 100)
	logger.debug(AI_number)
	
	#Игра
	while run:
		player_number = int(input("Введите своё число: "))
		if player_number == AI_number:			
			run = False
			console.print("Вы угадали!", style="bold green")
			print("=" * 40)
			awr = input('Хотите сыграть ещё раз? Введите "0" если нет: ')
			if awr == "0":
				quit()
			else:
				pass
		elif player_number > AI_number:
			console.print("Моё число [bold cyan]меньше[/bold cyan] вашего. Берите меньше")
		else:
			console.print("Моё число [bold cyan]больше[/bold cyan] вашего. Берите больше")
		print("=" * 40)

	os.system('cls')

input("Выйти")
quit()
