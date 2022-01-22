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
                today_date = datetime.datetime.now()
                death_date = birth_date + datetime.timedelta(days = life_expectancy * 365)
                delta = datetime.timedelta(days = 1)
                current_date = datetime.datetime.strptime(str(birth_date.year) + '-01-01', '%Y-%m-%d')
                end_date = datetime.datetime.strptime(str(death_date.year) + '-12-31', '%Y-%m-%d')

                dates = []

                while current_date <= end_date:
                    #print('{} {} {} {}'.format(current_date.strftime('%A'), current_date.day, current_date.strftime('%B'), current_date.year))
                    dates.append(current_date)
                    current_date += delta

                list_years = list(set([d.year for d in dates]))
                list_years.sort()

                str_table = '<div style="overflow: auto"><table>'
                str_table += '<tr><th>Years \ Months</th>'

                for month in range(1, 13):
                    temp_date = datetime.datetime.strptime('2020-' + str(month) + '-01', '%Y-%m-%d')
                    str_table += '<td colspan="31">' + temp_date.strftime('%B') + '</td>'

                str_table += '</tr>'

                for year in list_years:
                    str_table += '<tr><td>' + str(year) + '</td>'

                    for month in range(1, 13):
                        #str_table += '<td>'

                        for d in dates:
                            cell_color = 'lightgrey'
                            if d.year == year and d.month == month:
                                if d < birth_date:
                                    cell_color = 'lightgrey'
                                else:
                                    if d < death_date:
                                        if d < today_date:
                                            cell_color = 'lightpink'
                                        else:
                                            cell_color = 'lightgreen'
                                    else:
                                        cell_color = 'lightgrey'

                                str_table += '<td bgcolor="' + cell_color + '">' + str(d.day) + '</td>'

                                last_day = d.day
                            else:
                                pass

                        for d in range(last_day, 31):
                            str_table += '<td> </td>'

                        #str_table += '</td>'

                    str_table += '</tr>'

                str_table += '</table></div>'
                html_table =  mark_safe(str_table)
                
        else:
            pass
    else:
        pass

    return render(request, 'my_life_calendar/my_life_calendar.html', {'html_table':html_table})
