import random
from config import Config as config

class GeneticAlgorithm:
    def gerar_populacao(self, n_ind, dict_infos):
        """
            A função gerar_populacao tem como finalidade criar uma população inicial para um algoritmo genético, gerando 
            uma quantidade especificada de indivíduos. Cada indivíduo é construído a partir de um dicionário de listas (dict_infos), 
            onde cada chave representa um gene e suas possíveis opções estão nas listas associadas.

            Parâmetros:
                n_ind (int): O número de indivíduos a serem gerados para a população inicial.
                dict_infos (dict): Um dicionário de listas contendo as opções possíveis para cada gene.
            
            Retorno:
                list: Uma lista de sequências representando a população inicial para o algoritmo genético.
            
            Funcionamento:
                A função itera sobre o número especificado de indivíduos (n_ind). Para cada indivíduo, seleciona aleatoriamente 
                uma opção para cada gene a partir do dicionário dict_infos. Em seguida, a função realiza o somatório dos 
                valores de cada indivíduo e os adiciona na sequência. Posteriormente, a população é ordenada de forma 
                decrescente com base no valor do somatório.
        """
        individuos = []
        for _ in range(n_ind):
            tmp = []
            for key, value in dict_infos.items():
                tmp.append(random.choice(value))
        
            individuos.append(tmp)
        
        config.somatorio(individuos)
        
        individuos = config.ordenar_reverso(individuos)

        return individuos


    def crossover(self, individuos, qtd=10):
        """
            Realiza a operação de crossover em uma população de indivíduos, promovendo a troca aleatória 
            de informação genética entre pares de indivíduos para criar novos descendentes.

            Parâmetros:
                - individuos (list): Uma lista contendo os indivíduos que serão submetidos à operação de crossover.
                - qtd (int, padrão=10): O número de pares de indivíduos que passarão pelo crossover. Cada par resultará em dois 
                descendentes.
            
            Retorno:
                - list: Uma nova lista contendo a população original e os descendentes gerados pelo crossover.
            
            Funcionamento:
                Para cada par de indivíduos selecionado aleatoriamente, um ponto de crossover (n) é escolhido aleatoriamente. 
                Os cromossomos antes desse ponto de um pai e depois desse ponto no outro pai são trocados, gerando um descendente. 
                Esse descendentes é adicionado à população original.
        """

        tmp = []
        for _ in range(qtd):
            ind1 = random.choice(individuos)
            ind2 = random.choice(individuos)
        
            n = random.randint(0, len(ind1)-1)
        
            ind3 = ind1[:n] + ind2[n:]

            tmp.append(ind3)

        return (individuos + tmp).copy()

    def fit(self, individuos, n=10):
        """
            Realiza a seleção de indivíduos em um contexto de algoritmo genético, mantendo os mais adaptados na população 
            e descartando os n piores elementos.

            Parâmetros:
                - individuos (list): Uma lista contendo os indivíduos a serem avaliados e selecionados.
                - n (int, padrão=10): O número de indivíduos a serem mantidos na população. Os (len(individuos)-n) melhores indivíduos, 
                com base em sua aptidão, serão preservados.

            Retorno:
                - list: Uma lista contendo os n melhores indivíduos, selecionados com base em sua aptidão.
        """

        return individuos[:n].copy()

    def mutacao(self, individuos, original):
        """
            A função mutacao realiza a operação de mutação em um indivíduo selecionado aleatoriamente de 
            uma população de acordo com a tabela de dados original. A mutação envolve a troca de um cromossomo aleatório 
            do indivíduo por um novo valor proveniente da tabela original.

            Parâmetros:

                individuos (list): Uma lista de indivíduos que serão submetidos à operação de mutação.
                original (dict): Uma tabela de dados original que contém os possíveis valores que podem ser usados para realizar a 
                mutação.
                
            Retorno:

                list: Uma nova lista contendo a população após a realização da mutação.
            
            Funcionamento:
                Um índice aleatório é escolhido da tabela original (rand_index_original), representando a fonte de novos valores. 
                Um indivíduo aleatório (rand_individuo) é escolhido da população, e um índice aleatório desse indivíduo 
                (rand_index_individuo) é selecionado. O valor nesse índice é então substituído pelo valor correspondente na tabela 
                original.

                Após a mutação, a função realiza operações adicionais como somatório (config.somatorio) e ordenação reversa 
                (config.ordenar_reverso) na população resultante.
        """
        
        rand_index_original = random.choice(list(original.keys()))
        rand_individuo = random.choice(individuos)

        rand_index_individuo = random.randint(0, len(rand_individuo[:-1])-1)
        rand_individuo[rand_index_individuo] = original[rand_index_original][rand_index_individuo]

        individuos = config.somatorio(individuos)
        individuos = config.ordenar_reverso(individuos)

        return individuos.copy()
