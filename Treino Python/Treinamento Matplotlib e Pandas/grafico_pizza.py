import matplotlib.pyplot as plt

categorias = ['Z', 'Y', 'X']
valores = [26, 14, 3]

plt.pie(valores, labels=categorias, autopct="%1.1f%%")
plt.show()