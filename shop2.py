class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


Kudus = Shop('Kudus')
Kudus.add_to_cart('Mula')
Kudus.add_to_cart('Dharos')
print(Kudus.cart)

mokhles = Shop('Mokhles')
mokhles.add_to_cart('iPhone')
mokhles.add_to_cart('Samsung')
print(mokhles.cart)
