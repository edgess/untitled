from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/table/')
@app.route('/table/<name>')
def table(name=None):
    return render_template('table.html', name=name)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/path/<path:path>')
def show_path(path):
    # show the user profile for that user
    return '^path^' + path

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/post/<float:post_id>')
def show_post_float(post_id):
    # show the post with the given id, the id is an integer
    return 'Post_float %f' % post_id

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/')
def index():
    import MySQLdb
    db = MySQLdb.connect("192.168.10.30", "log", "1234", "bak_log")
    cur = db.cursor()
    cur.execute("SELECT * FROM log ORDER BY date DESC limit 60")
    data = cur.fetchall()
    db.close()
    return render_template('view.html', datas=data)

@app.route('/log')
@app.route('/log', methods=['POST', 'GET'])
def log(name = None):
    if request.method == 'POST':
        name = request.form['fname']
    if request.method == 'GET':
        #return request.args.get('abc')
        return request.args.items().__str__()
    return render_template('login.html', rname = name)

@app.route('/login')
@app.route('/login', methods=['POST', 'GET'])
def login(name = None):
    if request.method == 'POST':
        name = request.form['fname']
    if request.method == 'GET':
        name = request.args.get('abc')
    return render_template('login.html' , rname = name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)