    with open(r'Modules'+a) as f:
        obj = json.load(f)
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])