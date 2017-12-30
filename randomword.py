import random


def countedges(word):
    edgecount = 0
    counted = {(i, j): False for i in word for j in word}
    for i in word:
            for j in word:
                if i == j or counted[(i, j)] or counted[(j, i)]:
                    continue
                else:
                        edgeflag = True
                        pos_i = [index for index in range(len(word)) if word[index] == i]
                        pos_j = [index for index in range(len(word)) if word[index] == j]

                        curr = i1 = i2 = 0
                        while i1 < len(pos_i) and i2 < len(pos_j):
                            if pos_i[i1] < pos_j[i2]:
                                if curr == i:
                                    edgeflag = False
                                    break
                                else:              
                                    curr = i
                                    i1 += 1

                            else:
                                if curr == j:
                                    edgeflag = False
                                    break
                                else:
                                    curr = j
                                    i2 += 1

                        if curr == i and i1 < len(pos_i):
                            edgeflag = False
                            
                        if curr == j and i2 < len(pos_j):
                            edgeflag = False

                        if curr == i and i2 + 1 < len(pos_j):
                            edgeflag = False

                        if curr == j and i1 + 1 < len(pos_i):
                            edgeflag = False
                            
                        if edgeflag:
                            edgecount += 1

                counted[(i, j)] = counted[(j, i)] = True

    return edgecount


# number of iterations
iterations = 100000

# alphabet size - fixed? 
# n = 5

# word size (k-uniform)
k = 4

# alphabet size - variable?
for n in range(2, 11):
    
    alphabet = [i for i in range(1, n + 1)]
    edgecount = 0

    for iteration in range(iterations):
        word = alphabet * k
        random.shuffle(word)

        edgecount += countedges(word)

    print("Number of Letters (totally) =", n * k * iterations)
    print("Number of Edges (in", iterations, str(k) + "-uniform words of", n * k, "length) =", edgecount)
    print("Number of Edges (per word) =", float(edgecount)/iterations, "\n")
