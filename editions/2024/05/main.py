file_contents = open('editions/2024/05/input.txt').read()

rules, pages = file_contents.split('\n\n')

a = [0, 0]
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=lambda x: -sum(x+'|'+y in rules for y in p))
    a[p!=s] += int(s[len(s)//2])

print(f"Part 1: {a[0]}")
print(f"Part 2: {a[1]}")

# This solution is not mine, see credits below:
# https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0kezt2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
