""""
Author: Ameya Daigavane
Date: 29th December, 2017
Title: The Graphcheck Algorithm for 2-uniform words.
Code Version: 1.0 (runs on Python 3.5.2)
"""


def graphcheck(word, graph):
    # word is 2-uniform string, graph is list of edges

    # Check if number of vertices in G_word is same as in G
    vertcount = 0
    vertices = {}
    for edge in graph:
        if vertices.get(edge[0]) is None:
            vertices[edge[0]] = True
            vertcount += 1

        if vertices.get(edge[1]) is None:
            vertices[edge[1]] = True
            vertcount += 1

    if (len(word) // 2) != vertcount:
        return False

    # In mark[], 0 represents unmarked, 1 represents marked positions
    mark = [0] * len(word)
    edgecount = 0

    # Fenwick Tree to represent mark[]
    ft = FenwickTree(mark)

    # Associative array of positions
    null = -1
    pos = {letter: [null, null] for letter in word}

    for index, letter in enumerate(word):
        if pos[letter][0] == null:
            # letter's first occurrence in word
            pos[letter][0] = index
        else:
            # letter's second occurrence in word
            pos[letter][1] = index

            i = pos[letter][0]
            j = pos[letter][1]

            edgecount += (j - i - 1 - ft.range_sum(i + 1, j - 1))

            # marking the positions and updating the Fenwick tree
            mark[i] = 1
            ft.update(i, 1)

            mark[j] = 1
            ft.update(j, 1)

    if edgecount != len(graph):
        return False
    else:
        equalsflag = True
        for edge in graph:
            # check if edge exists, else break
            if not ((pos[str(edge[0])][0] < pos[str(edge[1])][0] < pos[str(edge[0])][1] < pos[str(edge[1])][1])
                    or (pos[str(edge[1])][0] < pos[str(edge[0])][0] < pos[str(edge[1])][1] < pos[str(edge[0])][1])):
                equalsflag = False
                break

        if equalsflag:
            return True
        else:
            return False


# Implementation of a Fenwick Tree
class FenwickTree:
    # initialize with a given array arr[]
    def __init__(self, arr=[]):
        self.size = len(arr)
        self.a = [0] * self.size

        for i in range(self.size):
            self.update(i, arr[i])

    # add val to arr[i]
    def update(self, i, val):
        i += 1  # 1-based indexing
        while i <= self.size:
            self.a[i - 1] += val
            i += i & -i

    # sum of elements from arr[i..j], endpoints included. If only one argument passed, we consider the sub-array arr[0..i]
    def range_sum(self, i, j=None):
        if j is None:
            return self.sum(i)
        else:
            return self.sum(j) - self.sum(i - 1)

    # sum of elements from arr[0..i]
    def sum(self, i):
        ans = 0
        i += 1  # 1-based indexing
        while i > 0:
            ans += self.a[i - 1]
            i = i & (i - 1)

        return ans


def main():
    # here, word is 2-uniform and on the letters 1, 2, 3 ...
    word = input()

    # example graph - feel free to change!
    graph = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]

    if graphcheck(word, graph):
        print("Yes, the word", word, "represents the given graph", graph, ".")
    else:
        print("No, the word", word, "does not represent the given graph", graph, ".")

if __name__ == '__main__':
    main()
