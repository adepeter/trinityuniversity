from django.core.cache import cache

from ..services.countries import get_countries


class FetchCountriesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # # Code to be executed for each request before
        # # the view (and later middleware) are called.
        current_cache = cache.get('countries_list', None)
        countries = []
        # # Code to be executed for each request/response after
        # # the view is called.
        response = self.get_response(request)
        if current_cache is None or len(current_cache) < 1:
            countries += get_countries()
            cache.set('countries_list', countries, 3600 * 24)
        return response


__all__ = [
    'FetchCountriesMiddleware'
]
