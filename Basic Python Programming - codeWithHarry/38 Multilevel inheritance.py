class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 9
    def isDance(self):
        return f"Yes! I dance {self.dance} no. of times"

class GrandSon(Son):
    dance = 6
    def isDance(self):
        return f"Yes I dance very awesomely {self.dance} no. of times"

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.dance)
print(harry.basketball)