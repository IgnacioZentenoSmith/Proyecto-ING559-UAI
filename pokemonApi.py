# POKEMON API
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type

## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

# Import module for creating folders
import os

def downloadImage(image_url, filename):
    # Open the url image, set stream to True, this will return the stream content.
    req = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if req.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        req.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(req.raw, f)
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')


def renameFile(filename, newName):
    path = "C:/Users/izent/" + filename
    newFileName = os.path.join(os.path.dirname(path), newName)
    os.rename(path, newFileName)

# Get all Sets
def getCardsFromSets(pokemonSets):
    i = 0
    for pokemonSet in pokemonSets:
        # Get 20 cards in this set or all if less than 20 in the set
        if pokemonSet.total_cards < 20:
            pokemonCards = Card.where(set = pokemonSet.name)
        else:
            pokemonCards = Card.where(set = pokemonSet.name, pageSize = 20)
        # Get filename and image_url for every card obtained
        for pokemonCard in pokemonCards:
            filename = pokemonCard.image_url_hi_res.split("/")[-1]
            image_url = pokemonCard.image_url_hi_res
            downloadImage(image_url, filename)

            newName = str(i) + '_' + pokemonSet.name + '_' + pokemonCard.name + '.png'
            renameFile(filename, newName)
            i += 1

getCardsFromSets(Set.all())
    