import matplotlib.pyplot as plt

f = open('list.txt', 'r')
Y = []
X = []
label = []
mas = []
for line in f:
    if line.find('\ufeff')!=-1:
        continue
    mas = line.split()
    if mas.__len__() == 1:
        label.append(mas[0])
    elif mas.__len__() == 0:
        continue
    elif mas.__len__() == 2:
        Y.append(float(mas[0]))
        X.append(float(mas[1]))


for n in range (label.__len__()) :
    plt.plot(Y[n*500+1:((n+1)*500)],X[n*500+1:((n+1)*500)],label=label[n])
plt.yscale('log')
plt.legend()
plt.xlabel('E, MeV')
plt.ylabel('count')
plt.title ('Carbon spectrum')
plt.show()
