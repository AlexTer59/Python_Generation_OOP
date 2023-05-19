class Postman:
    def __init__(self, delivery_data=[]):
        self.delivery_data = delivery_data

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        return list(dict.fromkeys([i[1] for i in self.delivery_data if i[0] == street]))

    def get_flats_for_house(self, street, house):
        return list(
            dict.fromkeys([i[2] for i in (filter(lambda x: x[0] == street and x[1] == house, self.delivery_data))]))


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
