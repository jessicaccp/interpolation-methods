import time
import sys


def progress_bar(toolbar_width):
    # setup toolbar
    sys.stdout.write('[%s]' % (' ' * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write('\b' * (toolbar_width+1))

    for _ in range(toolbar_width):
        time.sleep(0.05)
        sys.stdout.write('-')
        sys.stdout.flush()
    sys.stdout.write('\n')
