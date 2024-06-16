import os

def generate_markdown(strings: str, title: str) -> list[str]:
    # Obtém o diretório atual
    current_dir: str = os.path.dirname(os.path.abspath(__file__))

    # Define o caminho para a pasta "instances" fora do diretório "src"
    instances_dir: str = os.path.join(current_dir, '..','instances')

    # Verifica se a pasta "instances" existe, caso contrário, cria-a
    if not os.path.exists(instances_dir):
        os.makedirs(instances_dir)

    # Gera o nome do arquivo Markdown baseado no título
    nome_arquivo: str = os.path.join(instances_dir, f"markdown_{title.replace(' ', '_')}.md")

    # Abre o arquivo em modo de escrita
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        # Escreve o conteúdo de strings no arquivo
        arquivo.write(strings)
       
    print(f"Arquivo Markdown gerado em {nome_arquivo}")