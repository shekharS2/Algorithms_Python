#Dynamic Programming Solution

cat = [-100] * 200

def catalan(n):
    if n <= 1:
        cat[n] = 1
        return cat[n]
    elif cat[n] != -100:
        return cat[n]
    else:
        for i in range(0, n):
            cat[n] = cat[n-1] + catalan(i) * catalan(n-1-i)
        return cat[n]

catalan(100)

print(cat)