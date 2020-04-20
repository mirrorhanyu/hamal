from abc import abstractmethod, ABC
from typing import List

from youtube.domain.model.common.youtube_entry import YoutubeEntry


class SubscriptionBase(ABC):

    @abstractmethod
    def get_new_publishes(self) -> List[YoutubeEntry]:
        return []

    @abstractmethod
    def get_subscription_name(self) -> str:
        return ''

    @abstractmethod
    def get_google_drive_folder(self) -> List[str]:
        return []

    @abstractmethod
    def get_subtitles_regex(self) -> (str, str):
        return '', ''
