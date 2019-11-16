from flask import render_template, request, Blueprint,flash
from localingredients import db
from localingredients.models import Recipe

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home",methods=['GET', 'POST'])
def home():
    if(request.method=="POST"):
        return str(request.form)
    db.create_all()
    page = request.args.get('page', 1, type=int)
    """ posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) """
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')
@main.route("/recipelist")
def recipelist():
    recipelist = Recipe.query.all()
    return render_template('recipelist.html', recipelist=recipelist)
