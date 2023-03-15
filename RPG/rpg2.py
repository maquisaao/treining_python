from time import sleep

from talks import talks


def cooldown():
    sleep(3)


# menu de inicio
print("MENU: COMEÇAR O JOGO?")
cooldown()
input("MENU: DIGITE S OU N:\nRESPOSTA: ")
cooldown()
perso = input("MENU: Digite o nome do seu avatar:\nRESPOSTA:  ")
cooldown()

# apresentando o jogo.
print(saudacao_tumtum)
cooldown()
print("TUMTUM: Nesse jogo você poderá escolher seu nome e tomar as decisões do seu avatar.")


# receber o nome do personagem

# começando a historia
cooldown()
print("TUMTUM: Muito bem! Agora você já sabe como interagir comigo!")
cooldown()
print("TUMTUM: Falando nisso, esqueci de me apresentar.. meu nome é Tumtum e estou aqui para guiar você em nossa aventura!")
cooldown()
print("TUMTUM: Chega de papo furado, vamos começar!")
cooldown()


# recebendo a primeira escolha do jogador
escolha1 = input(
    "MENU: Você está pronto para começar nossa aventura? (s/n)\nRESPOSTA: ")
cooldown()
# historia para opçao n
if escolha1 == "n":
    print(f"TUMTUM: Como assim não está pronto {perso}?")
    cooldown()
    input("MENU: Vou dar a você uma chance de reconsiderar nossa aventura! Vamos? (s/n)\nRESPOSTA: ")
    cooldown()

# historia para opçao s
else:
    print(f"TUMTUM: Assim que eu gosto, você tem iniciativa {perso}!!!")
    cooldown()

# criando a historia
print("TUMTUM: Estamos no ano de 3055, mas diferente do que você deve estar pensando..")
cooldown()
print("TUMTUM: não vivemos em um futuro tecnológico! Depois de muitas guerras e doenças devastando nossa")
cooldown()
print("TUMTUM: população, a última tragédia foi a explosão de um foguete em nossa atmosfera, trazendo")
cooldown()
print("TUMTUM: quantidades massivas de gases tóxicos aos humanos.")
cooldown()
print("TUMTUM: No momento, pelo que se tem conhecimento, são apenas 14 humanos vivendo no planeta.. as opções")
cooldown()
print("TUMTUM: para salvar a humanidade estão limitadas ao contato e comunicação.")
cooldown()
print("TUMTUM: Agora que já está atualizado da situação atual, vamos começar a nossa aventura por esse mundo")
cooldown()
print("TUMTUM: solitário e cheio de surpresas.")
cooldown()
print("TUMTUM: Você está caminhando pelas ruínas de uma cidade que até então parece estar deserta. Depois de 30")
cooldown()
print("TUMTUM: minutos caminhando, você sente que está quase desidratado, as opções são poucas.")
cooldown()

# condiçoes de escolha da escolha2
print("TUMTUM: Você avista a cerca de 3km o que parece ser um caminhão pipa. Mas ao seu lado direito tem um predio de 10")
cooldown()
print("TUMTUM: andares com o nome de Cruse Building, com uma pintura na parede dizendo: NÃO ENTRE AQUI, PERIGO DE MORTE")
cooldown()
escolha2 = input("MENU: Qual sua decisão? (pipa/predio)\nRESPOSTA: ")

# historia para escolha PIPA
if escolha2 == "pipa":
    cooldown()
    print("TUMTUM: Escolha ousada! Já está cansado e desidratado. Caminhar mais 3km não será fácil. Mas por muita sorte, na")
    cooldown()
    print("TUMTUM: metade do caminho você encontra no chão uma garrafa com um líquido amarelo. A embalagem já está ilegivel")
    cooldown()
    print("TUMTUM: devido ao tempo abandonada. Aparentemente parece suco e não está com cheiro de podre.")
    cooldown()

# historia para escolha PIPA/BEBO
    escolha3 = input(
        "MENU: Você deixa a garrafa ou bebe o que tem nela? (deixo/bebo)\nRESPOSTA: ")
    if escolha3 == "bebo":
        print(
            f"TUMTUM: Parabens {perso},você morreu mais rápido que o esperado! Espero que as outras 13 pessoas não sejam burros como você.")
        cooldown()
        print("GAME OVER")
        cooldown()

# historia para escolha PIPA/DEIXO
    else:
        print(
            "TUMTUM: Sábia escolha! Sem duvida aquilo te mataria! Vamos seguir nossa caminhada...")
        cooldown()
        print("TUMTUM: Quando você soltou a garrafa no chão, percebe um som estranho, como o som de sopro..")
        cooldown()
        print("TUMTUM: Um sopro muito forte, com um tom grave.. ao mesmo tempo sente seu nariz secando e uma dificuldade para respirar..")
        cooldown()
        print("TUMTUM: Quando você levanta a cabeça e olha pra trás, avista uma enorme nuvem de fumaça, rodeada por 5 tornados vindo em sua direção")
        cooldown()
        print("TUMTUM: Ao olhar para frente mais uma vez, você percebe que ainda está longe do Caminhão Pipa.. e pela velocidade da nuvem")
        cooldown()
        print("TUMTUM: você não vai conseguir chegar a tempo.. adeus a possível água! Ou você corre mais rapido que a tempestade ou procura um abrigo rápido")
        cooldown()
        print("TUMTUM: Enquanto corre você procura por opções ao seu redor, e de repente avista um caminhão parado no meio do caminho")
        cooldown()
        print("TUMTUM: Você não sabe se está destrancado, mas percebe que uma das portas do báu traseiro está aberta.")
        cooldown()
        input(f"MENU: O que voce faz {perso}? (abrir porta/entrar no baú)")
        cooldown()

# historia para escolha PREDIO
else:
    print("TUMTUM: Está em um local estranho e perigoso, o aviso não foi o bastante pra você recuar?")
    cooldown()
    print("TUMTUM:  Mesmo com medo você entra no predio. Adando devagar você age como se pudesse haver algo ou alguém dentro do prédio..")
    cooldown()
    print("TUMTUM: Com sentimento de surpresa você avista uma lâmpada acesa.. ainda há eletricidade? Abaixo dessa lâmpada tem um elevador.")
    cooldown()
    print("TUMTUM: A porta está aberta e parece funcional. Todo o resto do térreo está destruído e deserto. O elevador parece um convite.")
    cooldown()
    print("TUMTUM: De repente você escuta um barulho forte e corre na porta para verificar.. uma forte tempestade está prestes a passar!")
    cooldown()
    print("TUMTUM: Mesmo antes de você se decidir, um caminhao é lançado em direção a porta de entrada!! Você tem segundos para decidir")
    cooldown()
    print("TUMTUM: se vai aceitar o convite do elevador ou correr da tempestade!")
cooldown()
input("MENU: Qual sua decisão? (elevador/tempestade)\nRESPOSTA: ")
