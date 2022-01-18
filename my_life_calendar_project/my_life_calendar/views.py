from django.shortcuts import render
from django.utils.safestring import mark_safe
import datetime

# Create your views here.

def my_life_calendar(request):

    html_table = ''

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
                current_date = datetime.datetime.strptime(str(birth_date.year) + '-01-01', '%Y-%m-%d')

                dates = []

                while current_date <= death_date:
                    #print('{} {} {} {}'.format(current_date.strftime('%A'), current_date.day, current_date.strftime('%B'), current_date.year))
                    dates.append(current_date)
                    current_date += delta

                list_years = list(set([d.year for d in dates]))
                list_years.sort()

                str_table = '<table>'
                # str_table += '<tr><td>  </td>'

                # str_table += '</tr>'

                for year in list_years:
                    str_table += '<tr><td> ' + str(year) + ' </td>'

                    for d in dates:
                        if d.year == year:
                            str_table += '<td> ' + str(d.day) + ' </td>'
                        else:
                            pass

                    str_table += '</tr>'

                str_table += '</table>'
                html_table =  mark_safe(str_table)
                
        else:
            pass
    else:
        pass

    return render(request, 'my_life_calendar/my_life_calendar.html', {'html_table':html_table})
