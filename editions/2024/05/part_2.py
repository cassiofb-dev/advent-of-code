# Not mine, credits: https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0kezt2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

filename = 'editions/2024/05/input.txt'

rules, pages = open(filename).read().split('\n\n')

a = [0, 0]
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=lambda x: -sum(x+'|'+y in rules for y in p))
    a[p!=s] += int(s[len(s)//2])

print(*a)
