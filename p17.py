__author__ = 'guardian'

first = {
0: 0,
1: 3,
2: 3,
3: 5,
4: 4,
5: 4,
6: 3,
7: 5,
8: 5,
9: 4,
10: 3,
11: 6,
12: 6,
13: 8,
14: 8,
15: 7,
16: 7,
17: 9,
18: 8,
19: 8
}
second = {
0: 0,
2: 6,
3: 6,
4: 5,
5: 5,
6: 5,
7: 7,
8: 6,
9: 6
}
hundred_c = 7
and_c = 3

count = 11  # one thousand
for i in range(1, 1000):
    if i < 20:
        count += first[i]
    elif i < 100:
        s = int(str(i)[0])
        f = int(str(i)[1])
        count += second[s] + first[f]
    elif i > 99:
        h = int(str(i)[0])
        if i % 100 == 0:
            count += first[h] + hundred_c
        else:
            s = int(str(i)[1])
            f = int(str(i)[2])
            if s < 2:
                count += first[h] + hundred_c + and_c + first[s * 10 + f]
            else:
                count += first[h] + hundred_c + and_c + second[s] + first[f]
print(count)