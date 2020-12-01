from django.shortcuts import render
import pandas as pd
from matplotlib import pyplot as plt
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib.auth.models import Group 

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Visualize(request):
	data = pd.read_csv('visualization/csv_files/Shortlist.csv')
	data.head() 
	df = pd.DataFrame(data)

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
	plt.xlabel('Listings')
	plt.ylabel('Shortlisted Count')

	plt.savefig('realbuy/static/img/List_img.png')

	
	return render(request, 'visualization/visual.html')
