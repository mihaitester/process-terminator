import os
import time


def main():
    # backdooring processes
    # processes=['concentr','receiver','vpn']
    processes = []
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "terminator.cfg"), 'r') as r:
        processes = r.readlines()
    while True:
        for p in processes:
            # run command only if processes are alive 'tasklist /v | find "{}"'.format(p)
            os.system('taskkill /f /im "{}*"'.format(p))
        time.sleep(5)


if __name__=="__main__":
    main()