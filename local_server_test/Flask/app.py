from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        result = request.form
        
        return render_template('test.html', result=result)
    else:
        return render_template('test.html')
    

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        result = request.form
        return render_template('test2.html', result=result)
    else:
        return render_template('test2.html')
if __name__=='__main__':
    app.run(debug=True)

