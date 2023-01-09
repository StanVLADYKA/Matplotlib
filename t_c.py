# Сочетания – выбранные из множества n объектов комбинации m объектов,
# отличающиеся хотя бы одним объектом. Порядок элементов не важен.
#  Например, мы хотим составить трехцветную комбинацию.
# Есть четыре доступных цвета.
# Вычислить все возможные трехцветные комбинации

# 2/ Размещения – те же сочетания, для которых важен порядок следования элементов.
# Определить все варианты как мы можем составить трехцветную комбинацию с учётом порядка следования цветов

# https://all-python.ru/osnovy/itertools.html#product

import itertools


n_1 = list(itertools.combinations_with_replacement(["red","yellow","blue","white"],r = 3))
print(type(n_1))
for i in n_1:
    print(i)
print("total: ",len(n_1))

n_2 = list(itertools.permutations(["red","yellow","blue","white"],r = 3))
print(type(n_2))
for i in n_2:
    print(i)
print("total: ",len(n_2))