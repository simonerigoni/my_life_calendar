# My Life Calendar

## Introduction

When I have first saw the [my life calendar]( https://www.ekn.io/calendar/) I was impressed by it. It made me think about how the time just flow without we noticing it. It is a great idea to visualize it so I have decided to make my own version of the life calendar.

## Software and Libraries

This project uses Python 3.11 and the most important packages are:

* [Django](https://www.djangoproject.com/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## Local configuration

To setup a new local enviroment and install all dependencies you can run `.\my_scripts\Set-Up.ps1`. It will install:

* [Python](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)
* [Pre-commit](https://pre-commit.com/)

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. A pre-commit hook is a script that runs before a commit operation in a version control system. This allows to shift left code quality checks and remediations. You can change the hooks by updateing the file `.pre-commit-config.yaml`.

To launch the pre-commit hooks without an actual commit you can run `pre-commit run --all-files -v`.

## Data

Have a look at the `data` folder and its [DATA.md](data/DATA.md) file.

## Testing

No test implemented.

## Running the code

To run the application `uv run python manage.py runserver`. The default url to connect to it is http://127.0.0.1:8000/

## Results

The django application 

![Home](images/home.png)

In the home we can insert the birth date and the life expectancy. By pressing the Submit button we get a graph showing the day distribution and a table with all the days from the first day of the birth year classified as:

- light grey: days before the birth date and after the expected death date
- light pink: lived days before the current date
- light green: future days until the expected death date 

![Days](images/days.png)

By clicking the **Download** button is possible to download the calendar in Excel format

## List of activities

In the [TODO.md](TODO.md) file you can find the list of tasks and on going activities.

## Licensing and acknowledgements

Have a look at [LICENSE.md](LICENSE.md) and thanks to [Erik K. Nyquist]( https://www.ekn.io/calendar/) for the ispiration.

## Outro

I hope this repository was interesting and thank you for taking the time to check it out. On my Medium you can find a more in depth [story](https://simone-rigoni01.medium.com/funny-little-python-project-my-life-calendar-aa1e751a69a0) and on my Blogspot you can find the same [post](https://simonerigoni01.blogspot.com/) in italian. Let me know if you have any question and if you like the content that I create feel free to [buy me a coffee](https://www.buymeacoffee.com/simonerigoni).