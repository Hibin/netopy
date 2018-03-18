import math

day_cost = int(input('Стоимость суток, евро:')) # euro

euro_exchange_rate = 70.71
budget_euro = 20000

trip_count = 3

trip_length1 = 10 # Framce
trip_length2 = 5 # Turkey
trip_length3 = 7 # Finland

flight_cost = 50
flights_per_trip = 2

# expenses
expenses_tourist1 = [500, 100, 50, 80]
expenses_tourist2 = [90, 763, 345, 229, 10]
expenses_tourist3 = [83, 6, 223, 1000, 4, 980]

# expenses sum
expenses_tourist1_sum = sum(expenses_tourist1);
expenses_tourist2_sum = sum(expenses_tourist2);
expenses_tourist3_sum = sum(expenses_tourist3);

# total expenses sum
expenses_tourists_all_sum = sum([expenses_tourist1_sum, expenses_tourist2_sum, expenses_tourist3_sum])

# sum, euro
trip_cost_euro = (trip_length1 + trip_length2 + trip_length3) * day_cost
trip_cost_euro += trip_count * flight_cost * flights_per_trip
trip_cost_euro += expenses_tourists_all_sum

# sum, rubles
trip_cost_rubles = round(trip_cost_euro * euro_exchange_rate, 2)

# balance
balance = budget_euro - trip_cost_euro

print('Курс евро', euro_exchange_rate, sep = ': ')
print('Стоимость поездок, евро', trip_cost_euro, sep = ': ')
print('Стоимость поездок, рубли', trip_cost_rubles, sep = ': ', end='\n\n')

print('Расходы туриста 1, евро', expenses_tourist1_sum, sep = ': ')
print('Расходы туриста 2, евро', expenses_tourist2_sum, sep = ': ')
print('Расходы туриста 3, евро', expenses_tourist3_sum, sep = ': ', end='\n\n')

if balance <= 0:
    print('Внимание! Бюджет превышен!')
else:
    print('В бюджете осталось, евро', balance, sep = ': ')

