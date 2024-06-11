def contar_caracteres(texto):
    return len(texto.replace(" ", ""))

def contar_palavras(texto):
    return len(texto.split())

while True: 
    opcao = input("Escolher opção: \n1. Contar caracteres\n2. Contar palavras\n3. Sair\n Digite um número da opção desejada: ")
    
    if opcao == '1':
        texto = input("Insira um texto: ")
        print(f"Número de caracteres: {contar_caracteres(texto)}")
    elif opcao == '2':
        texto = input("Insira um texto: ")
        print(f"Número de palavras: {contar_palavras(texto)}")
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")