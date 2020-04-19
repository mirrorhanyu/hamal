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

    def to_google_drive_description(self):
        return f'''
            Id: {self.video_id}

            Title: {self.title}

            Author: {self.author}

            Published: {self.published}

            Updated: {self.updated}

            Description: {self.media_description}
        '''
