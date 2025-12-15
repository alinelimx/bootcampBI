import matplotlib.pyplot as plt

dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
valores_vendas = [152, 224, 267, 395, 458, 500, 110]

plt.title('Vendas Semanais de Produtos')
plt.xlabel('Dias da Semana')
plt.ylabel('Número de Vendas')

plt.plot(dias_semana, valores_vendas, color = 'purple', marker = 'o')
plt.grid(True, alpha=0.3)
plt.show()