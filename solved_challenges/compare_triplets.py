# question url : https://www.hackerrank.com/challenges/compare-the-triplets/submissions/code/195901803
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_count = 0
    bob_count = 0
    for i in range (3):
        if a[i] > b[i]:
            alice_count +=1
        elif b[i] > a[i]:
            bob_count += 1
    return [alice_count, bob_count]
print(3//2)