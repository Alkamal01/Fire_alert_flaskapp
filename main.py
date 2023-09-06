from flask import Flask, request
import africastalking

app = Flask(__name__)


username = "sandbox"
api_key = "e526a8eb1f8ba4a51c05920267102d2faa4d58825868360762605c42c083d554"

africastalking.initialize(username, api_key)

sms = africastalking.SMS
call = africastalking.Voice


@app.route('/notify', methods=['GET'])
def handle_notification():
    message = request.args.get('Fire Detected')
    phone_number = "+2347044498532"

    response = sms.send(message, [phone_number])
    print(response)

    response = call.call(phone_number)
    print(response)

    return "Notification received", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
