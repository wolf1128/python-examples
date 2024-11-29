# Data Structures



def list_example():
    todos = ["buy milk", "clean house", "go to gym"]
    print("original list: ", todos)
    todos.append("do homework")
    print("list after appending: ", todos)
    todos.pop()
    print("list after popping: ", todos)
    todos.remove("clean house")
    print("list after removing: ", todos)
    todos.reverse()
    print("list after reversing: ", todos)
    todos.sort()
    print("list after sorting: ", todos)
    print("list length: ", len(todos))
    print("list index: ", todos.index("buy milk"))
    todos.append("buy milk")
    print("list count: ", todos.count("buy milk"))
    print("loop way#1")
    for index, todo in enumerate(todos):
        print(f"todo#{index} ", todo)
    print("loop way#2")
    for i in range(len(todos)):
        print(f"todo#{i} ", todos[i])


def tuple_example():
    items = ("item1", "item2", "item3")
    print("original tuple: ", items)
    print("tuple index: ", items.index("item1"))
    print("tuple count: ", items.count("item1"))
    print("loop way#1")
    for index, item in enumerate(items):
        print(f"item#{index} ", item)
    print("loop way#2")
    for i in range(len(items)):
        print(f"item#{i} ", items[i])

def set_example():
    set = {"member1", "member2", "member3"}
    print("original set: ", set)
    set.add("member4")
    print("set after adding: ", set)
    set.remove("member2")
    print("set after removing: ", set)
    print("set length: ", len(set))
    print("loop")
    for member in set:
        print("member: ", member) # NOTE: sets in Python are unordered collections, so you cannot access elements by index.

def dictionary_example():
    dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    print("original dictionary: ", dict)
    dict["key4"] = "value4"
    print("dictionary after adding: ", dict)
    del dict["key2"]
    print("dictionary after removing: ", dict)
    print("dictionary length: ", len(dict))
    print("loop")
    for key, value in dict.items():
        print(f"key: {key}, value: {value}")



if __name__ == "__main__":
    list_example()
    tuple_example()
    set_example()
    dictionary_example()