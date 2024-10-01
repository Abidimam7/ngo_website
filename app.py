from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        # Process the donation here
        donor_name = request.form['name']
        amount = request.form['amount']
        # Add logic for payment gateway here (Razorpay/Stripe/PayPal)
        return f"Thank you {donor_name} for donating ${amount}!"
    return render_template('donation.html')

#app = Flask(__name__, static_folder='static')


if __name__ == '__main__':
    app.run(debug=True)
