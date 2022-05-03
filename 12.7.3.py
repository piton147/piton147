
inv_sum = input ("please write a sum which you planed to invest for deposit: ")
x = inv_sum

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# deposit = list(map(int, list_of_inv_sum))
tkb = ("ТКБ:", int(per_cent.get("ТКБ")))
ckb = ("СКБ:", per_cent.get("СКБ"))
vtb = ("ВТБ:", per_cent.get("ВТБ"))
sb = ("СБЕР:", per_cent.get("СБЕР"))


deposit_tkb = (x * tkb/100)
deposit_ckb = (x * ckb/100)
deposit_vkb = (x * vkb/100)
deposit_sb = (x * sb/100)

print(deposit_tkb)
print(deposit_ckb)
print(deposit_vkb)
print(deposit_sb)
