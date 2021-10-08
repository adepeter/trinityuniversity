from celery import shared_task


@shared_task(name='print_demo')
def show_demo():
    print('Printing HELLLO')

