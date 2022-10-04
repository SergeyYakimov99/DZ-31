import csv
import json

DATA_ADS = 'ads.csv'
JSON_ADS = 'ads.json'
DATA_CATEGORIES = 'categories.csv'
JSON_CATEGORIES = 'categories.json'
DATA_LOCATION = 'location.csv'
JSON_LOCATION = 'location.json'
DATA_USER = 'user.csv'
JSON_USER = 'user.json'


def convert_file(csv_file, json_file, model_name):
    """
    конвертируем  файлы из csv в json
    """
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'Id' in row:
                del row['Id']
            else:
                del row['id']
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            if 'author_id' in row:
                row['author'] = int(row['author_id'])
            if 'category_id' in row:
                row['category'] = int(row['category_id'])
            if 'age' in row:
                row['age'] = int(row['age'])
            if 'location_id' in row:
                row['location_id'] = (int(row['location_id']),)

            to_add['fields'] = row
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_file(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
convert_file(DATA_ADS, JSON_ADS, 'ads.ad')
convert_file(DATA_LOCATION, JSON_LOCATION, 'ads.location')
convert_file(DATA_USER, JSON_USER, 'ads.user')
