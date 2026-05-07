from missoes import Missao, MissaoExploracao
from personagem import Personagem

print("Cadastro de Personagem")
p = Personagem("Malibu")
print(p.exibir_dados())

missao_exploracao = MissaoExploracao("Conquistar o território IFSUL", "Conquistar novo território", 50, "IFSUL", 10)

print("\nCadastro de Missão")
print(missao_exploracao.exibir_dados())

print("\nvinculando Missão ao personagem")
p.add_missao(missao_exploracao)
print(p.exibir_dados())

print("\nConcluindo Missão do personagem")
p.concluir_missao(missao_exploracao, 5)
print(p.exibir_dados())