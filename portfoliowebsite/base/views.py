from cgitb import html
from multiprocessing import context
from optparse import Values
from urllib.request import Request
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.db.models import Max, Count
from django.db import models
from django.db.models.functions import TruncMonth, TruncYear
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Skill, PBI_articles, Month, Year, Google_trends
from .scripts.PBIscraper import collect_data_increment
from .scripts.charts import create_chart, google_trends_data, google_trends_create_plot

# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailed_skills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects' : projects, 'skills' : skills, 'detailed_skills' : detailed_skills}
    return render(request, 'base/home.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project' : project}
    return render(request, 'base/project.html', context)

def pbiProjectPage(request):

    articles_year = PBI_articles.objects.annotate(Year = Year('Article_date')).values('Year').annotate(c=Count('Article_title'))
    articles_month = PBI_articles.objects.annotate(Month = Month('Article_date')).values('Month').annotate(c=Count('Article_title'))

    year_plot = create_chart(articles_year, 'Year')
    month_plot = create_chart(articles_month, 'Month')

    if request.method == "POST":
        if request.POST.get("refresh"):
            max_id = PBI_articles.objects.aggregate(Max('id'))['id__max']
            last_article = PBI_articles.objects.get(id=max_id).Article_title
            data_dict = collect_data_increment(last_article)
            if data_dict:
                data_dict.reverse()
                for data in data_dict:
                    b = PBI_articles(Article_title = data['Article_title'], Article_date = data['Article_date'], Article_short_text = data['Article_short_text'], 
                                                                    Aricle_list_tags = data['Aricle_list_tags'], Article_post_link = data['Article_post_link'])
                    b.save()
            
            trends_df = google_trends_data()
            if not trends_df.empty:
                Google_trends.objects.all().delete()
                for index, row in trends_df.iterrows():
                    g = Google_trends(DateTime = row['date'], PowerBi_trend = row['power bi'], Tableau_trend = row['tableau'], Qlik_trend = row['qlik'])
                    g.save()
            
    g_plot_data = google_trends_data()
    google_trends_plot = google_trends_create_plot(g_plot_data)

    pbi_articles = PBI_articles.objects.all().order_by('-id')[:12]
    context = {'pbi_articles':pbi_articles, 'articles_year':articles_year, 'articles_month':articles_month, 'year_plot':year_plot, 'month_plot':month_plot, 'google_trends_plot':google_trends_plot}
    return render(request, 'base/pbiProject.html', context)