
# Treinando Python através de projetos

Aqui estão alguns projetos que fiz para desenvolver minha habilidade e entendimento do python e principalmente pra reforçar minha habilidade com a logica de programação. Aqui vou deixar tanto projetos que vejo de exemplo nos materias de cursos como também alguns que achei válidos pra resolver alguns problemas no meu dia a dia.

## Lista dos Projetos: 

[`Adivinha o número`](https://github.com/maquisaao/treining_python/tree/main/what_the_number) : 

Nesse jogo o intuito é adivinhar o número e pode ser feito de duas formas: ou o computador pensa num número e o usuário precisa adivinhar ou o usuário pensa num número e o computador precisa adivinhar. Em ambos os casos vamos usar feedbacks para adivinhar o número, ou seja, a cada palpite será dito se o numero é mais alto, mais baixo ou igual.

[`Pedra-Papel-Tesoura`](https://github.com/maquisaao/treining_python/blob/main/tic_tac_toe) : 

Esse código implementa um jogo da velha (Tic Tac Toe) em Python, permitindo partidas entre jogadores humanos e computadores com diferentes níveis de inteligência. A classe `TicTacToe` gerencia o tabuleiro, verificando movimentos e condições de vitória. A função `play()` coordena o fluxo do jogo, alternando entre jogadores X e O, permitindo que cada um faça suas jogadas. O código suporta diferentes tipos de jogadores, como humanos e computadores, incluindo uma IA mais inteligente que toma decisões estratégicas. Ao final, o vencedor é declarado ou o jogo termina em empate.

[`Teste de velocidade da Internet`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :

Esse código utiliza a biblioteca `speedtest` para medir a velocidade de conexão de internet. Ele realiza três testes e exibe os resultados no console.

1. Download: Mede a velocidade de download em megabits por segundo (Mbps).

2. Upload: Mede a velocidade de upload, também em Mbps.

3. Ping: Mede a latência (tempo de resposta) em milissegundos (ms), que indica a rapidez com que os dados viajam até o servidor e voltam.

[`Solucionar sudoku`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :

Este projeto implementa um resolvedor de Sudoku utilizando a técnica de backtracking em Python. A ideia é preencher os espaços vazios (representados por -1) em um tabuleiro 9x9 seguindo as regras do Sudoku:

- Nenhum número pode se repetir na mesma linha.
- Nenhum número pode se repetir na mesma coluna.
- Nenhum número pode se repetir no mesmo quadrante 3x3.

### Funcionamento do Código
O algoritmo segue os seguintes passos:

1. Encontrar o próximo espaço vazio: Percorre o tabuleiro para identificar a próxima célula vazia, ou seja, um espaço representado por -1.

2. Fazer uma tentativa (guess): O algoritmo tenta preencher esse espaço com um número entre 1 e 9, verificando se a tentativa é válida de acordo com as regras do Sudoku.

3. Validação: O número é considerado válido se:

- Não estiver repetido na linha.
- Não estiver repetido na coluna.
- Não estiver repetido no quadrante 3x3.
4. Recursão e backtracking: Caso o número seja válido, ele é colocado no tabuleiro e o algoritmo tenta resolver o próximo espaço vazio. Se não for possível resolver com o número atual, o algoritmo volta atrás (backtracking) e tenta outro número.

5. Solução: O algoritmo continua até que todos os espaços vazios sejam preenchidos ou até que seja determinado que o tabuleiro é insoluvel.

[`Pesquisar no Google`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :

[`Campo Minado`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :

[`Calculadora de Calorias`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :

[`BudgetApp`](https://github.com/maquisaao/treining_python/blob/main/test_internet) :
