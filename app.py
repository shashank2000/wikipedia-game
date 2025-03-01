import wikipedia_game
from bottle import get, post, request, template, run
import os

@get('/')
def page():
    '''Main (and only) page, I'm testing this whole template thing '''

    info = {'title': 'Wikipedia Game',
    'content': 'Find the shortest path between any two web pages!'
    }

    return template('simple.tpl', info)

@post('/')
def form_post():
    start = request.forms.get('start')
    end = request.forms.get('end')
    start_page = 'https://en.wikipedia.org/wiki/' + start
    end_page = 'https://en.wikipedia.org/wiki/' + end
    results = wikipedia_game.run_bfs(end_page, start_page)
    # Bottle doesn't have the fancy state change stuff React does - or maybe it shouldn't matter and we can add it in another iteration?
    result = {'results': results, 'start': start, 'end': end}
    return template('result.tpl', result)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
