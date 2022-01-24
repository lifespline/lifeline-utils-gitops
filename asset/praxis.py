import json
import os 
root = os.path.dirname(os.path.realpath(__file__))

with open(f'{root}/score.json') as file:
    score = json.load(file)["score"]
    
with open(f'{root}/description.json') as file:
    description = json.load(file)['description']

with open(f'{root}/problem_statements.json') as file:
    problem_statements = json.load(file)
