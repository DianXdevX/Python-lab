import json
import os
#importanto  bibliotecas  para ver o sistema e interagir com arquivos 
ARQUIVO_json = "arquivo.json"
def Load_task():
    if not os.path.exists(ARQUIVO_json):
        return[]
    try:
        with open(ARQUIVO_json,"r",encoding="utf-8")as file:
            #with  = enquanto aberto   
            convertlist =json.load(file)
            return convertlist
    except json.JSONDecodeError:
        return[]
def save_task(task_list):
    with open(ARQUIVO_json,"w",encoding="utf-8")as file:
        json.dump(task_list,file, indent=4,ensure_ascii=False)
#TESTE
#tarefas_teste = [
  #  {"id": 1, "titulo": "Aprender a salvar JSON", "concluida": True},
   # {"id": 2, "titulo": "Criar o menu amanhã", "concluida": False}]
#save_task(tarefas_teste)
#read_data=Load_task() 
#print("Dados que vieram do arquivo:")
#print(read_data)
def menu():
    task_list =Load_task()
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("\n")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar como concluída")
        print("4. Excluir tarefa")
        print("5. Sair /n")
        print("Diana dev industries  kupo ><")
        #configura o menu 
        try:
         opition = int(input("\nEscolha uma opção:"))
        except ValueError:
            print("por favor digite um numero valido ")
            continue
        if opition  == 1:
            print("Você escolheu Listar.") #
            lista_tarefas(task_list) 
        elif opition  == 2:
            print("Você escolheu Adicionar.") 
            adicionar_tarefas(task_list)

        elif opition  == 3:
            print("Você escolheu Concluir.") 
            Marcar_como_concluída(task_list)
        elif opition  == 4:
            print("Você escolheu Excluir.") 
            deletar_tarefa(task_list)
        elif opition  == 5:
            print("Saindo do programa... Até logo!")
            
            break  # Comando essencial: quebra o while True

def lista_tarefas(task_list): 
    print("\n--- YOUR TASKS ---")
    if not task_list:
        print("Ainda nao possui lista ")
        return 
    for task in task_list:
        if task["concluido"] == True:
            status = "[x]"
        else:
            status = "[]"
        print(f"ID: {task['id']} | {status} {task['titulo']}")


def adicionar_tarefas(task_list):
    tarefa_name = input("\nDigite o nome da tarefa: ")
    if not task_list:
        new_id = 1
    else:
        new_id =len(task_list)+1
    new_tarefa = {
        "id": new_id,
        "titulo": tarefa_name,
        "concluido" :False
    }
    task_list.append(new_tarefa) #apped  e adicionar a lista 
    save_task(task_list)
    print(f"Tarefa '{tarefa_name}' salva com sucesso.")
    #o f serve para ler a variavel pelo que entendi 

def Marcar_como_concluída(task_list):
    lista_tarefas(task_list)
    if not task_list:
        return
    try:
        id_alvo = int(input("\nDigite o ID da tarefa que deseja concluir: "))
    except ValueError:
        print("Erro crítico: Você deve digitar um número inteiro.")
        return # Exits the function if the input is invalid
    task_encontrada = False
    for task in task_list: #se a tarefa estiver na lista
        if task["id"] == id_alvo: # e o id for igual ao  id salvo 
            task["concluido"] = True # muda o status para verdade ou melhor concluida
            task_encontrada = True 
            print(f"Sucesso! A tarefa '{task['titulo']}' foi marcada como [x].")
            break
    if not task_encontrada:
        print(f"Falha: Nenhuma tarefa encontrada com o ID {id_alvo}.")
    save_task(task_list)  #salva a lista com as ateraçoes

def deletar_tarefa(task_list):
    lista_tarefas(task_list)
    try:
        id_alvo = int(input("\nDigite o ID da tarefa que deseja excluir: "))
    except ValueError:
        print("Erro crítico: Você deve digitar um número inteiro.")
        return

    task_encontrada = False
    

    for task in task_list:
        if task["id"] == id_alvo:
            task_list.remove(task)  # Remove o dicionário inteiro da lista
            task_encontrada = True
            print(f"Sucesso! A tarefa '{task['titulo']}' foi excluída.")
            break  # Interrompe o loop pois o elemento já foi removido
            
    if not task_encontrada:
        print(f"Falha: Nenhuma tarefa encontrada com o ID {id_alvo}.")
        
    # 4. Sincronização com o armazenamento persistente
    save_task(task_list)


menu()  
#executa o menu 


       
         