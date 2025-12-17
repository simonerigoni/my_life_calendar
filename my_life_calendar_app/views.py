from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.conf import settings
import os
import datetime
import pandas as pd
import mimetypes
from django.http.response import HttpResponse
import json
from io import StringIO


# Create your views here.


def my_life_calendar(request):
    html_table = ""
    day_data_labels = []
    day_data_data = []

    if request.method == "POST":
        if "submit-button" in request.POST:
            life_expectancy = request.POST.get("life-expectancy", 0)

            if life_expectancy == "":
                life_expectancy = 0
            else:
                life_expectancy = int(life_expectancy)

            # print(life_expectancy)

            birth_date = request.POST.get("birth-date", 0)

            if birth_date == "":
                birth_date = 0
            else:
                birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

            # print(birth_date)

            if life_expectancy == 0 or birth_date == 0:
                pass
            else:
                today_date = datetime.datetime.now()
                death_date = birth_date + datetime.timedelta(days=life_expectancy * 365)
                delta = datetime.timedelta(days=1)
                current_date = datetime.datetime.strptime(
                    str(birth_date.year) + "-01-01", "%Y-%m-%d"
                )
                end_date = datetime.datetime.strptime(
                    str(death_date.year) + "-12-31", "%Y-%m-%d"
                )

                dates = []

                while current_date <= end_date:
                    # print('{} {} {} {}'.format(current_date.strftime('%A'), current_date.day, current_date.strftime('%B'), current_date.year))
                    dates.append(current_date)
                    current_date += delta

                list_years = list(set([d.year for d in dates]))
                list_years.sort()

                str_table = r"<table><tr><th>Years \ Months</th>"

                for month in range(1, 13):
                    temp_date = datetime.datetime.strptime(
                        "2020-" + str(month) + "-01", "%Y-%m-%d"
                    )
                    str_table += (
                        '<td colspan="31">' + temp_date.strftime("%B") + "</td>"
                    )

                str_table += "</tr>"

                count_lived_days = 0
                count_remaining_days = 0
                last_day = 0

                for year in list_years:
                    str_table += "<tr><td>" + str(year) + "</td>"

                    for month in range(1, 13):
                        for d in dates:
                            cell_color = "lightgrey"
                            if d.year == year and d.month == month:
                                if d < birth_date:
                                    cell_color = "lightgrey"
                                else:
                                    if d < death_date:
                                        if d < today_date:
                                            cell_color = "lightpink"
                                            count_lived_days = count_lived_days + 1
                                        else:
                                            cell_color = "lightgreen"
                                            count_remaining_days = (
                                                count_remaining_days + 1
                                            )
                                    else:
                                        cell_color = "lightgrey"

                                str_table += (
                                    '<td bgcolor="'
                                    + cell_color
                                    + '">'
                                    + str(d.day)
                                    + "</td>"
                                )

                                last_day = d.day
                            else:
                                pass

                        for d in range(last_day, 31):
                            str_table += "<td> </td>"

                    str_table += "</tr>"

                str_table += "</table>"

                df = pd.read_html(StringIO(str_table))[0]
                # print(df.shape)
                media_folder = os.path.join(settings.MEDIA_ROOT, "my_life_calendar_app")
                if not os.path.exists(media_folder):
                    os.makedirs(media_folder)
                else:
                    pass
                df.to_excel(
                    os.path.join(media_folder, "my_life_calendar.xlsx"), index=False
                )
                str_table = (
                    '<div style="overflow: auto">' + str_table + "</table></div>"
                )
                html_table = mark_safe(str_table)

                day_data_labels = ["Lived", "Remaining"]
                day_data_data = [count_lived_days, count_remaining_days]

                # print(day_data_labels)
                # print(day_data_data)

        elif "download-button" in request.POST:
            # TODO: create constant for filename
            filename = "my_life_calendar.xlsx"
            filepath = settings.MEDIA_ROOT + "/my_life_calendar_app/" + filename
            path = open(filepath, "rb")
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path.read(), content_type=mime_type)
            response["Content-Disposition"] = "attachment; filename={}".format(filename)
            return response
        pass
    else:
        pass

    return render(
        request,
        "my_life_calendar_app/my_life_calendar.html",
        {
            "html_table": html_table,
            "day_data_labels": json.dumps(day_data_labels),
            "day_data_data": json.dumps(day_data_data),
        },
    )
