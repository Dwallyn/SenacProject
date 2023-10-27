from model import somarInicioFim #Conecta a classe model e control
from model import tabuada
from model import somar10Numeros
from model import inicialFinal
from model import somar0Numero
from model import mediaNumeros
from model import ePar
from model import fatorial
import this
this.opcao = -1 #Declarando a varíavel
this.num = -1 #acionar o While
this.i = 0 #contador
this.negativo = 0
def exercicio01():
    inicio = int(input("informe o inicio: "))
    fim    = int(input("Informe o fim: "))
    print(somarInicioFim(inicio, fim))

def exercicio02():
    num = int(input("informe o numero que deseja multiplicar: "))
    fim = int(input("informe até onde deve ser multiplicado: "))
    print(tabuada(num, fim))

def exercicio03():
    inicio = int(input("informe o valor inicial"))
    fim    = int(input("informe o valor final"))
    print (inicialFinal(inicio, fim))

def exercicio04():
    inicio = int(input("informe o inicio: "))
    fim    = int(input("informe o fim: "))

def exercicio05():
    for i in range(0, 10, 1):
        num  = int(input("informe {} número:".format(i+1)))
        soma = somar10Numeros(num)
    print("A soma dos números digitados é: {}".format(soma))

def exercicio06():
     while (this.num != 0):
         this.num = int(input("informe um valor: "))
         soma = somar0Numero (this.num)
     print ("A soma dos valores é: {}".format(soma))

def exercicio07():
    while (this.num != 0):
        this.num = int(input("informe um numero: "))
        if ePar(this.num) == True:
           soma = somar10Numeros(this.num)
           this.i += 1
    print("A média dos numeros digitados é: {}".format(mediaNumeros(soma,this.i)))

def exercicio08():
    while(this.num != 0):
        this.num = int(input("Informe um número: "))
        if this.num !=0:
          if this.i == 0:
            maior = this.num
            menor = this.num
          this.i += 1
          if this.num > maior:
            maior = this.num
          if this.num < menor:
            menor = this.num
    print("O maior numero digitado é: {} \ne o menor número digitado é: {}".format(maior,menor))

def exercicio09():
    for i in range (20):
        this.num = int(input("informe o valor"))
        if this.num >= 0:
            soma = somar10Numeros(this.num)
        else:
            this.negativo += 1
    print(f"Há {this.negativo} numeros negativos\na soma dos positivos é {soma}")

def exercicio10():
    num = int(input("informe um numero: "))
    print(fatorial(num))

def exercicio11():
    quantidade = int(input("Informe a quantidade de jogadores: "))
    for i in range(0, quantidade, 1):
        altura = float(input(f"{i + 1} altura: "))
        while(altura <= 0):
            if altura <= 0:
                print("Erro! informe uma altura valida!")
            altura = float(input(f"{i + 1} altura: "))
        soma = somar10Numeros(altura)
    print(f"A media de altura desse time é: {mediaNumeros(soma, quantidade)}")

def exercicio12():
    for i in range(0, 16, 1):
        nota = float(input(f"{i+1} nota: "))
        while(nota < 0 or nota > 10):
            print("Erro! informe uma nota entre 0 e 10")
        cand = input(f"{i+1} candidata: ")
        if i == 0:
            maior = nota
        if nota > maior:
            maior = nota
            venc = cand
    print(f"A vencedora é: {venc}, sua nota foi: {maior}")






def menu():
    print("\nEscolha uma das opções abaixo: \n" +
          "0. Sair\n" +
          "1. Exercicio 01\n" +
          "2. Exercicio 02\n" +
          "3. Exercicio 03\n" +
          "4. Exercicio 04\n" +
          "5. Exercicio 05\n" +
          "6. Exercicio 06\n" +
          "7. Exercicio 07\n" +
          "8. Exercicio 08\n" +
          "9. Exercicio 09\n" +
          "10 Exercicio 10\n" +
          "11 Exercicio 11\n" +
          "12 Exercicio 12\n" )
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu() #Chamar o menu
        if this.opcao == 0:
            print("Obrigado")
        elif this.opcao == 1:
            (exercicio01())
        elif this.opcao == 2:
            (exercicio02())
        elif this.opcao == 3:
            (exercicio03())
        elif this.opcao == 4:
            (exercicio04())
        elif this.opcao == 5:
            (exercicio05())
        elif this.opcao == 6:
            (exercicio06())
        elif this.opcao == 7:
            (exercicio07())
        elif this.opcao == 8:
            (exercicio08())
        elif this.opcao == 9:
            (exercicio09())
        elif this.opcao == 10:
            (exercicio10())
        elif this.opcao == 11:
            (exercicio11())
        elif this.opcao == 12:
            (exercicio12())
        else:
            print("Erro! Escolha uma opção valída")

