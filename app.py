from flask import Flask, request, jsonify, redirect, url_for, make_response, render_template

app = Flask(__name__)

# 1ª Forma de criar rotas, foi muito utilizada no inicio dos usos do Flask


@app.route('/<name>/<int:age>', methods=['POST'])
def main(name, age):
    return 'Hello %s and my age is %s' % (name, age), 200


@app.route('/redirected', methods=['GET'])
def redirected():
    return "Redirected \o/\ô/", 200


@app.route('/request', methods=['POST'])
def request_data():
    # request.form['nome']
    person = request.args.get('person')
    return 'Hello my name is %s and I have %s years old' % (request.form['name'], request.form['age'])


@app.route('/request/v2', methods=['POST'])
def request_data_two():
    # request.form['nome']
    print("method: ", request.method)
    print("User-Agent:", request.headers.get('User-Agent'))
    print("Content-Length:", request.headers.get('Content-Length'))
    print("headers: ", request.headers)
    print("path: ", request.path)
    print("base_url: ", request.base_url)
    print("values: ", request.values)
    print("args: ", request.args)
    print("form: ", request.form)
    # print("json: ", request.json)
    # print("environ: ", request.environ)
    # print("date: ", request.date)
    print("url: ", request.url)
    print("blueprint: ", request.blueprint)
    print("endpoint: ", request.endpoint)
    print("host: ", request.host)
    print("host_url: ", request.host_url)
    print("origin: ", request.origin)
    person = request.args.get('person')
    return 'Hello my name is %s and I have %s years old e meu CPF é %s' % (request.form['name'], request.form['age'], person)


@app.route('/response', methods=['POST'])
def response_data():
    obj = {
        'username': 'higorsouza',
        'facebook': 'https://fb.me/higorsouza',
        'github': 'https://github.com/higorsouza83'
    }

    return jsonify(data = obj), 200


@app.route('/response', methods=['GET'])
def response_data_get():
    obj = {
        'username': 'higorsouza',
        'facebook': 'https://fb.me/higorsouza',
        'github': 'https://github.com/higorsouza83'
    }

    # return redirect(url_for('redirected'))
    return redirect('/redirected', code=302)


@app.route('/responsee', methods=['POST'])
def response_data_tree():
    obj = {
        'username': 'higorsouza',
        'facebook': 'https://fb.me/higorsouza',
        'github': 'https://github.com/higorsouza83'
    }

    resp = make_response(jsonify(data=request.form), 201)
    resp.headers['Couse-Powered-By'] = 'São João <Da Cruz>'
    return resp


@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return redirect(url_for('result', name=request.form['name']))


@app.route('/result/<name>', methods=['GET'])
def result(name):
    return render_template('main.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# 2ª Forma de criar rotas, foi muito utilizada no inicio dos usos do Flask
# def main():
#     return 'Hello Higor', 200
#
# app.add_url_rule('/', 'main', main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
