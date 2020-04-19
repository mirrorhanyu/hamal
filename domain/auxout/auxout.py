from typing import List

import requests
import xmltodict

from domain.common.subscription_base import SubscriptionBase
from domain.common.youtube_entry import YoutubeEntry
from domain.common.youtube_feed import YoutubeFeed


class AUXOUT(SubscriptionBase):
    youtube_rss = 'https://www.youtube.com/feeds/videos.xml?user=auxoutjp'

    def get_new_publishes(self) -> List[YoutubeEntry]:
        youtube_rss_xml = requests.get(self.youtube_rss).text
        youtube_rss = xmltodict.parse(youtube_rss_xml)
        return YoutubeFeed(youtube_rss).entries[::-1][0:1]

    def get_subscription_name(self) -> str:
        return 'AUXOUT'

    def get_google_drive_folder(self) -> List[str]:
        return ['1YFbaAwgxuYUAIVJXa5A4_aDiulVPR_T7']


auxout = AUXOUT()
