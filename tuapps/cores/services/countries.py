from typing import List, Tuple

from django.utils.translation import gettext_lazy as _

import requests


def get_countries() -> List[Tuple[str, str]]:
    try:
        api = requests.get('https://restcountries.eu/rest/v2/all')
        json = api.json()
        countries = []
        for country in json:
            countries.append((country['alpha3Code'], country['name']))
        return countries
    except requests.exceptions.ConnectionError:
        return []
