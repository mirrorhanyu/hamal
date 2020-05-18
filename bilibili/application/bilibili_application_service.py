from bilibili.domain.bilibili_service import upload
from youtube.domain.model.common.subscription_base import SubscriptionBase
from youtube.domain.model.common.youtube_entry import YoutubeEntry


class BilibiliApplicationService:
    @staticmethod
    def upload(subscription: SubscriptionBase, youtube_entry: YoutubeEntry):
        upload(subscription, youtube_entry)


