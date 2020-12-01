from django.shortcuts import render, redirect
import pandas as pd
from matplotlib import pyplot as plt
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib.auth.models import Group 
from django_pandas.io import read_frame
from shortlist.models import Shortlist
import plotly.graph_objects as go
# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Visualize(request):
    data = Shortlist.objects.all()

    df = read_frame(data)
    
    df = df.loc[:,['listing']]
    df.dropna( inplace=True)


    count = df.count(axis=1)


    df['count'] = count

    df.columns = ['Listing', 'Count']

    df = df.groupby(["Listing"])["Count"].count().reset_index()

    listing = df['Listing'].head(len(df))

    count = df['Count'].head(len(df))

    fig = go.Figure([go.Bar(x=listing[0:10], y=count[0:10], marker_color='#2fb56e')])
    fig.update_layout(
    title="Real Buy Stats 2020",
    xaxis_title="Properties",
    yaxis_title="Number of shortlists")

    
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {'graph': graph}
    return render(request, 'visualization/visual.html', context)
