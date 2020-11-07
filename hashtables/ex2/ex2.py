#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    1. create an empty hash table and an empty list 'route'
    2. loop through tickets and store the source and destination
    as a key/value pair in the hash table
    3. lookup the flight with source 'NONE'
    4. starting with this flight, push the destination into 'route',
    then find each subsequent flight, pushing the destination into 'route'
    each time
    5. once you reach the flight with destination 'NONE', you're finished
    """
    ht = {}
    route = []
    
    for t in tickets:
        ht[t.source] = t.destination
        
    location = ht['NONE']
    while location != 'NONE':
        route.append(location)
        location = ht[location]
    
    route.append('NONE') # necessary to pass tests

    return route
