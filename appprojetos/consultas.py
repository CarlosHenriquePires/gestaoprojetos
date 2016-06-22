from appprojetos.models import *

# Listar todos os projetos com seus respectivos membros.

projetos = Projetos.objects.all()
for projeto in projetos:
    print('titulo: ',projeto.titulo, )

#print()

# Listar todas as atividades que tenham sido executadas no mês de maio de 2015.

# Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A.

# Listar o custo total de cada projeto.