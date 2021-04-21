def pole_pos(cars):
    pos_arr = [0] * len(cars)

    for final_pos in range(len(cars)):
        initial_pos = final_pos + cars[final_pos][1]
        if initial_pos < 0 or initial_pos >= len(cars) or pos_arr[initial_pos]:
            return ["-1"]
        pos_arr[initial_pos] = cars[final_pos][0]
    return pos_arr


if __name__ == '__main__':
    outs = []
    while True:
        n = int(input())
        if not n:
            break
        lst = []
        for i in range(n):
            c, p = input().split(" ")
            lst.append([c, int(p)])
        outs.append(pole_pos(lst))

    for out in outs:
        print(" ".join(out))



"""
4
1 0
3 3
2 -1
4 0
4
22 1
9 1
13 0
21 -2
3
19 1
9 -345
17 0
7
2 2
8 0
5 -2
7 1
1 1
9 1
3 -3
0
"""