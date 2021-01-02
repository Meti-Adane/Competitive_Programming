
def sockMerchant(n, ar):
    if 1 <= n <= 100:
        no_matching_pairs = 0
        checked_colors = []
        sock_color_occurrence = 0
        for i in range(n-1):
            if 1 <= int(ar[i]) <= 100:
                sock_color = ar[i]
                if sock_color not in checked_colors:
                    sock_color_occurrence = ar.count(sock_color)
                    if sock_color_occurrence == 1:
                        continue
                    elif sock_color_occurrence % 2 == 0:
                        no_matching_pairs += sock_color_occurrence // 2
                    elif sock_color_occurrence % 2 != 0:
                        no_matching_pairs += (sock_color_occurrence - 1) // 2

                    checked_colors.append(sock_color)

                else:
                    continue
        return no_matching_pairs
    return 0



n = int(input())
ar = list(map(int, input().rstrip().split()))

print(sockMerchant(n, ar))
