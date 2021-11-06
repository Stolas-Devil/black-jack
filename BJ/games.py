#Модуль gemes
# Демонстрирует сосдание модуля

def ask_yes_no(question):
    """топрос да или нет"""
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)? ').lower()
    return response    

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
