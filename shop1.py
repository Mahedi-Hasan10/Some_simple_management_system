class Shop:
    cart = []  # class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehjabeen = Shop('Mehjabben')
mehjabeen.add_to_cart('Watch')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)


Nisho = Shop('Nisho')
Nisho.add_to_cart('Begun')
Nisho.add_to_cart('Kola')
print(Nisho.cart)
