
class PartyAnimal :
    x = 0

# self == this. en java
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
