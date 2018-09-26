'''
To count the number of 3-uniform words representing the cycle graphs.
It is known that this number is >= 4n.

Author: Ameya Daigavane
'''

n = 4
counts = [0] + [3 for i in range(1, n + 1)]
string_array = [0] * (3 * n)
wordcount = 0
validwordcount = 0

# prints string_array as a string
def print_string_array():
    print(''.join(str(i) for i in string_array))

# checks the 3 uniform word represented by string_array if it represents the cycle graph
def check_word():
    for i in range(1, n + 1):
        # edges from i to ((i % n) + 1)
        v1 = i
        v2 = 1 + (i % n)

        # get positions of v1 and v2
        pos1 = []
        pos2 = []
        for j in range(0, 3*n):
            if string_array[j] == v1:
                pos1.append(j)

            if string_array[j] == v2:
                pos2.append(j)

        # check if alternate
        if (pos1[0] < pos2[0] < pos1[1] < pos2[1] < pos1[2] < pos2[2]) or (pos2[0] < pos1[0] < pos2[1] < pos1[1] < pos2[2] < pos1[2]):
            continue
        else:
            return False

    # fill positions array
    positions = [[] for _ in range(0, n + 1)]
    for i in range(0, 3*n):
        positions[string_array[i]].append(i)

    # check for other edges
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j != i and j != 1 + (i % n) and i != 1 + (j % n):
                pos1 = positions[i]
                pos2 = positions[j]

                if (pos1[0] < pos2[0] < pos1[1] < pos2[1] < pos1[2] < pos2[2]) or (pos2[0] < pos1[0] < pos2[1] < pos1[1] < pos2[2] < pos1[2]):
                    return False

    return True


def count(currpos):
    if currpos == 3*n:
        global wordcount, validwordcount
        wordcount += 1

        if check_word():
            # valid word
            print_string_array()
            validwordcount += 1

    else:
        for i in range(1, n + 1):
            if counts[i] > 0:
                # set this character to i
                string_array[currpos] = i
                counts[i] -= 1

                # count from the next position now that this position is filled
                count(currpos + 1)

                # restore
                counts[i] += 1


count(0)
print(wordcount, validwordcount)