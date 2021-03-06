from flask import Flask,session,redirect,url_for,escape,request
app= Flask(__name__)
app.secret_key= b'ee\n\xbb\x81\xf2\xf5\x96s$D\x7fZ\r\xeaL'
app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	else:
		return 'you are not logged in '

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
		<form method="post">
			<p><input type=text name=username>
			<p><input type=submit value=login>
		</form>
	'''
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))
