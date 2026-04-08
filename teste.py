from missoes import MissaoCombate, MissaoColeta, MissaoExploracao
from personagem import Personagem

print("personagem")
p = Personagem("artur")
p.exibir_dados()

print("\nalterando")
p.nome = "Ana"
p.exibir_dados()


m1 = MissaoCombate("cacar", "derrotar inimigos", 20, "gooblin", 5)
m2 = MissaoColeta("coletar", "juntar recursos", 15, "madeira", 10)
m3 = MissaoExploracao("explorar", "descobrir area", 25, "caverna", 3.5)

# Testndo
for missao in [m1, m2, m3]:
    print("\n------")
    missao.iniciar_missao()
    missao.concluir_missao()
    missao.exibir_dados()