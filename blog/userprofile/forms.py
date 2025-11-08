from django import forms
from froala_editor.widgets import FroalaEditor
from mysiteblog.models import BlogModel, Profile


class profileupdateform(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['image']

class profilebgupdateform(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['background']