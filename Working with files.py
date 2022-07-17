from pprint import pprint

# Задача №1

file_name = "recipe.txt"


def file_reader(file_name):
    with open(file_name, encoding='utf-8') as file_obj:
        global cookbook
        cookbook = {}
        for line in file_obj:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline().split(' | ')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2].strip()})
            cookbook[dish_name] = ingredients
            file_obj.readline()
    return cookbook


dishes = file_reader(file_name)
pprint(dishes)
print()


# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                          'quantity': (ingredient['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в поваренной книге')
    return result


dishes_list = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
pprint(dishes_list)
print()


# Задача №3


import os

dir_name = "venv"
catalog_name = "Files_task_3"
merged_file_name = "merged.txt"

base_path = os.getcwd()
dir_path = os.path.join(base_path, dir_name)
catalog_path = os.path.join(base_path, dir_name, catalog_name)
merged_file_name_path = os.path.join(base_path, merged_file_name)


def process_files(base_path, dir_path, catalog_path):
    files = os.listdir(catalog_path)
    files_data = {}
    for filename in files:
        if ".txt" in filename:
            with open(os.path.join(catalog_path, filename), 'r', encoding='utf-8') as read_file:
                file_lines = read_file.readlines()
                count = len(file_lines)
                files_data[filename] = (count, file_lines)
        else:
            print('Нет файлов для обработки')

    sorted_files_data = sorted(files_data.items(), key=count)
        with open(os.path.join(dir_path, merged_file_name), 'w', encoding='utf-8') as write_file:
            write_file.write('sorted_files_data')

process_files(base_path, dir_path, catalog_path)