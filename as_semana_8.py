'''
Nome: Tiago Camargo Maciel dos Santos
Curso: Análise e Desenvolvimento de Sistemas
'''

import json

def valida_turma(codigo_professor: int, codigo_disciplina: int, operacao: str = "w") -> bool:
    """
    Verifica se a combinação de professor e disciplina é válida para uma turma.

    :param codigo_professor: Código do professor.
    :param codigo_disciplina: Código da disciplina.
    :param operacao: Operação a ser realizada: "w" (escrita - inclusão/atualização) e "l" (leitura).
    :return: True, se a combinação for válida; e False, se for inválida.
    :rtype: bool
    """
    if not (codigo_professor and codigo_disciplina):
        return False
    
    arquivo = "turmas"
    lista = ler_arquivo_json(arquivo)

    if operacao == "w":
        arquivo_professor = ler_arquivo_json("professores")
        arquivo_disciplina = ler_arquivo_json("disciplinas")

        if not (arquivo_professor and arquivo_disciplina):
            return False

        professor_existe = False
        for linha_p in arquivo_professor:
            if linha_p["codigo"] == codigo_professor:
                professor_existe = True
                break
        
        disciplina_existe = False
        for linha_d in arquivo_disciplina:
            if linha_d["codigo"] == codigo_disciplina:
                disciplina_existe = True
                break

        if not (professor_existe and disciplina_existe):
            return False
        elif not lista:
            return True
        else:
            flag_valido = True
            for linha in lista:
                if linha["codigo_professor"] == codigo_professor and linha["codigo_disciplina"] == codigo_disciplina:
                    flag_valido = False
                    break
            return flag_valido
    elif operacao == "l":
        if not lista:
            return False
        else:
            flag_valido = False
            for linha in lista:
                if linha["codigo_professor"] == codigo_professor and linha["codigo_disciplina"] == codigo_disciplina:
                    flag_valido = True
                    break
            return flag_valido
    else:
        return False


def valida_matricula(codigo_turma: int, codigo_estudante: int, operacao: str = "w") -> bool:
    """
    Verifica se a combinação de turma e estudante é válida para uma matrícula.

    :param codigo_turma: Código da turma.
    :param codigo_estudante: Código do estudante.
    :param operacao: Operação a ser realizada: "w" (escrita - inclusão/atualização) e "l" (leitura).
    :return: True, se a combinação for válida; e False, se for inválida.
    :rtype: bool
    """
    if not (codigo_turma and codigo_estudante):
        return False
    
    arquivo = "matrículas"
    lista = ler_arquivo_json(arquivo)
    
    if operacao == "w":
        arquivo_turma = ler_arquivo_json("turmas")
        arquivo_estudante = ler_arquivo_json("estudantes")

        if not (arquivo_turma and arquivo_estudante):
            return False

        turma_existe = False
        for linha_t in arquivo_turma:
            if linha_t["codigo"] == codigo_turma:
                turma_existe = True
                break
        
        estudante_existe = False
        for linha_e in arquivo_estudante:
            if linha_e["codigo"] == codigo_estudante:
                estudante_existe = True
                break

        if not (turma_existe and estudante_existe):
            return False
        elif not lista:
            return True
        flag_valido = True
        for linha in lista:
            if linha["codigo_turma"] == codigo_turma and linha["codigo_estudante"] == codigo_estudante:
                flag_valido = False
                break
        return flag_valido
    elif operacao == "l":
        if not lista:
            return False
        flag_valido = False
        for linha in lista:
            if linha["codigo_turma"] == codigo_turma and linha["codigo_estudante"] == codigo_estudante:
                flag_valido = True
                break
        return flag_valido
    else:
        return False


def escrever_arquivo_json(arquivo: str, dados: list) -> None:
    """
    Escreve em arquivo JSON.

    :param arquivo: Arquivo que contém os dados estruturados em lista de dicionários.
    :param dados: Dados a serem escritos no arquivo em questão.
    :return: None
    :rtype: None
    """
    with open(arquivo + ".json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)
    return None


def ler_arquivo_json(arquivo: str) -> list:
    """
    Lê arquivo JSON.

    :param arquivo: Arquivo que contém os dados estruturados em lista de dicionários.
    :return: Lista de dicionários contendo os dados presentes no arquivo em questão.
    :rtype: list
    """
    try:
        with open(arquivo + ".json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
    except:
        return []


def menu_principal() -> None:
    """
    Exibe, no console, o menu principal da aplicação.

    :return: None
    :rtype: None
    """
    print("----- MENU PRINCIPAL -----")
    print()
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")
    print()
    return None


def menu_operacoes(menu: str = "N/A") -> None:
    """
    Exibe, no console, o menu de operações da aplicação.

    :param menu: Opção, em formato de string, a partir do menu principal.
    :return: None
    :rtype: None
    """
    menu = menu.upper()
    if menu == "N/A":
        print("***** EM DESENVOLVIMENTO *****")
    elif menu not in ("ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"):
        print("Operação inválida.")
    else:
        print(f"***** [{menu}] MENU DE OPERAÇÕES *****")
        print()
        print("(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Voltar ao menu principal.")
    print()
    return None


def inclusao(arquivo: str) -> bool:
    """
    Inclui, no arquivo da opção em questão, um novo elemento.

    :param arquivo: Arquivo que contém os elementos da opção.
    :return: True, caso tenha sido possível incluir elemento, e False, caso não.
    :rtype: bool
    """
    print("===== INCLUSÃO =====")
    print()

    lista = ler_arquivo_json(arquivo)
    linha = {}

    # Inclusão de um nome de input do usuário à lista do menu
    if arquivo == "matrículas":
        pass
    elif not lista:
        codigo = 1
    else:
        codigo = lista[len(lista) - 1]["codigo"] + 1
    
    if arquivo == "estudantes":
        while True:
            nome = input("Nome do estudante: ").strip()
            cpf = input("CPF do estudante: ").strip()
            if nome and cpf:
                break
            else:
                print("\nFavor preencher os dados.\n")
        linha = {"codigo": codigo,"nome": nome, "cpf": cpf}
    elif arquivo == "professores":
        while True:
            nome = input("Nome do professor: ").strip()
            cpf = input("CPF do professor: ").strip()
            if nome and cpf:
                break
            else:
                print("\nFavor preencher os dados.\n")
        linha = {"codigo": codigo, "nome": nome, "cpf": cpf}
    elif arquivo == "disciplinas":
        while True:
            nome = input("Nome da disciplina: ").strip()
            if nome:
                break
            else:
                print("\nFavor preencher os dados.\n")
        linha = {"codigo": codigo, "nome": nome}
    elif arquivo == "turmas":
        while True:
            try:
                codigo_professor = int(input("Código do professor: "))
                codigo_disciplina = int(input("Código da disciplina: "))
            except:
                print("\nFavor preencher os dados.\n")
                continue
            if valida_turma(codigo_professor, codigo_disciplina):
                break
            else:
                print()
                print("Não foi possível cadastrar.")
                input("Pressione ENTER para continuar.")
                print()
                return False
        linha = {"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}
    elif arquivo == "matrículas":
        while True:
            try:
                codigo_turma = int(input("Código da turma: "))
                codigo_estudante = int(input("Código do estudante: "))
            except:
                print("\nFavor preencher os dados.\n")
                continue
            if valida_matricula(codigo_turma, codigo_estudante):
                break
            else:
                print()
                print("Não foi possível cadastrar.")
                input("Pressione ENTER para continuar.")
                print()
                return False
        linha = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
    else:
        return False
    lista.append(linha)
    escrever_arquivo_json(arquivo, lista)
    return True


def listagem(arquivo: str) -> bool:
    """
    Lista no console os elementos do arquivo em questão.

    :param arquivo: Arquivo que contém os elementos da opção.
    :return: True, caso tenha sido possível listar elementos, e False, caso não.
    :rtype: bool
    """
    print("===== LISTAGEM =====")
    print()

    lista = ler_arquivo_json(arquivo)

    if not lista:
        print(f"Não há {arquivo} cadastrados.")
        input("Pressione ENTER para continuar.")
        print()
        return False
    elif arquivo == "estudantes":
        for linha in lista:
            print(linha["codigo"], "-", "Nome:", linha["nome"], "- CPF:", linha["cpf"])
    elif arquivo == "professores":
        for linha in lista:
            print(linha["codigo"], "-", "Nome:", linha["nome"], "- CPF:", linha["cpf"])
    elif arquivo == "disciplinas":
        for linha in lista:
            print(linha["codigo"], "-", "Nome:", linha["nome"])
    elif arquivo == "turmas":
        for linha in lista:
            print(linha["codigo"], "-", "Código do professor:", linha["codigo_professor"], "- Código da disciplina:", linha["codigo_disciplina"])
    elif arquivo == "matrículas":
        for linha in lista:
            print("Código da turma:", linha["codigo_turma"], "- Código do estudante:", linha["codigo_estudante"])
    else:
        return False
    return True


def atualizacao(arquivo: str) -> bool:
    """
    Atualiza um elemento do arquivo em questão.

    :param arquivo: Arquivo que contém os elementos da opção.
    :return: True, caso tenha sido possível atualizar o elemento, e False, caso não.
    :rtype: bool
    """
    print("===== ATUALIZAÇÃO =====")
    print()

    lista = ler_arquivo_json(arquivo)

    if not lista:
        print(f"Não há {arquivo} cadastrados.")
        input("Pressione ENTER para continuar.")
        print()
        return False
    
    if arquivo == "professores":
        opcao_individual = "professor"
    else:
        opcao_individual = arquivo[:-1]

    if arquivo == "matrículas":
        try:
            codigo_turma = int(input("Código da turma: "))
            codigo_estudante = int(input("Código do estudante: "))
        except ValueError:
            print("Código(s) não existe(m).")
            input("Pressione ENTER para continuar.")
            print()
            return False
        
        if not valida_matricula(codigo_turma, codigo_estudante, "l"):
            print("Combinação de turma e estudante não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False
    else:
        try:
            codigo = int(input(f"Código do {opcao_individual}: "))
        except ValueError:
            print("Código não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False

        codigo_existe = False
        for linha in lista:
            if linha["codigo"] == codigo:
                codigo_existe = True
        if not codigo_existe:
            print("Código não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False

        try:
            novo_codigo = int(input(f"Código atualizado do {opcao_individual}: "))
        except ValueError:
            print("Código inválido: precisa ser número inteiro.")
            input("Pressione ENTER para continuar.")
            print()
            return False

        novo_codigo_valido = True

        for linha in lista:
            if linha["codigo"] == novo_codigo and codigo != novo_codigo:
                novo_codigo_valido = False
                break
        if not novo_codigo_valido:
            print(f"Código inválido: já está cadastrado para outro {opcao_individual}.")
            input("Pressione ENTER para continuar.")
            print()
            return False


    if arquivo == "estudantes":
        while True:
            nome = input("Nome atualizado do estudante: ")
            cpf = input("CPF atualizado do estudante: ")
            if nome and cpf:
                break
            else:
                print("\nFavor preencher os dados.\n")
        for linha in lista:
            if linha["codigo"] == codigo:
                i = lista.index(linha)
                lista[i]["codigo"] = novo_codigo
                lista[i]["nome"] = nome
                lista[i]["cpf"] = cpf
                print()
                print(f"Estudante {codigo} atualizado com sucesso.")
                print(f"Novo código: {novo_codigo} - Novo nome: {nome} - Novo CPF: {cpf}")
                break
    elif arquivo == "professores":
        while True:
            nome = input("Nome atualizado do professor: ")
            cpf = input("CPF atualizado do professor: ")
            if nome and cpf:
                break
            else:
                print("\nFavor preencher os dados.\n")
        for linha in lista:
            if linha["codigo"] == codigo:
                i = lista.index(linha)
                lista[i]["codigo"] = novo_codigo
                lista[i]["nome"] = nome
                lista[i]["cpf"] = cpf
                print()
                print(f"Professor {codigo} atualizado com sucesso.")
                print(f"Novo código: {novo_codigo} - Novo nome: {nome} - Novo CPF: {cpf}")
                break
    elif arquivo == "disciplinas":
        while True:
            nome = input("Nome atualizado da disciplina: ")
            if nome:
                break
            else:
                print("\nFavor preencher os dados.\n")
        for linha in lista:
            if linha["codigo"] == codigo:
                i = lista.index(linha)
                lista[i]["codigo"] = novo_codigo
                lista[i]["nome"] = nome
                print()
                print(f"Disciplina {codigo} atualizada com sucesso.")
                print(f"Novo código: {novo_codigo} - Novo nome: {nome}")
                break
    elif arquivo == "turmas":
        while True:
            try:
                codigo_professor = int(input("Código atualizado do professor: "))
                codigo_disciplina = int(input("Código atualizado da disciplina: "))
            except:
                print("\nFavor preencher os dados corretamente. Tente outro professor/disciplina.\n")
                continue
            if valida_turma(codigo_professor, codigo_disciplina, "w"):
                break
            else:
                print()
                print("Não foi possível cadastrar. Tente outra professor/disciplina.")
                input("Pressione ENTER para continuar.")
                print()
                return False
        for linha in lista:
            if linha["codigo"] == codigo:
                i = lista.index(linha)
                lista[i]["codigo"] = novo_codigo
                lista[i]["codigo_professor"] = codigo_professor
                lista[i]["codigo_disciplina"] = codigo_disciplina
                print()
                print(f"Turma {codigo} atualizada com sucesso.")
                print(f"Novo código da turma: {novo_codigo} - Novo código do professor: {codigo_professor} - Novo código da disciplina: {codigo_disciplina}")
                break
    elif arquivo == "matrículas":
        while True:
            try:
                codigo_turma_novo = int(input("Código atualizado da turma: "))
                codigo_estudante_novo = int(input("Código atualizado do estudante: "))
            except:
                print("\nFavor preencher os dados corretamente. Tente outra turma/estudante.\n")
                continue
            if valida_matricula(codigo_turma_novo, codigo_estudante_novo, "w"):
                break
            else:
                print()
                print("Não foi possível cadastrar. Tente outra turma/estudante.")
                input("Pressione ENTER para continuar.")
                print()
                return False
        for linha in lista:
            if linha["codigo_turma"] == codigo_turma and linha["codigo_estudante"] == codigo_estudante:
                i = lista.index(linha)
                lista[i]["codigo_turma"] = codigo_turma_novo
                lista[i]["codigo_estudante"] = codigo_estudante_novo
                print()
                print(f"Matrícula do estudante {codigo_estudante} na turma {codigo_turma} atualizada com sucesso.")
                print(f"Novo código da turma: {codigo_turma_novo} - Novo código do estudante: {codigo_estudante_novo}")
                break
    else:
        return False

    escrever_arquivo_json(arquivo, lista)
    return True


def exclusao(arquivo: str) -> bool:
    """
    Exclui um elemento do arquivo em questão.

    :param arquivo: Arquivo que contém os elementos da opção.
    :return: True, caso tenha sido possível excluir o elemento, e False, caso não.
    :rtype: bool
    """
    print("===== EXCLUSÃO =====")
    print()

    lista = ler_arquivo_json(arquivo)

    if not lista:
        print(f"Não há {arquivo} cadastrados.")
        input("Pressione ENTER para continuar.")
        print()
        return False
    
    if arquivo == "professores":
        opcao_individual = "professor"
    else:
        opcao_individual = arquivo[:-1]

    if arquivo == "matrículas":
        try:
            codigo_turma = int(input("Código da turma: "))
            codigo_estudante = int(input("Código do estudante: "))
        except ValueError:
            print("Código(s) não existe(m).")
            input("Pressione ENTER para continuar.")
            print()
            return False
        
        combinacao_existe = False
        for linha in lista:
            if linha["codigo_turma"] == codigo_turma and linha["codigo_estudante"] == codigo_estudante:
                lista.remove(linha)
                combinacao_existe = True
                print()
                print(f"{opcao_individual.capitalize()} do estudante {codigo_estudante} na turma {codigo_turma} excluída com sucesso.")
                break
        if not combinacao_existe:
            print("Combinação de turma e estudante não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False
    else:
        try:
            codigo = int(input(f"Código do {opcao_individual}: "))
        except ValueError:
            print("Código não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False

        codigo_existe = False
        for linha in lista:
            if linha["codigo"] == codigo:
                lista.remove(linha)
                codigo_existe = True
                print()
                print(f"{opcao_individual.capitalize()} {codigo} excluído com sucesso.")
                break
        if not codigo_existe:
            print("Código não existe.")
            input("Pressione ENTER para continuar.")
            print()
            return False
    
    escrever_arquivo_json(arquivo, lista)
    return True


running_menu = True
running_operations = True

# Criação do loop inicial do Menu
while running_menu:

    menu_principal()

    # Tentativa de converter o input do usuário em número inteiro. Se falhar, trata a exceção.
    try:
        operacao = int(input("Informe a operação desejada: "))
        print("\n")
    except ValueError:
        print("\n")
        print("Operação inválida.\n")
        continue

    # Caso a opção seja de saída
    if operacao == 9:
        break

    # Entrar no loop da parte de Operações. Se for escolhida uma operação ainda não suportada, volta ao loop do Menu Principal. Se for suportada, segue a operação.
    while running_operations:
        if operacao == 1:
            opcao_principal = "estudantes"
        elif operacao == 2:
            opcao_principal = "professores"
        elif operacao == 3:
            opcao_principal = "disciplinas"
        elif operacao == 4:
            opcao_principal = "turmas"
        elif operacao == 5:
            opcao_principal = "matrículas"
        else:
            menu_operacoes(menu="Inválido")
            break

        menu_operacoes(menu=opcao_principal)
        
        # Tentativa de converter o input do usuário em número inteiro. Se falhar, trata a exceção.
        try:
            acao = int(input("Informe a ação desejada: "))
            print("\n")
        except ValueError:
            print("\n")
            print("Ação inválida.\n")
            continue
        

        # Realização das ações para os menus suportados. Atualmente, só é suportada a operação "Estudantes"
        if acao == 1:
            # Inclusão dos nomes e CPF do estudante à lista de dicionários
            if not inclusao(opcao_principal):
                continue
        elif acao == 2:
            # Listagem dos nomes já cadastrados na lista "estudantes". Se não houver nenhum nome cadastrado, apresentar novamente o Menu de Operações
            if not listagem(opcao_principal):
                continue
        elif acao == 3:
            if not atualizacao(opcao_principal):
                continue
        elif acao == 4:
            if not exclusao(opcao_principal):
                continue
        elif acao == 9:
            break
        else:
            print("Ação inválida.\n")
            continue
        
        input("Pressione ENTER para continuar.")

        print()

print("Finalizando aplicação...")