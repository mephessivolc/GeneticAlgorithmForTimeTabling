import random 
import csv

import string

def random_word_generate():
    letras = string.ascii_lowercase  # Obtém todas as letras minúsculas do alfabeto
    random_word = ''.join(random.choice(letras) for _ in range(5))
    return random_word

teacher_lines = []
for i in range(10):
    tmp = []

    tmp.append(f"{i}_{random_word_generate()}")
    for j in range(8):
        tmp.append(random.randint(0, 5))
    
    teacher_lines.append(tmp)

with open('timetabling.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=" ", quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for i in teacher_lines:
        csvwriter.writerow(i)

print("Arquivos criados")
