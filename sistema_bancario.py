menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor que irá depositar: ")) 
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação inválida")
            
    elif opcao == "s":
        valor = float(input("Qual o valor deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo Insuficiente")
            
        elif excedeu_limite:
            print("Limite insuficiente")
        
        elif excedeu_saques:
            print("Saques máximo já realizado")
            
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            
        else:
            print("Valor informado inválido")
            
    elif opcao == "e":
        print("\n======= EXTRATO =======")
        print("Não foram realizadas moviemntações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============")
        
    elif opcao == "q":
        break
    
    else:
        print("Seleção incorreta! Selecione novamente o que deseja")