# newsapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News, Advertisement, Category
from django.contrib import messages
from .models import Advertisement

#── Public views ─────────────────────────────────────────────────────────────

def index(request):
    headline_news = News.objects.filter(is_headline=True).order_by('-created_at')[:10]
    latest_news = News.objects.filter(is_latest=True).order_by('-created_at')[:10]
    ads = Advertisement.objects.all()
    return render(request, 'index.html', {
        'headline_news': headline_news,
        'latest_news': latest_news,
        'advertisement': ads,
    })

def view_all_latest_news(request):
    all_latest_news = News.objects.filter(is_latest=True).order_by('-created_at')
    ads = Advertisement.objects.all()
    return render(request, 'all_latest_news.html', {
        'all_latest_news': all_latest_news,
        'advertisement': ads,
    })



def news_detail(request, id):
    item = get_object_or_404(News, id=id)
    others = News.objects.exclude(id=id).order_by('-created_at')[:5]
    advertisement = Advertisement.objects.all()
    return render(request, 'news_detail.html', {
        'news': item,
        'latest_news': others,
        'advertisement': advertisement,
    })


#── Admin auth ────────────────────────────────────────────────────────────────

def admin_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


#── Admin dashboard ──────────────────────────────────────────────────────────

@login_required(login_url='admin_login')
def admin_dashboard(request):
    all_news = News.objects.all().order_by('-created_at')
    total_latest_news_count = News.objects.filter(is_latest=True).count()
    total_headline_news_count = News.objects.filter(is_headline=True).count()
    return render(request, 'admin_dashboard.html', {
        'all_news': all_news,
        'total_news_count': all_news.count(),
        'total_ads_count': Advertisement.objects.count(),
        'total_latest_news_count': total_latest_news_count,
        'total_headline_news_count': total_headline_news_count,
    })

@login_required(login_url='admin_login')
def add_latest_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        News.objects.create(
            title=title,
            content=content,
            image=image,
            is_latest=True,
            is_headline=False
        )
        messages.success(request, "Latest News added successfully!")
        return redirect('admin_dashboard')

    return render(request, 'add_latest_news.html')

@login_required(login_url='admin_login')
def add_headline_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        News.objects.create(
            title=title,
            content=content,
            image=image,
            is_latest=False,
            is_headline=True
        )
        messages.success(request, "Headline News added successfully!")
        return redirect('admin_dashboard')

    return render(request, 'add_headline_news.html')

@login_required(login_url='admin_login')
def edit_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == 'POST':
        news.title = request.POST.get('title')
        news.content = request.POST.get('content')
        news.is_headline = request.POST.get('is_headline') == 'on'
        news.is_latest = request.POST.get('is_latest') == 'on'
        if 'image' in request.FILES:
            news.image = request.FILES['image']
        news.save()
        messages.success(request, "News updated successfully!")
        return redirect('admin_dashboard')
    return render(request, 'edit_news.html', {'news': news})

@login_required(login_url='admin_login')
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    messages.success(request, "News deleted successfully!")
    return redirect('view_all_news')

@login_required(login_url='admin_login')
def view_all_news(request):
    all_news = News.objects.all().order_by('-created_at')
    return render(request, 'view_all_news.html', {'all_news': all_news})




@login_required(login_url='admin_login')
def manage_ads(request):
    if request.method == 'POST':
        if 'delete_ad_id' in request.POST:
            # Handle delete
            ad_id = request.POST.get('delete_ad_id')
            ad = Advertisement.objects.get(id=ad_id)
            ad.delete()
            messages.success(request, "Advertisement deleted successfully!")
            return redirect('manage_ads')
        else:
            # Handle new ad creation
            image = request.FILES.get('image')
            link = request.POST.get('link')
            if image and link:
                Advertisement.objects.create(image=image, link=link)
                messages.success(request, "Advertisement added successfully!")
                return redirect('manage_ads')
            else:
                messages.error(request, "Both image and link are required.")

    ads = Advertisement.objects.all()
    return render(request, 'manage_ads.html', {'ads': ads})


def view_all_headline_news(request):
    all_headline_news = News.objects.filter(is_headline=True).order_by('-created_at')
    return render(request, 'view_all_headline_news.html', {'headline_news': all_headline_news})
