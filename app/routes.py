from flask import render_template, url_for, flash, redirect, request
from werkzeug.urls import url_parse
from app import app,db
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User, Transaction, Strategy, Subscription

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('dashboard.html', page_title='Dashboard')

@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html',page_title='Users', users=users)

@app.route('/users/<strategy_id>')
@login_required
def username(strategy_id):
    user = Transaction.query.filter_by(strategy_id=strategy_id).first_or_404()
    transactions = [
        {'securityId': 261, 
        'limit': 1.20, 
        'strategyId': 4, 
        'quantity': 1666.52, 
        'side': 'SELL', 
        'accountId': 1},
        
        {'securityId': 254, 
        'limit': 1.3001, 
        'strategyId': 2, 
        'quantity': 111.00, 
        'side': 'BUY', 
        'accountId': 1}
    ]

    subscriptions = [
        {'strategyId': 1},
        {'strategyId': 2},
        {'strategyId': 4}   
        ]
    return render_template('user.html', user=user, transactions=transactions, subscriptions=subscriptions)

@app.route('/dashboard')
@login_required
def dashboard():
    #get_total_subscriptions()
    #get_total_strategies()
    #get_transaction_totals()
    return render_template('dashboard.html', page_title='Dashboard')

@app.route('/transactions')
@login_required
def transactions():
    transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=transactions)

@app.route('/transactions/<transactionId>')
@login_required
def user_transactions(transactionId):
    return render_template('transaction.html', transaction=transactionId, page_title='Transactions/{}'.format(username))

@app.route('/strategies')
@login_required
def strategies():
    strategies = Strategy.query.all()
    return render_template('strategies.html', strategies=strategies)

@app.route('/strategy/<strategyname>')
@login_required
def strategy(strategyname):
    return render_template('strategy.html', user=strategyname, page_title='Strategies/{}'.format(strategyname))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,full_name=form.full_name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now registered.")
        return redirect(url_for('login'))
    return render_template('register.html', page_title='Register', form = form)



