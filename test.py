import requests
import re

def runner():
    saver = ''
    count = 0
    check = 0
    for x in range(1,99999):
        r = requests.get(f'https://coinmarketcap.com/?page={x}')
        if r.status_code == 404:
            print('acabou')
            break
        print(f'page {x}')
        saver += r.text
    pattern = ("/currencies/[\S]+/")
    r = re.findall(pattern, saver)
    listCoins = list(set(r))
    coin = open('coins.txt', 'w')
    for x in listCoins:
        count += 1
        if 'markets' in x:
            pass
        else:
            coin.write(f'{x}\r')
            check += 1
    print(f'Coins total: {count}')
    coin.close()

def compare():
    count = 0
    f1 = open('coins_new.txt', 'r')
    f2 = open('coins.txt', 'r')
    if sorted(f1.read()) == sorted(f2.read()):
        print('iguais')
    else:
        f1 = open('coins_new.txt', 'r')
        f1_split = f1.read().split('\n')
        f1.close()
        for x in f1_split:
            f2 = open('coins.txt', 'r')
            if x in f2.read().split('\n'):
                pass
            else:
                count +=1
                print(x)
            f2.close()
    print(f'Moedas novas {count}')
if __name__ == '__main__':
    runner()
    compare()