
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

projetos1=Projetos(titulo="Lógica de Programação com Scratch",dataInicio="2016-06-21",
                   dataTermino="2016-07-21",justificativa="Motivar os jovens a iniciar o estudo de programação",
                   metodologia="XXX",resultados="Criar artigos")
projetos1.save()

atividades1=Atividades(descricao="Visita à Escola",dataInicio="2016-06-21",dataTermino="2016-06-22",)
