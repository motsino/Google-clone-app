from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.urls import reverse, reverse_lazy
import requests
from bs4 import BeautifulSoup as bs
from requests.utils import requote_uri
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
import os
import datetime
from googleapiclient.discovery import build
from newsapi import NewsApiClient
import re
import maya
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, ProfileForm, EditProfileForm, ChangeUserPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.

a = ''
content = ''


@login_required
def searches(request, search):

    web_result_searches = []
    Top_related_search_first = []
    Top_related_search_second = []
    Side_related_search = []

    if request.method == 'POST':
        look_up = request.POST['search']

        if look_up:
            globals()['a'] = look_up

        search_url = 'https://www.ask.com/web?q={}/'.format(look_up)

        response = requests.get(search_url).text
        soup = bs(response, 'html.parser')

        related_search_first_col = soup.find(
            'ul', class_='PartialRelatedSearch-first-column').find_all('li', class_='PartialRelatedSearch-item')
        for a in related_search_first_col:
            rsf_link = a.find('a').get('href')
            rsf_item = a.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rsf = Top_search_first.objects.create(
            #     link=rsf_link, item=rsf_item)
            # new_rsf.save()
            Top_related_search_first.append((rsf_link, rsf_item))

        related_search_second_col = soup.find(
            'ul', class_='PartialRelatedSearch-second-column').find_all('li', class_='PartialRelatedSearch-item')
        for b in related_search_second_col:
            rss_link = b.find('a').get('href')
            rss_item = b.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rss = Top_search_second.objects.create(
            #     link=rss_link, item=rss_item)
            # new_rss.save()
            Top_related_search_second.append((rss_link, rss_item))

        related_search_full_list = soup.find(
            'ul', class_='PartialRelatedSearch-list').find_all('li', class_='PartialRelatedSearch-item')
        for c in related_search_full_list:
            rsl_link = c.find('a').get('href')
            rsl_item = c.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rsl = Side_search.objects.create(link=rsl_link, item=rsl_item)
            # new_rsl.save()
            Side_related_search.append((rsl_link, rsl_item))

        for page in range(1, 10):
            page_num = page
            new_url = requote_uri(search_url) + '&page={}'.format(page_num)

            response = requests.get(new_url).text
            soup = bs(response, 'html.parser')

            search_results = soup.find_all(
                'div', class_='PartialSearchResults-item')

            for i in search_results:
                result_link = i.find('a').get('href')
                result_title = i.find(
                    class_='PartialSearchResults-item-title').text
                result_item_url = i.find(
                    class_='PartialSearchResults-item-url').text
                result_desc = i.find(
                    'p', class_='PartialSearchResults-item-abstract').text

                # result = Search.objects.create(
                #     link=result_link, title=result_title, item_url=result_item_url, desc=result_desc)
                # result.save()

                web_result_searches.append(
                    (result_link, result_title, result_item_url, result_desc))

        # web_results = Search.objects.all()
        # top_first = Top_search_first.objects.all()
        # top_second = Top_search_second.objects.all()
        # side = Side_search.objects.all()

        # page = request.GET.get('page', 1)
        # paginator = Paginator(web_results, 11)

        # try:
        #     web_results = paginator.page(page)
        # except PageNotAnInteger:
        #     web_results = paginator.page(1)
        # except EmptyPage:
        #     web_results = paginator.page(paginator.num_pages)

        context = {
            'search_input': look_up,
            'Top_related_search_1st': Top_related_search_first,
            'Top_related_search_2nd': Top_related_search_second,
            'Side_related_search': Side_related_search,
            'web_result_searches': web_result_searches,
            # 'web_results': web_results,
            # 'top_first': top_first,
            # 'top_second': top_second,
            # 'side': side,
        }

        return render(request, 'search.html', context)

    elif search:
        search_url = 'https://www.ask.com/web?q={}/'.format(search)

        response = requests.get(search_url).text
        soup = bs(response, 'html.parser')

        related_search_first_col = soup.find(
            'ul', class_='PartialRelatedSearch-first-column').find_all('li', class_='PartialRelatedSearch-item')
        for a in related_search_first_col:
            rsf_link = a.find('a').get('href')
            rsf_item = a.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rsf = Top_search_first.objects.create(
            #     link=rsf_link, item=rsf_item)
            # new_rsf.save()
            Top_related_search_first.append((rsf_link, rsf_item))

        related_search_second_col = soup.find(
            'ul', class_='PartialRelatedSearch-second-column').find_all('li', class_='PartialRelatedSearch-item')
        for b in related_search_second_col:
            rss_link = b.find('a').get('href')
            rss_item = b.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rss = Top_search_second.objects.create(
            #     link=rss_link, item=rss_item)
            # new_rss.save()
            Top_related_search_second.append((rss_link, rss_item))

        related_search_full_list = soup.find(
            'ul', class_='PartialRelatedSearch-list').find_all('li', class_='PartialRelatedSearch-item')
        for c in related_search_full_list:
            rsl_link = c.find('a').get('href')
            rsl_item = c.find(
                class_='PartialRelatedSearch-item-link-text').text
            # new_rsl = Side_search.objects.create(link=rsl_link, item=rsl_item)
            # new_rsl.save()
            Side_related_search.append((rsl_link, rsl_item))

        for page in range(1, 10):
            page_num = page
            new_url = requote_uri(search_url) + '&page={}'.format(page_num)

            response = requests.get(new_url).text
            soup = bs(response, 'html.parser')

            search_results = soup.find_all(
                'div', class_='PartialSearchResults-item')

            for i in search_results:
                result_link = i.find('a').get('href')
                result_title = i.find(
                    class_='PartialSearchResults-item-title').text
                result_item_url = i.find(
                    class_='PartialSearchResults-item-url').text
                result_desc = i.find(
                    'p', class_='PartialSearchResults-item-abstract').text

                # result = Search.objects.create(
                #     link=result_link, title=result_title, item_url=result_item_url, desc=result_desc)
                # result.save()

                web_result_searches.append(
                    (result_link, result_title, result_item_url, result_desc))
        context = {
            'search_input': search,
            'Top_related_search_1st': Top_related_search_first,
            'Top_related_search_2nd': Top_related_search_second,
            'Side_related_search': Side_related_search,
            'web_result_searches': web_result_searches,
            # 'web_results': web_results,
            # 'top_first': top_first,
            # 'top_second': top_second,
            # 'side': side,
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'index.html')


def index(request):
    return render(request, 'Home/index.html', {'search_input': a})
    # 'logged_user': User.objects.filter(username=request.user)


@login_required
def images(request, search):
    contents = []

    if request.method == 'POST':
        look_up = request.POST['image']
        url = "https://bing-image-search1.p.rapidapi.com/images/search"

        headers = {
            'x-rapidapi-key': "774917db98mshef9c618b6e25435p134f03jsn1885b572adca",
            'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }

        querystring = {"q": look_up, 'count': 70}

        response = requests.get(url, params=querystring, headers=headers)

        results = response.json()['value']

        globals()['content'] = look_up

        for result in results:
            name = result['name']
            webSearchUrl = result['webSearchUrl']
            publish_date = result['datePublished']
            image = result['contentUrl']
            image_content = result['hostPageUrl']
            contents.append((webSearchUrl, image, name,
                             image_content, publish_date))

        return render(request, 'images.html', {'contents': contents, 'search_input': look_up})

    elif search:
        url = "https://bing-image-search1.p.rapidapi.com/images/search"

        headers = {
            'x-rapidapi-key': "774917db98mshef9c618b6e25435p134f03jsn1885b572adca",
            'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }

        querystring = {"q": search, 'count': 70}

        response = requests.get(url, params=querystring, headers=headers)

        results = response.json()['value']

        globals()['content'] = search

        for result in results:
            name = result['name']
            webSearchUrl = result['webSearchUrl']
            publish_date = result['datePublished']
            image = result['contentUrl']
            image_content = result['hostPageUrl']
            contents.append((webSearchUrl, image, name,
                             image_content, publish_date))

        return render(request, 'images.html', {'contents': contents, 'search_input': search})
    else:
        return render(request, 'Home/index.html')


def home_images(request):
    return render(request, 'Home/home_images.html', {'search_input': content, 'user': request.user})


@login_required
def videos(request, search):
    nextPageToken = None
    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')
    pages = 0
    all_videos = []

    if request.method == 'POST':
        look_up = request.POST['video']

        yt_api = 'AIzaSyBK9ieqRMnOO7TArsMyHX7Wv6GbI-B6mA0'

        youtube = build('youtube', 'v3', developerKey=yt_api)
        while pages < 3:
            output = youtube.search().list(q=look_up, part='snippet',
                                           type='video', maxResults=40, pageToken=nextPageToken).execute()
            for item in output['items']:
                vid_title = item['snippet']['title']
                video_id = item['id']['videoId']
                video = 'https://www.youtube.com/watch?v={}'.format(video_id)
                video_img = item['snippet']['thumbnails']['high']['url']
                img_width = item['snippet']['thumbnails']['high']['width']
                img_height = item['snippet']['thumbnails']['high']['height']
                vid_desc = item['snippet']['description']
                publish_time = item['snippet']['publishTime']
                publish_time = maya.parse(publish_time).slang_time()
                channel = item['snippet']['channelTitle']

                vid_info = youtube.videos().list(part='contentDetails', id=video_id).execute()
                videos = vid_info['items']
                vid_length = videos[0]['contentDetails']['duration']
                hours = hours_pattern.search(vid_length)
                minutes = minutes_pattern.search(vid_length)
                seconds = seconds_pattern.search(vid_length)

                hours = int(hours.group(1)) if hours else 0
                minutes = int(minutes.group(1)) if minutes else 0
                seconds = int(seconds.group(1)) if seconds else 0

                video_duration = maya.timedelta(
                    hours=hours, minutes=minutes, seconds=seconds).total_seconds()
                video_duration_mins, video_duration_secs = divmod(
                    video_duration, 60)
                video_duration_hrs, video_duration_mins = divmod(
                    video_duration_mins, 60)
                video_duration_hrs, video_duration_mins, video_duration_secs = int(
                    video_duration_hrs), int(video_duration_mins), int(video_duration_secs)

                if video_duration_hrs == 0:
                    duration = '{:02}:{:02}'.format(
                        video_duration_mins, video_duration_secs)
                else:
                    duration = '{:02}:{:02}:{:02}'.format(
                        video_duration_hrs, video_duration_mins, video_duration_secs)

                all_videos.append((video, video_img, img_width,
                                   img_height, vid_title, publish_time, channel, duration))

            nextPageToken = output.get('nextPageToken')
            pages += 1
            if not nextPageToken:
                break

        return render(request, 'videos.html', {'all_videos': all_videos, 'search_input': look_up})

    elif search:
        yt_api = 'AIzaSyBK9ieqRMnOO7TArsMyHX7Wv6GbI-B6mA0'

        youtube = build('youtube', 'v3', developerKey=yt_api)
        while pages < 3:
            output = youtube.search().list(q=search, part='snippet',
                                           type='video', maxResults=40, pageToken=nextPageToken).execute()
            for item in output['items']:
                vid_title = item['snippet']['title']
                video_id = item['id']['videoId']
                video = 'https://www.youtube.com/watch?v={}'.format(video_id)
                video_img = item['snippet']['thumbnails']['high']['url']
                img_width = item['snippet']['thumbnails']['high']['width']
                img_height = item['snippet']['thumbnails']['high']['height']
                vid_desc = item['snippet']['description']
                publish_time = item['snippet']['publishTime']
                publish_time = maya.parse(publish_time).slang_time()
                channel = item['snippet']['channelTitle']

                vid_info = youtube.videos().list(part='contentDetails', id=video_id).execute()
                videos = vid_info['items']
                vid_length = videos[0]['contentDetails']['duration']
                hours = hours_pattern.search(vid_length)
                minutes = minutes_pattern.search(vid_length)
                seconds = seconds_pattern.search(vid_length)

                hours = int(hours.group(1)) if hours else 0
                minutes = int(minutes.group(1)) if minutes else 0
                seconds = int(seconds.group(1)) if seconds else 0

                video_duration = maya.timedelta(
                    hours=hours, minutes=minutes, seconds=seconds).total_seconds()
                video_duration_mins, video_duration_secs = divmod(
                    video_duration, 60)
                video_duration_hrs, video_duration_mins = divmod(
                    video_duration_mins, 60)
                video_duration_hrs, video_duration_mins, video_duration_secs = int(
                    video_duration_hrs), int(video_duration_mins), int(video_duration_secs)

                if video_duration_hrs == 0:
                    duration = '{:02}:{:02}'.format(
                        video_duration_mins, video_duration_secs)
                else:
                    duration = '{:02}:{:02}:{:02}'.format(
                        video_duration_hrs, video_duration_mins, video_duration_secs)

                all_videos.append((video, video_img, img_width,
                                   img_height, vid_title, publish_time, channel, duration))

            nextPageToken = output.get('nextPageToken')
            pages += 1
            if not nextPageToken:
                break

        return render(request, 'videos.html', {'all_videos': all_videos, 'search_input': search})
    else:
        return render(request, 'Home/index.html')


@login_required
def news(request, search):
    # news_api = os.environ['NEWS_API_KEY']
    Available_news = []
    # date = str(datetime.datetime.today()).strip()[:10]
    # day = date.strip()[8:]
    # month = date.strip()[5:7]
    # year = date.strip()[:4]
    # yesterday = datetime.timedelta(int(day)-1).days
    # reference_date = '{}-{}-{}'.format(year, month, yesterday)
    newsapi = NewsApiClient(api_key='7c48fa4a03fb41a6ba258fa2eaad14a0')

    if request.method == 'POST':
        look_up = request.POST['news']
        all_articles = newsapi.get_everything(
            q=look_up, language='en', sort_by='publishedAt', page_size=100)
        for article in all_articles['articles']:
            source = article['source']['name']
            author = article['author']
            title = article['title']
            desc = article['description']
            url = article['url']
            image = article['urlToImage']
            publish_date = article['publishedAt']
            Available_news.append(
                (source, title, desc, url, image, publish_date))
        return render(request, 'news.html', {'search_input': look_up, 'Available_news': Available_news})

    elif search:
        all_articles = newsapi.get_everything(
            q=search, language='en', sort_by='publishedAt', page_size=100)
        for article in all_articles['articles']:
            source = article['source']['name']
            author = article['author']
            title = article['title']
            desc = article['description']
            url = article['url']
            image = article['urlToImage']
            publish_date = article['publishedAt']
            publish_date = maya.parse(publish_date).slang_time()
            Available_news.append(
                (source, title, desc, url, image, publish_date))
        return render(request, 'news.html', {'search_input': search, 'Available_news': Available_news})


def base(request):
    if request.method == 'POST':
        result = request.POST.get('search')
        return HttpResponseRedirect(reverse('searches', args=(result,)))
    return render(request, 'Home/index.html', {'search_input': result})


def base_images(request):
    if request.method == 'POST':
        result = request.POST.get('image')
        return HttpResponseRedirect(reverse('images', args=(result,)))
    return render(request, 'Home/home_images.html', {'search_input': result})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#     return render(request, 'registration/login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('index')
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.method == 'POST':
    #         username = self.request.POST['username']
    #         password = self.request.POST['password1']
    #         password2 = self.request.POST['password2']
    #         email = self.request.POST['email']
    #         first_name = self.request.POST['first_name']
    #         last_name = self.request.POST['last_name']
    #         new_user = User.objects.create_superuser(
    #             username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    #         new_user.save()
    #         return redirect('login')
    #     context['first_name'] = first_name
    #     context['last_name'] = last_name
    #     return context

    # def register(self, register):
    #     if self.request.method == 'POST':
    #         username = self.request.POST['username']
    #         password = self.request.POST['password1']
    #         password2 = self.request.POST['password2']
    #         email = self.request.POST['email']

    #         new_user = User.objects.create_user(
    #             username=username, password=password, email=email)
    #         new_user.save()
    #         return redirect('login')
    #     else:
    #         return redirect('signup')


@login_required
def account(request):
    return render(request, 'manage_account.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        change_form = EditProfileForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, request=request)
        # profile_form = ProfileForm(
        #     request.POST, request.FILES, instance=request.user.profile)

        if request.user.profile is None:
            profile_form = ProfileForm(
                request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid() and change_form.is_valid():
                change_form.save()
                user = request.user
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('profile')
        else:
            profile_form = ProfileForm(
                request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid() and change_form.is_valid():
                change_form.save()
                user = request.user
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('profile')
    else:
        change_form = EditProfileForm(instance=request.user)
        # profile_form = ProfileForm(request=request)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'profile_form': profile_form, 'change_form': change_form})


@login_required
def change_passwrd(request):
    if request.method == 'POST':
        change_form = ChangeUserPasswordForm(
            data=request.POST, user=request.user)

        if change_form.is_valid():
            form = change_form.save(commit=False)
            # form.set_password(request.POST['new_password1'])
            form.save()
            update_session_auth_hash(request, change_form.user)
            return redirect('profile')
        # else:
        #     return redirect('change_passwrd')

    else:
        change_form = ChangeUserPasswordForm(user=request.user)
    return render(request, 'change_passwrd.html', {'form': change_form})


@login_required
def reset_passwrd(request):
    # return render(request, 'reset_passwrd.html')
    return render(request, 'registration/password_reset_form.html')


# @login_required
# def reset_passwrd_done(request):
#     return render(request, 'registration/password_reset_done.html')
