import getpass

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create a regular django user with no superuser or admin privilege'
    requires_migrations_checks = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()

    def handle(self, *args, **kwargs):
        self.stdout.write('This is just done')
        self.stdout.write(getpass.getuser())

        # try:
        #     name = self.get_input('What\'s your name') or getpass.getuser()
        #     password = getpass.getpass()
        #     self.stdout.write(name, str(password))
        # except KeyboardInterrupt:
        #     self.stdout.write('\nOperation cancelled\n')

    def get_input(self, message):
        return input(f'{message}: ')
