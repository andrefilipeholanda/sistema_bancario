# André Filipe de Holanda Gonçalves

menu = ''' 

    [d] - Depositar
    [s]- Sacar
    [e] - Ver extrato
    [q] - Sair

Informe a opção que deseja ==>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3


while True:
  
  opcao = input(menu)

  if opcao == "d": 
    valor_deposito = float(input("Informe o valor que deseja depositar: "))
    
    if valor_deposito > 0: 
      saldo += valor_deposito 
      extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
      print("Depósito realizado!")

    else: 
      print("Operação falhou! O valor informado é inválido") 

  elif opcao == "s":
    valor_saque = float(input("Informe o valor que deseja sacar: "))

    excedeu_saldo = valor_saque > saldo
    execedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

    if excedeu_saldo:
      print("Não há saldo sufiente em sua conta!")

    elif execedeu_limite: 
      print("O limite para sacar é R$ 500.00")

    elif excedeu_saques: 
      print("Você já realizou os três saques diários. Por favor, aguarde o prazo.")  

    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f"Saque R$ {valor_saque:.2f}\n"
      numero_saques += 1
      print("Saque realizado")  


    else: 
      print("Operação falhou! Você não tem saldo suficiente")

  elif opcao == "e":
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===============================")

  elif opcao == "q":
    print("Obrigado por utilizar nossos serviços")  
    break
  
  else: 
    print("Digite uma opção válida!")