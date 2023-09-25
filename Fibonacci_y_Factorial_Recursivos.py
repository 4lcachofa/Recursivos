def fibo(nfi):
    if nfi == 0:
        return 0
    if nfi == 1:
        return 1
    return fibo(nfi - 1) + fibo(nfi - 2)

def factos(nfa):
    if nfa == 0:
        return 1
    return nfa * factos(nfa - 1)


def main():
    print("Seleccione un método de búsqueda:")
    print("1] Fibonacci")
    print("2] Factorial")
    
    elec = int(input())
    
    if elec not in [1, 2]:
        print("Opción inválida")
        return
    
    if elec == 1:
        nfi = int(input("Ingrese el valor de n: "))
        fibo(nfi)
        result = fibo(nfi)
        print(f"El resultado de Fibonacci para n={nfi} es: {result}")

    elif elec == 2:
        nfa = int(input("Ingrese el dato a calcular: "))
        factos(nfa)
        result = factos(nfa)
        print(f"El resultado de Factorial para n={nfa} es: {result}")
        

if __name__ == "__main__":
    main()
