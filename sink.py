import config
import subprocess
import contextlib

@contextlib.contextmanager
def ffmpeg():
    cmd = (
        'ffmpeg', '-y',

        '-re',


        '-i', 'skyrim.mp3',

        '-s', f'{config.frame_width}x{config.frame_height}',
        '-f', 'rawvideo',
        # '-pix_fmt', 'rgba',
        '-pix_fmt', 'rgb24',
        '-r', str(config.fps),  # input framrate
        '-i', '-',  # read video from the stdin

        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',

        '-vsync', 'cfr',
        '-b:v', '3m',
        '-deinterlace',
        '-r', str(config.fps),  # output framerate
        # f'/tmp/benchmark/{fname}.mp4',

        '-f', 'flv',
        '-flvflags', 'no_duration_filesize',
        'rtmp://a.rtmp.youtube.com/live2/u0x7-vxkq-6ym4-s4qk-0acg'
    )

    _ffmpeg = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    yield _ffmpeg.stdin
    _ffmpeg.communicate()
    _ffmpeg.wait()
