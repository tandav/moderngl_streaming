import config
import subprocess
import contextlib

@contextlib.contextmanager
def ffmpeg():
    cmd = (
        'ffmpeg', '-y',
        '-hwaccel', 'videotoolbox',
        '-threads', '16',

        # '-re',

        '-i', 'skyrim.mp3',

        '-s', f'{config.frame_width}x{config.frame_height}',
        '-f', 'rawvideo',
        # '-pix_fmt', 'rgba',
        '-pix_fmt', 'rgb24',
        '-r', str(config.fps),  # input framrate
        # '-thread_queue_size', '128',
        '-thread_queue_size', '1024',
        '-i', '-',  # read video from the stdin

        # '-c:v', 'libx264',
        '-c:v', 'h264_videotoolbox',

        '-pix_fmt', 'yuv420p',

        '-vsync', 'cfr',
        '-b:a', '320k',
        # '-b:v', '5M',
        '-b:v', '12M',
        '-deinterlace',
        '-r', str(config.fps), # output framerate
        # f'/tmp/benchmark/{fname}.mp4',

        '-f', 'flv',
        '-flvflags', 'no_duration_filesize',
        'rtmp://a.rtmp.youtube.com/live2/u0x7-vxkq-6ym4-s4qk-0acg'
    )

    _ffmpeg = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    yield _ffmpeg.stdin
    _ffmpeg.communicate()
    _ffmpeg.wait()
