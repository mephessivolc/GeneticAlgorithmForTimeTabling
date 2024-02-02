import csv
import random
import math
import numpy as np

class Config:
    def show(self, conjunto):
        for i in conjunto:
            print(i)

    def read_file(self, name="timetabling.csv"):
        """
            A função read_file tem como objetivo preparar um arquivo CSV fornecido para ser utilizado no algoritmo. O arquivo 
            contém informações necessárias para um problema de timetabling.

            Parâmetros:
                name (str, padrão="inputs/timetabling.csv"): O caminho e nome do arquivo CSV a ser lido.

            Retorno:
                list: Uma lista de listas contendo as informações do arquivo CSV preparado para uso no programa.
                Funcionamento:
                
            A função utiliza a biblioteca csv para ler o arquivo CSV especificado. Cada linha do arquivo é processada, convertendo os valores separados por espaços em uma lista de informações. A primeira entrada de cada linha é considerada como uma identificação única, enquanto as entradas subsequentes são convertidas em valores inteiros. As listas resultantes são agregadas em uma lista principal, que é então retornada.

        """
        with open(name, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=" ", quotechar=',')
            infos = []
            for row in csvreader:
                tmp = [row[0]]
                for i in row[1:]:
                    tmp.append(int(i))  
                
                infos.append(tmp)

        return infos

    def treatment(self, infos):
        """
            A função treatment tem como objetivo realizar o tratamento de dados transformando uma sequência de sequências em um 
            dicionário de listas. Cada lista é associada a uma chave, representada pelo índice da sequência original.

            Parâmetros:
                infos (list ou np.ndarray): Uma sequência de sequências contendo informações a serem tratadas.
            
            Retorno:
                dict: Um dicionário onde as chaves são os índices das sequências originais, e os valores são listas contendo 
                    tuplas com informações da sequência.
            
            Funcionamento:
                A função itera sobre cada sequência na entrada infos. Para cada elemento na sequência, exceto o primeiro, verifica 
                se a chave correspondente já existe no dicionário dict_infos. Se existir, adiciona uma tupla contendo o primeiro 
                elemento da sequência (o nome) e o valor na posição atual da sequência. Se a chave não existir, cria uma nova 
                chave e inicia uma lista com a primeira tupla.
        """

        if not isinstance(infos, np.generic):
            infos = np.array(infos)

        dict_infos = {}
        for _ in infos:
            for i in range(1,len(_[1:])): 
                if i in dict_infos:
                    
                    dict_infos[i].append((_[0], int(_[i])))
                else:
                    dict_infos[i] = [(_[0], int(_[i]))]

        return dict_infos

    def somatorio(self, individuos):
        """
            A função somatorio tem como objetivo calcular a soma de todos os valores em cada sequência de uma sequência 
            de sequências (individuos). O resultado da soma é então adicionado como um novo elemento, uma tupla contendo 
            a string "soma" e o valor da soma, ao final de cada sequência.

            Parâmetros:
                individuos (list): Uma sequência de sequências contendo valores a serem somados.

            Retorno:
                list: Uma nova sequência de sequências onde, para cada sequência original, foi adicionada uma tupla 
                    representando a soma dos valores contidos na sequência.

            Funcionamento:
                A função itera sobre cada sequência (individuo) na entrada individuos. Para cada sequência, calcula a soma 
                de todos os valores contidos nela. Se já existir uma tupla com a string "soma" como primeiro elemento na 
                sequência, ela é removida. Após o cálculo da soma, uma nova tupla é adicionada ao final da sequência, 
                contendo a string "soma" e o valor calculado.
        """
        for individuo in individuos:
            if "soma" in individuo[-1][0]:
                individuo.pop()

            soma = sum(item[1] for item in individuo)
            individuo.append(("soma", soma))

        return individuos

    def ordenar_reverso(self, individuos):
        """
            A função ordenar_reverso tem como objetivo ordenar uma sequência de sequências em ordem decrescente 
            com base no último parâmetro de cada sequência.

            Parâmetros:
                individuos (list): Uma sequência de sequências a ser ordenada.
            
            Retorno:
                list: Uma nova sequência de sequências ordenadas de forma decrescente com base no último parâmetro de cada sequência.
            
            Funcionamento:
                A função utiliza a função sorted para ordenar as sequências com base em uma chave definida pela expressão 
                lambda lambda x: x[-1], que extrai o último elemento de cada sequência. O parâmetro reverse=True indica 
                que a ordenação deve ser feita de forma decrescente.
        """
        return sorted(individuos, key=lambda x: x[-1], reverse=True)

if __name__ == "__main__":
    q = Config()