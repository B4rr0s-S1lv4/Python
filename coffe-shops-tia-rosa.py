lista_cadastro = []  # Lista global para armazenar os cadastros dos clientes

def main():
    """Função principal para executar o programa."""
    while True:  # Adiciona um loop para exibir o menu repetidamente
        print("Coffee Shops Tia Rosa")
        print("Seja bem vindo")
        print("Escolha uma opção:")
        print("1 - Fazer pedido")
        print("2 - Cardápio")
        print("3 - Cadastrar no clube da tia rosa, membros do clube ganham acesso as promoções.")
        print("4 - Promoções (apenas para membros do clube será necessário o CPF para verificar se é membro no balcão)")
        try:
            escolha = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Por favor, digite um número correspondente à opção desejada.")
            continue  # Volta para o início do loop
        # Chama a função correspondente à escolha do usuário
        funcao = opcoes.get(escolha, opcao_invalida)  # Obtém a função do dicionário, ou opcao_invalida se não encontrada
        funcao()  # Chama a função
        voltar_menu = input("Digite 'm' para voltar ao menu: ")  # Pergunta ao usuário se deseja voltar ao menu
        if voltar_menu.lower() != 'm':  # Verifica se o usuário digitou 'm' (ou 'M')
            print("Opção inválida, digite 'm'")
            break  # Se a entrada não for 'm', sai do loop e o programa termina

def fazer_pedido():
    """Função para processar um pedido."""
    print("Você escolheu fazer um pedido.")
    while True:
        try:
            produto = int(input("Digite o número do produto que deseja pedir: "))
            quantidade = int(input("Digite a quantidade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números para o produto e quantidade.")

    print(f"Confirmação: {quantidade}x Produto {produto}")
    pedido = quantidade * produto
    confirmacao = input("Deseja confirmar o pedido? (s/n): ")
    if confirmacao.lower() == "s":
        print("Pedido confirmado!")
        lista_pedidos = []
        lista_pedidos.append(pedido)
        print(f"Pedido: {pedido}")
    elif confirmacao.lower() == "n":
        print("Pedido cancelado. Lembre-se que o pedido só será aceito se você digitar 's' para confirmar.")
    else:
        print("Opção inválida. Pedido cancelado.")
    print("Obrigado por escolher o Coffee Shops Tia Rosa!")

def ver_cardapio():
    print("Você escolheu ver o cardápio.")
    print("--------------- CARDÁPIO ----------------")
    print("--------------- BEBIDAS -----------------")
    print("1 - Café 5 R$ (café puro)")
    print("2 - Chá 5 R$ (chá gelado)")
    print("3 - Espresso 5 R$ (espresso com leite)")
    print("4 - Cappuccino 5 R$ (cappuccino com leite)")
    print("5 - Água 5 R$ (água mineral)")
    print("6 - Latte 5 R$ (latte com leite)")
    print("--------------- ALIMENTOS -----------------")
    print("7 - Bolo 5 R$ (bolo de cenoura com chocolate)")
    print("8 - Sanduíche 5 R$ (sanduíche natural, pão e presunto)")
    print("9 - Salada de frutas 5 R$ (maça, banana, laranja e uva)")
    print("10 - Pão de queijo 5 R$ (pão de queijo tradicional)")

def cadastrar_clube():
    """Função para cadastrar um cliente no clube."""
    print("Você escolheu cadastrar no clube da tia rosa.")
    print("Para se cadastrar, preencha os dados abaixo:")
    while True:
        nome = input("Nome: ")
        if not nome:
            print("Nome é obrigatório. Por favor, insira um nome.")
            continue
        break

    while True:
        email = input("Email: ")
        if not validar_email(email):
            print("Email inválido. Por favor, insira um email válido.")
            continue
        break

    while True:
        cpf = input("CPF: ")
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")
            continue
        break
    print(f"Cadastro realizado com sucesso!\nNome: {nome}\nEmail: {email}\nCPF: {cpf}")
    # Adiciona o dicionário à lista global `lista_cadastro`
    lista_cadastro.append({"nome": nome, "email": email, "cpf": cpf})

def ver_promocoes():
    """Função para exibir as promoções."""
    cpf_consulta = input("Você escolheu ver as promoções. Para isso, digite seu CPF: ")
    # Verifica se o CPF está na lista de cadastros
    for cliente in lista_cadastro:
        if cliente["cpf"] == cpf_consulta:
            print("Promoções disponíveis para membros do clube:")
            print("1 - 10% de desconto em bebidas.")
            print("2 - Dois cafés grátis na compra de 2 lanches.")
            print("3 - Na terceira vinda ao café, o cliente ganha um café grátis.")
            return
    print("Você não é membro do clube. Para se cadastrar, vá até o balcão e preencha o formulário.")

def opcao_invalida():
    """Função para lidar com opções inválidas."""
    print("Opção inválida. Por favor, escolha uma opção válida.")

def validar_email(email):
    """
    Função para validar o formato do email.
    """
    if not email:
        return False
    if '@' not in email or '.' not in email:
        return False
    partes = email.split('@')
    if len(partes) != 2:
        return False
    usuario, dominio = partes
    if not usuario or not dominio:
        return False
    if '.' not in dominio:
        return False
    partes_dominio = dominio.split('.')
    for parte in partes_dominio:
        if not parte:
            return False
    return True

def validar_cpf(cpf):
    """
    Função para validar o formato do CPF.
    """
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    for i in range(9, 11):
        soma = 0
        for j in range(i):
            soma += int(cpf[j]) * (i + 1 - j)
        resto = soma % 11
        digito = 0 if resto < 2 else 11 - resto
        if digito != int(cpf[i]):
            return False

    return True
# Dicionário que mapeia opções do menu para funções
opcoes = {
    1: fazer_pedido,
    2: ver_cardapio,
    3: cadastrar_clube,
    4: ver_promocoes,
}

if __name__ == "__main__":
    main()
