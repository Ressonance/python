# Программа "Автодилер"

car_price = int(input("Стоимость автомобиля без наценок :"))
tax = car_price * 5 / 100
reg = car_price * 15 / 100
collection_agency = 5000
delivery = 2500
total = car_price + tax + reg + collection_agency + delivery
print("Стоимость вашего автомобиля составляет :",int(total), "тыс.руб")

