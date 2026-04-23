from missoes import MissaoCombate, MissaoColeta, MissaoExploracao
from personagem import Personagem

# print("personagem")
# p = Personagem("artur")
# p.exibir_dados()

# print("\nalterando")
# p.nome = "Ana"
# p.exibir_dados()


# m1 = MissaoCombate("cacar", "derrotar inimigos", 20, "gooblin", 5)
# m2 = MissaoColeta("coletar", "juntar recursos", 15, "madeira", 10)
# m3 = MissaoExploracao("explorar", "descobrir area", 25, "caverna", 3.5)

# # Testndo
# for missao in [m1, m2, m3]:
#     print("\n------")
#     missao.iniciar_missao()
#     missao.concluir_missao()
#     missao.exibir_dados()



# p1 = Personagem("jao")
# print("personagem criado...")
# p1.exibir_dados()

# print("-" * 20)

# # criando as missao tudo pra testar a heranca
# m_luta = MissaoCombate("mata rato", "tem q mata os rato do bueiro", 50, "rato", 3)
# m_pegar = MissaoColeta("pega galho", "cata uns graveto na floresta", 20, "graveto", 5)
# m_longe = MissaoExploracao("caverna", "ir ate o final do mapa", 100, "caverna do dragao", 5.5)


# # nao pode termina a missao sem antes comeca 
# print("tentando termina a missao sem iniciar (deve dar erro):")
# m_luta.concluir_missao() 

# print("-" * 20)

# m_luta.iniciar_missao()
# print("matando os bicho no bueiro...")
# m_luta.concluir_missao()

# print("\n-- status final da missao de combate ---")
# m_luta.exibir_dados()

# print("\n--- testando a de coleta agora --")
# m_pegar.iniciar_missao()
# m_pegar.exibir_dados()

# print("\n--- testando a de exploracao --")
# m_longe.iniciar_missao()
# m_longe.exibir_dados()

#######atividade 22/04 testes
p = Personagem("Artur")

m1 = MissaoColeta("Madeira", "Pegar 10", 50, "Graveto", 10)
m2 = MissaoCombate("Ratos", "Matar 5", 30, "Rato", 5)

p.add_missao(m1)
p.add_missao(m2)

print("\n-- teste --")
p.concluir_missao(m1, 15)
p.concluir_missao(m2, 2)

print("\n" + p.exibir_dados())
