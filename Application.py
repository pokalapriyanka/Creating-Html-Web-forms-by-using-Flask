from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
FAI=Flask(__name__)

@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        fd=request.form
        return fd['un']
    return render_template('htmlforms.html')

class NameForm(Form):
    Sname=StringField(validators=[DataRequired()])
    submit=SubmitField()

@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    ENFO=NameForm()
    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.data
    return render_template('webforms.html',ENFO=ENFO)


if __name__=='__main__':
    FAI.run(debug=True)