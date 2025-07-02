class Customer:
    def __init__(self, cid, fname, lname, email, phone, address):
        self.customer_id = cid
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone = phone
        self.address = address

    def print_info(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}")
