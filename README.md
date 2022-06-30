# sf22_feature_selection

Ferramenta para automatizar e simplificar a execução dos métodos.

Primeiras ideias:
(1) a ferramenta deve ser capaz de executar o método selecionado pelo usuário;
(2) a ferramenta deve ser flexível e simples para incorporar novos métodos (e.g., 1 diretório e 1 script de bootstrap por método);
(3) com a saída do método (i.e., dataset de características selecionadas), a ferramenta deve executar os modelos RF e SVM;
(4) a ferramenta irá apresentar o resultado das métricas dos modelos;
(5) a ferramenta deve permitir especificar: 
- o dataset de entrada;
- o prefixo do arquivo do dataset de saída de cada modelo de seleção;
- o arquivo de saída para as métricas dos modelos de ML RF e SVM;
(6) a ferramenta poderá também gerar automaticamente gráficos ou tabelas das saídas dos modelos RF e SVM;

Exemplos de parâmetros e execução:

tool.py --list-fs-methods --list-ml-models

tool.py --run-fs-rfg --run-fs-sigapi --run-ml-rf --run-ml-svm --output-fs-rfg rfg.csv --output-fs-sigapi sigapi.csv --output-ml-rf rf.csv --output-ml-svm svm.csv --plot-graph-all --dataset motodroid.csv 

tool.py --run-fs-all --run-ml-all --plot-graph-all --datasets motodroid.csv androcrawl.csv drebin215.csv

tool.py --run-fs-all --run-ml-all --plot-graph-all --datasets-all


###### methods
Códigos dos métodos.

###### datasets 
Datasets construídos para o estudo.

