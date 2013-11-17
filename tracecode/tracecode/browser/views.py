# Create your views here.
from django.shortcuts import HttpResponse as render_html
def home(Request):
    '''
	Render View.
    '''
    return render_html("Hello browser")
