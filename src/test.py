favorite_languiges = {
    'Mike': 'python',
    'Jake': 'c',
    'Steve': 'ruby',
    'Alex': 'c#',
    'Max': 'ruby',
    'James': ['delphi', 'python']
}
langs = []
for lang in favorite_languiges.values():
    if type(lang) == list:
        langs += lang
    else:
        langs.append(lang)
print(set(langs))