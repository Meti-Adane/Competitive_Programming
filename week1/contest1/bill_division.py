 
def bonAppetit(bill, k, b):
    if 2<= len(bill) <= 10 **5 and 0 <= b<= sum(bill):
        if 0 < k < len(bill):
            anna_bill = 0
            m = 0
            for i in bill:
                if 0<= bill[m] <= 10**4:
                    if i != bill[k]:
                        anna_bill += i
                m +=1
            anna_share = anna_bill / 2
            if anna_share == b:
                print("Bon Appetit")
            elif b > anna_share:
                print(int(b - anna_share))