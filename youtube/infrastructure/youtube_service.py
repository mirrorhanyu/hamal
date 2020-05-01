from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.margin import margin
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from you_get.extractors import youtube

from utils.file_utils import add_prefix_to_filename, replace_extension


def get_youtube_downloader():
    return youtube


def add_subtitle(video_path, default_subtitle_path):
    if default_subtitle_path is None:
        return
    default_subtitle = margin(
        clip=SubtitlesClip(default_subtitle_path, _subtitle_generator(30)).set_position(('center', 'bottom')),
        bottom=35,
        opacity=0
    )
    video = VideoFileClip(video_path, audio=True)
    composed_video = CompositeVideoClip([video, default_subtitle])
    output_filename = replace_extension(add_prefix_to_filename(video_path, '[WITH-SUBTITLE] '), '.mp4')
    composed_video.write_videofile(output_filename, threads=2, fps=video.fps)


def _subtitle_generator(font_size):
    return lambda txt: TextClip(
        txt,
        font='ArialUnicode',
        fontsize=font_size,
        color='white',
        bg_color='#00000066'
    )
