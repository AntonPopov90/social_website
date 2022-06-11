from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, StatisticForm, TrophyForm, NewsForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Statistic, Trophy, News
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

def home_page(request):
    stats = Statistic.objects.all()
    profile = Profile.objects.all()
    max_time = profile.order_by('fish_kg').last()
    count_vodka = 0
    count_beer = 0
    count_fish = 0
    count_fishing_number = 0

    for e in stats:
        if e.vodka != None:
            count_vodka += float(e.vodka)
        else:
            continue
    for e in stats:
        if e.beer != None:
            count_beer += float(e.beer)
        else:
            continue
    for e in stats:
        if e.fish_kg != None:
            count_fish += float(e.fish_kg)
        else:
            continue
    for e in stats:
        if e.place != None:
            count_fishing_number += 1
    fish_beer_coefficient = count_vodka / (count_fish+0.0001) * 100
    return render(request, 'account/dashboard.html',{"count_vodka":count_vodka,
                    "count_beer": count_beer,
                    "count_fish": count_fish,
                    "fish_beer_coefficient": fish_beer_coefficient,
                    'count_fishing_number':count_fishing_number,
                                                     'max_time': max_time})

@login_required
def all_users(request):
    profiles = Profile.objects.all()
    return render(request, 'account/user/list.html', {'profiles': profiles})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_login(request):
    """Аутентификация пользователя"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        # если вызывается с запросом GET,создаем новую log-in
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создание нового пользователя, без сохранения в БД
            new_user = user_form.save(commit=False)
            # Устанавливаем выбранный пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем ноового пользователя в БД
            # Создание профиля пользователя.
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')
        else:
            messages.error(request, 'Ошибка обновления профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    profiles = Profile.objects.all()
    return render(request,
            'account/user/list.html',
            {'section': 'people',
            'users': users,
            'profiles': profiles})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    profiles = Profile.objects.filter(user=user)
    return render(request,
            'account/user/detail.html',
            {'section': 'people',
            'user': user,
            'profiles': profiles})

@login_required
def statistic(request):
    return render(request,
                  'statistic.html',)

@login_required
def add_statistic(request):
    if request.method == 'POST':
        statistic_form = StatisticForm(request.POST)
        if statistic_form.is_valid():
            stat = statistic_form.save(commit=False)
            stat.save()
            messages.success(request, 'Отчет успешно добавлен')
            return redirect('dashboard')
        else:
            messages.error(request, 'Введен неверный формат данных')
    else:
        statistic_form = StatisticForm()
    return render(request,
                      'account/add-statistic.html',
                      {'statistic_form': statistic_form,
                       })

@login_required
def show_statistic(request):
    stats = Statistic.objects.all()
    count_vodka = 0
    count_beer = 0
    count_fish = 0
    count_fish_sum = 0
    count_fishing_number = 0
    for e in stats:
        if e.place != None:
            count_fishing_number += 1
    for e in stats:
        if e.vodka != None:
            count_vodka += float(e.vodka)
        else:
            continue
    for e in stats:
        if e.beer != None:
            count_beer += float(e.beer)
        else:
            continue
    for e in stats:
        if e.fish_kg != None:
            count_fish += float(e.fish_kg)
        else:
            continue
    for e in stats:
        if e.fish_sum != None:
            count_fish_sum += float(e.fish_sum)
    coefficient = count_fishing_number/count_fish_sum+0.01
    return render(request,
                  'account/show-statistic.html',
                  { "stats":stats,
                    "count_vodka":count_vodka,
                    "count_beer": count_beer,
                    "count_fish": count_fish,
                    "coefficient": coefficient,
                    "people":Statistic.objects.all()
                   })



def news(request):
    return HttpResponse('Трофеев нет')

@login_required
def add_trophy(request):
    if request.method == 'POST':
        trophy_form = TrophyForm(request.POST, request.FILES)
        if trophy_form.is_valid():
            trophy = trophy_form.save(commit=False)
            trophy.save()
            messages.success(request, 'Трофей добавлен')
            return redirect('statistic')
        else:
            messages.error(request, 'Введен неверный формат данных')
    else:
        trophy_form = TrophyForm()
    return render(request,
                      'account/add_trophy.html',
                      {'trophy_form': trophy_form,
                       })

@login_required
def trophy_gallery(request):
    gallery = Trophy.objects.all()
    return render(request, 'account/trophy_gallery.html', {'gallery': gallery})


def post_list(request):
    posts = News.objects.order_by('-published_date')
    return render(request, 'account/news_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'account/news_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = NewsForm()
    return render(request, 'account/news_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=News.pk)
    else:
        form = NewsForm(instance=post)
    return render(request, 'account/news_edit.html', {'form': form})


def map(request):
    mapbox_access_token = 'pk.eyJ1IjoiYW50b25wb3BvdjkwIiwiYSI6ImNsNDlzemdkcTE0ajczaW1vNHJmaXl5cDcifQ.yrhKP-SuHZGn1oY0JscfRw'
    return render(request, 'account/map.html',
                  {'mapbox_access_token': mapbox_access_token})

