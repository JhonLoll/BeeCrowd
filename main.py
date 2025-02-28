import os
import sys

# Captura o nome de todos os arquivos em Questions/Iniciante e Questions/Math
# e adiciona em uma lista
def get_questions():
    questions = []
    # Verifica a pasta "Iniciante"
    for question in os.listdir('Questions/Iniciante'):
        if question.endswith('.py'):  # Verifica se é um arquivo Python
            questions.append(f'Iniciante.{os.path.splitext(question)[0]}')  # Retira a extensão e adiciona o prefixo
    # Verifica a pasta "Math"
    for question in os.listdir('Questions/Math'):
        if question.endswith('.py'):  # Verifica se é um arquivo Python
            questions.append(f'Math.{os.path.splitext(question)[0]}')  # Retira a extensão e adiciona o prefixo
    return questions

# Mostra ao usuário todas as questões disponíveis, e o usuário escolhe uma para ser resolvida
def show_questions():
    questions = get_questions()
    print("\nQuestões disponíveis:")
    for idx, question in enumerate(questions):
        print(f'{idx} - {question}')
    print("-1 - Sair")
    
    question = int(input("Escolha uma questão (ou -1 para sair): "))
    return question, questions

# Executa a questão escolhida pelo usuário
def run_question(question):
    try:
        # Tenta importar a função da questão selecionada
        module = __import__(f'Questions.{question}', fromlist=[question])
        getattr(module, question.split('.')[-1])()  # Executa a função do módulo, removendo o prefixo
    except Exception as e:
        print(f"Erro ao tentar executar a questão {question}: {e}")

# Função principal
def main():
    # Adiciona a pasta "Questions" ao caminho de pesquisa do Python
    sys.path.append(os.path.abspath('Questions'))
    
    while True:
        # Exibe as questões e permite a escolha do usuário
        choice, questions = show_questions()

        if choice == -1:
            print("Saindo do programa...")
            break
        
        if 0 <= choice < len(questions):
            # Chama a função da questão selecionada
            question = questions[choice]
            run_question(question)
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == '__main__':
    main()
