def previous_url(request):
    try:
        return {'previous_url': request.session['previous_url']}
    except KeyError:
        return {'previous_url': '/'}
