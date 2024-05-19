import pandas as pd

#Comando para criar uma tabela com dados especificados no DataFrame()
var = pd.DataFrame(dict)

# .index altera os valores do index nas linhas do DataFrame gerado para o que você colocar na lista.
var.index = []

#Caso tenham muitos dados e eles esteja separado por um arquivo CSV (valores separados por virgulas)
#Detalhe que pode realizar a leitura de diversos formatos além de CSV
var = pd.read_csv("caminho/para/documento.csv", index_col=0) #index_col diz que o index da tabela é a coluna especificada.


#Para selecionar dados de uma coluna especifica do DataFrame, basta realizar a chamada utilizando 2 [["nome_da_coluna"]]
#Assim, iremos consultar os dados da coluna selecionada ou de mais de uma se for necessários
colunas = nomeDataFrame[["nome_da_coluna", "nome_da_coluna_2"]]

#Para selecionar as linhas, utilizamos o [0:1], lembrnado que exclui o valor final.
linhas = nomeDataFrame[0:3]

# .loc possibilita pegar dados das linhas de forma mais fácil, basta usar o nomeDataFrame.loc[["index"]]
linhas_loc = nomeDataFrame.loc[["index"], ["coluna1", "coluna2"]] #após o index, caso queira selecionar colunas especificas é só colocar a virgula.


# com .iloc podemos usar de forma igual ao .loc, porém utilizando os números como indices.