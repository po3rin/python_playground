from dnorm_j import DNorm

model = DNorm.from_pretrained()
result = model.normalize('水いぼ')
print(result)
result = model.normalize('胃ガン')
print(result)
result = model.normalize('乳がん')
print(result)
result = model.normalize('子宮頸管ポリープ')
print(result)
result = model.normalize('腟カンジダ症')
print(result)
