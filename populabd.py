
from appprojetos.models import *

# Inserindo dados no banco.


# Inserindo participantes

participante1=Participantes(nome="Matheus",descricao="aluno")
participante2=Participantes(nome="Carlos",descricao="aluno")
participante3=Participantes(nome="Luan",descricao="aluno")
participante4=Participantes(nome="Claudivan",descricao="aluno")
participante5=Participantes(nome="Galego",descricao="aluno")

# Criando objeto e inserindo no banco
participante1.save()
participante2.save()
participante3.save()
participante4.save()
participante5.save()
