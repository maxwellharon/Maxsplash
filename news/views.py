from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Post

# Create your views here.


def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    return render(request, 'welcome.html')


def news_today(request):
    date = dt.date.today()
    news = Post.todays_news()
    posts = Post.objects.all()
    return render(request, 'all-news/today-news.html', {"date": date, "news": news, 'posts': posts})

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Post.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message": message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message": message})


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-news/post.html", {"post": post})
# def convert_dates(dates):
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)
#
#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
#
#     # Returning the actual day of the week
#     day = days[day_number]
#     return day


def posts(request):
    posts = Post.objects.all()
    return render(request, "all-news/postss.html", {"posts": posts})
