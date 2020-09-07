def comparando(a,b,c,d,e):
    mx = a
    if b > a and b>c and b>d and b>e:
        mx = b
        return mx
    elif c > a and c>b and c>d and c>e:
        mx = c
        return mx
    elif d > a and d>b and d>c and d>e:
        mx = d
        return d
    elif e > a and e>b and e>c and e>c:
        mx = e
        return mx 
    return mx
def outro(a,b,c,d,e):
    mnr = a
    if b<a and b<c and b<d and b<e:
        mnr = b
        return mnr
    elif c<a and c<b and c<d and c<e:
        mnr = c
        return mnr
    elif d<a and d<b and d<c and d<e:
        mnr = d
        return mnr
    elif e<a and e<b and e<c and e<d:
        mnr = e
        return mnr
    return mnr
def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    d = int(input("Digite o quarto número: "))
    e = int(input("Digite o quinto número: ")) 

    maior = comparando(a,b,c,d,e)
    menor = outro(a,b,c,d,e)

    print(f'O maior número digitado foi {maior} e o menor foi {menor}')

if __name__=='__main__':
    main()
