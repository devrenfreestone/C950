class Package:
    def __init__(self, id, address, status, deliveryDeadline=None, deliveryTime=None, specialNotes=None):
        self.id = id
        self.address = address
        self.status = status
        self.deliverDeadline = deliveryDeadline
        self.deliveryTime = deliveryTime
        self.specialNotes = specialNotes

