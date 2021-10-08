from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils import timezone

User = get_user_model()


class OnlineStatusMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        now = timezone.now()
        if request.user.is_authenticated:
            cache.set(f'seen_{current_user.username}', now,
                      settings.USER_LASTSEEN_TIMEOUT)
        response = self.get_response(request)
        get_last_seen = cache.get(f'seen_{current_user.username}', now)
        diff = now - get_last_seen
        if diff.seconds < 5:
            try:
                user = User.objects.get(username=current_user.username)
                user.last_seen = now
                user.save(update_fields=['last_seen'])
            except User.DoesNotExist:
                pass
        return response
