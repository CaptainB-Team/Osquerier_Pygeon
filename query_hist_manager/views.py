from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from query_hist_manager.models import QueryHistItem
from query_hist_manager.forms import SendCustomQuery, SendBuiltQuery
from query_hist_manager.send_query import sendQuery

def index(request):
    place_holder = 'PLACEHOLDER' #This is a placeholder variable and corresponding context element for eventual replacement with a short list of query-related statistics to display on the homepage
    context = {
        'placeholder': place_holder,
    }
    return render(request, 'index.html', context=context)

class queryHistView(generic.ListView):
    model = QueryHistItem
    #Assign the template variable
    context_object_name = 'query_history_list'
    #Grabs all the rows from the QueryHistItem table; this will be changed to filter by user when user authentication is implemented
    queryset = QueryHistItem.objects.all()
    #This is the template file name
    template_name = 'queryhist.html'

def customQueryView(request):
    #Validates the form and retrieves the required data
    if request.method == 'POST':
        form = SendCustomQuery(request.POST)
        if form.is_valid():
            query_text = form.cleaned_data['query_text']
            #Gets the query response and saves it to the database
            response_text = sendQuery(str(query_text))
            query_instance = QueryHistItem.objects.create(query_text=query_text, response_text=response_text)
            query_instance.save()
    #Block to handle non-POST requests. Mostly this is used for when the page is loaded fresh
    else:
        form = SendCustomQuery()
        query_text = ''
        response_text = ''
    #Puts the relevant data in context and then renders the form on the page
    context = {
                'form': form,
                'query_text': query_text,
                'response_text': response_text,
            }
    return render(request, 'custom_query.html', context)

def builderQueryView(request):
    #Validates the form and retrieves the required data
    if request.method == 'POST':
        form = SendBuiltQuery(request.POST)
        if form.is_valid():
            from_clause = form.cleaned_data['query_from']
            select_clause = form.cleaned_data['query_select']
            where_clause = form.cleaned_data['query_where']
            #Builds the query text based on the input data
            query_text = 'select ' + select_clause + ' from ' + from_clause
            if(where_clause != ''):
                query_text += ' where ' + where_clause

            #Gets the query response and saves it to the database
            response_text = sendQuery(str(query_text))
            query_instance = QueryHistItem.objects.create(query_text=query_text, response_text=response_text)
            query_instance.save()
    #Block to handle non-POST requests. Mostly this is used for when the page is loaded fresh
    else:
        form = SendBuiltQuery()
        query_text = ''
        response_text = ''
    #Puts the relevant data in context and then renders the form on the page
    context = {
                'form': form,
                'query_text': query_text,
                'response_text': response_text,
            }
    return render(request, 'querybuilder.html', context)
