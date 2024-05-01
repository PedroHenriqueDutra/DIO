def deposito(saldo,valor):
    return saldo+valor
def extrato(saldo,saq_dia):
    print(f"O saldo atual é : {saldo}\nRestam {saq_dia} saques possíveis hoje")
def saque(saldo,valor):
    if valor>saldo:
        print(f"Valor indicado maior do que o saldo  existente\nSaldo atual{saldo}")
    else:
        return saldo-valor

saldo=0.0
saq_dia=3
while(1):
    operacao=int(input("Selecione a operação que deseja realizar:\n1 - Deposito\n2 - Extrato\n3 - Saque\n0 - Sair\n"))
    if operacao == 1 :
        valor=input("Qual o valor será depositado: ")
        valor=valor.replace(",",".")
        valor=float(valor)
        saldo=deposito(saldo,valor)
    elif operacao == 2 :
        extrato(saldo, saq_dia)
    elif operacao == 3:
        menu_ini=0
        while( menu_ini!=1):
            valor = float(input("Qual o valor será sacado: ").replace(",","."))
            if valor > 0.0:
                saldo=saque(saldo,valor)
                saq_dia-=1
                menu_ini=1
            else:
                menu_ini=input("O valor a ser sacado deve ser MAIOR do que 0\nPara tentar realizar o saque novamente digite 0 e para "
                      "voltar ao menu inicial digite 1")
    elif operacao == 0 :
        break
    else:
        print("Operação informada não disponível")
