from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms import ValidationError

#Валидатор, который проверяет одинаковость двух паролей
def validate_password(form, field):
    if field.data != form.data['password']:
        raise ValidationError('Password incorrect!')

class ContactForm(FlaskForm):
    email = StringField(validators=[
        validators.Email()
    ])
    password = StringField(validators=[
        validators.Length(min=6, max=25)
    ])
    passw_2 = StringField(validators=[
        validators.Length(min=6, max=25),
        validate_password
    ])



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

#------------------------------------------------------
#По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
#Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают.
#Возрващать пользователю json вида: "status" - 0 или 1 (если ошибка валидации), "errors" - список ошибок, если они есть, или пустой список.
@app.route('/form/user', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = ContactForm(request.form)
        print(form.validate())
        print(form.errors)
        if form.validate():
            form.errors['s']=0
        else:
            form.errors['s']=1
        return jsonify(form.errors)
    return 'hello world!', 200
#-------------------------------------------------------
#По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
@app.route('/locales')
def get_json():
    l = ['ru', 'en', 'it']
    return jsonify(l)
#-------------------------------------------------------
#По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
@app.route('/sum/<int:first>/<int:second>')
def get_sum(first,second):
    return 'summ = {}!'.format(first+second)
#-------------------------------------------------------
#По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<user_name>')
def get_user(user_name):
    return 'Hello, {}!'.format(user_name)
#-------------------------------------------------------
#По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
#Файлы можно туда положить любые текстовые. А если такого нет - 404
@app.route('/serve/<path:filename>')
def get_text_file(filename):
    f = open('./files/'+filename, 'r')
    a = f.read()
    f.close()
    return a
#--------------------------------------------------------

if __name__ == '__main__':
    app.run()
