import glob
from typing import List

from utils.file_utils import is_video
from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry
# from youtube.domain.model.auxout.auxout import auxout
from youtube.domain.model.ted_education.ted_education import ted_education
from youtube.infrastructure.youtube_service import get_youtube_downloader, add_subtitle


class YoutubeApplicationService:

    @staticmethod
    def get_subscriptions():
        return [ted_education]

    @staticmethod
    def get_new_publishes(subscriptions: List[SubscriptionBase]) -> List[List[YoutubeEntry]]:
        return [subscription.get_new_publishes() for subscription in subscriptions]

    @staticmethod
    def download(download_url: str, destination: str):
        get_youtube_downloader().download(url=download_url, output_dir=destination, merge=True, caption=True)

    @staticmethod
    def add_subtitle(subscription: SubscriptionBase):
        default_regex, translation_regex = subscription.get_subtitles_regex()
        video, default_subtitle, translated_subtitle = None, None, None
        for file in glob.glob(f'{subscription.get_subscription_name()}/*'):
            if is_video(file):
                video = file
            if default_regex and default_regex in file:
                default_subtitle = file
            if translation_regex and translation_regex in file:
                translated_subtitle = file
        add_subtitle(video, default_subtitle)
