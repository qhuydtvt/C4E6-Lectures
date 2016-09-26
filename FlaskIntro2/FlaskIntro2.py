from flask import *

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return '<h1>C4E6 Hello everyone</h1>'

name1 = "Elon Musk"
name2 = "Bill Gates"
img1 = "https://lh5.googleusercontent.com/-89xTT1Ctbrk/AAAAAAAAAAI/AAAAAAAABcc/Kg0vilTzpKI/photo.jpg"

class Person: #class
    def __init__(self, name, img): #constructor
        self.name = name
        self.img = img

elon_musk = Person(
    "Elon musk",
    "https://lh5.googleusercontent.com/-89xTT1Ctbrk/AAAAAAAAAAI/AAAAAAAABcc/Kg0vilTzpKI/photo.jpg"
) #object

bill_gates = Person(
    "Bill gates",
    "https://pbs.twimg.com/profile_images/558109954561679360/j1f9DiJi.jpeg"
) #object

mark_zuckerberg = Person(
    "Mark Zuckerberg",
    "http://a4.files.biography.com/image/upload/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTIwNjA4NjMzNjg3ODAzNDA0.jpg"
)


person_list = [elon_musk, bill_gates, mark_zuckerberg] #1

person_dict = {
    "elon-musk" : elon_musk,
    "bill-gates" : bill_gates
}

@app.route('/new')
def new():
    return redirect(url_for('techkids'))

@app.route('/<name>')
def hello(name):
    return "Hello {0}".format(name)


@app.route('/')
@app.route('/elon-musk')
def view_elon_musk():
    return render_template("rolemodel.html", person=elon_musk)

@app.route("/rm")
def view_role_models():
    return render_template("rolemodels.html", person_list=person_list)

@app.route('/school')
def techkids():
    return redirect("http://techkids.vn")

@app.route('/rm2/<name>')
def view_role_model2(name):
    if name not in person_dict:
        return "Role model not found"
    else:
        return render_template("rolemodel.html", person = person_dict[name])

@app.route('/rm/<int:index>')
def view_role_model(index):
    return render_template("rolemodel.html", person = person_list[index])

if __name__ == '__main__':
    app.run()
