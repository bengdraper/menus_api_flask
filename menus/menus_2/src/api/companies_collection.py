# # api collection
# from flask import Blueprint, jsonify, abort, request
# from ..models import Tweet, User, db

# bp = Blueprint('menus', __name__, url_prefix='/menus')

# @bp.route('', methods=['GET']) # decorate path and list of http verbs
# def index():
#     log = ['hello hello']
#     return jsonify(log)

#     # tweets = Tweet.query.all() # ORM performs select query

#     # result = []

#     # for t in tweets:
#     #     result.append(t.serialize()) # build list of tweets as dicts

#     # return jsonify(result) # return json res


# # show a tweet
# # decorate bp with path @ /tweets:id GET
# @bp.route('/<int:id>', methods=['GET'])
# def show(id: int):

#     t = Tweet.query.get_or_404(id)

#     return jsonify(t.serialize())


# # post a tweet from client
# @bp.route('', methods=['POST'])  # for POST requests @ /tweets/'' (ala blueprint)
# def create():

#     # check if client request body includes user_id and content
#     if 'user_id' not in request.json or 'content' not in request.json:
#         return abort(400)  # flask method abort() w/ status code 

#     # check if client request user_id exists in users
#     User.query.get_or_404(request.json['user_id'])  # get_or_404 method from User @db.Model

#     # create record tweet from user request body
#     t = Tweet(
#         user_id=request.json['user_id'],
#         content=request.json['content']
#     )

#     db.session.add(t)  # create this tweet migration at db; sqlalchemy .add()
#     db.session.commit()  # send it; sqlalchemy .commit()

#     return jsonify(t.serialize())


# # delete a tweet from client
# @bp.route('/<int:id>', methods=['DELETE'])  # for delete requests @ /tweets/'' (ala blueprint)
# def delete(id: int):

#     t = Tweet.query.get_or_404(id)

#     try:
#         db.session.delete(t)
#         db.session.commit()
#         return jsonify(True)
#     except:
#         return jsonify(False)

# @bp.route('/<int:id>/liking_users', methods=['GET'])
# def liking_users(id: int):  # takes an id

#     t = Tweet.query.get_or_404(id)

#     result = []

#     for u in t.liking_users:
#         result.append(u.serialize())

#     return jsonify(result)