# Declaração
nome_completo = "Gabriel Casemiro"

nome_completo_aspas = """Gabriel
Casemiro
"""

nome_completo_quebra = "Gabriel \
Casemiro"

nome = "Gabriel"
sobrenome = "Casemiro"

# Formatação
print("Nome completo (1ª forma):", nome_completo)
print("Nome completo (2ª forma):" + nome_completo)
print("Nome completo (3ª forma):" + "Gabriel" + "Casemiro")
print("Nome completo (4ª forma):" + "Gabriel", "Casemiro")
print("Nome completo (5ª forma):", nome_completo_aspas)
print("Nome completo (6ª forma):", nome_completo_quebra)
print("Nome completo (7ª forma): %s" % nome_completo)
print("Nome completo (8ª forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª forma): {nome} {sobrenome}")
print("Nome completo (10ª forma): {} {}".format(sobrenome, nome))