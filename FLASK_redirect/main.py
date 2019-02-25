from flask import Flask, render_template_string
import os
from subprocess import call

call(['sudo', 'rm', '/etc/nginx/sites-available/ride-proxy'])
call([
    'sudo', 'cp', '/ride/work/ride-proxy',
    '/etc/nginx/sites-available/ride-proxy'
])
call(['sudo', '/etc/init.d/nginx', 'reload'])

sessionId = os.environ.get('RBRAIN_SESSION_ID')

app = Flask(__name__)
print(app.url_map)


@app.route('/index')
@app.route('/')
def index():
    #return render_template('questions.html')
    return render_template_string("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Questions</title>
</head>
<body>
<a href = "{{ url_for('question',question_id=1) }}">Question 1</a>
<a href = "{{ url_for('question',question_id=2) }}">Question 2</a>
</body>
</html>
""")


@app.route(
    '/' + sessionId + '/p/5000/question/<int:question_id>'
)  #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def question(question_id):
    return ('you asked for question{0}'.format(question_id))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

