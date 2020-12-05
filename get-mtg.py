import json, urllib.request

"""
Get Commander legal cards ordered by price (descending). This should have enough assorted cards with no alphabetical
relation or uniform borders. These are the first three page results, 525 cards (175*3). The testing dataset is fairly 
intuitive, as you could simply make this same request but order the price in an ascending fashion
"""

getfiles = False
parsefiles = True
start = 1
end = 60

if getfiles:
    for page in range(start, end):
        url = f"https://api.scryfall.com/cards/search?format=json&q=legal%3Avintage&include_extras=false&include_multilingual=false&order=usd&page={page}&unique=cards&order=usd&dir=desc"
        request = urllib.request.urlopen(url)
        data = json.load(request)
        # save to file
        with open(f'json_data/mtg_data_{page}.json', 'w') as fp:
            json.dump(data, fp)
        # next page for next iteration
        url = data['next_page']

if parsefiles:
    image_urls = []
    for i in range(start, end):
        with open(f'json_data/mtg_data_{i}.json') as json_file:
            data = json.load(json_file)
            for j in range(175):
                try:
                    image_urls.append(data['data'][j]['image_uris']['normal'])
                except:
                    pass
    itr = 0
    for i in image_urls:
        urllib.request.urlretrieve(i, f"img/mtg_{itr}.jpg")
        itr += 1

