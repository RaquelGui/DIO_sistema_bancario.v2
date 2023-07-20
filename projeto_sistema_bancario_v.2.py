import textwrap


def menu ():
    menu = """\n

    BEM VINDO AO BANCO XPTO
O que posso fazer por você hoje?
=================================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo Usuário
[5]\tNova Conta
[6]\tListar Contas
[7]\tSair
==> """
    return (input(textwrap.dedent(menu)))
  
def depositar (saldo, valor, extrato, /):    #positional only

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print ("Depósito realizado com sucesso!")    
    
    else:
        print ("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):    #keyword only
    LIMITE_SAQUES = 3
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    

    if excedeu_saldo:
        print ("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print ("Operação falhou! Limite de saque excedido.")

    elif excedeu_saques:
        print ("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print ("Operação realizada com sucesso.")

    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):    #positional e keyword
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuarios):     #lista (nome, nascimento, cpf, endereço)
    cpf = (input ("Informe o CPF (somente números): "))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print ("Operação falhou! CPF já cadastrado.")
        return
    
    nome = input ("Informe nome completo: ")
    nascimento = input ("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input ("Informe o endereço completo (logradouro, número, bairro, cidade/estado): ")

    usuarios.append({"nome":nome, 
                     "nascimento":nascimento,
                     "cpf":cpf,
                     "endereco":endereco
                     })
    
    print ("Usuário cadastrado com sucesso!")

def verificar_cpf (cpf):    #Verificações do CPF   
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False   
    print("CPF Inválido. Por favor digite um CPF válido.")

     # Verifica se o CPF contém apenas números
    if not cpf.isdigit():
        return False
    print("CPF Inválido. Por favor digite um CPF válido.")
    # Verifica se o CPF já foi cadastrado para algum usuário
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta (agencia, numero_da_conta, usuarios):    #lista
    cpf = (input ("Infome o CPF (somente números): ")) 
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario}

    else:
        print ("Usuário não encontrado. Processo de criação de conta encerrado!")
    
def listar_contas (contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_da_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:
        opcao = menu ()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))  

            saldo, extrato = sacar (
                saldo = saldo, 
                valor = valor,
                extrato = extrato, 
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)   
            
        elif opcao == "4": 
            novo_usuario (usuarios)
    
        elif opcao == "5": 
            numero_da_conta = len(contas)+1
            conta = nova_conta(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)         
    
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break
            print ("Obrigado por usar nossos serviços. Tenha um bom dia!")
        
        else:
            print ("Operação inválida!Tente novamente.")

main ()