def main():
    math_exp = input()
    print(f"{interpreter(math_exp):.1f}")

def interpreter(math_exp):
    try:
        tmp_li = math_exp.split()
        first_op = float(tmp_li[0])
        op = tmp_li[1]
        second_op = float(tmp_li[2])
        if op == '+':
            return first_op + second_op
        elif op == '-':
            return first_op - second_op
        elif op == '*':
            return first_op * second_op
        else:
            return first_op / second_op
    except ValueError:
        pass

if __name__ == "__main__":
    main()