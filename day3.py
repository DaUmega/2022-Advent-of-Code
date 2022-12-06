with open('input') as f:
    lines = f.readlines()
ans = 0
for i in lines:
    i = i.strip('\n')
    part1 = set(i[:len(i)//2])
    part2 = set(i[len(i)//2:])
    for letter in part1:
        if letter in part2 and letter.isupper():
            ans += ord(letter) - ord('A') + 27
        elif letter in part2 and letter.islower():
            ans += ord(letter) - ord('a') + 1
print('part 1:')
print(ans)
n = 0
ans = 0
while(n < len(lines)):
    set1 = set(lines[n])
    set2 = set(lines[n + 1])
    set3 = set(lines[n + 2])
    for letter in set1:
        if letter in set2 and letter in set3 and letter.isupper():
            ans += ord(letter) - ord('A') + 27
        elif letter in set2 and letter in set3 and letter.islower():
            ans += ord(letter) - ord('a') + 1
    n += 3
print('part 2:')
print(ans)