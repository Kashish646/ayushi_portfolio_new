from flask import Flask, render_template, request, redirect, url_for, session,flash


app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_flashed_messages():
    return [message for message in (session.pop('_flashes', []))]

@app.route('/')
def home():
    if 'logged_in' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_password = request.form['password']
        if user_password == 'JOHNIANAGRS2016':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash(u"Wrong password!")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/Childhood')
def Childhood():
    return render_template('Childhood.html')

@app.route('/Transformation')
def Transformation():
    return render_template('Transformation.html')

@app.route('/Wedding')
def Wedding():
    return render_template('Wedding.html')
    
@app.route('/external_url/<url>')
def external_url(url):
    return redirect(url)

@app.route('/FriendsCorner')
def FriendsCorner():
    return redirect(url_for('external_url', url='https://friendscorner.vercel.app/'))
# @app.route('/FriendsCorner')
# def FriendsCorner():
#     return redirect(url_for('external_url', url='https://friendscorner.vercel.app/'))

@app.route('/external-url/<path:url>')
def external_url(url):
    return redirect(url)

# @app.route('/voice-print', methods=['POST']) 
# def upload_voice_print(): 
#     return main()
