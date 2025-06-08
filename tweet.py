
import tweepy
import os

# Twitter API credentials (replace with your own)
API_KEY = 'L2M368O02udrKexWTD3F2soMu'
API_SECRET = '332s5KlgHpwSLj2x755oiE9DMtxGFFcVkINq79zxxm02ZbCP9k'
ACCESS_TOKEN = '1931433978445111296-LbOhx2LMztRKgKt5Ut5feiPnRoEbE2'
ACCESS_TOKEN_SECRET = 'Z0sca4EG93K6peAJ8IFvthkFjzJVeJKYpumfkZzHBSSsO'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAH9N2QEAAAAA6B%2FiAqJKz2BvSYZXSCLCS3NM9ZI%3DWMZmA474TxTHx7eEqO0Pq8PrF57U072gR8Gl0WzgTp6JkIF8Yy'  # You need to add your Bearer Token here

# Create API v2 client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

# For media upload, we still need API v1.1 auth
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Path to your MP4 video
video_path = 'monday.mp4'

# Tweet text
tweet_text = "TGIM Sir!"

try:
    # Check if file exists
    if not os.path.exists(video_path):
        print(f"Video file {video_path} not found!")
    else:
        # Upload media using v1.1 (this should work with basic access)
        media = api.media_upload(filename=video_path, media_category='tweet_video')
        
        # Create tweet using v2 API
        response = client.create_tweet(
            text=tweet_text,
            media_ids=[media.media_id_string]
        )
        
        print("Tweet posted successfully!")
        print(f"Tweet ID: {response.data['id']}")

except tweepy.Forbidden as e:
    print(f"Access forbidden: {e}")
    print("You may need elevated access for media uploads. Try posting a text-only tweet first:")
    
    # Try posting just text without media
    try:
        response = client.create_tweet(text="Hello from my Python script! #TestTweet")
        print("Text-only tweet posted successfully!")
        print(f"Tweet ID: {response.data['id']}")
    except Exception as text_error:
        print(f"Even text tweet failed: {text_error}")

except Exception as e:
    print(f"An error occurred: {e}")
