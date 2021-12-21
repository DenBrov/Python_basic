from sys import argv

script_name, prod_in_hour, rate_in_hour, prize = argv

wage = int(prod_in_hour) * int(rate_in_hour) + int(prize)

print('Ваша заработная плата: ', wage)