import re

hey = 'carol@gmail.com.br'

# Findall
result = re.findall(r"(@.{1,8}\.)", hey)
print(result)

# Search
result = re.search(r"(@.{1,8}\.)", hey)
print(result)

# Split
result = re.split(r"(@.{1,8}\.)", hey)
print(result)

# Sub
result = re.sub(r"(@.{1,8}\.)", '@yahoo.', hey)
print(result)
