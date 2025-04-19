from colorama import init, Fore, Back, Style

init()

print(Fore.RED + 'Червоний текст' + Style.RESET_ALL)
print(Back.GREEN + 'Текст із зеленим фоном' + Style.RESET_ALL)
print(Style.BRIGHT + 'Яскравий текст' + Style.RESET_ALL)


##colorama.init() — ініціалізує бібліотеку

#Fore, Back, Style — основні підмодулі для керування кольором тексту фоном і стилем

#deinit(), reinit() — дозволяють вимкнути або перевстановити colorama 

#Fore.RED, Back.YELLOW, Style.BRIGHT тощо — це коди для кольорів/стилів, які використовуються у форматуванні рядків
#
