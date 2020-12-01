from django.shortcuts import render
import pandas as pd
from matplotlib import pyplot as plt
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib.auth.models import Group 
from django_pandas.io import read_frame
from shortlist.models import Shortlist
# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Visualize(request):
    data = Shortlist.objects.all()

    df = read_frame(data)

    print(df)
    
    df = df.loc[:,['listing']]
    df.dropna( inplace=True)


    count = df.count(axis=1)


    df['count'] = count

    df.columns = ['Listing', 'Count']

    df = df.groupby(["Listing"])["Count"].count().reset_index()

    listing = df['Listing'].head(len(df))

    count = df['Count'].head(len(df))

    fig = plt.figure(figsize =(7, 5))

    plt.bar(listing[0:10], count[0:10], color='#2ca665') 
    plt.xlabel('Listing')
    plt.ylabel('Shortlisted Count')

    plt.savefig('realbuy/static/img/List_img.png')

    
    return render(request, 'visualization/visual.html')
