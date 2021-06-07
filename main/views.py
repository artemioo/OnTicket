from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Matches, Teams, Profile
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, BuyingTicketForm
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas


@login_required(login_url='/main/login/')
def office(request):
    return HttpResponse('любимые команды')


def home(request):
    matches = Matches.objects.all()
    return render(request, 'main/home.html', {'matches': matches})


def match_details(request, slug):
    post = Matches.objects.get(slug__iexact=slug)
    return render(request, 'main/match_details.html', {'post': post, })


def my_fav(request, name):
    team = Teams.objects.get(name=name)
  #  user = Profile.objects.get(request.user)
    Profile.user.fav_team.set(team)
  #  request.user.fav_team = team
    request.user.save()
    return render(request, 'main/my_fav.html', {'team': team, })


def contacts(request):
    return render(request, 'main/contacts.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    pass


def favorite(request):
    return render(request, 'main/favorite.html')


class BuyingTicketForm(object):
    pass

def coming(request):
    #matches = Matches.objects.filter(date="2021-06-11 18:00")
    matches = Matches.objects.order_by('date')
    m1 = list(matches)
    m2 = m1[:2]
    return render(request, 'main/coming.html', {'m2': m2})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Ошибка авторизации')
        else:
            return HttpResponse('Ошибка в вводе')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            #Сохраняем пользователя в базе данных.
            new_user.save()
            return render(request,
                          'main/register_done.html',
                           {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def buying_ticket(request, slug):
    match = Matches.objects.get(slug__iexact=slug)
    form = BuyingTicketForm()
    return render(request, 'main/buying_ticket.html', {'match': match, 'form': form})


def confirm(request, slug):
    match = Matches.objects.get(slug__iexact=slug)
    return render(request, 'main/confirm.html', {'match': match})


def add_favorite(request):
    teams = Teams.objects.all()
    return render(request, 'main/add_favorite.html', {'teams': teams})


def return_ticket(request):
    return render(request, 'main/return_ticket.html')


def check(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)

    p.drawString(300, 300, 'info about match :) ')

    p.showPage()
    p.save()
    return response