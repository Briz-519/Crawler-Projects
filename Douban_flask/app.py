from flask import Flask,render_template
import sqlite3
import jieba
from matplotlib import pyplot as pyp
from wordcloud import WordCloud
from PIL import Image
import numpy
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/movie')
def movie():
    datalist=[]
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies=datalist)

@app.route('/rating')
def rating():
    rating=[]
    num=[]
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        rating.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("rating.html",rating=rating,num=num)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.run()
