counter = 0
for x1 in 'БАЛОН':
    for x2 in 'БАЛОН':
        for x3 in 'БАЛОН':
            for x4 in 'БАЛОН':
                for x5 in 'БАЛОН':
                    for x6 in 'БАЛОН':
                        s = x1+x2+x3+x4+x5+x6
                        if s.count('А') <= 1 and s.count('О') <=1:
                            counter += 1
print(counter)