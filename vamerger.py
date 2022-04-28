import os
import sys


ffmpeg_path = os.path.abspath(os.path.join(sys.argv[0], "../ffmpeg"))
if not os.path.exists(ffmpeg_path):
    ffmpeg_path = "ffmpeg"


class VAMerger:
    def __init__(self, audio, video, output):
        self.audio = audio
        self.video = video
        self.output = output

    def run(self):
        cmd = '{} -i \"{}\" -i \"{}\" -c:v copy -c:a aac -strict experimental \"{}\"'.format(
            ffmpeg_path, self.video, self.audio, self.output)
        print(cmd)
        return os.system(cmd) == 0
