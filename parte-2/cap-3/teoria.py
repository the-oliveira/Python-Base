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


#podemos usar comparações em DataFrames
#basta selecionar o dataframe, fazer a comparação e armazenar em uma nova variavel(dataframe series) assim criamos um dataframe depois

#selecionar coluna para comparação:


#Criamos primeiro a seleção da coluna e sua comparação
comparar_info = dataFrame["coluna"] > 8
#Depois é só utilizar o dataframe[filtro], assim obteremos os resultados que se encaixam no filtro.
dataFrame[comparar_info] #Ou podemos fazer tudo em uma linha: dataFrame[dataFrame["coluna"] > 8]

#no caso do and, or e not, utilizamos as comparações do numpy (logical)