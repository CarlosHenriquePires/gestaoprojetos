
from appprojetos.models import *

# Inserindo dados no banco.


# Inserindo participantes

participante1=Participantes(nome="Matheus",matricula="20142148060101",descricao="aluno")
participante2=Participantes(nome="Carlos",matricula="20142148060102",descricao="aluno")
participante3=Participantes(nome="Luan",matricula="20142148060103",descricao="aluno")
participante4=Participantes(nome="Claudivan",matricula="20142148060104",descricao="aluno")
participante5=Participantes(nome="Galego",matricula="20142148060105",descricao="aluno")
participante6=Participantes(nome="Juliana",matricula="20142148060106",descricao="aluno")

# Criando objeto e inserindo no banco
participante1.save()
participante2.save()
participante3.save()
participante4.save()
participante5.save()
participante6.save()

#Criando os projetos
projetos1=Projetos(titulo="Lógica de Programação com Scratch", dataInicio="2016-06-21",
                   dataTermino="2016-07-21",justificativa="Motivar os jovens a iniciar o estudo de programação",
                   metodologia="XXX",resultados="Criar artigos")
projetos1.save()
projetos2 = Projetos(titulo="Jiu-Jitsu: Lutando pela cidadenia", dataInicio="2016-08-12",
                     dataTermino="2016-10-23", justificativa="Incentivar a prática desportiva",
                     metodologia="XXX", resultados="Concientizar a sociedade e beneficiados do projeto")
projetos2.save()
projetos3 = Projetos(titulo="Robótica: do básico ao avançado", dataInicio="2016-08-05",
                     dataTermino="2016-12-14", justificativa="Ajudar crianças a desenvolver de maneira lúdica a criatividade",
                     metodologia="XXX", resultados="Reciclagem")
projetos3.save()

# Inserindo os participantes do projeto
projetos1.participantes.add(participante1,participante2,participante3)
projetos2.participantes.add(participante4,participante5,participante3)
projetos3.participantes.add(participante1,participante2,participante6)

# Criando Atividades
atividades1=Atividades(descricao="Visita à Escola",dataInicio="2016-06-21",dataTermino="2016-06-22",custos=1,projetos=projetos1)
atividades1.save()
atividades2=Atividades(descricao="Prepatrando o Tatame",dataInicio="2016-08-21",dataTermino="2016-08-22",custos=1,projetos=projetos2)
atividades2.save()
atividades3=Atividades(descricao="Separando o Material",dataInicio="2016-09-21",dataTermino="2016-09-22",custos=1,projetos=projetos3)
atividades3.save()
atividades4=Atividades(descricao="Aplicação do minicurso",dataInicio="2016-09-21",dataTermino="2016-09-22",custos=3,projetos=projetos1)
atividades4.save()

# Criando o acompanhamento das atividades
acompanhamento1=Acompanhamento(descricao="Manutenção dos Laboratórios",data="2016-06-22",atividades=atividades1)
acompanhamento1.save()
acompanhamento2=Acompanhamento(descricao="Limpando Sala de treinos",data="2016-08-23",atividades=atividades2)
acompanhamento2.save()
acompanhamento3=Acompanhamento(descricao="Separar material para aulas práticas",data="2016-09-24",atividades=atividades3)
acompanhamento3.save()
