import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("dados.csv")

dias = dados['Date']
petro = dados['PETR4']
itau = dados['ITUB4']

# petro.diff() (Ver variação)

# Gráfico Principal
""" 
fig = plt.figure(figsize=(12, 8))

plt.plot(dias, petro, label='Petro', color='green', linestyle='--', marker='.')
plt.plot(dias, itau, label='Itaú', color='orange', linestyle='--', marker='.')

plt.title('Cotação - 2025/1')
plt.xlabel('Dias')
plt.ylabel('Valor da ação (R$)')
plt.legend()
plt.xticks(ticks=dias[::20])
plt.show()
"""
# Subgráficos
""" 
plt.style.use('dark_background')

fig, (ax_cima, ax_baixo) = plt.subplots(figsize=(12, 8), nrows=2, sharex=True)

ax_cima.hist(petro.diff(), label='Petro', color='green', bins=50)
ax_cima.axvline(petro.diff().mean(), color='white', linestyle='--', linewidth=4)
ax_cima.set_xlabel('Variação (R$)')
ax_cima.set_ylabel('Frequência')
ax_cima.grid('on')

ax_baixo.hist(itau.diff(), label='Itaú', color='orange', bins=50)
ax_baixo.axvline(itau.diff().mean(), color='white', linestyle='--', linewidth=4)
ax_baixo.set_xlabel('Variação (R$)')
ax_baixo.set_ylabel('Frequência')
ax_baixo.grid('on')

fig.suptitle('Variação diária - 2025/1')
fig.legend()
plt.show()  
"""

# Resultado Final

plt.style.use('dark_background')

fig = plt.figure(figsize=(12, 8))

grid = fig.add_gridspec(2, 2)

ax_linha = fig.add_subplot(grid[0, :])
ax_hist_1 = fig.add_subplot(grid[1, 0])
ax_hist_2 = fig.add_subplot(grid[1, 1])

# Gráfico principal
ax_linha.plot(dias, petro, label='Petro', color='green', linestyle='--', marker='.')
ax_linha.plot(dias, itau, label='Itaú', color='orange', linestyle='--', marker='.')

ax_linha.set_title('Cotação - 2025/1')
ax_linha.set_xlabel('Dias')
ax_linha.set_ylabel('Valor da ação (R$)')
ax_linha.set_xticks(ticks=dias[::20])
ax_linha.grid('on')

# Subgráficos
ax_hist_1.hist(petro.diff(), color='green', bins=50)
ax_hist_1.axvline(petro.diff().mean(), color='white', linestyle='--', linewidth=4)
ax_hist_1.set_xlabel('Variação (R$)')
ax_hist_1.set_ylabel('Frequência')
ax_hist_1.grid('on')

ax_hist_2.hist(itau.diff(), color='orange', bins=50)
ax_hist_2.axvline(itau.diff().mean(), color='white', linestyle='--', linewidth=4)
ax_hist_2.set_xlabel('Variação (R$)')
ax_hist_2.set_ylabel('Frequência')
ax_hist_2.grid('on')

fig.suptitle('Análise de ações')
fig.legend()
fig.tight_layout()

# plt.savefig('figura.png') (Tipo tirar dar um printscreen)

plt.show() 
