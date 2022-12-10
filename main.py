from pprint import pprint


def dict_collector(file_path):
    with open(file_path, 'r', encoding='utf 8') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                ingredient_name, quantity, measure = file_work.readline().strip().split(' | ')
                list_of_ingridient.append({'ingredient_name': ingredient_name,  'quantity': quantity, 'measure': measure})
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return menu


pprint(dict_collector('dishes.txt'), width=140)


def get_shop_list_by_dishes(dishes, person_count=int):
    menu = dict_collector('dishes.txt')
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*person_count})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {person_count} человек  нам необходимо:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
