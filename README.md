# Project-Defense


If you are trying to run the project, make sure you have:
1) installed all the packages required in requirements.txt;
2) have 2 more terminals running, command for the 1st - "celery -A CarRental worker -l info --pool=solo" (worker),
command for the 2nd - "celery -A CarRental beat -l info" (beat)
3) You have set "EMAIL_HOST_USER" and "EMAIL_HOST_PASSWORD" in settings.py



The running terminals having celery commands are required in order to properly update revenue page as well as
update when a car is available to be rented again.



NOTE: if you want to manually run a celery task, in a new terminal (you have to have worker terminal opened)
run "celery -A CarRental call CarRental.common.tasks.task_name"
                                                     ^^^^^^^^^
                           replace task_name with the name of the task you want to run.
