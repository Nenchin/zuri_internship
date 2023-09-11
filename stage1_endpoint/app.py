import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    # query request parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # the current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # the current UTC time (accurate within +/- 2 minutes)
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    # GitHub file URL and repo URL
    github_file_url = 'https://github.com/Nenchin/zuri_internship/blob/master/stage1_endpoint/app.py'
    github_repo_url = 'https://github.com/Nenchin/zuri_internship/tree/master/stage1_endpoint'

    # the response JSON object
    response = {
        'Slack_Name': slack_name,
        'track': track,
        'current_day': current_day,
        'current_utc_time': current_time,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200  # HTTP status code
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
