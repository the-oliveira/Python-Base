import pandas as pd

#Comando para criar uma tabela com dados especificados no DataFrame()
var = pd.DataFrame(dict)

# .index altera os valores do index nas linhas do DataFrame gerado para o que você colocar na lista.
var.index = []

#Caso tenham muitos dados e eles esteja separado por um arquivo CSV (valores separados por virgulas)
#Detalhe que pode realizar a leitura de diversos formatos além de CSV
var = pd.read_csv("caminho/para/documento.csv", index_col=0) #index_col diz que o index da tabela é a coluna especificada.


