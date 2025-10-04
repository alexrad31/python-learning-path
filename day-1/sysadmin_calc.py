#Расчет свободного места на диске (имитация)
print("===Сисадминский калькулятор===")
total_space_gb = 500
used_space_gb = 345
free_space = total_space_gb - used_space_gb
print(f"Всего места: {total_space_gb} GB")
print(f"Использовано: {used_space_gb} GB")
print(f"Свободно: {free_space} GB")
# Расчет в процентах
used_percent = used_space_gb/total_space_gb*100
print(f"Заполнено: {used_percent:.1f}%")