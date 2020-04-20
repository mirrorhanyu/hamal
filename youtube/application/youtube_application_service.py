from typing import List

from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry
from youtube.domain.model.auxout.auxout import auxout
from youtube.domain.model.ted_education.ted_education import ted_education
from youtube.infrastructure.youtube_service import youtube


class YoutubeApplicationService:

    @staticmethod
    def get_subscriptions():
        return [ted_education, auxout]

    @staticmethod
    def get_new_publishes(subscriptions: List[SubscriptionBase]) -> List[List[YoutubeEntry]]:
        return [subscription.get_new_publishes() for subscription in subscriptions]

    @staticmethod
    def download(download_url: str, destination: str):
        youtube.download(url=download_url, output_dir=destination, merge=True, caption=True)
