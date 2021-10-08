class RequestMonitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization

    def process_template_response(self, request, response):
        request.session['previous_url'] = request.META.get('HTTP_REFERER', request.path)
        return response

    def __call__(self, request):
        return self.get_response(request)
