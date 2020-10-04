from flask import Flask
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamoTable = dynamodb.Table('images')
app = Flask(__name__)

@app.route('/')
def index():
    response = dynamoTable.scan()
    data = response['Items']
    url = ''
    for valor in data:
        url = valor['url']
    return '<h1 style="text-align: center;">Arthur Coutinho Santos</h1><h1 style="text-align: center;">RM336256</h1><div style="display: flex;justify-content: center;"><img src="%s" /></div>' % (url)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)