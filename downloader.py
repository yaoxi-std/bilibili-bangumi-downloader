import os


class Downloader:
    def __init__(self, url, num, dest, header):
        self.url = url
        self.num = num
        self.dest = dest
        self.header = ''
        for key, value in header.items():
            self.header += "-H \"{}: {}\" ".format(key, value)

    def run(self):
        cmd = 'axel -n {} -o \"{}\" {} \"{}\"'.format(
            self.num, self.dest, self.header, self.url)
        print(cmd)
        os.system(cmd)
