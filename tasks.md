# líder da FT: Estevão

## Equipe

- Estevão, Sávio, Luiza, Diego

## Tarefas pendentes
- Definir a interface de linha de comando (CLI) do `moto_suite`:
    - Definir o comportamento padrão da ferramenta, isto é, o que ela faz quando executada apenas com argumentos obrigatórios (se houver algum)
    - Definir os parâmetros obrigatórios
    - Definir os parâmetros opcionais
- (Luiza e Sávio) Refatorar `executa_modelos_RFeSVM.py` para rodar opcionalmente os dois modelos SVM e RF
    - Atualmente, o código executa ou o SVM ou o RF, mas é necessário fazer com que ele seja capaz de rodar os dois e não apenas um.
- (Estevão) Refatorar demais scripts `roda_<metodo>.sh` conforme o `roda_sigapi.sh` para receber datasets por linha de comando.

## Tarefas realizadas

- Decidir como cada método de seleção será invocado
    - Vamos usar os _shell scripts_ `roda_<metodo>.sh`? Resposta: sim, pois eles também instalam dependências das ferramentas
- planejar as primeiras atividades;
- definir o time de trabalho;
