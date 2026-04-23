from Status import Status
from Missao import Missao, MissaoColeta, MissaoCombate, MissaoExploracao

missao_combate = MissaoCombate("Conquistar o povo de Teste", "Combater os inimigos do local Teste", 25, "Goblins", 5)
missao_coleta = MissaoColeta("Coletar 10 caixas de suprimentos", "Coletar suprimentos", 20, "Caixa de Suprimento", 10)
missao_exploracao = MissaoExploracao("Conquistar o território IFSUL", "Conquistar novo território", 50, "IFSUL", 10)

print(missao_combate.exibir_dados())
print(missao_combate.iniciar_missao())
print(missao_combate)
#print(missao_combate.concluir_missao())
print(missao_combate)
print()


print(missao_coleta.exibir_dados())
print()
print(missao_exploracao.exibir_dados())


missao = Missao("Teste Missao", "Teste missao abstrada", 10)
print(missao.exibir_dados())