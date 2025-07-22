def menu():
    menu = """
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [lu] Listar usuário
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    => """
    return input(menu)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print("=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado. Crie o usuário antes de criar a conta. @@@")

def listar_contas(contas):
    print("\n============= CONTAS =============")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")
            print("----------------------------------")

def listar_usuarios(usuarios):
    print("\n============= USUÁRIOS =============")
    if not usuarios:
        print("Nenhum usuario cadastrada.")        
    else:
        for usuarios in usuarios:
            print(f"usuario: {usuarios["nome"]}")   
            print("----------------------------------")

def deposito(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, extrato, valor, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato  = deposito(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo , extrato, numero_saques = saque(
                saldo=saldo, 
                extrato=extrato,
                valor=valor, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(AGENCIA, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "q":
            print("Encerrando sistema... 👋")
            break

        else:
            print("Operação inválida, tente novamente.")


main()