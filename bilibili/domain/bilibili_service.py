import glob

from bilibiliupload import VideoPart

from bilibili.infrastructure.bilibili_helper import bilibili_upload
from utils.file_utils import is_video
from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry


def upload(subscription: SubscriptionBase, youtube_entry: YoutubeEntry):
    title = subscription.get_bilibili_title(youtube_entry.title)
    description = subscription.get_bilibili_description(youtube_entry.media_description)
    video_paths = [path for path in glob.glob(f'{subscription.get_subscription_name()}/*') if is_video(path)]
    video_to_be_uploaded = next((path for path in video_paths if '[WITH-SUBTITLE]' in path), video_paths[0])
    tid = subscription.get_bilibili_video_type()
    tags = subscription.get_bilibili_video_tags()
    source = subscription.get_bilibili_source()
    bilibili_upload.upload(
        parts=[VideoPart(path=video_to_be_uploaded, title=title, desc=description)],
        title=title,
        tid=tid,
        tag=tags,
        desc=description,
        source=source,
        cover='',
        dynamic=''
    )
