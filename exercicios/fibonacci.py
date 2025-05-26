def fibonacci_iterativo(n_termos):
   
    if n_termos <= 0:
        return []
    elif n_termos == 1:
        return [0]
    else:
        sequencia = [0, 1]
        while len(sequencia) < n_termos:
            proximo_termo = sequencia[-1] + sequencia[-2]
            sequencia.append(proximo_termo)
        return sequencia


while True:
    try:
        termos_str = input("Quantos termos da sequência de Fibonacci você quer gerar? ")
        termos = int(termos_str) 

        if termos < 0:
            print("Por favor, digite um número não negativo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
resultado = fibonacci_iterativo(termos)
print(f"A sequência de Fibonacci com {termos} termos é: {resultado}")