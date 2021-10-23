#Модуль gemes
# Демонстрирует сосдание модуля

def ask_yes_no(question):
    """топрос да или нет"""
    reseponse = None
    while reseponse not in ("y", "n"):
        reseponse = input(question + ' (y/n)? ').lower

#

def ask_number(question, low, high):
    """Просит вести число из диапозона"""
    response = None
    while response not in range(low, high + 1):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("Вы запустили модуль games")
    input("\n\nНамите Enter, чтобы выйти.")
