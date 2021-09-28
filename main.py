from sympy import *

x, y, z, t = symbols('x y z t')

li = []
with open('test.txt') as f:
    li = f.read().splitlines()
for i in range(len(li)):
    li[i] = float(li[i])
print('Значения')
print(li)

f = li[0] + li[1] * x + li[2] * y + li[3] * z + li[4] * t + li[5] * x ** 2 + li[6] * x * y + li[7] * x * z + li[8] \
    * x * t + li[9] * y * x + li[10] * y ** 2 + li[11] * y * z + li[12] * y * t + li[13] * z * x + li[14] * z * y + \
    li[15] * z ** 2 + li[16] * z * t + li[17] * t * x + li[18] * t * y + li[19] * t * z + li[20] * t ** 2 + \
    li[5] * x ** 2 + li[10] * y ** 2 + li[15] * z ** 2 + li[20] * t ** 2

d_x = diff(f, x)
d_y = diff(f, y)
d_z = diff(f, z)
d_t = diff(f, t)

print('Производная по X')
print(d_x, '= 0')
print('Производная по Y')
print(d_y, '= 0')
print('Производная по Z')
print(d_z, '= 0')
print('Производная по T')
print(d_t, '= 0')

li_2_x = str(d_x).split('+')
s_x = ''.join(li_2_x)
li_3_x = s_x.split()
s_2_x = ''.join(li_3_x)
li_x = s_2_x.split('*')
for i in range(1, len(li_x)):
    li_x[i] = li_x[i][1:]

li_2_y = str(d_y).split('+')
s_y = ''.join(li_2_y)
li_3_y = s_y.split()
s_2_y = ''.join(li_3_y)
li_y = s_2_y.split('*')
for i in range(1, len(li_y)):
    li_y[i] = li_y[i][1:]

li_2_z = str(d_z).split('+')
s_z = ''.join(li_2_z)
li_3_z = s_z.split()
s_2_z = ''.join(li_3_z)
li_z = s_2_z.split('*')
for i in range(1, len(li_z)):
    li_z[i] = li_z[i][1:]

li_2_t = str(d_t).split('+')
s_t = ''.join(li_2_t)
li_3_t = s_t.split()
s_2_t = ''.join(li_3_t)
li_t = s_2_t.split('*')
for i in range(1, len(li_t)):
    li_t[i] = li_t[i][1:]

for r in range(len(li_x)):
    li_x[r] = float(li_x[r])
    li_y[r] = float(li_y[r])
    li_z[r] = float(li_z[r])
    li_t[r] = float(li_t[r])

list = [li_x, li_y, li_z, li_t]
print('Матричный вид')
print(*list, sep='\n')

for j in range(4):
    for i in range(4):
        if i > j:
            c = (list[i][j] / list[j][j])
            for k in range(5):
                list[i][k] = list[i][k] - c * list[j][k]
x = [0, 0, 0, 0]
x[3] = list[3][4] / list[3][3]
for i in range(2, -1, -1):
    sum = 0
    j = i
    for j in range(i, 4):
        sum = sum + list[i][j] * x[j]
    x[i] = (list[i][4] - sum) / list[i][i]
print('Решение')
print('X =', x[1] * -1)
print('Y =', x[2] * -1)
print('Z =', x[3] * -1)
print('T =', x[0] * -1)
input('Press Enter')
