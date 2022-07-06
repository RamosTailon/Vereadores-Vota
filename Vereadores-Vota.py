'''
Esse programa faz leitura de arquivos gigantes de .csv e edita os valores
para fácil apresentação em excel, facilitando a utilização de gráficos.

'''

import pandas as pd

#Importa a tabela em csv
tabela_Vereador = pd.read_csv("votos_Vereadores_2020.csv", encoding= 'unicode_escape', sep=";")
tabela_Vereador.shape

#*************************************************

#Seleciona as colunas desejadas
tabela_resumida = tabela_Vereador[["CD_MUNICIPIO","NM_MUNICIPIO","NR_ZONA","NR_SECAO","NM_VOTAVEL","QT_VOTOS"]]

#*************************************************

#Cria uma nova coluna Bairro
tabela_resumida["BAIRROS"] = "sem bairro"

#**************************************************

#Coloca os números de cada seção em listas dos bairros
#VARIÁVEIS POR BAIRROS
ceu_azul_1 = [21,22,23,24,25,26,27,28,29,30,121,148,153,158,170,180,187,210,223,234,48,49,50,51,52,53,54,109,124,152,186] 
ceu_azul_2 = [55,56,57,129,135,193,212,228,100,101,102,103,104,105,106,113,131,155,166,179,190,194,203,207,211,216,222,230]
ceu_azul_3 = [67,68,69,126,174,200,71,72,73,74,75,108,167,181,204,227]
chac_anhan_b = [115,138,156,172,201,217] 
chac_ipanema = [76,77,78,119,145,161,171,188,224]
cidade_jardins = [70,94,114,130,142,162,176,191,205,215,229]
cruzeiro_sul = [63,64,65,66,123,151,173,185]
jardim_oriente = [46,47,82,83,84,85,86,95,96,97,141,150,184,192,117,122,128,133,136,157,189,163,175,198,213,226,236,110,125,137,149]
pacaembu = [80,81,107,182]
parq_araruama = [79,195]
parq_esplanada_V = [146,177,220]
parq_marajo = [93,111,127,134,168,197,219,233]
santa_rita = [89,90,91,92,154]
valparaiso_II = [36,37,38,39,40,41,42,43,44,45,208,231,98,99,120,139,165,196,221]
etapa_a = [13,14,15,16,17,18,160,178,199,214,225,235]
etapa_b = [1,2,3,4,5,6,7,8,9,10,11,12,19,20,31,32,33,34,35,140]
etapa_c = [58,59,60,61,118,144,209]
etapa_e = [87,88,112,164,206]
vila_guaira = [116,132,143,159,169,183,202,218,232] 

#**************************************************

#FUNÇÃO PYTHON PARA CONVERTER
'''
verifica os números das células da planilha tabela_resumida 
e converte no nome do bairro na coluna BAIRRO

'''

def conversor(num):
    for d in ceu_azul_1:
        if num == d:
            return "1 ETAPA DO JARDIM CÉU AZUL"
        else:
            pass
    for d in ceu_azul_2: 
        if num == d: 
            return "2 ETAPA DO JARDIM CÉU AZUL"
        else:
            pass
    for d in ceu_azul_3:
        if num == d: 
            return "3 ETAPA DO JARDIM CÉU AZUL"
        else:
            pass
    for d in chac_anhan_b:
        if num == d: 
            return "CHACARAS ANHANGUERA B"
        else:
            pass
    for d in chac_ipanema:
        if num == d: 
            return "CHACARAS IPANEMA"
        else:
            pass
    for d in cidade_jardins:
        if num == d: 
            return "Cidade Jardins"
        else:
            pass
    for d in cruzeiro_sul:
        if num == d: 
            return "CRUZEIRO DO SUL"
        else:
            pass
    for d in jardim_oriente:
        if num == d: 
            return "Jardim oriente"
        else:
            pass
    for d in pacaembu:
        if num == d: 
            return "Loteamento Pacaembu"
        else:
            pass
    for d in parq_araruama:
        if num == d: 
            return "Parque araruama"
        else:
            pass
    for d in parq_esplanada_V:
        if num == d: 
            return "Parque Esplanada V"
        else:
            pass
    for d in parq_marajo:
        if num == d: 
            return "Parque Marajo"
        else:
            pass
       
    for d in santa_rita:
        if num == d: 
            return "Parque Santa Rita de Cassia"
        else:
            pass
    for d in valparaiso_II:
        if num == d: 
            return "Parque Valparaizo II"
        else:
            pass
    for d in etapa_a:
        if num == d: 
            return "Valparaiso I Etapa A"
        else:
            pass
    for d in etapa_b:
        if num == d: 
            return "Valparaiso I Etapa B"
        else:
            pass
    for d in etapa_c:
        if num == d: 
            return "Valparaiso I Etapa C"
        else:
            pass
    for d in etapa_e:
        if num == d: 
            return "Valparaiso I Etapa E"
        else:
            pass
    for d in vila_guaira:
        if num == d: 
            return "VILA GUAIRA"
        else:
            pass

#**************************************************

#Escolhe o nome do Parlamentar escolhido, no caso, "MARCELO OLIVEIRA BRASIL"
val_carnes = tabela_resumida.loc[tabela_resumida["NM_VOTAVEL"] == "MARCELO OLIVEIRA BRASIL"]
val_carnes.shape

#**************************************************
#converte em .xlsx
val_carnes.to_excel("Vereador_val_carnes.xlsx")

#**************************************************
'''
Devido não poder modificar uma visão de lista é mais pratico  
criar uma lista e abri-la novamente
'''
val_carnes_excel = pd.read_excel("Vereador_val_carnes.xlsx")

#**************************************************
#substituição por condição
for indice, valor in enumerate(val_carnes_excel["NR_SECAO"]):
    val_carnes_excel.loc[indice,"BAIRROS"] = conversor(valor)


#**************************************************

display(val_carnes_excel)

#**************************************************
#converte em .xlsx
val_carnes_excel.to_excel("Marcelo Val Carnes.xlsx")