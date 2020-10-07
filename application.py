from flask import Flask
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamoTable = dynamodb.Table('images')

application = Flask(__name__)

@application.route("/")
def index():
    response = dynamoTable.scan()
    data = response['Items']
    url = ''
    for valor in data:
        url = valor['url']
    return '<img src="%s" /></div>' % (url)

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)
