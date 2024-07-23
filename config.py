import json

with open('settings.json', 'r') as f:
    settings = json.load(f)

class Config:
    SECRET_KEY = 'your_secret_key'
    GOOGLE_ANALYTICS_KEY_FILE_LOCATION = settings['google_analytics']['key_file_location']
    GOOGLE_ANALYTICS_VIEW_ID = settings['google_analytics']['view_id']
    TWITTER_CONSUMER_KEY = settings['twitter']['consumer_key']
    TWITTER_CONSUMER_SECRET = settings['twitter']['consumer_secret']
    TWITTER_ACCESS_TOKEN = settings['twitter']['access_token']
    TWITTER_ACCESS_TOKEN_SECRET = settings['twitter']['access_token_secret']
    FACEBOOK_ACCESS_TOKEN = settings['facebook']['access_token']
    INSTAGRAM_ACCESS_TOKEN = settings['instagram']['access_token']
