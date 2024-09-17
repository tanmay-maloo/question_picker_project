# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .question_picker import QuestionPicker
import os

def get_sheet_path(username):
    sheet_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sheets')
    user_sheet = os.path.join(sheet_dir, f'{username}.json')
    return user_sheet if os.path.exists(user_sheet) else os.path.join(sheet_dir, 'default.json')

@login_required
def dashboard(request):
    sheet_path = get_sheet_path(request.user.username)
    picker = QuestionPicker(sheet_path)
    
    context = {
        'random_question': picker.get_random_unsolved_question(),
        'suggested_questions': picker.get_suggested_questions(),
        'favorite_questions': picker.get_favorite_questions(),
        'topic_progress': picker.get_topic_progress(),
    }
    return render(request, 'dashboard.html', context)

@login_required
def mark_done(request, question_id):
    sheet_path = get_sheet_path(request.user.username)
    picker = QuestionPicker(sheet_path)
    picker.mark_question_done(question_id)
    return redirect('dashboard')

@login_required
def mark_favorite(request, question_id):
    sheet_path = get_sheet_path(request.user.username)
    picker = QuestionPicker(sheet_path)
    picker.mark_question_favorite(question_id)
    return redirect('dashboard')

@login_required
def reset_sheet(request):
    sheet_path = get_sheet_path(request.user.username)
    picker = QuestionPicker(sheet_path)
    backup_file = picker.reset_sheet()
    return redirect('dashboard')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def restore_progress(request):
    if request.method == 'POST':
        backup_file = request.POST.get('backup_file')
        if backup_file:
            sheet_path = get_sheet_path(request.user.username)
            sheet_dir = os.path.dirname(sheet_path)
            backup_path = os.path.join(sheet_dir, backup_file)
            
            if os.path.exists(backup_path):
                # Restore the backup
                with open(backup_path, 'r') as src, open(sheet_path, 'w') as dst:
                    dst.write(src.read())
                
                return redirect('dashboard')
    
    return redirect('dashboard')