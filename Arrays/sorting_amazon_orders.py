from queue import PriorityQueue, Queue


class Prime_Order:
    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix

    def __lt__(self, other):
        if self.suffix < other.suffix:
            return 1
        elif self.suffix == other.suffix:
            if self.prefix < other.prefix:
                return 1
            else:
                return 0


def sortOrders(orderList):
    prime_orders = PriorityQueue()
    regular_orders = Queue()

    for order in orderList:
        check = order.split()
        if check[1].isalpha():
            prime_order = Prime_Order(check[0], check[1:])
            prime_orders.put(prime_order)
        else:
            regular_orders.put(order)

    sortedOrdersList = []

    while not prime_orders.empty():
        prime_order = prime_orders.get()
        order_to_append = prime_order.prefix + \
            ' ' + ' '.join(prime_order.suffix)
        sortedOrdersList.append(order_to_append)

    while not regular_orders.empty():
        sortedOrdersList.append(regular_orders.get())

    return sortedOrdersList


orderList = ["t2 13 121 98",
             "r1 box ape bit",
             "b4 xi me nu",
             "br8 eat nim did",
             "w1 has uni gry",
             "f3 52 54 31"]

print(sortOrders(orderList))
