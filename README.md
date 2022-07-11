# sf22_feature_selection

Ferramenta para automatizar e simplificar a execução dos métodos.

Primeiras ideias:
1. A ferramenta deve ser capaz de executar o método selecionado pelo usuário;
2. A ferramenta deve ser flexível e simples para incorporar novos métodos (e.g., 1 diretório e 1 script de bootstrap por método);
3. Com a saída do método (i.e., dataset de características selecionadas), a ferramenta deve executar os modelos RF e SVM;
4. A ferramenta irá apresentar o resultado das métricas dos modelos;
5. A ferramenta deve permitir especificar: 
- o dataset de entrada;
- o prefixo do arquivo do dataset de saída de cada método de seleção;
- o arquivo de saída para as métricas dos modelos de ML RF e SVM;

6. A ferramenta poderá também gerar automaticamente gráficos ou tabelas das saídas dos modelos RF e SVM;

Exemplos de parâmetros e execução:

```bash
tool.py list --methods
tool.py list --models
tool.py list

tool.py run --fs-rfg --fs-sigapi --ml-rf --ml-svm --output-prefix resultados --plot-graph-all -d datasets/*.csv 

tool.py run --fs-rfg --fs-sigapi --ml-rf --ml-svm --output-fs-rfg rfg.csv --output-fs-sigapi sigapi.csv --output-ml-rf rf.csv --output-ml-svm svm.csv --plot-graph-all -d motodroid.csv 

tool.py run --fs-all --ml-all --plot-graph-all -d motodroid.csv androcrawl.csv drebin215.csv
```

###### methods
Códigos dos métodos.

###### datasets 
Datasets construídos para o estudo.

