total = 0
list = [{"product":1, "quantity":1}, {"product":2, "quantity":2}]

for x in list:
    total = total + (x['product'])
print(total)