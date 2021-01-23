# question_url : https://www.hackerrank.com/contests/a2sv-contest-3/challenges/sparse-arrays/problem
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    c = []
    for i in queries:
        c.append(strings.count(i))

    return c
