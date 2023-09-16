import tweepy
import requests
from requests_oauthlib import OAuth1
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your credentials
api_key = "cGZg6r1p9FmOVpQoOrSDyDkBE"  # API Key
api_secret_key = "FhcVYk3ddTz9VRhkmywwb5KKyz52QDKTaqWip6T5J459jWuszG"  # API Secret Key
access_token = "1702812890708029440-NHMlWOaYcKgJY6VVRpXFNo1HW9uuug"  # Access Token
access_token_secret = "NduLAk2Wim5CEeuMGKvUc7xyOGiUioHCMtKlNB2XtH731"  # Access Token Secret

# Initialize Tweepy
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

# OAuth1 authentication for direct API calls
auth_api = OAuth1(api_key, api_secret_key, access_token, access_token_secret)

def create_tweet(text):
    """Create a tweet with the given text."""
    URL = "https://api.twitter.com/2/tweets"
    headers = {
        "Content-Type": "application/json"
    }
    data_payload = {
        "text": text
    }
    response = requests.post(URL, auth=auth_api, headers=headers, data=json.dumps(data_payload))
    if response.status_code == 201:
        return "Tweet posted successfully!"
    else:
        return f"Failed to post tweet. Status code: {response.status_code}, Message: {response.text}"

def delete_tweet(tweet_id):
    """Delete a tweet with the given tweet_id."""
    URL = f"https://api.twitter.com/2/tweets/{tweet_id}"
    response = requests.delete(URL, auth=auth_api)
    if response.status_code in [200, 204]:  
        return f"Tweet with ID {tweet_id} deleted successfully!"
    else:
        return f"Failed to delete tweet. Status code: {response.status_code}, Message: {response.text}"

def fetch_user_details():
    """Fetch details of the authenticated user."""
    URL = "https://api.twitter.com/2/users/me"
    response = requests.get(URL, auth=auth_api)
    
    if response.status_code == 200:  
        user_data = response.json()
        logger.info(f"User Data: {user_data}")  
        return user_data
    else:
        error_message = f"Failed to fetch user details. Status code: {response.status_code}, Message: {response.text}"
        logger.error(error_message)  
        return {"error": error_message}