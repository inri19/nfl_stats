from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

	dico = {}

	return render(request, 'NFL/home.html', dico)

def offense(request):

	from .data_scrape import offense_func

	qb_stats = offense_func.get_offense_pass()
	rb_stats = offense_func.get_offense_rush()
	wr_stats = offense_func.get_offense_receive()

	dico = { "qbs" : qb_stats, "rbs" : rb_stats, "wrs" : wr_stats }

	return render(request, 'NFL/offense.html', dico)

def defense(request):

	from .data_scrape import defense_func

	tackles_stats = defense_func.get_defense_tackle()
	ints_stats = defense_func.get_defense_int()

	dico = { "tackles" : tackles_stats, "ints" : ints_stats }

	return render(request, 'NFL/defense.html', dico)
