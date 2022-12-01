#from loguru import logger 
from rich.console import Console
import random as r
import os

#Переменные
console = Console()
run = True #Отвечает за продолжение цикла
AI_number = 0 #Загаданое число
player_number = 0 #Число игрока
counter = 0 #Кол-во попыток 

#MAIN LOOP
while True: 
	
	#Обнуляем переменные
	run = True
	counter = 0

	#Вступление
	print("Я загадал число от 1 до 100, попробуйте его угадать!")
	print("=" * 40)
	AI_number = r.randint(1, 100)
	#logger.debug(AI_number)
	
	#Игра
	while run:
		player_number = int(input("Введите своё число: "))
		counter += 1

		if player_number == AI_number: #Игрок угадал		
			run = False
			console.print(f"Вы угадали потратив на это {counter} попыток!", style="bold green")
			print("=" * 40)
			
			if input('Хотите сыграть ещё раз? Введите "0" если нет: ') == "0":
				quit()
			
			else:
				pass
		
		elif player_number > AI_number: #Число игрока больше загадоного
			console.print("Моё число [bold cyan]меньше[/bold cyan] вашего. Берите меньше")
		
		else: #Число игрока меньше загадоного
			console.print("Моё число [bold cyan]больше[/bold cyan] вашего. Берите больше")
		
		print("=" * 40)

	os.system('cls')

input("Бесконечный цикл закончился. Штирлиц застрелился. Enter - выйти")
quit()
