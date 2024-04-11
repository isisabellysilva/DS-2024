def fibonacci(n):
    fibonacci_sequence = [1, 1]  # Inicializa os primeiros dois termos da sequência Fibonacci
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calcula o próximo termo
        fibonacci_sequence.append(next_term)  # Adiciona o próximo termo à sequência
    return fibonacci_sequence

def main():
    n = int(input("Digite o número de termos da sequência Fibonacci: "))
    fibonacci_terms = fibonacci(n)  # Chama a função para gerar os termos
    print("Sequência Fibonacci até o", n, "° termo:")
    for term in fibonacci_terms:
        print(term, end=" ")

if __name__ == "__main__":
    main()