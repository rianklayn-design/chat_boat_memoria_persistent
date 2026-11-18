def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    resposta = input("Digite a resposta: ").strip().lower()

    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta}-{resposta}\n")
    print("bot: obrigado! aprendi algo novo.")


def conversar():
    fala = input("você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split("-")
                if len(dados) == 2:
                    pergunta_salva, resposta_salva = dados
                    if fala == pergunta_salva.strip():
                        print(f"bot: {resposta_salva.strip()}")
                        encontrou = True
                        break

        if not encontrou:
            print("bot: desculpe, nao sei a resposta. use a opçao 2 para me ensinar.")

    except FileNotFoundError:
        print("bot: meu cerebro esta vazio! me ensine algo primeiro.")


def listar_conhecimento():
    base_dados = []
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split("-")
                if len(dados) == 2:
                    # cria tupla (pergunta, resposta) e adiciona na lista
                    base_dados.append((dados[0].strip(), dados[1].strip()))

        # ordena alfabeticamente pela primeira posicao da tupla (pergunta)
        base_dados.sort()

        print("\n--- memoria do pybot (ordenada) ---")
        for item in base_dados:
            print(f"pergunta: {item[0]} -> resposta: {item[1]}")

    except FileNotFoundError:
        print("nenhum dado cadastrado ainda.")


while True:
    print("\n--- MENU PYBOT ---")
    print("1 - Conversar")
    print("2 - Ensinar")
    print("3 - Listar conhecimento")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar()
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")