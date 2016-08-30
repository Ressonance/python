# Щедрый посетитель

score = int(input("Введите сумму счета за обед: "))
print("Сумма счета :", score, "руб.")
first_tip = score * 15 / 100
second_tip = score * 20 / 100
print("Чаевые из расчета 15% : ", int(first_tip))
print("Чаевые из расчета 20% : ",int(second_tip))
