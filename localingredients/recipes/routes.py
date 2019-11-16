from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint,jsonify)
from flask_login import current_user, login_required
from localingredients import db
from localingredients.models import Recipe
from localingredients.recipes.forms import RecipeForm,CardForm
from localingredients.users.utils import save_picture
import json
recipes = Blueprint('recipes', __name__)

"""
@stores.route("/store/new", methods=['GET', 'POST'])
@login_required
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        store = Store(title=form.title.data, author=current_user,code=form.Code.data)
        db.session.add(store)
        db.session.commit()
        flash('Your Store has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_store.html', title='New Store',
                           form=form, legend='New Store')

@stores.route("/store/<string:store_name>/<string:mode>",methods=['GET','POST'])
def store(store_name,mode):
    if(current_user.is_authenticated):
        store = Store.query.filter_by(title=store_name).first()
        if(store==None):
            abort(404)
        elif store.author != current_user:
            abort(403)
        else:
            if(request.method=='POST'):
                form = CardForm()
                if form.validate_on_submit():
                    if form.picture.data:
                        picture_file = save_store_material(form.picture.data,store_name)
                    else:
                        flash('No Image Chosen!', 'warning')
                else:
                    flash('Upload failed for some reason :( only png and jpg are supported!', 'warning')
                return redirect(url_for('stores.store',store_name=store_name,mode=mode))
            else:
                if(mode=="dashboard"):
                    return render_template('store_dashboard.html', title=store.title, store=store)
                elif(mode=="design"):
                    form = CardForm()
                    store_uploaded_images = storeass.get_ass(store_name)
                    total = int(len(store_uploaded_images) //6)
                    return render_template('store_design.html', title=store.title, 
                        store=store,form=form,store_uploaded_images=store_uploaded_images,
                        store_uploaded_images_length=len(store_uploaded_images),page=0,
                         total_page_num=total)
                elif(mode=="messages"):
                    return render_template('store_messages.html', title=store.title, store=store)
                elif(mode=="settings"):
                    return render_template('store_settings.html', title=store.title, store=store)
    else:
        flash('please login first!','error')
        return redirect(url_for('main.home'))

@stores.route("/get-started")
def get_started():
    return render_template('get-started.html', type="store")

@stores.route("/save-state",methods=['POST'])
def save_state():
    if request.method == 'POST':
        a = request.get_json()
        if(a !=None):
            return "wsk",200   # parse as JSON
        else:
            return "not WSK"

@stores.route("/mystores")
def manage_stores():
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        stores = Store.query.filter_by(author=current_user)\
        .order_by(Store.date_posted.desc())\
        .paginate(page=page, per_page=5)
        return render_template("manage_stores.html",stores=stores,user=current_user)
    else:
        return redirect(url_for('users.login'))
@stores.route("/store/<int:store_id>/update", methods=['GET', 'POST'])
@login_required
def update_store(store_id):
    store = Store.query.get_or_404(store_id)
    if store.author != current_user:
        abort(403)
    form = StoreForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        store.image_file = picture_file
        store.title = form.title.data
        store.code = form.Code.data
        db.session.commit()
        flash('Your Code has been updated!', 'success')
        return redirect(url_for('stores.store', store_name=store.title,mode="dashboard"))
    elif request.method == 'GET':
        form.title.data = store.title
        form.Code.data = store.code
    return render_template('create_store.html', title='Update Store',
                           form=form, legend='Update Store')

@stores.route("/store/<int:store_id>/delete", methods=['POST'])
@login_required
def delete_store(store_id):
    store = Store.query.get_or_404(store_id)
    if store.user_id != current_user.id:
        abort(403)
    db.session.delete(store)
    db.session.commit()
    flash('Your store has been deleted!', 'success')
    return redirect(url_for('main.home'))
"""