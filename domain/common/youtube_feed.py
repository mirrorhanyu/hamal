from domain.common.youtube_entry import YoutubeEntry


class YoutubeFeed:
    def __init__(self, youtube_feed_xml):
        self.youtube_feed = youtube_feed_xml['feed']
        self.channel_id = self.youtube_feed['yt:channelId']
        self.title = self.youtube_feed['title']
        self.author = self.youtube_feed['author']['name']
        self.published = self.youtube_feed['published']
        self.entries = [YoutubeEntry(entry) for entry in self.youtube_feed['entry']]



