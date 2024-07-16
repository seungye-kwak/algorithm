num = int(input())
start = 1
layer = 1

while num > start :
    start += layer*6
    layer += 1
    
print(layer)