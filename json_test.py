import json

#x='{"name":"Alex","age":30,"city":"New York"}'
#y= json.loads(x)
x={"name":"Alex","age":30,"city":"New York"}
y= json.dumps(x,indent=4,separators=(".","="),sort_keys=True)
print(y)