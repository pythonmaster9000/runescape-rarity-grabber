import requests


def rarity_sucker(name_of_monster: str):

    name_of_monster = name_of_monster.capitalize()

    url = f'https://oldschool.runescape.wiki/w/{name_of_monster}'

    page = requests.get(url)

    splithtml = page.text.split('style="text-align:center"><td class="inventory-image"><a')

    info = {}
    for i in splithtml:
        if f'{name_of_monster} drops' in i:

            info[i.split('title="')[1].split('"')[0].replace('&#39;',"'")] = {}

            info[i.split('title="')[1].split('"')[0].replace('&#39;',"'")]['rarity'] = int(i.split('rarity ')[1].split(' ')[0].replace(',', '').split('/')[0])/ float(i.split('rarity ')[1].split(' ')[0].replace(',', '').split('/')[1]) if 'Always' not in i.split('rarity ')[1].split(' ') else 100

            quantity = range(int(i.split('quantity ')[1].split('"')[0].replace(' (noted)', '')),int(i.split('quantity ')[1].split('"')[0].replace(' (noted)', ''))) if '-' not in i.split('quantity ')[1].split('"')[0] else range(int(i.split('quantity ')[1].split('"')[0].split('-')[0].replace(' (noted)', '')),int(i.split('quantity ')[1].split('"')[0].split('-')[1].replace(' (noted)', '')))

            info[i.split('title="')[1].split('"')[0].replace('&#39;',"'")]['quantity'] = quantity
    print(info)


rarity_sucker('hydra')

