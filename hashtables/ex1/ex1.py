#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = []

    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)
        print(f"inserted {i} with the key {weights[i]}")

    for i in range(length - 1, -1, -1):
        # retrieve the highest index's key
        value = hash_table_retrieve(ht, weights[i])
        # add key value to answer
        answer.append(value)
        # remove the key
        hash_table_remove(ht, weights[i])
        # limit - key = thing
        search = limit - weights[i]
        # if ht contains key of thing:
        if limit/2 == search:
            answer.append(0)
            break

        elif hash_table_retrieve(ht, search):
        #     retrive thing
            second_value = hash_table_retrieve(ht, search)
        #     add thing value to answer
            answer.append(second_value)
            break
        # else remove key value from answer
        else:
            answer.remove(answer[0])
    print(f"answer: {answer}")


    if len(answer) > 0:
        return answer
    else:
        return None





def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + "" + answer[1]))
    else:
        print("None")
