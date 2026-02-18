
def notas_aprovacao_alunos(nota):

    if nota < 5:
        return "Reprovado"

    elif nota >= 5 and nota <= 7:
        return "Recuperação"

    elif nota >= 7 and nota <= 9:
        return "Aprovado"

    elif nota >= 9 and nota <= 10:
        return "Aprovado e Mérito!"

    else:
        return "Nota Invalida"


nota = float(input("Qual a sua nota? "))

resultado = notas_aprovacao_alunos(nota)

print(resultado)