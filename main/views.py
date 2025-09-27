# from django.shortcuts import render
#
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world.")
#

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """Render a simple placeholder page.

    This view is decorated with ``login_required`` so only authenticated users
    can access it. When a user visits the root URL, django‑allauth will
    automatically redirect unauthenticated visitors to the login page. After
    logging in via Google, they will return here and see a welcome message.
    """
    return render(request, 'home.html', {})
