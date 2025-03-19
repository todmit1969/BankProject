'#-*- coding: utf-8 -*-'
from collections import Counter
from itertools import chain


def get_categories(transactions):
    print(transactions)
    categories = list(map(lambda d: d.get("description"), filter(lambda d: "description" in d, transactions)))

    unique_categories = set(categories)

    return list(unique_categories)

