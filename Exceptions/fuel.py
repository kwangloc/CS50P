def main():
    fuel()

def fuel():
    while True:
        try:
            ip = input("Fraction: ")
# cach 1
            # flag = True
            # num = ""
            # den = ""
            # for i in ip:
            #     if i == '/':
            #         flag = False
            #         continue
            #     if flag:
            #         num += i
            #     else:
            #         den += i
            # num = int(num)
            # den = int(den)
# cach 2
            num_den = ip.split('/')
            num = int(num_den[0])
            den = int(num_den[1])
            if num <= den:
                per = int((round(num/den, 2))*100)
                if per >= 99:
                    print("F")
                elif per <= 1:
                    print("E")
                else:
                    print(per, "%", sep="")
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()