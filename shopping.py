class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price']*item['quantity']
        print(f'Total price is : {total}')
        if amount < total:
            extra = total - amount
            print(f'You have to pay {extra} taka more')
        else:
            extra = amount-total
            print(f'take your extra {extra} money')


swapan = Shopping('Alen Sopon')
swapan.add_to_cart('Alu', 30, 6)
swapan.add_to_cart('begun', 80, 5)
swapan.add_to_cart('vagetable', 20, 2)
swapan.checkout(500)
