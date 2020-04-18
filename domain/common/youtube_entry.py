class YoutubeEntry:
    def __init__(self, youtube_entry):
        self.id = youtube_entry['id']
        self.video_id = youtube_entry['yt:videoId']
        self.title = youtube_entry['title']
        self.author = youtube_entry['author']['name']
        self.published = youtube_entry['published']
        self.updated = youtube_entry['updated']
        self.media_description = youtube_entry['media:group']['media:description']
        self.link = youtube_entry['link']['@href']
