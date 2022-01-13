from django.shortcuts import render

# Create your views here.

def my_life_calendar(request):

    if request.method == 'POST':
        if 'submit-button' in request.POST:
            pass
        else:
            pass

    return render(request, template_name = 'my_life_calendar/my_life_calendar.html')
