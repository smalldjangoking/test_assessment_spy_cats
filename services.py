import requests

catsBreeds = 'https://api.thecatapi.com/v1/breeds'


async def breeds_validation(cat_breed: str) -> bool:
    response = requests.get(catsBreeds)

    if response.status_code == 200:
        breeds = response.json()

        for breed in breeds:
            if breed['name'].lower() == cat_breed.lower():
                return True
    return False