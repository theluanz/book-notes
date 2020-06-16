import book
import erro
import pomodoro
livro=""
capitulo=""
anotacao=""
pgAtual=0
login=False
listaDeLivros=[]

print("\n" * 10)
print("Seja bem vindo ao Book Note")
while login==False:
    opcao=str(input("Selecione uma opção\n1 - Cadastrar Livro\n2 - Selecionar Livro\n"))
    opcao=erro.isInt(opcao)
    if opcao == 1:
        livro = str(input("Digite o nome do Livro\n"))
        capitulo = str(input("Digite o número de capitulos\n"))
        pgAtual = str(input("Digite em qual pagina você está\n"))
        book.cadastrarLivro(livro,capitulo,pgAtual)
    elif opcao == 2:
        listaDeLivros=book.listarLivros()
        cont=1
        print("Estes são os livros disponíveis")
        for i in listaDeLivros:
            print("{} - {}".format(cont,i[0]))
            cont+=1
        livro= str(input("Selecione o livro desejado\n"))
        livro=erro.isIntPro(livro,0,(cont-1))
        if not(livro==False):
            livro = listaDeLivros[livro-1]
            login=True
            print("\n" * 10)
    else:
        print("{}Não é um numero valido!!{}".format("\033[1;31m","\033[m"))

while login==True:
    opcao=str(input("Voce está no Livro {}, selecione o que você quer fazer\n0 - Sair\n1 - Ler(Pomodoro)\n2 - Anotação\n3 - Verificar/Alterar Pagina Atual\n".format(livro[0])))
    opcao=erro.isIntPro(opcao,-1,3)
    if not(opcao==False):
        print("\n" * 10)
        if opcao==0:
            exit()
        elif opcao==1:
            minutos=str(input("Você está no Pomodoro, digite o tanto de minutos que você vai ler\n"))
            minutos=erro.isInt(minutos)
            descanso=str(input("Digite o tanto de minutos que você vai descansar\n"))
            descanso=erro.isInt(descanso)
            repeticoes=str(input("Digite o tanto de vezes que isso vai acontecer\n"))
            repeticoes=erro.isInt(repeticoes)
            if not(minutos==False) and not(repeticoes==False) and not(descanso==False):
                pomodoro.pomodoroTimer(repeticoes,minutos,descanso)    

        elif opcao==2:
            print("\n" * 10)
            opcao=str(input("Digite uma opção\n1 - Anotar\n2 - Consultar Anotações\n3 - Excluir uma anotação\n"))
            opcao=erro.isIntPro(opcao,0,3)
            if opcao==1:
                capitulo=str(input("Qual Capitulo do livro {} você deseja anotar algo?\n".format(livro[0])))
                anotacao=str(input("Escreva sua anotação\n"))
                book.escreverAnotacao(livro[0],capitulo,anotacao)
                print("\n" * 10)

            elif opcao==2:
                print("\n" * 10)            
                capitulo=str(input("Qual capitulo deseja consultar?"))
                capitulo=erro.isInt(capitulo)
                if not(capitulo==False):
                    try:
                        consulta=(book.consultarAnotacaoCapitulo(livro[0], capitulo))
                        index=0
                        for i in consulta:
                            print("{} - {}".format(index+1, i))
                            index+=1
                        input("Digite qualquer coisa para sair\n")
                    except:
                        print("{}Não é um numero valido!{}".format("\033[1;31m","\033[m"))    
            elif opcao==3:
                print("\n" * 10)
                capitulo=str(input("Qual capitulo deseja consultar para excluir?\n"))
                capitulo=erro.isInt(capitulo)
                consulta=(book.consultarAnotacaoCapitulo(livro[0], capitulo))
                if not(consulta==False):
                    print("\n" * 10)
                    index=0
                    for i in consulta:
                        print("{} - {}".format(index+1, i))
                        index+=1
                    opcao=str(input("Qual anotação deseja remover do capitulo {} do livro {}?".format(livro[1],livro[0])))
                    opcao=erro.isIntPro(opcao,0,index)
                    if not(opcao==False):
                        linha = consulta[opcao-1]
                        book.excluirAnotacao(livro[0],capitulo,linha)
            else:
                print("{}Não é um numero valido!!{}".format("\033[1;31m","\033[m"))     

        elif opcao==3:
            opcao=str(input("Você esta na página {},  desejar alterar?\n1 - Sim\n2 - Não".format(livro[2])))
            opcao=erro.isIntPro(opcao,0,2)
            if opcao==1:
                pgAtual=str(input("Digite a pagina em que você está atualmente"))
                pgAtual=erro.isInt(pgAtual)
                if not(pgAtual==False):
                    book.alterarPaginaAtual(livro[0],livro[1],livro[2],pgAtual)
                    livro[2]=pgAtual
            print("\n" * 10)



