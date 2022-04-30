class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return tota

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return f"{store.name} - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {store.stock_price()}"


st=Store("AtoZ")
st1=Store("Amazon")
st.add_item('abc',10)
st.add_item('afc',14)

print(Store.franchise(st))
print(Store.franchise(st1))

print(Store.store_details(st))
print(Store.store_details(st1))

