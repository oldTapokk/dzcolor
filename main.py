import colorama
from colorama import Fore, Back, Style

print(Fore.RED + "Этот текст красного цвета")
print(Back.BLUE + "Синий фон для этого текста")
print(Style.BRIGHT + "Яркий текст")
print(Fore.BLUE + Back.YELLOW + "Синий текст на желтом фоне")
print("Этот текст вернется к обычным цветам и стилю")
print(Style.RESET_ALL + "Теперь все сброшено")

