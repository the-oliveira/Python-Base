#Para utilizar comparações com arrays usando numpy utilizamos:
import numpy as np
lista = [0, 1, 2, 10, 30]
nomeArray = np.array(lista)

#np.logical_and(comparação) para AND
#np.logical_or(comparação) para OR
#np.logical_not(comparação) para NOT

#exemplo:
np.logical_and(nomeArray < 20, nomeArray > 30)

#Se colocar o resultando entre [] teremos os valores TRUE
#Exemplo:

print(nomeArray[np.logical_and(nomeArray < 20, nomeArray > 1)])


