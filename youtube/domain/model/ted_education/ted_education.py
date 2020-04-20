from typing import List

import requests
import xmltodict

from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry
from youtube.domain.model.common.youtube_feed import YoutubeFeed


class TEDEducation(SubscriptionBase):

    YOUTUBE_RSS = 'https://www.youtube.com/feeds/videos.xml?user=TEDEducation'

    def get_new_publishes(self) -> List[YoutubeEntry]:
        youtube_rss_xml = requests.get(self.YOUTUBE_RSS).text
        youtube_rss = xmltodict.parse(youtube_rss_xml)
        return YoutubeFeed(youtube_rss).entries[::-1][0:1]

    def get_subscription_name(self) -> str:
        return 'TED-Ed'

    def get_google_drive_folder(self) -> List[str]:
        return ['1Ghgv4WWsm330PXBC0OJ5GxRdVjfQ9afZ']


ted_education = TEDEducation()
