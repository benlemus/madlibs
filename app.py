from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import all_stories

app = Flask(__name__)

'''debug toolbar'''
app.config['SECRET_KEY'] = 'shhthisismypassword'
debug = DebugToolbarExtension(app)

'''home page. place to choose template'''
@app.route('/')
def home_page():
    return render_template('home.html', stories=all_stories.values())

'''asks questions according to template'''
@app.route('/questions')
def questions_page():
    story_id = request.args['story_id']
    story = all_stories[story_id]

    promts = story.prompts

    return render_template('questions.html', story_id=story_id, prompts=promts)

'''generates/shows story'''
@app.route('/story')
def story_page():
    story_id = request.args['story_id']
    story = all_stories[story_id]

    full_story = story.generate(request.args)

    return render_template('story.html', story=full_story)