from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges = {
    "january":"Run",
    "february": "Walk",
    "march": "Sleep",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
   

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text,
        "month_name": month})
        
    except:
        raise Http404()
    