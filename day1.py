with open('input') as f:
    lines = f.readlines()
ans = []
temp = 0
for i in lines:
    i = i.strip('\n')
    if i == '':
        ans.append(temp)
        temp = 0
    else:
        temp += int(i)
print("part 1 answer:")
print(max(ans))
print("part 2 answer:")
temp = 0
temp += max(ans)
ans.remove(max(ans))
temp += max(ans)
ans.remove(max(ans))
temp += max(ans)
print(temp)