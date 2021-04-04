from collections import defaultdict


def find_demo():
    test_grades = defaultdict(list)
    test_grades["Alice"].append(99)
    test_grades["Alice"].append(85)
    test_grades["Bob"].append(79)

    print("Alice Grades:", test_grades["Alice"])
    print("Bob Grades:", test_grades["Bob"])


def insert_demo():
    dictionary = defaultdict(list)
    dictionary["type"].append("a category of people or things having common characteristics")
    dictionary["type"].append("write (something) on a typewriter or computer by pressing the keys")
    dictionary["fall"].append("an act of falling or collapsing; a sudden uncontrollable descent")
    dictionary["fall"].append("autumn")

    print(dictionary.items())


def remove_demo():
    shopping_cart = defaultdict(list)
    shopping_cart["person1@example.com"].append("Toothbrush")
    shopping_cart["person1@example.com"].append("Sneakers")
    shopping_cart["person2@example.com"].append("Headphones")
    print(shopping_cart.items())

    shopping_cart["person1@example.com"].remove("Toothbrush")
    print(shopping_cart.items())

    shopping_cart.pop("person2@example.com")
    print(shopping_cart.items())


def keys_demo():
    people = defaultdict(list)
    people["Alice"].append("alice@example.com")
    people["Alice"].append("alice@work.com")
    people["Bob"].append("bob@company.com")
    print(people.keys())


def values_demo():
    people = defaultdict(list)
    people["Alice"].append("alice@example.com")
    people["Alice"].append("alice@work.com")
    people["Bob"].append("bob@company.com")
    print(people.values())


if __name__ == "__main__":
    find_demo()
    insert_demo()
    remove_demo()
    keys_demo()
    values_demo()
