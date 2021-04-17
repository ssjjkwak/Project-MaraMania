from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import json


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbMara



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Mara_lev1')
def mara_lev1():
    return render_template('Mara_lev1.html')

@app.route('/Mara_lev2')
def mara_lev2():
    mara_info = request.args.get('mara_info')
    return render_template('Mara_lev2.html', mara_info=mara_info)

@app.route('/Mara_lev2', methods=['POST'])
def save_recipe():

    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    content_receive = request.form['content_give']
    recipe_receive = request.form['mara_info']



    review = {
        'title': title_receive,
        'author': author_receive,
        'content': content_receive,
        'recipes': json.loads(recipe_receive)
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '레시피가 성공적으로 작성되었습니다.'})


@app.route('/Mara_recipes')
def Mara_recipe():
    return render_template('Mara_recipes.html')

@app.route('/Mara_recipes_get', methods=['GET'])
def read_reviews():

    reviews = list(db.reviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


@app.route('/Mara_map')
def Mara_map():
    return render_template('Mara_map.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)