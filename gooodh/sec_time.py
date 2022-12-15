import time


def sec_timer(s):
    sec = 0
    while True:
        time.sleep(1)
        sec += 1
        if sec == s:
            break
    return True


if __name__ == '__main__':
    sec_timer()
