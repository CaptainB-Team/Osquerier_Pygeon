from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy

#Form to send a custom query
class SendCustomQuery(forms.Form):
    query_text = forms.CharField(label='Custom Query')
    def clean_query_text(self):
        data = self.cleaned_data['query_text']
        if len(data) > 50000:
            raise ValidationError(ugettext_lazy('Invalid query - Querier Pygeon does not support queries greater than 50000 characters in length.'))
        return data


#Form to send a query from the query builder tool
class SendBuiltQuery(forms.Form):
    query_from = forms.CharField(label='What table would you like to get data from? ')
    query_select = forms.CharField(label='What columns would you like to be displayed? ')
    query_where = forms.CharField(label='How would you like to filter that data? ', required=False)
    def clean_query_text(self):
        from_clause = self.cleaned_data['query_from']
        select_clause = self.cleaned_data['query_select']
        where_clause = self.cleaned_data['query_where']
