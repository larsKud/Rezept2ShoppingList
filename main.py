import database_api as db
# input: liste von list[(ingredient listen, portion count)]
# output liste[items, quantity]

def combine_ingredient_lists(input: list):
    items_list = {}
    # go through all ingredient lists multiply by portions and add to items_list
    for ingredient_list, portion_count in input:
        for item, quantity in ingredient_list:
            if item not in items_list.keys():
                 items_list[item] = quantity * portion_count
                 continue
            items_list[item] = items_list[item] + quantity*portion_count
    return items_list

def sort_by_category(shopping_dict: dict)-> list:
    categories = db.get_categories_in_order()
    shopping_list = []
    for item in shopping_dict.keys():
        ind = categories[item]
    pass

if __name__ == "__main__":
    in1 = [
        ('Karotten', 1000),
        ('Couscous', 300),
        ('Knoblauch', 1)
    ]
    in2 = [
        ('Sojagranulat', 100),
        ('Knoblauch', 2)
    ]

    res = combine_ingredient_lists([(in1, 2), (in2, 1)])
    print(res)