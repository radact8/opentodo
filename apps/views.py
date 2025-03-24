from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from flask_wtf import FlaskForm

import datetime
import time

import main
import forms
import db
import models
import os
import time



@main.app.route('/')
def index():
    db.create_user_table()
    return redirect(url_for('login'))

@main.app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        db_user = db.get_user()
        users_num = len(db_user)
        users = []
        for i in range(users_num):
            users.append(models.User(id=db_user[i][0],username=db_user[i][1],password=db_user[i][2]))
        user = next((u for u in users if u.username == form.username.data), None)
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')

    
    return render_template("login.html",form=form)


@main.app.route('/add_user_info',methods=["GET","POST"])
def add_user_info():
    form = forms.AddUser()
    if form.validate_on_submit():
       #user = next((u for u in main.users.values() if u.username == form.username.data), None)
       username = form.username.data
       password = form.password.data
       db.add_user(username,password)
       return redirect(url_for('login'))
    return render_template('adduser.html',form=form)

@main.app.route('/dashboard')
@login_required
def dashboard():
    name=current_user.username+"Task"
    db.create_tasks_table(name)
    tasks = db.get_users_task(name)
    db.create_task_results(current_user.username)
    now_result_num = db.get_result_size(current_user.username)
    if(now_result_num == 0):
        db.task_insert_day_change(current_user.username)

    views_result = []
    todays_result = db.get_todays_result(current_user.username)
    print("-----------")
    print(todays_result)
    check_emptys = db.get_check_empty(current_user.username)
    
    for i in range(7):
        if(check_emptys[i] == 0):
            views_result.append("No")
        else:
            if(todays_result[i] == 0):
                views_result.append("x")
            else:
                views_result.append("o")
    
    date = datetime.date.today().strftime("%Y/%m/%d")
    date = date
    print(views_result)
    return render_template('dashboard.html',tasks=tasks,views_result=views_result,date=date)

@main.app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@main.app.route('/add_task')
def add_task():
    return render_template('addtask.html')

@main.app.route('/add_task0',methods=["GET","POST"])
def add_task0():
    name = current_user.username
    namefortask = name+'0'
    task_name=request.form[namefortask]
    print(task_name)
    tablename = name+"Task"
    db.sql_add_task(name,tablename,0,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task1',methods=["GET","POST"])
def add_task1():
    name = current_user.username
    namefortask = name+'1'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,1,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task2',methods=["GET","POST"])
def add_task2():
    name = current_user.username
    namefortask = name+'2'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,2,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task3',methods=["GET","POST"])
def add_task3():
    name = current_user.username
    namefortask = name+'3'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,3,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task4',methods=["GET","POST"])
def add_task4():
    name = current_user.username
    namefortask = name+'4'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,4,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task5',methods=["GET","POST"])
def add_task5():
    name = current_user.username
    namefortask = name+'5'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,5,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task6',methods=["GET","POST"])
def add_task6():
    name = current_user.username
    namefortask = name+'6'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,6,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/add_task7',methods=["GET","POST"])
def add_task7():
    name = current_user.username
    namefortask = name+'7'
    task_name=request.form[namefortask]
    tablename = name+"Task"
    db.sql_add_task(name,tablename,7,task_name)
    return redirect(url_for('dashboard'))

@main.app.route('/update0',methods=["GET","POST"])
def update0():
    name = current_user.username
    db.update_doing(name,0)
    return redirect(url_for('dashboard'))

@main.app.route('/update1',methods=["GET","POST"])
def update1():
    name = current_user.username
    db.update_doing(name,1)
    return redirect(url_for('dashboard'))

@main.app.route('/update2',methods=["GET","POST"])
def update2():
    name = current_user.username
    db.update_doing(name,2)
    return redirect(url_for('dashboard'))

@main.app.route('/update3',methods=["GET","POST"])
def update3():
    name = current_user.username
    db.update_doing(name,3)
    return redirect(url_for('dashboard'))

@main.app.route('/update4',methods=["GET","POST"])
def update4():
    name = current_user.username
    db.update_doing(name,4)
    return redirect(url_for('dashboard'))

@main.app.route('/update5',methods=["GET","POST"])
def update5():
    name = current_user.username
    db.update_doing(name,5)
    return redirect(url_for('dashboard'))

@main.app.route('/update6',methods=["GET","POST"])
def update6():
    name = current_user.username
    db.update_doing(name,6)
    return redirect(url_for('dashboard'))

@main.app.route('/result_test')
def result_test():
    size = db.get_result_size(current_user.username)
    tasknames = db.get_result_taskname(current_user.username)
    view_num = db.get_per(current_user.username)
    return render_template('resultTest.html',size=size,tasknames=tasknames,view_num=view_num)
