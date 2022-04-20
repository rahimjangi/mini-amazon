from flask import Flask
from flask_restful import Api
from security import identity,authenticate

app = Flask(__name__)
app.secret_key='my_super_secret_key'
api = Api(app)







if __name__=="__main__":
    app.run(port=3000,debug=True)