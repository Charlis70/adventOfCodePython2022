# 1. extract data from file
result = []
with open('input.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n\n')

    for group in lines:
        group = group.split('\n')
        sum = 0
        for elem in group:
            sum += int(elem)
        result.append(sum)
print(result)

# get the index of the highest value of the list
max_index = result.index(max(result))
print(max_index)
print(result[max_index])