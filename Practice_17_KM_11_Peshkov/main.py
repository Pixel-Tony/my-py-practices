from logarithm import *
from exp_root import *
from factorial import *
from sys import exit as s_exit
from os import system, name as os_name

def main():
    funcs = [log, lg, ln, fact,
            exp2, exp3, root2, root3]
    finished = False
    while not finished:
        clear = (lambda: system('clear' if os_name not in ['nt', 'dos'] else 'cls'))()
        clear
        print('\nChoose an option:\n')
        for ind in range(len(funcs)):
            print(f'{ind+1}. {funcs[ind].__name__}')
        print('\n[Q]uit')
        choice = input('> ').upper()
        if choice == 'Q':
            s_exit()
        else:
            if choice not in [str(a) for a in range(len(funcs))]:
                print('Incorrect option, try again;')
                input()
                continue
            else:
                choice = int(choice) - 1
                __endings = ('1','') if funcs[choice] != log else ('2', 's')
                clear
                args = input('Choose {} argument{} for function {}: '.format(*__endings, funcs[choice].__name__))
                try:
                    args = [float(a) for a in args.strip().split(' ') if len(a) > 0]
                    result = funcs[choice](*args)
                    print(f'Result is {round(result, 5) if round(result, 5) != 0 else "too small to display but != 0" if result != 0 else result}')
                    if not input('Continue (Y/N)? ').upper() == 'Y':
                        clear
                        s_exit()
                except Exception:
                    print('Incorrect input, try again.')
                    input()


if __name__ == '__main__':
    main()