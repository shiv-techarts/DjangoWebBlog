from django.shortcuts import render

posts = [
    {
        'name': 'Shiv Pratap Singh',
        'topic': 'Technical',
        'content': """Technology is the collection of 
        techniques, skills, methods, and processes used in the production of goods or 
        services or in the accomplishment of objectives, such as scientific investigation. 
        Technology can be the knowledge of techniques, processes, and the like, or it can be 
        embedded in machines to allow for operation without detailed knowledge of their workings. 
        Systems (e. g. machines) applying technology by taking an input, changing it according 
        to the system's use, and then producing an outcome are referred to as technology systems 
        or technological systems.""",
        'fb_link': "https://fb.com/shiv",
        'twitter_link': "#",
        'google_plus_link': "#",
    },
    {
        'name': 'Shiv P Singh',
        'topic': 'Message',
        'content': """Technology is the collection of 
        techniques, skills, methods, and processes used in the production of goods or 
        services or in the accomplishment of objectives, such as scientific investigation. 
        Technology can be the knowledge of techniques, processes, and the like, or it can be 
        embedded in machines to allow for operation without detailed knowledge of their workings. 
        Systems (e. g. machines) applying technology by taking an input, changing it according 
        to the system's use, and then producing an outcome are referred to as technology systems 
        or technological systems.""",
        'fb_link': "#",
        'twitter_link': "#",
        'google_plus_link': "#",
    },
    {
        'name': 'Shiv Singh',
        'topic': 'Meditation',
        'content': """Technology is the collection of 
        techniques, skills, methods, and processes used in the production of goods or 
        services or in the accomplishment of objectives, such as scientific investigation. 
        Technology can be the knowledge of techniques, processes, and the like, or it can be 
        embedded in machines to allow for operation without detailed knowledge of their workings. 
        Systems (e. g. machines) applying technology by taking an input, changing it according 
        to the system's use, and then producing an outcome are referred to as technology systems 
        or technological systems.""",
        'fb_link': "#",
        'twitter_link': "#",
        'google_plus_link': "#",
    },
]


# Create your views here.
def home(request):
    return render(request=request, template_name='blog/home.html', context={'posts': posts})


def about(request):
    return render(request=request, template_name='blog/about.html', context={})
