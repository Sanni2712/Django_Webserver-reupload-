from django import forms
from froala_editor.widgets import FroalaEditor
from mysiteblog.models import BlogModel, Comment

class PageForm(forms.ModelForm):

    content = forms.CharField(widget=FroalaEditor(options={
    'heightMin': 300
  }))
    class Meta:
        model = BlogModel
        fields = ('content',)

class commentForm(forms.ModelForm):

    content = forms.CharField(widget=FroalaEditor(options={
    'heightMin': 300,
    'charCounterMax': 300,
  }))
    class Meta:
        model = Comment
        fields = ('content',)        