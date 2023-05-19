# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'Thanu' and password == '5512':   
        account_sid = 'AC72e54035f90fec23cead8648f3076b29'
        auth_token = '2091ce744d6a81e746acf75863a7a622'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VAe0f3450d7ed22714026ed6e2cb6e04a1') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')
    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC72e54035f90fec23cead8648f3076b29'
    auth_token = '2091ce744d6a81e746acf75863a7a622'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VAe0f3450d7ed22714026ed6e2cb6e04a1') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://collaborative-document-c272.onrender.com")


if __name__ == "__main__":
    app.run()

