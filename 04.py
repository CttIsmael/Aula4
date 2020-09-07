def media(n1, n2, n3, n4, n5):
    return (n1+n2+n3+n4+n5)/5
    
def main():
    n1 = int(input("Primeira nota: "))
    n2 = int(input("Segunda nota: "))
    n3 = int(input("Terceira nota: "))
    n4 = int(input("Quarta nota: "))
    n5 = int(input("Quinta nota: "))
    
    md = media(n1, n2,n3,n4,n5)
    print(f'{md:.2f}')   

    if n1 > md:
        print(f'{n1:.2f}')
    if n2>md:
        print(f'{n2:.2f}')
    if n3 > md:
        print(f'{n3:.2f}')
    if n4 > md:
        print(f'{n4:.2f}')
    if n5 > md:
        print(f'{n5:.2f}')  
   
    

if __name__=='__main__':
    main()
