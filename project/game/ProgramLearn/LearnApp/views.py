from django.shortcuts import render, get_object_or_404, redirect
from .models import Level, Challenge, UserProgress
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    levels = Level.objects.all()
    return render(request, 'index.html', {'levels': levels})

def challenges(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    challenges = Challenge.objects.filter(level=level)
    return render(request, 'challenges.html', {'level': level, 'challenges': challenges})


def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    if request.method == 'POST':
        user_code = request.POST.get('code')
        # Check the solution (simplified; in production, use a safe execution environment)
        if user_code.strip() == challenge.solution.strip():
            UserProgress.objects.update_or_create(
                user=request.user,
                challenge=challenge,
                defaults={'completed': True, 'score': 10}
            )
            feedback = "Correct!"
        else:
            feedback = "Incorrect. Try again!"
        return render(request, 'challenge_detail.html', {'challenge': challenge, 'feedback': feedback, 'user_code': user_code})
    return render(request, 'challenge_detail.html', {'challenge': challenge})




# @login_required
# def challenge_detail(request, challenge_id):
#     challenge = get_object_or_404(Challenge, id=challenge_id)

#     # Check if the request method is POST (when the user submits the code)
#     if request.method == 'POST':
#         user_code = request.POST.get('code')
#         feedback = ""

#         # Check if the submitted code matches the correct solution
#         if user_code.strip() == challenge.solution.strip():
#             # Save user progress, ensuring the user is properly authenticated
#             UserProgress.objects.update_or_create(
#                 user=request.user,  # This assumes the user is authenticated
#                 challenge=challenge,
#                 defaults={'completed': True, 'score': 10}
#             )
#             feedback = "Correct!"
#         else:
#             feedback = "Incorrect. Try again!"

#         # Render the template with feedback
#         return render(request, 'challenge_detail.html', {
#             'challenge': challenge,
#             'feedback': feedback,
#             'user_code': user_code
#         })

#     # Render the challenge detail page initially
#     return render(request, 'challenge_detail.html', {'challenge': challenge})


