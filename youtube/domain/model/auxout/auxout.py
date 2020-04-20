from typing import List

import requests
import xmltodict

from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry
from youtube.domain.model.common.youtube_feed import YoutubeFeed


class AUXOUT(SubscriptionBase):

    YOUTUBE_RSS = 'https://www.youtube.com/feeds/videos.xml?user=auxoutjp'

    def get_new_publishes(self) -> List[YoutubeEntry]:
        youtube_rss_xml = requests.get(self.YOUTUBE_RSS).text
        youtube_rss = xmltodict.parse(youtube_rss_xml)
        return YoutubeFeed(youtube_rss).entries[::-1][0:1]

    def get_subscription_name(self) -> str:
        return 'AUXOUT'

    def get_google_drive_folder(self) -> List[str]:
        return ['1YFbaAwgxuYUAIVJXa5A4_aDiulVPR_T7']

    def get_subtitles_regex(self) -> (str, str):
        return None, None


auxout = AUXOUT()
