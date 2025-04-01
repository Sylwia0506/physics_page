from flask import Flask, render_template, abort
from settings import PHYSICS_TOPICS
import json
import os
from urllib.parse import quote, unquote

app = Flask(__name__)

def slugify(text):
    polish_chars = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    
    for pl, en in polish_chars.items():
        text = text.replace(pl, en)
    
    text = text.lower().replace(' ', '-')
    text = ''.join(c for c in text if c.isalnum() or c == '-')
    
    return text

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/matura')
def matura():
    try:
        with open('static/data/matury.json', 'r', encoding='utf-8') as f:
            matury = json.load(f)
    except FileNotFoundError:
        matury = []
    return render_template('matura.html', matury=matury)

@app.route('/działy')
def topics():
    topics_with_slugs = []
    for topic in PHYSICS_TOPICS:
        topic_with_slug = topic.copy()
        topic_with_slug['slug'] = slugify(topic['name'])
        topics_with_slugs.append(topic_with_slug)
    return render_template('index.html', topics=topics_with_slugs)

@app.route('/działy/<path:topic_slug>')
def topic(topic_slug):
    decoded_slug = unquote(topic_slug)
    
    topic = None
    for t in PHYSICS_TOPICS:
        if slugify(t['name']) == decoded_slug:
            topic = t
            break
    
    if topic is None:
        abort(404)
    
    return render_template('topic.html', topic=topic)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)