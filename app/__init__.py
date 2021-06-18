import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from .backgrounds import get_random_background
from .profileInfo import get_profile_data

app = Flask(__name__)


@app.route('/')
def index():
    homeData = get_profile_data("data/home.json")
    return render_template('index.html',
                           title="MLH Fellow",
                           url=os.getenv("URL"),
                           random_background=get_random_background(),
                           homeData=homeData)


@app.route('/profile/<profile>')
def profile(profile):
    profile_data = get_profile_data("data/{profile}.json".format(profile=profile))

    return render_template('profile.html',
                           profile_data=profile_data)


@app.route('/health')
def health():
    return {'message': 'Healthy'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
