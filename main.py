from google.application.google_application_service import GoogleApplicationService as Google
from youtube.application.youtube_application_service import YoutubeApplicationService as Youtube

from utils import file_utils

subscriptions = Youtube.get_subscriptions()
new_publishes_each_subscription = Youtube.get_new_publishes(subscriptions)

for subscription, new_publishes in zip(subscriptions, new_publishes_each_subscription):
    for new_publish in new_publishes:
        Youtube.download(new_publish.link, subscription.get_subscription_name())
        Youtube.add_subtitle(subscription)
        # Google.upload_to_google_drive(parent_folder_ids=subscription.get_google_drive_folder(),
        #                               file_name=new_publish.title,
        #                               local_file_path=subscription.get_subscription_name(),
        #                               description=new_publish.to_google_drive_description())
        # file_utils.remove_folder(subscription.get_subscription_name())
