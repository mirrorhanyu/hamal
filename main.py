from domain.auxout.auxout import auxout
from domain.ted_education.ted_education import ted_education
from youtube.youtube_application_service import YoutubeApplicationService

subscriptions = [
    ted_education,
    auxout
]

new_publishes_per_subscription = [YoutubeApplicationService.get_new_publishes(subscription) for subscription in subscriptions]

for new_publishes, subscription in zip(new_publishes_per_subscription, subscriptions):
    for new_publish in new_publishes:
        YoutubeApplicationService.download(new_publish.link, subscription.get_subscription_name())
