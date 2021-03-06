import os
import sys


axel_path = os.path.abspath(os.path.join(sys.argv[0], "../axel"))
if not os.path.exists(axel_path):
    axel_path += ".exe"
    if not os.path.exists(axel_path):
        axel_path = "axel"


class Downloader:
    def __init__(self, url, num, dest, header={}, max_retry=5):
        self.url = url
        self.num = num
        self.dest = dest
        self.header = ''
        self.max_retry = max_retry
        for key, value in header.items():
            self.header += "-H \"{}: {}\" ".format(key, value)

    def run(self):
        cmd = '{} -n {} -o \"{}\" {} \"{}\"'.format(
            axel_path, self.num, self.dest, self.header, self.url)
        print(cmd)
        for i in range(self.max_retry):
            if os.system(cmd) == 0:
                break
            if i == self.max_retry - 1:
                return False
        return True
