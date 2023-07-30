from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import YourQuestionForm, YourAnswerForm  # Replace with the actual forms you created
from .models import Question, Answer

def index(request):
    return render(request, 'index.html')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = YourQuestionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = request.user
            question = Question.objects.create(title=title, content=content, author=author)
            return redirect('view_questions')  # Redirect to the view_questions page after successful post
    else:
        form = YourQuestionForm()  # Assuming you have created a form named YourQuestionForm
    return render(request, 'post_question.html', {'form': form})

@login_required
def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = YourAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('view_questions')  # Remove the 'question_id' parameter from the redirection
    else:
        form = YourAnswerForm()

    return render(request, 'answer_question.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    user = request.user

    if user in answer.likes.all():
        answer.likes.remove(user)
    else:
        answer.likes.add(user)

    return redirect('view_questions')  # Redirect to the view_questions page after liking/unliking an answer

def register(request):
    if request.method == 'POST':
        form = YourUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = YourUserRegistrationForm()  # Assuming you have created a form named YourUserRegistrationForm
    return render(request, 'registration/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')