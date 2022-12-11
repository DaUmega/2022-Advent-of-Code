with open('input.txt') as f:
    content = f.read().split('\n')
del content[-1]
def visible_check(content, x, y):
    if x == 0 or y == 0 or x == len(content[0]) - 1 or y == len(content) - 1:
        return 1
    max = int(content[y][x])
    tempx = x
    tempy = y
    while x < len(content[0]) - 1:
        x += 1
        if int(content[y][x]) >= max:
            break
        if x == len(content[0]) - 1:
            return 1
    x = tempx
    while x > 0:
        x -= 1
        if int(content[y][x]) >= max:
            break
        if x == 0:
            return 1
    x = tempx
    while y < len(content) - 1:
        y += 1
        if int(content[y][x]) >= max:
            break
        if y == len(content) - 1:
            return 1
    y = tempy
    while y > 0:
        y -= 1
        if int(content[y][x]) >= max:
            break
        if y == 0:
            return 1
    return 0

def scenic_score(content, x, y):
    ans = 1
    multiply = 0
    max = int(content[y][x])
    tempx = x
    tempy = y
    while x < len(content[0]) - 1:
        x += 1
        multiply += 1
        if int(content[y][x]) >= max or x == len(content[0]) - 1:
            ans = ans * multiply
            multiply = 0
            break
    x = tempx
    while x > 0:
        x -= 1
        multiply += 1
        if int(content[y][x]) >= max or x == 0:
            ans = ans * multiply
            multiply = 0
            break
    x = tempx
    while y < len(content) - 1:
        y += 1
        multiply += 1
        if int(content[y][x]) >= max or y == len(content) - 1:
            ans = ans * multiply
            multiply = 0
            break
    y = tempy
    while y > 0:
        y -= 1
        multiply += 1
        if int(content[y][x]) >= max or y == 0:
            ans = ans * multiply
            break
    return ans

ans1 = 0
ans2 = 0
y = 0
while y < len(content):
    x = 0
    while x < len(content[0]):
        ans1 += visible_check(content, x, y)
        ans2 = max(ans2, scenic_score(content, x, y))
        x += 1
    y += 1
print(f'part 1: {ans1}')
print(f'part 2: {ans2}')