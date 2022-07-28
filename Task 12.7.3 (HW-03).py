per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму денег:")
a = int(money)
a = per_cent['ТКБ'] * a / 100, per_cent['СКБ'] * a / 100, per_cent['ВТБ'] * a / 100, per_cent['СБЕР'] * a / 100
deposit = list(a)
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
