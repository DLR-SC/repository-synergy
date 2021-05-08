# author: relbaff
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import datetime
from . import PAGES, controller, models


import pandas as pd
import csv, io

### Helper Function
def set_context(request):
    context = {
        'username': request.session['username'],
        'fullname': request.session['fullname'],
        'is_staff': request.session['is_staff'],
        'batch': request.session['batch'],
    }
    return context

def is_logged_in(request):
    return 'username' in request.session.keys() and request.session['username'] is not None

def is_batch_assigned(request):
    return 'batch' in request.session.keys() and request.session['batch'] is not None

def is_admin(request):
    return 'is_staff' in request.session.keys() and request.session['is_staff'] is True

def checkbox_value(request, key):
    return True if key in request.POST.keys() and request.POST[key] == 'on' else False
#### Views
def index(request):
    if is_logged_in(request):
        return dashboard(request)
    return render(request, PAGES.LOGIN_PAGE)


### Login
def login(request):
    if is_logged_in(request):
        return dashboard(request)

    context = {}
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        user.last_login = timezone.now()
        user.save()

        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['is_staff'] = user.is_staff
        request.session['fullname'] = ('{} {}').format(user.first_name, user.last_name)
        request.session['batch'] = user.batch

        return dashboard(request)

    else:
        context['message'] = PAGES.MESSAGE_LOGIN_FAILED
        context['message_type'] = PAGES.MESSAGE_TYPE_ALERT
        return render(request, PAGES.LOGIN_PAGE, context)


## Logout
def logout(request):
    request.session.flush()
    return render(request, PAGES.LOGIN_PAGE)


## Dashboard: shows progress for each bacth
def dashboard(request):
    if not is_logged_in(request) :
        return index(request)

    context = set_context(request)

    if is_admin(request):
        return render(request, PAGES.ADMIN_DASHBOARD_PAGE, context)

    if not is_batch_assigned(request):
        return render(request, PAGES.ERROR_PAGE)


    # get a list of all the pairs and if they are annotated or not with synergy and view with repo_pair id
    repo_pairs, total, annotated = controller.get_annotations_info(request.session['user_id'], request.session['batch'])
    context['repo_pairs'] = repo_pairs
    context['total'] = total
    context['annotated'] = annotated
    return render(request, PAGES.DASHBOARD_PAGE, context)



def annotate(request, pair_id):

    if not is_logged_in(request):
        return index(request)

    if not is_batch_assigned(request):
        return render(request, PAGES.ERROR_PAGE)
    # Grab the readme files for repo1 and repo2
    ## 1. get repo names
    readme1, readme2 = controller.get_repo_pair_info(pair_id)

    context = set_context(request)
    context['readme1'] = readme1
    context['readme2'] = readme2
    context['annotated'] = False
    context['pair_id'] = pair_id

    # check if repo exists
    annotation = models.Annotation.getAnnotation(request.session['user_id'], pair_id)
    if annotation is not None:
        context['explanation'] = annotation.explanation
        context['synergy'] = annotation.synergy
        context['direction'] = annotation.direction

    context['total'] = len(models.RepositoryPair().getBatchRepoPairs(context['batch']))
    context['annotated'] = len(models.Annotation.objects.filter(user=request.session['user_id']))


    return render(request, PAGES.ANNOTATION_PAGE, context)

def save_annotation(request):
    if  not is_logged_in(request):
        return index(request)

    if not is_batch_assigned(request):
        return render(request, PAGES.ERROR_PAGE)

    user_id = request.session['user_id']
    batch = request.session['batch']
    pair_id = request.POST['pair_id']

    synergy = request.POST['synergyQuestion']
    direction = request.POST['directionQuestion'] if 'directionQuestion' in request.POST.keys() else 0
    explanation = request.POST['explanation']

    u = models.User.objects.get(pk=user_id)
    annotation = models.Annotation.getAnnotation(user_id, pair_id)
    if annotation == None: #create
        u.annotation_set.create(repository_pair_id=pair_id, synergy=synergy, direction=direction,
                                explanation=explanation, annotation_date=datetime.now())
    else: # update
        annotation.synergy = synergy
        annotation.direction = direction
        annotation.explanation = explanation
        annotation.save()

    next_pair= controller.get_next_unnotated_pair(user_id, batch)
    if next_pair == None:
        return dashboard(request)

    return annotate(request,  next_pair)

### Admin pages: create user, upload repo-pair  and download annotations
def create_show_users(request):
    if not is_logged_in(request) or not is_admin(request):
        return index(request)

    context = set_context(request)

    if request.method != 'GET':

        user, created = models.User.objects.update_or_create(
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname'],
            username=request.POST['username'],
            email = request.POST['email'],
            batch = request.POST['batch'] if not checkbox_value(request, 'staff') else None,
            is_staff =  checkbox_value(request, 'staff'),
            is_active = checkbox_value(request, 'active'),

        )
        user.set_password(request.POST['password'])
        user.save()

    context['users_data'] = models.User.objects.all()

    return render(request, PAGES.USERS_PAGES, context)

def upload_repopairs(request):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)

    context = set_context(request)

    if request.method != 'GET':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a .csv file with the following order: 'id'	"
                                    "'repo_url1'	'repo_description1'	'repo_url2'	'repo_description2'	'score'	'is_random'	'algorithm'	'batch'")
        else:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string) # skip header
            for column in csv.reader(io_string, delimiter=','):
                repopair, created = models.RepositoryPair.objects.update_or_create(
                    id = int(column[0]),
                    defaults = {
                        'repo_url1' : column[1],
                        'repo_description1' : column[2],
                        'repo_url2' : column[3],
                        'repo_description2' : column[4],
                        'score': float(column[5]),
                        'is_random': (True if column[6].strip() == 'True' else False),
                        'algorithm': column[7],
                        'batch': column[8],

                    }
                )
                repopair.save()

    context['repo_pairs_data'] = models.RepositoryPair.objects.all()
    context['count'] = len(models.RepositoryPair.objects.all())
    return render(request, PAGES.UPLOAD_REPO_PAIRS, context)


def download_annotations(request):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)
    return controller.export_to_csv(models.Annotation)

def download_users(request):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)
    return controller.export_to_csv(models.User)

def download_repo_pairs(request):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)
    return controller.export_to_csv(models.RepositoryPair)

def view_annotations(request, batch_num):

    if  not is_logged_in(request) or not is_admin(request):
        return index(request)

    context = set_context(request)
    context['annotations_data'], context['annotated_count'], context['total_count'] = controller.get_all_annotations(batch_num)
    context['batch_num'] = batch_num
    return render(request, PAGES.VIEW_ANNOTATIONS_PAGE, context)

def deactivate_user(request, user_id):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)

    controller.deactivate_user(user_id)
    return create_show_users(request)

def activate_user(request, user_id):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)

    controller.activate_user(user_id)
    return create_show_users(request)

def download_annotations_view(request, batch_num):
    if  not is_logged_in(request) or not is_admin(request):
        return index(request)
    ann_df, _, _ =  controller.get_all_annotations(batch_num)
    return controller.export_to_csv(df=ann_df, name='batch{}_annotations'.format(batch_num))