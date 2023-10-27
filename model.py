#1. Faça um algoritmo que calcule a soma dos números inteiros entre 1 e 100.
# while = Utilizo quando eu não sei quantas vezes vou repetir
# for = quando eu sei quantas repetições acontecerão
import this
this.soma = 0
this.num = 0

def somarInicioFim(inicio, fim):
    soma = 0 #Instanciei a varíavel
    for i in range(inicio,fim+1,1):
        soma += i
    return soma

#2. Construa um programa que exiba a tabuada de  até N.

def tabuada(num, fim):
    multiplicacao = "" #Instanciando uma variavel do tipo texto
    for i in range (1, fim+1, 1):
        multiplicacao += "{} * {} = {}\n".format(num, i, num * i)
    return multiplicacao

#3. Faça um algoritmo que escreva na tela os números
# de um número inicial a um número final. Os números iniciais
# e final devem ser informados pelo usúario;

def inicialFinal(inicio, fim):
    mostrar = ""
    for i in range (inicio, fim+1, 1):
        mostrar += "{}\n".format(i)
    return mostrar


#4. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200;

def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar

#5. Escrever um algoritmo que leia 10 números inteiros e, ao final, apresente a
#soma de todos os números lidos;

def somar10Numeros(num):
     this.soma += num
     return this.soma

#6. Faça o mesmo que antes, porém ao invés de ler 10 numeros, o programa deverá ler e somar números até que o valor digitado seja zero (0);

def somar0Numero(num):
    this.soma += num
    return this.soma

#7. Escreva um algortimo que calcule a média dos números digitados pelo usuario, se eles forem pares. Termine a leitura se o usuario digitar zero (0);

def mediaNumeros(soma, qtde):
    return soma / qtde
def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False

#8. Escreva um algoritmo que leia valores inteiros e encontre o maior e o menor deles. Termine a leitura se o usuario digitar zero (0);

#9.Escreva um algoritmo que leia 20 valores inteiros e ao final exiba: A) a soma dos numeros positivos; B) a qantidade de valores negativos;

#10. Escreva um programa que lido um número, calcule e informe o seu fatorial.
#EX: 5! = 5 * 4 * 3 * 2 * 1 = 120

def fatorial(num):
    aux = num
    fat = 1
    while (num > 1):
        fat= fat * num
        num -= 1
    return f"O fatorial de {aux} é {fat}"

#11. Escreva um programa que leia um valor correspondente ao numero de jogadores de um time de volei. O programa devera ler uma altura para cada um dos jogadores e, ao final, informar a altura media do time.

#12. Em um concurso de miss, os jurados precisam digitar o nome das 16 candidatas e suas respectivas notas (0 a 10). Crie um programa que leia estas informações e que, ao final d programa, apresente apenas o nome e a nota da vencedora





