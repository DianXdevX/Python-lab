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
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar como concluída")
        print("4. Excluir tarefa")
        print("5. Sair")
           #configura o menu 
        try:
         opition = int(input("\nEscolha uma opção:"))
        except ValueError:
            print("por favor digite um numero valido ")
            continue
        if opition  == 1:
            print("Você escolheu Listar.") #
        elif opition  == 2:
            print("Você escolheu Adicionar.") 
        elif opition  == 3:
            print("Você escolheu Concluir.") 
        elif opition  == 4:
            print("Você escolheu Excluir.") 
        elif opition  == 5:
            print("Saindo do programa... Até logo!")
            break  # Comando essencial: quebra o while True
menu()  #executa o menu 