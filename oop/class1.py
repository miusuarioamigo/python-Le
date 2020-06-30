class pp:
    def __init__(self, nom, smt):
        self.nom = nom
        self.om = 4
        self.something = smt


x = pp("Augusto","something")
y = pp("Rivwox", "molecule")

print (x.nom, y.nom)
print (x.om)
print (y.something)