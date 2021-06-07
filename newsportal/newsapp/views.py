from django.shortcuts import render

# Create your views here.
def index(request):
    head = 'Welcome To My News Portal'
    msg1 = 'Sports Information'
    msg2 = 'Filmy Fundda'
    info = {'head': head,
            'msg1': msg1,
            'msg2':msg2
            }
    return render(request, 'index.html', context=info)

def sportsinfo(request):
    head = 'Welcome to sports News'
    msg1 = 'Here we find largest track'
    msg2 = 'hey!!! usain bolt breaks the record'
    img = 'keerthi.jpg'
    info = {'head': head,
            'msg1': msg1,
            'msg2': msg2,
            'img': img
            }
    return render(request,'profile.html', context=info)

def film(request):
    head = 'Welcome to Filmy Fundda'
    msg1 = 'Priyanka started her gymnastics'
    msg2 = 'Keerthi raj beats to priya ...'
    img = 'college.jpg'
    info = {'head': head,
            'msg1': msg1,
            'msg2': msg2,
            'img': img
            }
    return render(request,'profile.html',context=info)