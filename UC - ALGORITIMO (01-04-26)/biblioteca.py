catalogo = {}

emprestimosAtivos = {}

historico = []

def adicionarLivro (codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarLivro("L001", "Codigo Limpo", "Robert Martin", 2)

def empresta_livro(codigo, nome_aluno):
    if codigo not in catalogo:
        print(f"Erro: Livro com código {codigo} não encontrado!")
        return False
    
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo]['titulo']}' não está disponível!")
        return False
    
    if codigo in emprestimosAtivos and nome_aluno in emprestimosAtivos[codigo]:
        print(f"Erro: {nome_aluno} já pegou este livro!")
        return False
    
    if codigo not in emprestimosAtivos:
        emprestimosAtivos[codigo] = []

    emprestimosAtivos[codigo].append(nome_aluno)

    catalogo[codigo]["quantidade"] -= 1

    historico.append({
        "tipo": "emprestimo",
        "codigo": codigo,
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print(f"{nome_aluno} pegou '{catalogo[codigo]['titulo']}' com sucesso!")
    return True

def devolve_livro(codigo, nome_aluno):
    if codigo not in emprestimosAtivos or nome_aluno not in emprestimosAtivos[codigo]:
        print(f"Erro: {nome_aluno} não pegou este livro!")
        return False
    
    emprestimosAtivos[codigo].remove(nome_aluno)

    catalogo[codigo]["quantidade"] += 1

    historico.append({
        "tipo": "devolução",
        "codigo": codigo,
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print(f"{nome_aluno} devolveu '{catalogo[codigo]}' com sucesso!")
    return True

def conta_livros_alunos(nome_aluno):

    contador = 0

    for codigo, alunos in emprestimosAtivos.itens():
        
        if nome_aluno in alunos:
            contador += 1

    return contador

def lista_emprestimo():
    print("\n" + "="*60)
    print("LIVROS EMPRESTADOS NO MOMENTO")
    print("="*60)
    
    if not emprestimosAtivos:
        print("nenhum livro emprestado.")
        return
    
    for codigo, alunos in emprestimosAtivos.itens():
        titulo = catalogo [codigo] ["titulo"]
        print(f"\n {titulo} ({codigo})")

        for aluno in alunos:
            print(f"Emprestimo para: {aluno}")


            # PASSO 1: Adiciona alguns livros ao catálogo
    print("\n--- Adicionando livros ao catálogo ---")
    adicionarLivro("L001", "Clean Code", "Robert Martin", 2)
    adicionarLivro("L002", "Python Fluente", "Luciano Ramalho", 1)
    adicionarLivro("L003", "Algoritmos", "Thomas Cormen", 3)
    
    # PASSO 2: Alunos pegam livros
    print("\n--- Alunos pegando livros ---")
    empresta_livro("L001", "Ana")
    empresta_livro("L001", "Bruno")
    empresta_livro("L002", "Ana")
    empresta_livro("L003", "Carlos")
    
    # PASSO 3: Tenta emprestar novamente (deve falhar)
    print("\n--- Tentando emprestar novamente ---")
    empresta_livro("L001", "Ana")  # Erro: Ana já pegou este livro
    empresta_livro("L002", "Ana")  # Erro: Ana já pegou 2 livros
    
    # PASSO 4: Lista empréstimos ativos
    print("\n--- Listando empréstimos ativos ---")
    lista_emprestimo()
    
    # PASSO 5: Devolve um livro
    print("\n--- Devolvendo um livro ---")
    devolve_livro("L001", "Ana")
    
  # PASSO 6: Lista empréstimos novamente
    print("\n--- Listando empréstimos após devolução ---")
    lista_emprestimo()
    
    print("\n" + "="*60)
    print("Teste finalizado!")
    print("="*60 + "\n")
