def f(s):

    r = s[:0]

    for i in range(len(s)):

        if s[:i]<s[i:]:

            r += s[:i]

        else:
            r += s[i:]
    return r

print(f("luidi"))