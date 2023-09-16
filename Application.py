from flask import Flask, render_template, request, redirect, url_for, flash
import twitter_service      
import logging

app = Flask(__name__)
app.secret_key = 'some_secret_key'

logging.basicConfig(level=logging.INFO)
app.logger.addHandler(logging.StreamHandler())


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_tweet', methods=['POST'])
def create_tweet():
    tweet_content = request.form.get('tweet_content')
    result = twitter_service.create_tweet(tweet_content)
    if "successfully" in result:
        flash('Tweet created successfully!', 'success')
    else:
        flash('Failed to create tweet.', 'danger')
    return redirect(url_for('index'))

@app.route('/delete_tweet', methods=['POST'])
def delete_tweet():
    tweet_id = request.form.get('tweet_id')
    result = twitter_service.delete_tweet(tweet_id)
    if "successfully" in result:
        flash('Tweet deleted successfully!', 'success')
    else:
        flash('Failed to delete tweet.', 'danger')
    return redirect(url_for('index'))

@app.route('/user_details')
def user_details():
    user_data = twitter_service.fetch_user_details()
    app.logger.info(f"Data in app.py: {user_data}")  # Using Flask's logger here
    if user_data and 'error' not in user_data:
        return render_template('user_details.html', user=user_data)
    else:
        error_message = "Failed to fetch user details."
        return render_template('error.html', error=error_message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Page not found."), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error="Internal server error."), 500

if __name__ == '__main__':
    app.run(debug=True)