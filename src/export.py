import os

def generateMarkdown(strings) -> None:
    # Verifica se a pasta "instances" existe, caso contrário, cria-a
    if not os.path.exists("instances"):
        os.makedirs("instances")

    # Gera o nome do arquivo Markdown baseado na quantidade de strings
    nome_arquivo: str = f"instances/markdown_{len(strings)}.md"

    # Abre o arquivo em modo de escrita
    with open(nome_arquivo, "w") as arquivo:
        # Escreve as strings no arquivo Markdown
        for string in strings:
            arquivo.write(f"- {string}\n")

    print(f"Arquivo Markdown gerado em {nome_arquivo}")