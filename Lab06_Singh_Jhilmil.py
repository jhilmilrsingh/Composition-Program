class Address:
    
    def __init__(self, street, city, state, zip):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip
        
    def __str__(self):
        return '{:s} {:s} {:s} {:s}'.format(
        self.__street, self.__city,
        self.__state, self.__zip)

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

class Customer:

    def __init__(self, fname, lname, addr):
        self.__first_name = fname
        self.__last_name = lname
        self.__addr = addr
    
    def __str__(self):
        return '{:s} {:s} {:s}'.format(
            self.__first_name,
            self.__last_name,
            self.__addr)

    def get_address(self):
        return self.__addr
 
class Store:

    def __init__(self, storenum):
        self.__storenum = storenum
        self.__customer = list()
        
    def add_customer(self, customer):
        self.__customer.append(customer)

    def get_num_customer(self, given_state = 'ALL'):
        if given_state == 'ALL':
            return len(self.__customer)
        count = 0
        for customer in self.__customer:
            state = customer.get_address().get_state()
            if state == given_state:
                count += 1
        return count
    
def main():

    store = Store(202)

    addr1 = Address('100 Main', 'Sterling', 'VA', '20197')
    cust1 = Customer('John', 'Doe', addr1)
    store.add_customer(cust1)

    addr2 = Address('200 Main', 'Reston', 'VA', '20173')
    cust2 = Customer('Jane', 'Jones', addr2)
    store.add_customer(cust2)

    addr3 = Address('300 Main', 'Herndon', 'NJ', '20189')
    cust3 = Customer('Jane', 'Jones', addr3)
    store.add_customer(cust3)
    
    print('Number of customers in VA:',
        store.get_num_customer('VA'))
    print('Number of students in all states:',
        store.get_num_customer('ALL'))
    print('Number of customers in CA:',
        store.get_num_customer('CA'))
    
main()
