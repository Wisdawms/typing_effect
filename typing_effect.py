import time
import os

clear = lambda: os.system('clear')

# bcolors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG = '\033[7m'

def typewriter():
    init_word = ""
    word = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam imperdiet est nec vestibulum auctor. In hac habitasse platea dictumst. Morbi lacinia orci ac leo laoreet, nec euismod nibh euismod. Quisque quis ipsum arcu. Etiam in porttitor risus. Mauris interdum lacus ex, eget pretium enim vulputate non. Curabitur ultrices odio eu ultrices maximus. Etiam aliquam eget nulla sit amet tristique. Cras vitae ex vehicula, suscipit nisi ac, tempor lectus. Proin sed dapibus velit. Donec id pulvinar urna, vitae maximus ante. Mauris ac malesuada ipsum.

    Fusce sapien enim, porta ut libero quis, facilisis dapibus libero. Vivamus laoreet tellus arcu, a fermentum nisi porttitor a. Ut facilisis eros ut enim maximus, in auctor ante euismod. Fusce eu mi tincidunt, fermentum est a, convallis odio. Nam facilisis ligula metus, suscipit feugiat metus mattis id. Cras a pulvinar libero, at pulvinar risus. Fusce condimentum ut ipsum vulputate imperdiet.

    Aliquam erat volutpat. Fusce eget mollis nunc. Nunc tempor diam quis turpis tristique vulputate. Aliquam bibendum dui eget ornare sagittis. Donec gravida purus sed congue vehicula. Mauris ornare aliquet sem, quis facilisis metus pretium consectetur. Donec volutpat in quam vel volutpat. Nunc aliquet diam ut felis efficitur finibus. Vestibulum pretium orci eget velit condimentum, ac convallis ligula porttitor. Donec gravida, metus nec porta varius, diam odio varius quam, vel ornare dui velit at nunc. Phasellus tempus dui est, sed ornare velit consequat vel. Nunc tristique erat id semper rutrum.

    Aliquam elementum ligula ac libero imperdiet efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla lacinia vulputate pellentesque. Vivamus consequat eros molestie mi fringilla elementum. Aliquam molestie hendrerit libero ut imperdiet. In pulvinar malesuada nunc at rhoncus. Nam mollis quis risus ut volutpat. Nulla diam lorem, eleifend at euismod id, ultrices a ipsum. Quisque ultrices mauris nec nunc condimentum ultrices. Duis metus lacus, dictum ac metus ac, mattis eleifend urna.

    Pellentesque placerat ac elit in molestie. Aliquam ex lectus, rhoncus ac mollis nec, semper eu diam. Pellentesque consectetur ipsum a ligula ultricies facilisis. Praesent ac enim in erat iaculis sagittis sit amet sed velit. Quisque vel elementum mi, quis aliquet dui. Quisque commodo mi ut aliquet pellentesque. In hac habitasse platea dictumst. Quisque interdum arcu ut rhoncus pulvinar. Interdum et malesuada fames ac ante ipsum primis in faucibus.'''

    while len(init_word) != len(word):
        for char in word:
            init_word += char
            clear()
            print(f"{bcolors.BG}{init_word}")
            time.sleep(0.01)

def nested_loop():
    sleep_interval = 0.04

    rows = input("How many rows?: ")
    columns = input("How many columns?: ")
    if rows.isdigit() and columns.isdigit():
        pass
    else: return
    symbol = input("Enter a symbol to use: ")[0]

    init = ""
    for r in range(int(rows)):
        for i in range(int(columns)):
            init += f"{symbol} \033[7m[COLUMN {i+1}]\033[0m "
            clear()
            print(init)
            time.sleep(sleep_interval)
        init += f" \033[33m[ROW {r+1}]\033[0m\n"
        clear()
        print(init)
        time.sleep(sleep_interval)
    print("Here's your table:")
    for r in range(int(rows)):
        for i in range(int(columns)):
            print(symbol, end="")
        print()
    print()

#typewriter()
nested_loop()