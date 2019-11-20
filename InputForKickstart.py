# input code for kickstart
input_string = """2
3
5 1 2
6
1 3 3 2 2 15"""
input_list = input_string.split('\n')


def input():
    if input_list:
        return input_list.pop(0)


if __name__ == "main":
    T = int(input())
    for x in range(1, T + 1):
        N = int(input())
        A = map(int, input().split())
        h = 0
        y = ""
        citations = [0] * (N + 1)
        new_citations = 0
        for A_i in A:
            if A_i > h:
                try:
                    citations[A_i] += 1
                except IndexError:
                    citations[N] += 1
                if new_citations == citations[h]:
                    h += 1
                    new_citations = 0
                else:
                    new_citations += 1
            y += ' ' + str(h)
        print("Case #{}:{}".format(x, y), flush=True)
