# líder da FT: Estevão

**CONVENÇÕES IMPORTANTES**: 

- Sempre que possível, criar tarefas atômicas (independente e pequena, significando que ela se refere a uma única coisa) e possíveis de serem resolvidas em até um dia;
- Mensagens de commit devem ser escritas em Português.

## Equipe

- Estevão, Sávio, Luiza, Diego, Nicolas

## Tarefas pendentes
- (Nicolas) Revisar os papers dos métodos e verificar se a nossa implementação condiz com o paper
    - Revisar LinearRegression, JOWMDroid, RFG, SigAPI e SigPID
- (Estevão) `fs3e.py`: Adicionar opção `--output-prefix`
- (Estevão) `fs3e.py`: Gerar gráfico dos resultados da avaliação
- (Estevão) descrever dependências do `fs3e.py`
## Tarefas realizadas
- (Estevão) `fs3e.py`: implementar opção que executa modelos de ML
- (Estevão) `fs3e.py`: rodar métodos de seleção em paralelo
- (Estevão) RFG: Automatizar escolha do melhor dataset de features selecionadas
- (Estevão) mover os shells scripts `roda_<metodo>.sh` para o diretório respectivo de cada método
- (Estevão) Corrigir nomes dos arquivos de saída nos métodos
    - O objetivo é fazer com que o dataset de features selecionadas seja exportado com o nome passado como parâmetro, ao passo que outros arquivos de saída tenham o nome sufixado com alguma coisa para diferenciar
- (Estevão) `fs3e.py`: implementar opção que executa métodos de feature selection usando os shell scripts
- (Estevão) `fs3e.py`: fazer parsing das opções do comando run
- (Luíza) Fazer validação cruzada 10 fold no `evaluation.py`
    - Atualmente, o mesmo conjunto de amostras é usado no treino e na validação, mas queremos que ele use amostras diferentes no treino. Por isso a validação cruzada 10
    - Lembrando de colocar como parâmetro de linha de comando o valor de k, que representada o número de folds (definido como 10 por padrão)
    - (Estevão) revisão realizada
- (Estevão) `fs3e.py`: implementar opção que lista métodos e/ou modelos disponíveis
- (Estevão) Implementar a estrutura inicial do `fs3e.py`
- (Estevão) Usar "_" nos arquivos de saída dos scripts `roda_<método>.sh`
- (Estevão) Usar a mesma interface do utils.py no `evaluation.py`
    - Queremos que o `evaluation.py` use o parser e a função `get_X_y(...)` do utils.py. Isso é importante para mantermos o padrão dos métodos de seleção também no script de avaliação de modelos.
- (Estevão) Atualizar dependências do RFG
    -  Remover dependências não utilizadas (Java, LogitBoost e etc), manter somente o Random Forest
- (Luiza) Refatorar `executa_modelos_RFeSVM.py` para rodar opcionalmente os dois modelos SVM e RF
    - Atualmente, o código executa ou o SVM ou o RF, mas é necessário fazer com que ele seja capaz de rodar os dois e não apenas um.
- (Estevão) Refatorar demais scripts `roda_<metodo>.sh` conforme o `roda_sigapi.sh` para receber datasets por linha de comando.
- Decidir como cada método de seleção será invocado
    - Vamos usar os _shell scripts_ `roda_<metodo>.sh`? Resposta: sim, pois eles também instalam dependências das ferramentas
- planejar as primeiras atividades;
- definir o time de trabalho;
- (Sávio) Usar underlines ("\_") nos arquivos de saída dos métodos
    - Verificar os códigos python de cada método
- (Sávio) `LinearRegression.py`: incluir a coluna de classe do dataset no dataset exportado
    - Atualmente, o código gera um dataset que contém apenas as features selecionadas, mas é preciso também ter a classe deles.
