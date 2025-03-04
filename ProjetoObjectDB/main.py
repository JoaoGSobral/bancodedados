from modelos import Usuario, Funcionario, Livro, Emprestimo
from biblioteca_db import BibliotecaDB

def main():
    # Inicializa o banco de dados
    db = BibliotecaDB()

    try:
     
            
                  # Criar e salvar um usuário
        usuario = Usuario(1, "João Silva", "123.456.789-00", "joao@email.com", "U001")
        db.salvar_usuario(usuario)

        # Criar e salvar um funcionário
        funcionario = Funcionario(2, "Maria Santos", "987.654.321-00", 
                                "maria@biblioteca.com", "F001", "Bibliotecária")
        db.salvar_funcionario(funcionario)

        # Criar e salvar um livro
        livro = Livro(1, "O Senhor dos Anéis", "J.R.R. Tolkien", "978-8533613379")
        db.salvar_livro(livro)
        livro = Livro(2, "O Senhor dos Anéis - As Duas Torres", "J.R.R. Tolkien", "978-8845292255")
        db.salvar_livro(livro)

        # Criar e salvar um empréstimo
        emprestimo = Emprestimo(1, usuario, livro)
        db.salvar_emprestimo(emprestimo)

        # Buscar e exibir empréstimos ativos
        print("\nEmpréstimos ativos:")
        emprestimos_ativos = db.listar_emprestimos_ativos()
        for emp in emprestimos_ativos:
            print(f"Empréstimo: Usuário={emp.usuario.nome}, Livro={emp.livro.titulo}")

        # Listar livros disponíveis
        print("\nLivros disponíveis:")
        livros_disponiveis = db.listar_livros_disponiveis()
        for livro in livros_disponiveis:
            print(f"Livro: {livro.titulo} - {livro.autor}")

    finally:
        # Fecha a conexão com o banco
        db.fechar()
while opcao=!5:
    print("1- livro:")
    print("2- usuario:")
    print("3- funcionario")
    print("4-emprestimo ")
    print("5- sair") 
    opcao=int(input("digite a opcão:"))

 
    if opcao == "1":
       print("1- salvar livro: ")
       print("2- buscar livro: ")
       print("3- editar livro: ")
       print("4- excluir livro")
       print("5-saida")
       acao=int(input("digite a ação que deseja:"))
        if acao == "1":
            id_livro = int(input("digite o id do livro: "))
            titulo_livro= input("digite o titulo do livro: ")
            autor = input("digite o nome do autor: ")
            isbn= int(input("digite o numeração isbn: "))
            adicionar_livro = livro(id_livro,titulo_livro,autor,isbn)
            db.salvarlivro(adicionar_livro)
        elif acao == "2":
          livros = db.listar_livros_disponiveis()
          if livro:
            for livro in livros:
              print(f"livro encontrado: titulo{livro.titulo_livro}, autor:{livro.autor}")
          else:
            print("não encontrado")
        elif acao == "3":
            id = int(input("digite o id do livro que deseja editar: "))
            livro = db.buscar_livro(id)
            if livro:
              titulo_livro:input("titulo novo: ")
              autor = input("autor novo: ")
              isbn=input("isbn novo: ")
              db.salvar_livro(livro)
              print("livro atualizado")
            else:
              print("livro nao atualizado ")
        elif acao == "4":
            id= int(input("digite o id do livro que deseja excluir: "))
            livro = db.buscar_livro(id_livro)
            if livro: 
              del db.root.livros[livro.id]
              print("livro excluido com sucesso")
            else: 
              print("livro não encontrado")  
        else acao == "5":
          break       

   

    elif opcao == "2":

       print("1- salvar usuario: ")
       print("2- buscar usuario: ")
       print("3- editar usuario: ")
       print("4- excluir usuario")
       print("5-saida")
       acao=int(input("digite a ação que deseja:"))

        

          if acao == "1":
            id_usuario = int(input("digite o id do usuario: "))
              nome_usuario= input("digite o nome do usuario: ")
              usuario_cpf = int(input("digite o cpf: "))
              email_usuario= input("digite o email do usuario: ")
              cartao_usuario= int(input("digite o numero do cartão: "))
              adicionar_usuario = usuario(id_usuario, nome_usuario,usuario_cpf,email_usuario,numero_cartao)
              db.salvarusuario(adicionar_usuario)
        elif acao == "2":
          usuario = db.listar_usuarios()
          if usuario:
            for usuario in usuarios:
              print(f"Usuario encontrado: nome: {nome_usuario}, cpf: {usuario_cpf} ")
          else:
            print("não encontrado")
        elif acao == "3":
            id = int(input("digite o id do usuario que deseja editar: "))
            usuario = db.buscar_usuario(id)
            if usuario:
              nome_usuario:input("nome novo: ")
              email_usuario = input("email novo: ")
             
              db.salvar_usuario(usuario)
              print("usuario atualizado")
            else:
              print("usuario nao atualizado ")
        elif acao == "4":
            id= int(input("digite o id do usuario que deseja excluir: "))
            livro = db.buscar_usuario(id_usuario)
            if usuario: 
              del db.root.usuarios[usuario.id_usuario]
              print("usuario excluido com sucesso")
            else: 
              print("usuario não encontrado")  
        else acao == "5":
          break       

        
    elif opcao == "3":
       print("1- salvar funcionario: ")
       print("2- buscar funcionario: ")
       print("3- editar funcionario: ")
       print("4- excluir funcionario")
       print("5-saida")
       acao=int(input("digite a ação que deseja:"))

        if acao =="1":
          id_funcionario = int(input("digite o id do funcionario: "))
          nome_funcionario= input("digite o nome do funcionario: ")
          cpf_funcionario=int(input("digite o cpf do funcionario:"))
          email_funcionario= input("digite o email do funcionario: ")
          cargo_funcionario= input("digite o cargo do funcionario: ")
          matricula_funcionario=int(input("digite a matricula do funcionario:"))
          adicionar_funcionario = funcionario(id_funcionario,nome_funcionario,cpf_funcionario,email_funcionario,matricula_funcionario,cargo_funcionario)
          db.salvarfuncionario(adicionar_funcionario)

        elif acao == "2":
            funcionario = db.buscar_funcionario_por_matricula()
            if funcionario:
              for funcionario in funcionarios:
                print(f"funcionario encontrado: nome: {nome_funcionario}, matricula: {matricula_funcionario} ")
            else:
              print("não encontrado")
        elif acao == "3":
              id = int(input("digite a matricula do funcionario que deseja editar: "))
              funcionario = db.buscar_funcionario_por_matricula(matricula_funcionario)
              if funcionario:
                nome_funcionario=input("nome novo: ")
                email_funcionario = input("email novo: ")
                cargo_funcionario=input("cargo novo:")
              
                db.salvar_funcionario(funcionario)
                print("funcionario atualizado")
              else:
                print("funcionario nao atualizado ")
        elif acao == "4":
              id= int(input("digite a matricula do funcionario que deseja excluir: "))
              funcionario = db.buscar_funcionario_por_matricula(matricula_funcionario)
              if funcionario: 
                del db.root.funcionario[funcionario.matricula_funcionario]
                print("funcionario excluido com sucesso")
              else: 
                print("funcionario não encontrado")  
        else acao == "5":
            break       

    else opcao == "4":
       print("1- salvar emprestimo: ")
       print("2- buscar emprestimo: ")
       print("3- editar emprestimo: ")
       print("4- excluir emprestimo")
       print("5-saida")
       acao=int(input("digite a ação que deseja:"))

       
       
        if acao == '1':
          id_emprestimo=input("digite o id do emprestimo: ")
           id_livro = int(input("digite o id do livro: "))
        nome_usuario= input("digite o nome do usuario: ")
        data_retirada=input("digite a data do emprestimo: ")
        data_devolução=input("digite a data de devolução: ")
        novoemprestimo=emprestimo(id_usuario,id_livro,data_retirada,data_devolucao)
        db.salvar_emprestimo(novoemprestimo)


        elif opcao == '2':
            emprestimos = db.listar_emprestimos_ativos()
            if emprestimos:
                for emprestimo in emprestimos:
                   print(f" Emprestimo encontrado: Usuário: {emprestimo.nome_usuario}, Livro: {emprestimo.id_livro}, Data de Empréstimo: {emprestimo.data_retirada}, Devolução: {emprestimo.data_devolucao}")
            else:
                print("emprestimo nao encontrado.")

        elif opcao == '3':
            id = int(input("ID do empréstimo a ser editado: "))
            emprestimo = db.buscar_emprestimo(id_emprestimo)
            if emprestimo:
              nome_usuario=input("nome novo: ")
              id_livro = input("id do novo livro: ")
                novo_usuario = db.buscar_usuario(int(novo_usuario))
                novo_livro = db.buscar_livro(int(id_livro))
                if novo_usuario and novo_livro:
                    emprestimo.nome_usuario = novo_usuario
                    emprestimo.id_livro = novo_livro
                    db.salvar_emprestimo(emprestimo)
                    print(f"novo empréstimo atualizado com sucesso.")
                else:
                    print("Usuário ou livro não encontrado.")
            else:
                print("Empréstimo não encontrado.")

        elif opcao == '4':
            id = int(input("ID do empréstimo a ser excluído: "))
            emprestimo = db.buscar_emprestimo(id)
            if emprestimo:
                del db.root.emprestimos[emprestimo.id_emprestimo]
                emprestimo.livro.disponivel = True
                db.salvar_livro(emprestimo.id_livro)  # Atualiza o status do livro
                print(f"Empréstimo excluído com sucesso.")
            else:
                print("Empréstimo não encontrado.")
            else:
                print("Empréstimo não encontrado.")

        elif opcao == '5':
            break
                


       
if __name__ == "__main__":
    main()  
 