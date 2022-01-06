def printList(mylist):
    if(len(mylist) > 0):
        lista.sort(key = int)
        print(' '.join(str(x) for x in mylist))
        
lista = input().split()

while True:
    command = input().split()
    if 'adicionar' in command:
        lista.append(command[1])
    elif 'remover' in command:
        if(command[1] in lista):
            lista.remove(command[1])
        else:
            print ("código",command[1],"não encontrado")
    elif 'exibir' in command:
        printList(lista)
    elif 'encerrar' in command:
        break

printList(lista)

    
