# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
#
# 2+2 => 4;
#
# 1+2*3 => 7;
#
# 1-2*3 => -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#
#     *Пример:*
#
#     1+2*3 => 7;
#
#     (1+2)*3 => 9;


def parce_input(chars):
    chars = chars.replace(' ', '')
    result = []
    temp = ''
    for i in range(len(chars)):
        if chars[i].isdigit() or (chars[i] == '-' and not chars[i - 1].isdigit()):
            temp += chars[i]
        else:
            if temp.isdigit() or (temp.startswith('-') and len(temp) > 1):
                result.append(int(temp))
            result.append(chars[i])
            temp = ''
    if len(temp) > 0:
        result.append(int(temp))
    return result


def calculate(args):
    def find_closing(args):
        count = 0
        for i in range(args.index('('), len(args)):
            if args[i] == '(':
                count += 1
            if args[i] == ')':
                count -= 1
            if count == 0:
                return i

    while '(' in args and ')' in args:
        args[args.index('('): find_closing(args) + 1] = [calculate(args[args.index('(') + 1: find_closing(args)])]

    while '*' in args or '/' in args:
        try:
            ind_mul = args.index('*')
        except:
            ind_mul = 10000
        try:
            ind_dev = args.index('/')
        except:
            ind_dev = 10000
        if ind_mul < ind_dev:
            args[ind_mul - 1] = args[ind_mul - 1] * args[ind_mul + 1]
            args.pop(ind_mul + 1)
            args.pop(ind_mul)

        if ind_mul > ind_dev:
            args[ind_dev - 1] = args[ind_dev - 1] / args[ind_dev + 1]
            args.pop(ind_dev + 1)
            args.pop(ind_dev)

    while '+' in args or '-' in args:
        try:
            ind_sum = args.index('+')
        except:
            ind_sum = 10000
        try:
            ind_deg = args.index('-')
        except:
            ind_deg = 10000
        if ind_sum < ind_deg:
            args[ind_sum - 1] = args[ind_sum - 1] + args[ind_sum + 1]
            args.pop(ind_sum + 1)
            args.pop(ind_sum)

        if ind_sum > ind_deg:
            args[ind_deg - 1] = args[ind_deg - 1] - args[ind_deg + 1]
            args.pop(ind_deg + 1)
            args.pop(ind_deg)

    return args[0]


data = parce_input(input('Bведите выражение >>> '))

print(f'Результат: {calculate(data)}')
