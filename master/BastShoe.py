current_string = ""  # Текущая строка
list_changed = []  # Список изменений
list_redo = []  # Список для отмены отмены
changed = False  # Признак, что были изменения

def BastShoe(command:str):
    global current_string, list_changed, list_redo, changed  # Помечаем глобальные переменные, что позволит записывать в них новые значения. Важно это сделать в начале ф-ии
    
    if command[0] == "1":  # Добавить строку
        if changed == True:  # Обнуляем список изменений и список отмены изменений
            list_changed = list_changed[-1:]
            list_redo = []
        current_string += command[2:]
        list_changed.append(current_string)
        changed = False 

    elif command[0] == "2":  # Удалить n = int(command[2:]) символов
        if changed == True:  # Обнуляем список изменений и список отмены изменений
            list_changed = list_changed[-1:]
            list_redo = []
        i = len(current_string) - int(command[2:])
        if i > 0:
            current_string = current_string[:i]
        else: 
            current_string = ""
        list_changed.append(current_string)
        changed = False 

    elif command[0] == "3":  # Выдать i-й символ текущей строки
        i = int(command[2:])
        if i <= (len(current_string) - 1):
            return current_string[i]
        else:
            return ""

    elif command[0] == "4":  # Отмена последней операции 1 или 2
        if len(list_changed) > 1:
            current_string = list_changed[-2]
            list_redo.append(list_changed[-1])
            list_changed.pop()  # Удаляем последний эл-т из списка
        else:
            current_string = list_changed[-1]
        changed = True

    elif command[0] == "5":  # выполнить заново последнюю отменённую операцию
        if len(list_redo) >= 1:
            current_string = list_redo[-1]
            list_changed.append(list_redo[-1])
            list_redo.pop()
        else:
            current_string = current_string
        changed = True
 
    return current_string
