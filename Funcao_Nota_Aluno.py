def converter_nota(nota):
    if nota >= 9:
        return "A"
    if nota >= 8:
        return "B"
    if nota >= 7:
        return "C"
    if nota >= 6:
        return "E"
    else:
        return "F"

nota = int(input("Nota do Aluno: "))
convertida = converter_nota(nota) 
print(f"sua nota foi: {convertida}")