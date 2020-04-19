from domain.auxout.auxout import auxout
from domain.ted_education.ted_education import ted_education
from google.google_application_service import GoogleApplicationService as Google
from utils.file_utils import remove_folder
from youtube.youtube_application_service import YoutubeApplicationService as Youtube

subscriptions = [
    ted_education,
    auxout
]

new_publishes_each_subscription = [
    Youtube.get_new_publishes(subscription) for subscription in subscriptions
]

for subscription, new_publishes in zip(subscriptions, new_publishes_each_subscription):
    for new_publish in new_publishes:
        Youtube.download(new_publish.link, subscription.get_subscription_name())
        Google.upload_to_google_drive(parent_folder_ids=subscription.get_google_drive_folder(),
                                      file_name=new_publish.title,
                                      local_file_path=subscription.get_subscription_name(),
                                      description=new_publish.to_google_drive_description())
        remove_folder(subscription.get_subscription_name())
