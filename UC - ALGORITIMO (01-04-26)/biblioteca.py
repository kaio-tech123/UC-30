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

