import os


class VAMerger:
    def __init__(self, audio, video, output):
        self.audio = audio
        self.video = video
        self.output = output

    def run(self):
        cmd = 'ffmpeg -i \"{}\" -i \"{}\" -c:v copy -c:a aac -strict experimental \"{}\"'.format(
            self.video, self.audio, self.output)
        print(cmd)
        os.system(cmd)
