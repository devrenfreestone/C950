class Package:
    def __init__(self, id, address, city, zip, weight, status, truck, deliveryDeadline=None, deliveryTime=None, specialNotes=None, addressId=0):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.weight = weight
        self.status = status
        self.truck = truck
        self.deliverDeadline = deliveryDeadline
        self.deliveryTime = deliveryTime
        self.specialNotes = specialNotes
        self.addressId = addressId

    # 'Getter' functions below allow values from a package to easily be passed to other functions for comparison,
    # searching, etc.
    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_zip(self):
        return self.zip

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    def get_truck(self):
        return self.truck

    def get_deliveryDeadline(self):
        return self.deliverDeadline
    def get_deliveryTime(self):
        return self.deliveryTime

    def get_specialNotes(self):
        return self.specialNotes

    def get_addressId(self):
        return self.addressId
