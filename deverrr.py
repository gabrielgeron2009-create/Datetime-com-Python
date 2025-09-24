from datetime import datetime

data_devolucao_str = input("Digite a data de devolução (dd/mm/aaaa): ")


data_devolucao = datetime.strptime(data_devolucao_str, "%d/%m/%Y").date()
data_hoje = datetime.now().date()


diferenca = (data_devolucao - data_hoje).days


if diferenca > 0:
    print(f"Você tem {diferenca} dias para devolver.")
elif diferenca < 0:
    print(f"O livro está atrasado em {abs(diferenca)} dias!")
else:
    print("O livro vence hoje!")
