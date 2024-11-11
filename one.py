from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def example_page():
    return ('good job')

@app.route('/example/<num>')
def example_page_number(num):
    #num = int(num)
    #return jsonify ({ num : "is the page number you are looking for " })
    return jsonify({"message": f'You are looking for page number: {num}'})

if __name__ == "__main__":
    app.run(debug=True)