from typing import List

import requests
import xmltodict

from utils.translate_utils import translator
from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry
from youtube.domain.model.common.youtube_feed import YoutubeFeed


class TEDEducation(SubscriptionBase):

    YOUTUBE_RSS = 'https://www.youtube.com/feeds/videos.xml?playlist_id=PLJicmE8fK0EiskDjD7XE9hMTRnwFtWj1Y'

    BILIBILI_ENTERTAINMENT_VIDEO_TYPE = 71

    BILIBILI_TAGS = ['TED', '教育', 'YOUTUBE搬运', '英语听力', 'YOUTUBE', '英语学习', '美国', '英语', '欧美']

    BILIBILI_SOURCE = 'http://www.youtube.com'

    def get_new_publishes(self) -> List[YoutubeEntry]:
        youtube_rss_xml = requests.get(self.YOUTUBE_RSS).text
        youtube_rss = xmltodict.parse(youtube_rss_xml)
        return YoutubeFeed(youtube_rss).entries[::-1]

    def get_subscription_name(self) -> str:
        return 'TED-Ed'

    def get_google_drive_folder(self) -> List[str]:
        return ['1Ghgv4WWsm330PXBC0OJ5GxRdVjfQ9afZ']

    def get_subtitles_regex(self) -> (str, str):
        return '.zh-CN.srt', '.en.srt'

    def get_bilibili_video_type(self):
        return self.BILIBILI_ENTERTAINMENT_VIDEO_TYPE

    def get_bilibili_video_tags(self):
        return self.BILIBILI_TAGS

    def get_bilibili_source(self) -> str:
        return self.BILIBILI_SOURCE

    def get_bilibili_title(self, origin_title: str) -> str:
        chinese_title = translator.translate(origin_title, dest='zh-cn').text
        return f'#TED# {chinese_title}'[:80]

    def get_bilibili_description(self, origin_description: str) -> str:
        return origin_description.replace('\n\n', '\n')[:250]


ted_education = TEDEducation()
