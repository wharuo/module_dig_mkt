from flask import Blueprint, send_file
from flask_login import login_required
import pandas as pd
from services.google_analytics import initialize_analyticsreporting, get_report, parse_response
from services.twitter import get_twitter_data
from services.facebook import get_facebook_data
from services.instagram import get_instagram_data
import asyncio

export_bp = Blueprint('export', __name__)

@export_bp.route('/export/traffic')
@login_required
def export_traffic():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    data = parse_response(response)
    data.to_csv('traffic_data.csv', index=False)
    return send_file('traffic_data.csv', as_attachment=True)

@export_bp.route('/export/socialmedia')
@login_required
def export_socialmedia():
    data = asyncio.run(get_twitter_data())
    data.to_csv('social_media_data.csv', index=False)
    return send_file('social_media_data.csv', as_attachment=True)

@export_bp.route('/export/facebook')
@login_required
def export_facebook():
    data = get_facebook_data()
    data.to_csv('facebook_data.csv', index=False)
    return send_file('facebook_data.csv', as_attachment=True)

@export_bp.route('/export/instagram')
@login_required
def export_instagram():
    data = asyncio.run(get_instagram_data())
    data.to_csv('instagram_data.csv', index=False)
    return send_file('instagram_data.csv', as_attachment=True)
