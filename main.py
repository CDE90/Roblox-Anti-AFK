import random, keyboard, time

def get_interval(interval):
    if not interval:
        return random.randint(60, 600)
    else:
        return interval

def action(keys: list):
    random.shuffle(keys)
    for i in keys:
        keyboard.press(i)
        time.sleep(random.randint(1, 30) / 10)
        keyboard.release(i)

def main():
    interval_choice = input('[1] Random intervals\n[2] Fixed interval\n>>> ')
    mode_choice = input('[1] All keys\n[2] Movement keys\n[3] Jump Key\n>>> ')

    if interval_choice == '1':
        interval = None
    elif interval_choice == '2':
        interval = int(input('Enter interval in seconds: '))

    if mode_choice == '1':
        keys = ['space', 'w', 'a', 's', 'd']
    elif mode_choice == '2':
        keys = ['w', 'a', 's', 'd']
    elif mode_choice == '3':
        keys = ['space']

    return interval, keys


if __name__ == '__main__':
    interval, keys = main()

    while True:
        action(keys)
        time.sleep(get_interval(interval))