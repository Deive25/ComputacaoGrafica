import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vector(vector, origin=[0, 0, 0], color='b', label='Vector'):
    """Função para plotar um vetor 3D"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(origin[0], origin[1], origin[2],
              vector[0], vector[1], vector[2],
              color=color, label=label)

    max_val = max(abs(np.array(vector)))
    ax.set_xlim([-max_val-1, max_val+1])
    ax.set_ylim([-max_val-1, max_val+1])
    ax.set_zlim([-max_val-1, max_val+1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()

def ler_vetor():
    """Função para ler um vetor do teclado"""
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    return np.array([x, y, z])

def main():
    print("\nDigite os valores do vetor inicial:")
    vetor = ler_vetor()

    while True:
        print("\nMenu de Operações:")
        print("a) Calcular o tamanho do vetor")
        print("b) Normalizar o vetor")
        print("c) Adicionar outro vetor")
        print("d) Subtrair outro vetor")
        print("e) Multiplicar por escalar")
        print("f) Dividir por escalar")
        print("g) Calcular produto escalar com outro vetor")
        print("h) Sair")

        opcao = input("\nEscolha uma opção: ").lower()

        if opcao == 'a':
            tamanho = np.linalg.norm(vetor)
            print(f"\nTamanho do vetor: {tamanho:.2f}")
            plot_vector(vetor)

        elif opcao == 'b':
            vetor_norm = vetor / np.linalg.norm(vetor)
            print(f"\nVetor normalizado: [{vetor_norm[0]:.2f}, {vetor_norm[1]:.2f}, {vetor_norm[2]:.2f}]")
            plot_vector(vetor_norm, color='r', label='Vetor Normalizado')

        elif opcao == 'c':
            print("\nDigite os valores do vetor a ser adicionado:")
            vetor2 = ler_vetor()
            resultado = vetor + vetor2
            print(f"\nVetor resultante: [{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}]")
            plot_vector(vetor, color='b', label='Vetor 1')
            plot_vector(vetor2, color='g', label='Vetor 2')
            plot_vector(resultado, color='r', label='Resultado')
            vetor = resultado

        elif opcao == 'd':
            print("\nDigite os valores do vetor a ser subtraído:")
            vetor2 = ler_vetor()
            resultado = vetor - vetor2
            print(f"\nVetor resultante: [{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}]")
            plot_vector(vetor, color='b', label='Vetor 1')
            plot_vector(vetor2, color='g', label='Vetor 2')
            plot_vector(resultado, color='r', label='Resultado')
            vetor = resultado

        elif opcao == 'e':
            escalar = float(input("\nDigite o valor do escalar para multiplicação: "))
            resultado = vetor * escalar
            print(f"\nVetor resultante: [{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}]")
            plot_vector(vetor, color='b', label='Original')
            plot_vector(resultado, color='r', label='Resultado')
            vetor = resultado

        elif opcao == 'f':
            escalar = float(input("\nDigite o valor do escalar para divisão: "))
            if escalar != 0:
                resultado = vetor / escalar
                print(f"\nVetor resultante: [{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}]")
                plot_vector(vetor, color='b', label='Original')
                plot_vector(resultado, color='r', label='Resultado')
                vetor = resultado
            else:
                print("\nErro: Divisão por zero!")

        elif opcao == 'g':
            print("\nDigite os valores do segundo vetor para produto escalar:")
            vetor2 = ler_vetor()
            produto_escalar = np.dot(vetor, vetor2)
            print(f"\nProduto escalar: {produto_escalar:.2f}")
            plot_vector(vetor, color='b', label='Vetor 1')
            plot_vector(vetor2, color='g', label='Vetor 2')

        elif opcao == 'h':
            print("\nPrograma encerrado!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
