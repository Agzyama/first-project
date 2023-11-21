#считать данные и построить график дата\скорость
import matplotlib.pyplot as plt
def massives(x,n):
    y = 0
    for t in range(n,len(R),2):
        x[y] = R[t]
        y += 1
f = open("PZ_Mon_v_radial_1__1.dat" , "r")
f = f.read()
g = [0 for j in range(len(f))]
for i in range(len(f)):
    if f[i].isupper():
        g[i] = f[i].lower()
    else:
        g[i] = f[i]

q = 0
while q < len(g):
    if g[q] == '_':
        g.pop(q)
        q -= 1
    elif g[q] == "\n":
        g[q] = " "
    q += 1
Q = ''.join(g)
R = Q.split(' ')

e = 0
while e < len(R):
    if R[e] == '':
        R.pop(e)
        e -= 1
    e += 1

w = 0
while w < 2:
    R.__delitem__(0)
    w += 1
print(len(R))
for i in range(len(R)):
    R[i] = float(R[i])
data = [0 for i in range(int(len(R)/2))]
massives(data,0)
coord = [0 for i in range(int(len(R)/2))]
massives(coord,1)
plt.figure()
plt.scatter(data,coord)
plt.xlabel("MJD")
plt.ylabel("Vr")
plt.title("Grafic")
plt.show()
print(data,coord)