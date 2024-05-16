from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/v1/classify', methods=['GET'])
def hello():
    # extract the data from the request
    text = request.args.get('text', None)

    # prepare the response
    response = {
        'data': '',
        'status': 'success'
    }
    status = 200
    # handle if text is None
    if(text is None):
        response['status'] = 'Text is missing'
        status = 400 # bad request code
    else:
        # classify
        response['data'] = 'Spam'

    return jsonify(response), 200



if __name__ == '__main__':
    app.run(debug=True)