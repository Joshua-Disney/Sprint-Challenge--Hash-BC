#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    answer = []

    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        print(f"inserted key: {tickets[i].source} value: {tickets[i].destination} into hashtable")
    
    while len(answer) < length:
        if len(answer) < 1:
            answer.append(hash_table_retrieve(hashtable, "NONE"))
        else:
            answer.append(hash_table_retrieve(hashtable, answer[-1]))
    print(f"answer: {answer}")

    return answer
