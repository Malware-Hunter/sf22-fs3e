# líder da FT: Estevão

## Equipe

- Estevão, Sávio, Luiza, Diego, Nicolas

## Tarefas pendentes
- (Sávio) Usar underlines ("\_") nos arquivos de saída dos métodos
    - Verificar os códigos python de cada método

- (Nicolas) Revisar os papers dos métodos e verificar se a nossa implementação condiz com o paper
    - Revisar LinearRegression, JOWMDroid, RFG, SigAPI e SigPID
- (Estevão) `tool.py`: implementar opção que executa métodos de feature selection
- (Estevão) `tool.py`: implementar opção que executa modelos de ML

## Tarefas realizadas
- (Luíza) Fazer validação cruzada 10 fold no `evaluation.py`
    - Atualmente, o mesmo conjunto de amostras é usado no treino e na validação, mas queremos que ele use amostras diferentes no treino. Por isso a validação cruzada 10
    - Lembrando de colocar como parâmetro de linha de comando o valor de k, que representada o número de folds (definido como 10 por padrão)
- (Estevão) `tool.py`: implementar opção que lista métodos e/ou modelos disponíveis
- (Estevão) Implementar a estrutura inicial do `tool.py`
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
