from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
 
@app.route('/about')
def about():
    posts=[
        {
            'name':"nitesh",
            "roll":21
        },
        {
            'name':"sahu",
            "roll":3
        }
    ]
    title="title provided"
    return render_template("about.html",posts=posts,title=title)
 
if __name__ == '__main__':
   app.run(port=8090,host='localhost',debug=True)
   
