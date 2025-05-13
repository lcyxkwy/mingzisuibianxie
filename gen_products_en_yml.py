import yaml
from googletrans import Translator

translator = Translator()

with open('_data/products.yml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

cats_en = {}
for cat, items in data.items():
    cats_en[cat] = []
    for item in items:
        name = item.get('name', '')
        desc = item.get('desc', '')
        # 翻译
        try:
            name_en = translator.translate(name, src='zh-cn', dest='en').text if name else ''
        except Exception:
            name_en = name
        try:
            desc_en = translator.translate(desc, src='zh-cn', dest='en').text if desc else ''
        except Exception:
            desc_en = desc
        item_en = dict(item)
        item_en['name'] = name_en
        item_en['desc'] = desc_en
        # image 字段直接用商品详情页链接
        item_en['image'] = item.get('image') or item.get('img')
        cats_en[cat].append(item_en)

with open('_data/products_en.yml', 'w', encoding='utf-8') as f:
    yaml.dump(cats_en, f, allow_unicode=True) 