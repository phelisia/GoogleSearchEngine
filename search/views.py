from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request   ):
    return render(request, 'index.html')

def search(request  ):
    if request.method =='POST':
        search = request.POST['search']
    url='https://www.ask.com/web?='+search
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')
    results_listing=soup.find_all('div',{'class':'PartialSearch'})