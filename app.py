import json
import trueskill
from bottle import Bottle, response, request, abort, run

app = Bottle()

@app.error(400)
def error400(err):
    response.content_type = 'application/json'
    return json.dumps({'error': err.body})

@app.get('/')
def index_page():
    return {'help': 'POST to /rate'}

@app.post('/quality')
def get_quality():
    (ranked, _) = build_ranked()
    return {'quality': trueskill.quality(ranked) * 100}

@app.post('/rate')
def rate_players():
    (ranked, teams) = build_ranked()
    ranked = trueskill.rate(ranked)

    # JSONify
    result = []
    for t, team in enumerate(ranked):
        rated_team = []
        for i, player in enumerate(team):
            rated_team.append(jsonify_rating(player, teams[t][i]))

        result.append(rated_team)

    return {'teams': result}

def build_ranked():
    # Not JSON?
    if 'application/json' not in request.headers.get('Content-Type'):
        return abort(400, 'content type must be `application/json`')

    # Validate JSON body
    body = request.json
    if body is None or 'teams' not in body:
        return abort(400, '`teams` must be present in request body')

    teams = body['teams']
    if type(teams) is not list:
        return abort(400, '`teams` must be an array')

    if (len(teams) < 2):
        return abort(400, '`teams` must be an array of at least two elements')

    # Build rating items
    ranked = []
    for team in teams:
        if type(team) is not list:
            return abort(400, 'entries of `teams` must be arrays')

        rated_team = []
        for player in team:
            rated_team.append(trueskill.Rating(
                mu=player.get('mu', 25),
                sigma=player.get('sigma', 25 / 3)
            ))

        ranked.append(rated_team)

    return (ranked, teams)

def jsonify_rating(rating, original):
    new_rating = original.copy()
    new_rating.update({'mu': rating.mu, 'sigma': rating.sigma})
    return new_rating

if __name__ == '__main__':
    run(app)
