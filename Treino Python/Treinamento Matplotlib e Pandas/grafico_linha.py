import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 5, 9, 3, 8]
y2 = [3, 4, 2, 1, 9]

plt.scatter(x, y1, label="Relação entre X e Y1", 
            color='red', linestyle='--', marker='o', s=100)
plt.scatter(x, y2, label="Relação entre X e Y2", 
            color='gray', linestyle='-', marker='x')
plt.fill_between(x, y1, y2, color='orange')

plt.title("Gráfico de linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()