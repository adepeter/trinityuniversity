from django.contrib.auth.models import Group


class Role(Group):

    class Meta:
        proxy = True