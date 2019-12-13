from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/x_power_y_request')
def x_power_y_request():
    return render_template("x_power_y_req.html")


@app.route('/x_power_y_response', methods=["POST"])
def x_power_y_response():
    power_value = request.form.get("x_value")
    base_value = request.form.get("y_value")
    flask_obj = ScientificCalc()
    x_power_y_value = flask_obj.var_initialization(power_value, base_value)
    return render_template("x_power_y_res.html", result=x_power_y_value)


@app.route('/tangent_req')
def tangent_req():
    return render_template("tangent_req.html")


@app.route('/tangent_res', methods=["POST"])
def tangent_res():
    angle_value = request.form.get("tan_value")
    flask_obj = ScientificCalc()
    tan_angle_value = flask_obj.tan_fun(angle_value)
    return render_template("tangent_res.html", result=tan_angle_value)


@app.route('/10_power_x_request')
def ten_power_x_request():
    return render_template("10_power_x_req.html")


@app.route('/10_power_x_response', methods=["POST"])
def ten_power_x_response():
    x_value = request.form.get("value_x")
    flask_obj = ScientificCalc()
    ten_power_x_value = flask_obj.cal_power_ten(x_value)
    return render_template("x_power_y_res.html", result=ten_power_x_value)


@app.route('/factorial_request')
def factorial_request():
    return render_template("factorial_req.html")


@app.route('/factorial_response', methods=["POST"])
def factorial_response():
    f_value = request.form.get("fact_value")
    flask_obj = ScientificCalc()
    fact_result = flask_obj.factorial(f_value)
    return render_template("factorial_res.html", result=fact_result)


@app.route("/cos_req")
def calculate_cos_request():
    return render_template('cos_req.html')


@app.route("/cos_res", methods=['POST'])
def calculate_cos_response():
    if request.method == 'POST':
        angle = request.form['angle']
        calculate_cos_obj = ScientificCalc()
        cos_result = calculate_cos_obj.calculate_cos(angle)
    return render_template('cos_res.html', value=cos_result)


@app.route("/cosh_req")
def cosh_req():
    return render_template('cosh_req.html')


@app.route("/cosh_res", methods=['POST'])
def cosh_res():
    angle = request.form.get('input')
    cosh_obj = ScientificCalc()
    cosh_result = cosh_obj.trig_cosh(angle)
    return render_template('cosh_response.html', value=cosh_result)


@app.route('/e_power_x_req')
def e_power_x_req():
    return render_template('e_power_x_req.html')


@app.route('/e_power_x_res', methods=['POST'])
def e_power_x_res():
    power_value = request.form['input']
    e_power_x_obj = ScientificCalc()
    e_power_x_result = e_power_x_obj.exponential_func(power_value)
    return render_template('e_power_x_res.html', value=e_power_x_result)


@app.route("/ln_req")
def ln_req():
    return render_template('ln_req.html')


@app.route("/ln_res", methods=['POST'])
def ln_res():
    angle = request.form.get('input')
    ln_obj = ScientificCalc()
    ln_result = ln_obj.ln_func(angle)
    return render_template('ln_response.html', value=ln_result)


@app.route("/radian_req")
def radian_req():
    return render_template('rad_req.html')


@app.route("/radian_res", methods=['POST'])
def radian_res():
    angle = request.form.get('input')
    rad_obj = ScientificCalc()
    rad_result = rad_obj.rad(angle)
    return render_template('rad_res.html', value=rad_result)


@app.route("/addition_req")
def addition_req():
    return render_template('addition_req.html')


@app.route("/addition_res", methods=['POST'])
def addition_res():
    num1 = request.form.get('input1')
    num2 = request.form.get('input2')
    list_add = [num1, num2]
    c1 = ScientificCalc()
    result = c1.addition(list_add)
    return render_template('addition_response.html', value=result)


@app.route("/subtraction_req")
def subtraction_req():
    return render_template('subtraction_req.html')


@app.route("/subtraction_res", methods=['POST'])
def subtraction_res():

    num1 = request.form.get('input1')
    num2 = request.form.get('input2')
    list_sub = [num1, num2]
    c1 = ScientificCalc()
    result = c1.subtraction(list_sub)
    return render_template('subtraction_response.html', value=result)


@app.route("/multiplication_req")
def multiplication_req():
    return render_template('multiplication_req.html')


@app.route("/multiplication_res", methods=['POST'])
def multiplication_res():
    num1 = request.form.get('input1')
    num2 = request.form.get('input2')
    list_mul = [num1, num2]
    c1 = ScientificCalc()
    result = c1.multiplication(list_mul)
    return render_template('multiplication_response.html', value=result)


@app.route("/division_req")
def division_req():
    return render_template('division_req.html')


@app.route("/division_res", methods=['POST'])
def division_res():
    num1 = request.form.get('input1')
    num2 = request.form.get('input2')
    list_div = [num1, num2]
    c1 = ScientificCalc()
    result = c1.division(list_div)
    return render_template('division_response.html', value=result)


@app.route("/cube_root_req")
def cube_root_req():
    return render_template('cube_root_req.html')


@app.route("/cube_root_res", methods=['POST'])
def cube_root_res():
    number1 = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.cube_root(number1)
    return render_template('cube_root_res.html', value=result)


@app.route("/sin_req")
def sin_req():
    return render_template('sin_request.html')


@app.route("/sin_res", methods=['POST'])
def sin_res():
    angle = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.sin_func(angle)
    return render_template('sin_response.html', value=result)


@app.route("/sineh_req")
def sineh_req():
    return render_template('sinh_request.html')


@app.route("/sineh_res", methods=['POST'])
def sinh_res():
    angle = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.sine_h(angle)
    return render_template('sinh_response.html', value=result)


@app.route("/tanh_req")
def tanh_req():
    return render_template('tanh_req.html')


@app.route("/tanh_res", methods=['POST'])
def tanh_res():
    angle = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.calculate_tanh(angle)
    return render_template('tanh_response.html', value=result)


@app.route("/square_root_req")
def square_root_req():
    return render_template('square_root_request.html')


@app.route("/square_root_res", methods=['POST'])
def square_root_res():
    value = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.square_root(value)
    return render_template('square_root_response.html', value1=result)


@app.route("/one_by_x_req")
def one_by_x_req():
    return render_template('one_by_x_request.html')


@app.route("/one_by_x_res", methods=['POST'])
def one_by_x_res():
    number = request.form.get('input')
    ca1c = ScientificCalc()
    result = ca1c.one_by_x(number)
    return render_template('one_by_x_response.html', value=result)


if __name__ == '__main__':
    app.run(debug=True)
