from bs4 import BeautifulSoup as soup
import requests

def get_defense_tackle():

	url = 'https://www.nfl.com/stats/player-stats/category/tackles/2022/reg/all/defensivecombinetackles/desc'
	html_doc = requests.get(url).content

	ma_soupe = soup(html_doc, 'html.parser')

	tbody = ma_soupe.tbody
	trs = tbody.contents

	dico = dict()

	for i, tr in enumerate(trs[:12]) :

		nom_joueur = tr.find('a').string
		img_lien = tr.find(class_='img-responsive')['src']
		img_lien = img_lien[:64] + img_lien[71:]
		tackles_comb = tr.find_all('td')[-4].string
		tackles_assist = tr.find_all('td')[-3].string
		tackles_solo = tr.find_all('td')[-2].string
		sacks = tr.find_all('td')[-1].string

		dico[i] = nom_joueur, tackles_comb, tackles_assist, tackles_solo, sacks, img_lien

	return dico

def get_defense_int():

	url = "https://www.nfl.com/stats/player-stats/category/interceptions/2022/reg/all/defensiveinterceptions/desc"
	html_doc = requests.get(url).content

	ma_soupe = soup(html_doc, 'html.parser')

	tbody = ma_soupe.tbody
	trs = tbody.contents

	dico = dict()

	for i, tr in enumerate(trs[:12]):

		nom_joueur = tr.find('a').string
		img_lien = tr.find(class_='img-responsive')['src']
		img_lien = img_lien[:64] + img_lien[71:]
		ints = tr.find_all('td')[-4].string
		int_for_td = tr.find_all('td')[-3].string
		long_int_return_yard = tr.find_all('td')[-2].string
		long_int__return_td = tr.find_all('td')[-1].string

		dico[i] = nom_joueur, ints, int_for_td, long_int_return_yard, long_int__return_td, img_lien

	
	return dico