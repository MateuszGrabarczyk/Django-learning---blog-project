from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Please enter your username", error_messages={
#         "required": "Your name must not be empty"
#     })
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "username": "Enter your name",
            "review_text": "Your feedback",
            "rating": "Your rating"
        }
        error_messages = {
            "username": {
                "required": "Your name must not be empty"
            }
        }

