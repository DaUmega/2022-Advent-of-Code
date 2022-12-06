with open("input.txt") as f:
    data = f.read().split('\n')
arr = ['' for x in range(9)]
for i in range(9):
    for j in range(len(data[8])):
        if data[i][j].isalpha():
            arr[int(data[8][j]) - 1] += data[i][j]
arr2 = arr[:]
with open("input2.txt") as f:
    data2 = f.read().split('\n')
for i in data2:
    i = i.replace('move', '').replace('from', '').replace('to', '').replace('\n', '').split()
    for x in range(3):
        i[x] = int(i[x])
    for x in range(i[0]):
        arr[i[2] - 1] = arr[i[1] - 1][0] + arr[i[2] - 1]
        arr[i[1] - 1] = arr[i[1] - 1][1:]
    arr2[i[2] - 1] = arr2[i[1] - 1][:i[0]] + arr2[i[2] - 1]
    arr2[i[1] - 1] = arr2[i[1] - 1][i[0]:]
print('part 1:')
print(arr)
print('part 2:')
print(arr2)