# forms.py
from django import forms

class VoiceUserForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'input w-full',
            'placeholder': 'Enter your username',
            'required': 'true'
        })
    )
    
    voice_note = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'hidden',
            'accept': 'audio/*',
            'required': 'true'
        }),
        label='Voice Recording',
        help_text='Record a short voice sample for authentication'
    )