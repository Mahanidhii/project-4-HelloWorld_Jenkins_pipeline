from Flask import Flask 
app=Flask(__name__)
@app.route('/')
def hello_world();
     Return 'Hello, Jenkins!'

If __name__=='__main__'
     app.run(host='0.0.0.0',port=5000)