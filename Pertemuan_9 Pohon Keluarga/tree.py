class CoupleNode:
    def __init__(self, married):
        self.married = married
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Membuat pohon keluarga
grandparents = CoupleNode("Killab and Fatimah")
parents = CoupleNode("Zuhroh and Qushay")
children1 = CoupleNode("Abdi and Atikah")
children2 = CoupleNode("Hasim and Salma")
grandson1 = CoupleNode("Abdul and Siti")

grandparents.add_child(parents)
parents.add_child(children1)
parents.add_child(children2)
children1.add_child(grandson1)

# Menampilkan pohon keluarga
def display_family_tree(node, level=0):
    print("    " * level + "|__ " + node.married)
    for child in node.children:
        display_family_tree(child, level + 1)

print("Family Tree:")
display_family_tree(grandparents)
