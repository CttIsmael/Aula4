def seu_imc(m,h):
    imc = m/(h**2)
    return imc
def main():
    massa = float(input("Informe sua massa corporal em kg: "))
    altura = float(input("Informe sua altura: "))
        
    indice = seu_imc(massa, altura)
    print(int(indice))

    if indice < 18.5:
        print(f'Abaixo do peso')
    elif indice < 25:
        print(f'Peso normal')
    elif indice < 30:
        print(f'Sobrepeso')
    elif indice < 35:
        print(f'Obeso leve')
    elif indice < 40:
        print(f'Obeso moderado')
    elif indice >= 40:
        print(f'Obeso mórbido')

if __name__=='__main__':
    main()
