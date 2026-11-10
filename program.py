##43. Fazer um algoritmo que leia dois valores correspondentes a anos e mostre quantos anos nao bissextos existem entre eles. (A diferenca entre os anos nao pode ser maior que 1000 caso seja, deve ser novamente solicitado.)

def contar_anos_nao_bisexual(primeiro_ano: int, segundo_ano: int):
    if primeiro_ano > segundo_ano:
        primeiro_ano, segundo_ano = segundo_ano, primeiro_ano

    if (segundo_ano - primeiro_ano) > 1000:
        print("A diferença entre os anos não pode ser maior que 1000. Por favor, insira novamente.")
        return None

    anos_nao_bisexual = 0
    for ano in range(primeiro_ano, segundo_ano + 1):
        if not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            anos_nao_bisexual += 1

    return anos_nao_bisexual

def main():
    while True:
        primeiro_ano = int(input("Digite o primeiro ano: "))
        segundo_ano = int(input("Digite o segundo ano: "))

        resultado = contar_anos_nao_bisexual(primeiro_ano, segundo_ano)
        if resultado != None:
            print(f"Quantidade de anos não bissextos entre {primeiro_ano} e {segundo_ano}: {resultado}")
            break

if __name__ == "__main__":
    main()
