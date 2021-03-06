from flask import Flask, jsonify, request
from flask_cors import CORS
from mvc.controllers import players
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return jsonify({"message": 'Welcome to my Flask API for snooker players!'}), 200

@app.route('/api/players', methods=['GET', 'POST'])
def players_handler():
    fns = {
        'GET': players.index,
        'POST': players.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/players/<int:player_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def player_handler(player_id):
    fns = {
        'GET': players.show,
        'PATCH': players.update,
        'PUT': players.update,
        'DELETE': players.destroy
    }
    resp, code = fns[request.method](request, player_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)