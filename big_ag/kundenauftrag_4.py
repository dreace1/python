import matplotlib.pyplot as plt

fig, ax = plt.subplots()

items = ['Zement', 'Warnweste', 'Rote Ampeln', 'Rasen']
counts = [30, 10, 60, 90]
bar_labels = ['grey', 'orange', '_red', 'green']
bar_colors = ['tab:grey', 'tab:orange', 'tab:red', 'tab:green']

ax.bar(items, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('item supply')
ax.set_title('Item supply by kind and color')
ax.legend(title='Item color')

plt.gcf()
plt.savefig('Kundenauftrag4.png',dpi=30)
plt.show()