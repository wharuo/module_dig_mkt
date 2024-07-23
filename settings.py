from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
import json

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/dashboard/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        global settings
        settings['google_analytics']['key_file_location'] = request.form['ga_key_file_location']
        settings['google_analytics']['view_id'] = request.form['ga_view_id']
        settings['twitter']['consumer_key'] = request.form['twitter_consumer_key']
        settings['twitter']['consumer_secret'] = request.form['twitter_consumer_secret']
        settings['twitter']['access_token'] = request.form['twitter_access_token']
        settings['twitter']['access_token_secret'] = request.form['twitter_access_token_secret']
        settings['twitter']['handle'] = request.form['twitter_handle']
        settings['facebook']['access_token'] = request.form['facebook_access_token']
        settings['instagram']['access_token'] = request.form['instagram_access_token']
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        return redirect(url_for('dashboard.index'))
    return render_template('settings.html', settings=settings)
