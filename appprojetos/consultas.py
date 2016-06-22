from appprojetos.models import *

# Listar todos os projetos com seus respectivos membros.

for projeto in Projetos.objects.all():
    lista = []
    for participante in projeto.participantes.iterator():
        lista.append(participante.nome)
    print('Projeto: ',projeto.titulo,  '\nParticipantes: ', lista)


# Listar todas as atividades que tenham sido executadas no mês de maio de 2015.

for atividade in Atividades.objects.filter(dataInicio__year=2015,dataInicio__month=5):
    print(atividade.descricao)


# Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A.

for participantes in Participantes.objects.filter(nome__startswith='A'):
    print(participantes.nome)

# Listar o custo total de cada projeto.

for projeto in Projetos.objects.all():
    lista = []
    for atividades in projeto.atividades_set.iterator():
        lista.append(atividades.custos)
    print('Projeto: ',projeto.titulo,  '\nCustos: ', sum(lista))


