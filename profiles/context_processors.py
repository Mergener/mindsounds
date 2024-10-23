from django.contrib.auth.decorators import login_required

@login_required
def profile_processor(request):
    profile = None
    if request.user.is_authenticated:
        profile = request.user.profile 

    return {'profile': profile}