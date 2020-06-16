import os
import csv
homePastBooks="./projeto2/book-notes/Books/"
logArquive= "./projeto2/book-notes/log.csv"

def existe(livro):
    inc=0
    tmp = open(logArquive, 'r')
    leitor =csv.reader(tmp)
    for i in leitor:
        if(i[0]==livro):
            inc+=1
    if inc==0:
        return False
    else:
        return True  

def cadastrarLivro(livro, numCap,paginaAtual):
    if not(existe(livro)):
        os.makedirs('{}{}'.format(homePastBooks,livro))
        data_list = [livro, numCap,paginaAtual],
        with open(logArquive, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)
            print("Cadastrado com sucesso!")
            return True
    else:
        print("Livro ja existe!")
        return False
        
def listarLivros():
    data_list=[]
    tmp = open(logArquive, 'r')
    leitor =csv.reader(tmp)
    for i in leitor:
        data_list.append(i)
    return data_list

def escreverAnotacao(livro,capitulo, escreverAnotacao):
    data_list = [escreverAnotacao],
    with open("{}{}/{}.csv".format(homePastBooks,livro,capitulo), 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
        print("Anotação feita com Sucesso")


def excluirAnotacao(livro, capitulo, linha):
    tmp = open("{}{}/{}.csv".format(homePastBooks,livro,capitulo), 'r')
    lines = tmp.readlines()
    tmp.close()
    tmp = open("{}{}/{}.csv".format(homePastBooks,livro,capitulo), 'w')
    for line in lines:
        if (line!="{}\n".format(linha)) and (line!=linha):
            tmp.write(line)
    tmp.close()

def consultarAnotacaoCapitulo(livro,capitulo):
    try:
        with open("{}{}/{}.csv".format(homePastBooks,livro,capitulo),'r') as file:
            texto=file.readlines()
        data_list=[]
        for i in texto:
            data_list.append(i)
        return data_list
    except:
        print("{}Alguma informação incorreta{}".format("\033[1;31m","\033[m"))
        return False

def alterarPaginaAtual(livro,numCapitulo,paginaAntes,paginaAtual):
    newFile=""
    comp="{},{},{}".format(livro,numCapitulo,paginaAntes)
    with open(logArquive,'r') as file:
        texto=file.readlines()
    for i in texto:
        if i ==comp:
            newFile+="{},{},{}".format(livro,numCapitulo,paginaAtual)
        else:
            newFile+=i
    file.close()
    with open(logArquive,'w') as file:
        file.write(newFile)
    print("Alterado com sucesso!")


   


