from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def jyoti(request):
    return HttpResponse('<h1> <marquee>I am developers </h1>')


def bioData(request):
    return HttpResponse('''
    <h1> Name is Teddy </h1>
    <i> age is 20 </i>
    <b> Gender is Male(Not Defined)</b>
    <img src=https://wallpapercave.com/wp/wp3530510.jpg>
                        ''')