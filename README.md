# Algoritmo Genético para Problema de Timetabling
Este repositório contém um código Python implementando um algoritmo genético para resolver um problema de timetabling. O problema é especificamente formulado para atender a necessidades de agendamento, e o algoritmo genético busca otimizar uma solução para esse problema.

## Estrutura do Repositório
`geneticalgorithm.py`: Este arquivo contém a implementação principal do algoritmo genético. A classe GeneticAlgorithm possui métodos para gerar uma população inicial, realizar crossover, seleção dos melhores indivíduos (fitness), e mutação. Além disso, há comentários detalhados explicando cada função.

`config.py`: Este arquivo contém uma classe Config que fornece funcionalidades auxiliares, como leitura de arquivo CSV, tratamento de dados, somatório, e ordenação reversa. Essas funções são utilizadas na lógica do algoritmo genético.

`main.py`: Este é o arquivo principal do programa. Ele instancia a classe GeneticAlgorithm, define um dicionário de informações, gera uma população inicial, executa o algoritmo genético e exibe os resultados.

`Dockerfile` e `docker-compose.yml`: Estes arquivos fornecem a configuração para criar um ambiente de contêiner Docker. Isso facilita a execução do código em diferentes ambientes sem a necessidade de configurar dependências manualmente.

## Utilização

### Requisitos:
Certifique-se de ter o Docker instalado em seu sistema.

### Construção do Contêiner:
Execute o seguinte comando para construir o contêiner:
```bash
docker-compose build
```

### Execução do Jupyter Notebook:
Inicie o Jupyter Notebook dentro do contêiner:
```bash
docker-compose up
```

Isso iniciará o Jupyter Notebook na porta 4000. Acesse o link gerado no navegador para interagir com o código.

## Execução do Algoritmo Genético:
Abra o arquivo main.py no Jupyter Notebook e execute as células. Isso gerará uma população inicial, realizará as iterações do algoritmo genético e exibirá os resultados.

# Observações
Este código é fornecido como exemplo educacional e pode ser adaptado para diferentes problemas de otimização. Certifique-se de ajustar os parâmetros do algoritmo genético de acordo com a natureza específica do problema que você está resolvendo.

Lembre-se de ajustar o arquivo `requirements.txt` conforme necessário e considerar as configurações específicas do ambiente em que o código será executado. 