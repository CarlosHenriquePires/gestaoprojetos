
from appprojetos.models import *

# Inserindo dados no banco.


# Inserindo participantes

participante1=Participantes(name="Matheus",descricao="aluno")
participante2=Participantes(name="Carlos",descricao="aluno")
participante3=Participantes(name="Luan",descricao="aluno")
participante4=Participantes(name="Claudivan",descricao="aluno")
participante5=Participantes(name="Galego",descricao="aluno")

# Criando objeto e inserindo no banco
participante1.save()
participante2.save()
participante3.save()
participante4.save()
participante5.save()

# Inserindo Projetos

projeto1=Projetos(titulo="Scratch",dataInicio="2016-05-28",dataTermino="2016-06-03",justificativa="Ensino de lógica para jovens",metodologia="minicursos",resultados="dados coletados",participates="Matheus, Luan e Carlos")
projeto1.save
projeto2=Projetos(titulo="Meio Ambinte e Cidadania",dataInicio="2016-08-18",dataTermino="2016-11-12",justificativa="Importancia do meio ambiente",metodologia="palestras",resultados="concientização",participates="Galego e Crau")
projeto2.save

# Inserindo as Atividades