from datetime import datetime
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from random import randint
import requests
from bs4 import BeautifulSoup
import time
import undetected_chromedriver.v2 as uc
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

User = get_user_model()


def index(request):
    date = datetime.today()
    # return HttpResponse("<h1>Test11</h1>")
    return render(request, "DocBlog/index.html", context={"date":date})

def fonction1(request):
    return render(request,'DocBlog/scrapp.html') 

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user = User.objects.create_user(username=username,firstname=firstname,lastname=lastname,email=email,password=password,password1=password1)
        login(request, user) 
        # mon_utilisateur = User.objects.create(username, email, password)
        # mon_utilisateur.first_name=firstname
        # mon_utilisateur.last_name = lastname
        # mon_utilisateur.save()
        # messages.success(request, 'Votre compte a été crée avec success ')
        # return redirect('DocBlog/scrapp.html')
        return redirect('DocBlog/index')
    return render(request, 'DocBlog/register.html')

def login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username)
    return render(request, 'DocBlog/login.html')

def logout(request):
    pass







def fonction2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            your_name = form.cleaned_data['your_name']
            driver = uc.Chrome()
            url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+your_name+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+your_name+""
            pages = range(1, 3)
            with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrappFrance.csv', "w+") as f:
                for page in pages:
                    driver.get(url.format(page=page))
                    time.sleep(3)    
                    phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
                    for phone_element in phone_elements:
                        phone_element.click()
                        time.sleep(1) 
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stores = soup.find_all("li", class_="bi bi-generic") 
                    for store in stores: 
                        try:
                            nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
                        except:
                            nom=""
                        try:    
                            adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
                        except:
                            adr=""
                        try:
                            tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                        except:
                            tel = ""
                        print(f"{nom}; {adr}; {tel}", file=f)
                        print(f"{nom}; {adr};{tel}")
            return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'DocBlog/scrapp.html', {'form': form})

def fonction3(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            your_name = form.cleaned_data['your_name']
            driver = uc.Chrome()
            url = "https://www.whitepages.com/business/NY/"+your_name+"?page={page}"
            pages = range(1, 26)
            with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrappUSA.csv', "w+") as f:
                for page in pages:
                    driver.get(url.format(page=page))
                    time.sleep(3)    
                    phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
                    for phone_element in phone_elements:
                        phone_element.click()
                        time.sleep(1) 
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stores = soup.find_all("li", class_="bi bi-generic") 
                    for store in stores: 
                        try:
                            nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
                        except:
                            nom=""
                        try:    
                            adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
                        except:
                            adr=""
                        try:
                            tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                        except:
                            tel = ""
                        print(f"{nom}; {adr}; {tel}", file=f)
                        print(f"{nom}; {adr};{tel}")
            return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'DocBlog/scrapp.html', {'form': form})
        # data=requests.get("https://reqres.in/api/users")
        # print(data.text)
        # data=data.text
        # return render(request,'DocBlog/index.html',{'data':data})
        



# def fonction2(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=carrefour%20city&ou=Ile-de-France&idOu=R11&page=2&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete=carrefour%20city"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
# def fonction3(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.whitepages.com/business/NY/Nike"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
# def fonction4(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=carrefour%20city&ou=Ile-de-France&idOu=R11&page=2&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete=carrefour%20city"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
  













#     driver = uc.Chrome()
#     url = "https://www.iga.com/find-a-store?page={page}"
#     pages = range(2, 5)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/iga.csv', 'w+') as f:
#         for page in pages:
#             driver.get(url.format(page=page))
#             time.sleep(4)
#             soup = BeautifulSoup(driver.page_source,'html.parser')
#             stores = soup.find_all("div", class_="span8 store-location-details")
#             for store in stores:
#                 nom = store.find("h3").text.replace("\n", "").strip()
#                 # adresse = store.find("address", class_="store-address clearfix").text.replace("\n", "").strip()
#                 # try:
#                 #     tel=store.find("p", class_="store-phone-fax").find("a").text.replace("\n", "").strip()
#                 # except:
#                 #     tel = ""
#                 print(f"{nom}", file=f)
#                 print(f"{nom}")
#     return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")
        
# #    




    # data=requests.get("https://www.google.com/")
    # print(data.text)
    # data=data.text
    # return render(request,'index.html',{'data':data})




   

            