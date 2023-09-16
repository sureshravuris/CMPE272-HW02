# Twitter_Service - App

This application provides basic functionalities to interact with the Twitter API, such as creating tweets, deleting tweets, and fetching user details.

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
