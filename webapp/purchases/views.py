from flask import Blueprint, current_app, render_template
from webapp.purchases.models import Purchases


blueprint = Blueprint('purchases', __name__)

@blueprint.route('/')
@blueprint.route('/index')
def index():
    news_list = Purchases.query.order_by(Purchases.date.desc()).all()
    title = 'Аналитика расходов'
    return render_template('purchases/index.html', title=title, news_list=news_list)