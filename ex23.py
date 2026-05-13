alunos = []
alunoMaior ={
        "nome": "nome",
        "idade": 0,
        "nota": 0.0
    }
alunoMenor ={
        "nome": "nome",
        "idade": 0,
        "nota": 0.0
    }
i = 0
notatot = 0
apr = 0
rec = 0
rep = 0
maior = -1
menor = 11

def classificar_aluno(nota):
    if nota >= 7:
        return "aprovado(a)"
    elif nota >= 5 and nota < 7:
        return "de recuperação"
    else:
        return "reprovado(a)"
        
def calc_media(notatot, i):
    return notatot/i

while True: 
    nome = input("Digite o nome do aluno: ")
    while True:
        try:
            idade = int(input("Digite a idade do aluno: "))
            if idade < 0:
                print("A idade deve ser maior que 0")
            else:
                break
        except ValueError:
            print("Valor inválido inserido, tente novamente")

    while True:
        try:
            nota = float(input("Digite a nota do aluno: "))
            if nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10")
            else:
                break
        except ValueError:
            print("Valor inválido inserido, tente novamente")
            
    aluno ={
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    
    alunos.append(aluno)
    
    i += 1
    notatot += nota
    if nota > maior:
        maior = nota
        alunoMaior = aluno
        
    if nota < menor:
        menor = nota
        alunoMenor = aluno
        
    while True:
        continuar = input("Deseja adicionar mais alunos? (S/N)")
        if continuar.lower() != "s" and continuar.lower() != "n":
            print("Digite apenas S ou N")
        else:
            break
    if continuar.lower() == "n":
        break
    

media = calc_media(notatot, i)

for aluno in alunos:
    situacao = classificar_aluno(aluno["nota"])
    print(f"O(A) aluno(a): {aluno["nome"]}, de idade: {aluno["idade"]} ficou com: {aluno["nota"]} e está {situacao}")
    if situacao == "aprovado(a)":
        apr += 1
    elif situacao == "de recuperação":
        rec += 1
    else:
        rep += 1
        
print(f"A turma está com uma média de {media:.2f}")
print(f"A qtd de alunos aprovados foi {apr} \nA qtd de alunos em recuperação foi {rec} \nA qtd de alunos reprovados foi {rep}")
print(f"O aluno com a maior nota foi: {alunoMaior["nome"]} com a nota {maior}")
print(f"O aluno com a menor nota foi: {alunoMenor["nome"]} com a nota {menor}")