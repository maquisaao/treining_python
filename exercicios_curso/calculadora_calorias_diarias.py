# receber so dados do usuario: Nome, Idade, Peso, Altura, Gênero e Frequencia de atividade fisica
escolha = input('[E]ntrar [S]air \n')
while 'E' in escolha:

    nome = input('Qual seu nome? ')
    idade = input('Qual sua idade? ')
    peso = input('Qual seu peso? ')
    altura = input('Qual sua altura? ')
    genero = input('Qual seu gênero, [H]omem ou [M]ulher? ')
    frequencia_fisica = input(
        'Sua frequencia de atividade fisica é [L]eve, [M]oderada ou [I]ntensa? ')

    # pela atividade fisica, multiplicar pelo valor
    if genero == 'H' and frequencia_fisica == 'L':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    elif genero == 'H' and frequencia_fisica == 'M':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    elif genero == 'H' and frequencia_fisica == 'I':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    elif genero == 'M' and frequencia_fisica == 'L':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    elif genero == 'M' and frequencia_fisica == 'M':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    elif genero == 'M' and frequencia_fisica == 'I':
        consumo_diario = ((0.063*float(peso)+2.896)*239)*1.5
        valor = '%s, seu gasto calorico diario é de %.2f.\n' % (
            nome, consumo_diario)
        print(valor)

    escolha = input('[RE]petir [S]air \n')
