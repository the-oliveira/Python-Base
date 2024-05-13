#Histogramas:
import matplotlib.pyplot as plt

values = [0, 1.2, 1.6, 2.3, 2.4, 3.5, 4.6]

plt.hist(values, bins=3) #bins = Grafico exibe quantos valores possuem a cada X bins.

plt.show()
