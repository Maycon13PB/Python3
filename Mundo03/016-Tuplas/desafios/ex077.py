palavras = ("Aprender", "Programar", "Linguagem", "Python", "Curso", "Gratis", "Estudar", "Praticar", "Trabalhar ", "Mercado", "Programar", "Futuro")
for vol in palavras:
    print(f"\nNa palavra {vol.upper()} temos", end=" ")
    for letra in vol:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
