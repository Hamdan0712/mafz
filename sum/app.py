from flask import Flask, render_template, request
from sum import Sum  

app = Flask(__name__)
instance_sum=Sum()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = instance_sum.addtwonumber(num1, num2)  
        return str(result)

if __name__ == '__main__':
    app.run(debug=True)
