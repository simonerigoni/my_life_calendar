from django.shortcuts import render

import datetime

# Create your views here.

def my_life_calendar(request):

    if request.method == 'POST':
        if 'submit-button' in request.POST:
            life_expectancy = request.POST.get('life-expectancy', 0)

            if life_expectancy == '':
                life_expectancy = 0
            else:
                life_expectancy = int(life_expectancy)

            #print(life_expectancy)

            birth_date = request.POST.get('birth-date', 0)

            if birth_date == '':
                birth_date = 0
            else:
                birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

            #print(birth_date)

            if life_expectancy == 0 or birth_date == 0:
                pass
            else:
                death_date = birth_date + datetime.timedelta(days = life_expectancy * 365)
                delta = datetime.timedelta(days = 1)
                current_date = birth_date

                while current_date <= death_date:
                    print('{} {} {} {}'.format(current_date.strftime('%A'), current_date.day, current_date.month, current_date.year))
                    current_date += delta

        else:
            pass
    else:
        pass

    return render(request, template_name = 'my_life_calendar/my_life_calendar.html')
