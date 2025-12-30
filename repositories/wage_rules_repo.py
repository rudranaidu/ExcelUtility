import json

def load_wage_rules(path="data/wage_rules.json"):
    with open(path) as f:
        return json.load(f)

