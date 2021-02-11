from dnorm_j import DNorm

model = DNorm.from_pretrained()
result = model.normalize('胃がん')
print(result)
