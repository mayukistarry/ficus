from ficus.status import Status, Statuses
from ficus.order import Order
from ficus.client import Client

def test_order_and_client():
    tmp_array = []
    tmp_array.append(Status('a', 'apple', 0.8))
    tmp_array.append(Status('a', 'not apple', 0.2))
    tmp_array.append(Status('b', 'banana', 0.6))
    tmp_array.append(Status('b', 'not banana', 0.4))
    statuses = Statuses(tmp_array)
    client = Client()
    client.set_status(statuses)
    order = Order(3)
    client.set_order(order)
    for key in client.items.keys():
        print(key)
        for item in client.items[key]:
            print(item.value)