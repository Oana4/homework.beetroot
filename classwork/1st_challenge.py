t = 'sshh'
s = 'bbnn'

related_chars = {}

if len(t) != len(s):
    print('The strings are of different lengths.')
else:
    for i in range(len(t)):
        if t[i] not in related_chars:
            related_chars[t[i]] = s[i]
        else:
            if related_chars[t[i]] == s[i]:
                print('It\'s ok.\n')
                continue
            else:
                print('The rules of the universe are broken!')
                break