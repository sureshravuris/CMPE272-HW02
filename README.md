# Twitter_Service - App

This application provides basic functionalities to interact with the Twitter API, such as creating tweets, deleting tweets, and fetching user details.


This is a team-project with Joash Muganda, Suresh Ravuri, and Alexis Ambriz, we didn't specify who wrote which code however we all assisted each-other during development.

The base-line code was partially generated using iterative chatGPT-4 prompts using the command-line 'gpt-engineer' tool here: https://github.com/AntonOsika/gpt-engineer.
We used Tweepy library with Twitter's API Version 1.1, using the developer tool found at https://developer.twitter.com/en/portal/dashboard
To use this wordpress-plugin, you would need to make an account, set up your user authentication settings, 
and then copy-paste your developer keys and tokens into the docker-compose.yml.
They will need to be posted in the section belonging to the X-Twitter service. 
Make sure that you have marked the 'Read & Write' box for APP permissions, marked 'Web App' for the app type, and have marked localhost:5000 as the callback URL.
The website URL is required and must be a valid domain name, but it could be anything if you do not need to connect it to your site.

Once you have your keys/tokens and updated authentication settings, you could clone the repo into your local computer.
CD into the directory in your terminal, and the run "bash run.sh"
This will start the docker-compose service that will create the wordpress site, the plugin app, and the database services.
Once it is live, you can open the http://localhost/ address in your web browser.
You will need to wait a couple seconds for the webserver to bring up the wordpress install page.
Once the install page is up, you select a language and install as you would for a wordpress site.
Enter the details and then you will be brought to the admin dashboard after you sign-in.

To set up the plugin:

1. Head to the dashboard on the top-left of the interface.
   <img width="383" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/be05e700-da15-4b2e-b2e4-14bb9e6ced09">
2. Go to 'plugins', look for the X-Twitter-Plugin, and click 'Activate'
   <img width="553" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/8d542ab8-87f3-4ce5-983e-956c4e39c7af">
4. Open the posts page, and edit any post to include a Wordpress block called "short-code".
   <img width="255" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/48b41549-5c50-44e3-b6af-1a13d2836777">
5. For the code, type "[x_twitter]"
   <img width="740" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/0c2f8190-1fab-468a-a1f0-1d16da98719b">
6. Save the code-block and open the page by clicking the link in the top right.
   <img width="290" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/e5efef0b-b130-4ac3-9774-95f642dd4dc6">
7. On the post you just made, you can now see the GUI of the X plugin. You can enter text in the first box and click the button and your tweet will be made.
8. To delete a tweet, you will need to enter the ID in the second box by visiting the tweet you made on twitter,
   looking at the URL, and write down the long string of numbers at the end of the url. Once you enter it, click the button and your tweet should be deleted.
   <img width="692" alt="image" src="https://github.com/Bryan-Az/X-Twitter-API-Plugin/assets/36939025/37fab2a5-d5ee-4af7-80f5-22fd4f4f73f1">



## Features

- **Create Tweet**: Allows users to post a tweet to their Twitter account.
- **Delete Tweet**: Enables users to delete a specific tweet based on its ID.
- **User Details**: Fetches and displays the details of the authenticated user.

## Getting Started

### Prerequisites

- Python 3
- Flask
- Tweepy
- Requests
- Requests-OAuthlib

### Setup

1. Install the tweepy module:
   \```install the tweepy module using pip:
   pip install tweepy
   \```


2. Setting Up Flask
\```bash
pip install Flask
\```

3. **Important**: Replace the placeholders for API keys and tokens in `twitter_service.py` with your own Twitter API credentials:
\```python
api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
\```

4. Run the application:
\```bash
python Application.py
\```

## Running Tests

To run the unit tests, use the following command:
\```bash
python -m unittest test_twitter_service
\```

## Usage

- Visit `http://127.0.0.1:5000/` in your browser.
- Use the provided interface to create tweets, delete tweets, and view user details.

## Notes

- The application is designed for demonstration and learning purposes.
- Ensure you've set up the Twitter API credentials correctly to avoid authentication issues.

## License

This project is licensed under the MIT License.









