from django import forms


class ArticleForm(forms.Form):
    aid = forms.IntegerField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    aid = forms.IntegerField()
    name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
