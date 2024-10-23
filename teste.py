import random
nome = []
dif = []
acertos = []
rodada = []
cad = []
user = []
senha = []

def trataerron():
    while True:
        usuario = input("Você acha que é qual número? ")
        try:
            usuario = int(usuario)
            return usuario
            break
        except:
            print("Tente novamente, dado inválido.")

def dificuldade():
    while True:
        x = input("Digite 'sair' para encerrar ou escolha entre fácil, médio e difícil. Digite F para fácil, M para médio e D para difícil: ")
        x = x.upper()
        if x == "F":
            return "Nível fácil, 10"
            break
        elif x == "M":
            return "Nível médio, 5"
            break
        elif x == "D":
            return "Nível difícil, 3"
            break
        elif x == "SAIR":
            return "SAIR"
        else:
            print("Dificuldade inválida.")

def jogo():
    while True:
        print("Jogo da adivinhação")
        y = dificuldade()
        if y == "SAIR":
            break
        else:
            num = random.randint(1,100)
            z = y.split(", ")
            vartxt= z[0]
            dif.append(vartxt)
            varnum=z[1]
            varnum = int(varnum)
            acertos.append("Jogo perdido")
            for i in range(varnum):
                print("Rodada",i+1,"de",varnum)
                usuario = int(trataerron())
                if usuario == num:
                    print("Parabéns, você acertou! O número sorteado é: ",num)
                    acertos.pop()
                    acertos.append("Jogo ganho")
                    break
                else:
                    if num < usuario:
                        print("O número é menor que o digitado!")
                    elif num > usuario:
                        print("O número é maior que o digitado!")
            print("O número era:", num)
            print("\n")
            rodada.append("jogo")
    nr= len(rodada)
    for i in range(nr):
        # arrumar print de nome e rodadas
        print("\n")
        print(user[i])
        # corrigir
        print(dif[i])
        print(acertos[i])

def cadastro():
    while True:
        user2 = input("Digite seu nome de usuário: ")
        if user2 in user:
            print("Username em uso, tente outro: ")
    # (tratativa de erro nome do usuario)
        else:
            user.append(user2)
            break
    while True:
        senha2 = input("Digite uma senha: ")
    # // (Fazer try-except para permitir apenas senhas com letra maiúscula e caracteres especiais)
        senha.append(senha2)
        break

while True:
    var1 = input("Digite seu usuário ou 'c' para cadastrar um novo usuário: ")
    if var1 == 'c':
        cadastro()
    elif var1 in user:
        index = user.index(var1)
        while True:
            senhaentrada = input("Digite a senha: ")
            if senhaentrada == senha[index]:
                print("Login bem-sucedido!")
                jogo()
                break
            else:
                print("A senha não está correta, tente novamente.")
    else:
        print("Dados inválidos, tente novamente.")