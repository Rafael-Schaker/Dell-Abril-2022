#Rafael Schaker Kocpczynski da Rosa
#Desafio IT Academy - Edição #15
#27/03/2022
import csv          #para ler um arquivo csv
import unidecode    #para retirar grande parte dos acentos de strings
import os           #para limpar o terminal
import string       #para possibilitar converter uma string para ficar completamente maiúscula 
class Bolsas:# cada Bolsa será salva com esses parâmetros
    def __init__(self,Nome,CPF,EE,Ano,VB):
        self.Nome = Nome    #A - 0
        self.CPF = CPF      #B - 1
        self.EE = EE        #C - 2
        self.Ano = Ano      #E - 4
        self.VB  = VB       #K - 10
#Função para pegar a primeira bolsa de certo ano
def C_BolsaZero(vetor,ANO):
    achou = False #Verificador de existência
    for i in range (len(vetor)):
        if vetor[i].Ano == ANO:
            print('Nome:'+vetor[i].Nome+'; CPF:'+vetor[i].CPF+'; Entidade de Ensino:'+vetor[i].EE+'; Valor da Bolsa:'+vetor[i].VB+'.')
            achou = True
            break
    if achou == False:
        print('Ano não registrado!')
#Codificação de Nomes   
def Codifica(codificar):
    final=""  
    cortada = codificar.split(' ')#Ao encontrar um espaço separa cada pedaço do nome da pessoa
    lista = list(string.ascii_uppercase)#cria a lista com todas as letras do alfabeto em maiúsculo
    for i in range(len(cortada)):
        palavra=''
        codificada = cortada[i][-1] + cortada[i][1:-1] + cortada[i][0]#troca a primeira com o ultimo char do nome
        if len(cortada[i])>3:#para ocorrer somente com as palavras com mais de 3 chars, isso é devido ao exemplo que mostrou 'PAZ' se tornando 'ABQ' não 'QBA'
            codificada=codificada[::-1]#inverte a palavra
        for b in range(len(codificada)):#for para passar por todas as letras da palavra
            trocou = False
            for a in range(len(lista)):#for para passar por todas as letras do alfabeto
                if codificada[b]==lista[a] and trocou==False:
                    if 25!=a:
                        letra=lista[a+1]#troca a atual letra pela proxima no alfabetor
                    else:
                        letra=lista[0]
                    trocou=True #processo para verificar se essa letra já foi trocada ou não
                    palavra += letra
        final+=palavra+' '
    return final
#Procura pelo nome de algum bolsista
def C_Nome (vetor,NOME):
    achou = False #Verificador de existência
    NOME=NOME.upper()#deixa a letra em maiúscula
    NOME = unidecode.unidecode(NOME)#retira grande parte dos acentos
    NOME = NOME.replace("'","")#retira até as apóstrofes do nome
    if len(NOME) == 1:#Para caso a usuário entregue somente uma letra, não entregar nada que era previsto
        print('Nome não registrado ou porfavor insira pelo menos um pedaço do respectivo nome!')
        return
    for i in range (len(vetor)):
        #CASO: usuário entregue o nome inteiro
        if NOME==vetor[i].Nome:
            achou = True 
            print('Nome:'+Codifica(vetor[i].Nome)+'; Ano:'+vetor[i].Ano+'; Entidade de Ensino:'+vetor[i].EE+'; Valor da Bolsa:'+vetor[i].VB+'.')
            break
        #CASO: usuário entregue um ou mais pedaços do nome
        parteNome=vetor[i].Nome.split(" ")#sepra cada pedaço de nome registrado ao encontrar um espaço
        parteNOME=NOME.split(" ")#Separa o nome obtido, caso ele sejá maior que uma palavra
        for j in range (len(parteNome)):#quando for somente uma parte do nome
            if parteNome[j] == parteNOME[0]:#caso encontre a primeira parte do nome obtido pelo usuário
                tam=len(parteNOME)
                if tam > 1:
                    p1=''#guardará cada parte do nome do aluno
                    p2=''#guardará cada parte do nome recebido
                    for h in range(j,j+tam):
                        p1 +=parteNome[h]+' '
                    for h in range(len(parteNOME)):
                        p2 +=parteNOME[h]+' '
                    if p1==p2:#verifica se o restante do nome obtido é igual ao restante do nome 
                        print('Nome:'+Codifica(vetor[i].Nome)+'; Ano:'+vetor[i].Ano+'; Entidade de Ensino:'+vetor[i].EE+'; Valor da Bolsa:'+vetor[i].VB+'.')
                        achou = True
                else: #caso somente tenha recebido 1 parte do nome
                    print('Nome:'+Codifica(vetor[i].Nome)+'; Ano:'+vetor[i].Ano+'; Entidade de Ensino:'+vetor[i].EE+'; Valor da Bolsa:'+vetor[i].VB+'.')
                    achou = True 
    if achou == False:
        print('Nome não registrado ou porfavor insira pelo menos um pedaço do respectivo nome!')
#Média Anual das bolças
def C_MediaAnual(vetor,ANO):
    achou = False #Verificador de existência
    Soma=0
    qnt=0#quantidade de bolsistas encontradas no ano
    for i in range (len(vetor)):
        if vetor[i].Ano == ANO:
            Soma += int(vetor[i].VB)
            qnt+=1
            achou = True
    if achou == False:
        print('Ano não registrado!')
    else:
        Soma/=qnt
        print('Média do Valor da bolsa do ano de:'+ANO+', foi de: R$'+"%.2f"%Soma+'.')        
#main
vetor = []
top = [0,0,0,0,0,0,0]#metade é o Top 3 que mais valem e o resto Top 3 que menos valem o ultimo é somente para guardar o primeiro valor obtido na consulta
try:#caso ocorra algum erro durante a leitura do arquivo
    with open('br-capes-bolsistas-uab.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader.__next__()#pula a linha que indica oque é cada coluna
        for coluna in csv_reader:
            vetor.append((Bolsas(coluna[0],coluna[1],coluna[2],coluna[4],coluna[10])))
            #Os dados das Top bolsas são gravados no momento da gravação de dados
            vBolsa = int(coluna[10])  
            if len(vetor) == 1:#caso seja o primeiro dado adicionado ao vetor
                top[0]=vBolsa
                #guarda o valor da primeira bolsa para parâmetro de valor
                for i in range(3,7):
                    top[i]=vBolsa#guarda o valor inicial, para podermos comparar posteriormente
            if len(vetor) > 1:
                if top[0] < vBolsa:#top 3 maiores
                    if top [1] < top[0]:
                        top[2]=top[1]
                    top[1] = top[0]
                    top[0] = vBolsa
                if top[3]>vBolsa:#top 3 menores
                    if top [4] > top[3]:
                        top[5]=top[4]
                    top[4] = top[3]
                    top[3] = vBolsa    
    opcao=1
    while opcao != 5:
        if opcao<1 or opcao>5:
            print(' Opção inexistente!')
        try:#Para caso o usuário escrever uma string ou um float não um inteiro
            opcao=int(input('\n --Opções--\n 1 -> Consultar bolsa zero/Ano;\n 2 -> Codificar nomes;\n 3 -> Consultar a média anual; \n 4 -> Ranking valores de bolsa; \n 5 -> Terminar o programa.\n Sua escolha:'))
            os.system('cls' if os.name == 'nt' else 'clear')#limpa o terminal
        except:
            print(' Opção obtida tem que ser um número inteiro!!!')
            opcao=6
        match opcao:
            case 1:
                val = input('Indique um Ano:')   
                C_BolsaZero(vetor,val)
            case 2:
                val = input('Qual o nome:')
                C_Nome(vetor,val)
            case 3:
                val = input ('Indique o Ano:')
                C_MediaAnual(vetor,val)
            case 4:
                print('Top 3 maiores valores das bolsas:')
                for i in range(6):
                    if top[i]>0 and i<3:#top 3 maiores
                        print(' ',i+1,'º: R$',top[i])
                    if top[i] != top[0] and top[i] != top[1] and top[i] != top[2]  and i>2:#top 3 menores, tem que ter o valor diferente de todos os Tops 3, para ser considerado outra categoria mesmo, ou se não estaria repetindo os mesmo valores em grupos diferentes
                        if i==3:
                            print('Top 3 menores valores das bolsas:')
                            print(' ',i-2,'º: R$',top[i])
                        else:
                            if top[i] != top[i-1]:#com a utilização do valor do top[6], posso saber se o valor de terceiro lugar realmente foi mudado ou não
                                print(' ',i-2,'º: R$',top[i])  
    print('Processo Encerrado!')   
except:
  print("Erro na leitura do arquivo")                             