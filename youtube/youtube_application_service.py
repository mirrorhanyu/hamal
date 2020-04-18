from typing import List

from you_get.extractors import youtube

from domain.common.subscription_base import SubscriptionBase
from domain.common.youtube_entry import YoutubeEntry


class YoutubeApplicationService:

    @staticmethod
    def get_new_publishes(subscription: SubscriptionBase) -> List[YoutubeEntry]:
        return subscription.get_new_publishes()

    @staticmethod
    def download(download_url: str, destination: str):
        youtube.download(url=download_url, output_dir=destination, merge=True, caption=True)
