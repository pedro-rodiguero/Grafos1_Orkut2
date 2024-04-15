import json
import networkx as nx
import matplotlib.pyplot as plt


class User:
    def __init__(self, course, registration, email):
        self.course = course
        self.registration = int(registration)
        self.email = email


# Lê o arquivo JSON
with open("new_list.json", "r") as file:
    friends = json.load(file)

# Cria um objeto User para cada amigo na lista
users = [User(**friend) for friend in friends]

# Cria um grafo
G = nx.Graph()

# Adiciona cada usuário ao grafo
for user in users:
    G.add_node(user)

# Cria uma aresta entre cada par de usuários cuja diferença de "registration" seja a menor possível
for i in range(len(users)):
    for j in range(i + 1, len(users)):
        G.add_edge(
            users[i],
            users[j],
            weight=abs(users[i].registration - users[j].registration),
        )

# Ordena os usuários por "registration" em ordem decrescente
users.sort(key=lambda x: x.registration, reverse=True)

# Desenha o grafo
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=6)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
