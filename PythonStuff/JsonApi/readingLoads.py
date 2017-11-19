import json

stringJson = '{"name": "chhatra", "sex":"Male"}'

jsonAsPython = json.loads(stringJson)
print(jsonAsPython)