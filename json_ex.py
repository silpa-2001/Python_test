import json

x='{"name":"Silpa", "age":"22"}'
y=json.loads(x)
print(y)
print(type(y))
z=json.dumps(y)
print(z)
print(type(z))