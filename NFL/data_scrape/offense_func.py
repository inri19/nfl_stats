from bs4 import BeautifulSoup as soup 
import requests

def get_offense_pass():

	url = "https://www.nfl.com/stats/player-stats/"
	html_doc = requests.get(url).content
	ma_soupe = soup(html_doc, 'html.parser')

	tbody = ma_soupe.tbody
	trs = tbody.contents

	dico = dict()

	for i, tr in enumerate(trs[:12]):
	    
	    nom_joueur = tr.find("a").string
	    img_lien = tr.find(class_='img-responsive')['src']
	    pass_yds = tr.find("td", class_="selected").string
	    yds_per_att = tr.find_all("td")[-14].string
	    att = tr.find_all("td")[-13].string
	    cmpt = tr.find_all("td")[-12].string
	    pourc_cmp = tr.find_all("td")[-11].string
	    td = tr.find_all("td")[-10].string
	    interception = tr.find_all("td")[-9].string
	    pass_20yds = tr.find_all("td")[-5].string
	    pass_40yds = tr.find_all("td")[-4].string
	    sack = tr.find_all("td")[-2].string
	    img_lien = img_lien[:64] + img_lien[71:]
	    
	    dico[i] = nom_joueur, pass_yds, yds_per_att, att, cmpt, pourc_cmp, td, interception, pass_20yds, pass_40yds, sack, img_lien

	return dico

def get_offense_rush():

	url = "https://www.nfl.com/stats/player-stats/category/rushing/2022/reg/all/rushingyards/desc"

	html_doc = requests.get(url).content
	ma_soupe = soup(html_doc, "html.parser")

	tbody = ma_soupe.tbody
	trs = tbody.contents

	dico = dict()

	for i, tr in enumerate(trs[:12]) :

	    nom_joueur = tr.find("a").string
	    img_lien = tr.find(class_='img-responsive')['src']
	    rush_yards = tr.find_all('td')[-9].string
	    nb_porter = tr.find_all('td')[-8].string
	    tds = tr.find_all('td')[-7].string
	    porter_plus_20 = tr.find_all('td')[-6].string
	    porter_plus_40 = tr.find_all('td')[-5].string
	    nb_fumble = tr.find_all('td')[-1].string
	    img_lien = img_lien[:64] + img_lien[71:]

	    dico[i] = nom_joueur, rush_yards, nb_porter, tds, porter_plus_20, porter_plus_40, nb_fumble, img_lien
	    
	return dico

def get_offense_receive():

	url = "https://www.nfl.com/stats/player-stats/category/receiving/2022/reg/all/receivingreceptions/desc"

	html_doc = requests.get(url).content
	ma_soupe = soup(html_doc, "html.parser")

	tbody = ma_soupe.tbody
	trs = tbody.contents

	dico = dict()

	for i, tr in enumerate(trs[:12]):

	    nom_joueur = tr.find('a').string
	    img_lien = tr.find(class_='img-responsive')['src']
	    nb_reception = tr.find_all('td')[-11].string
	    yards = tr.find_all('td')[-10].string
	    tds = tr.find_all('td')[-9].string
	    reception_plus_20 = tr.find_all('td')[-8].string
	    reception_plus_40 = tr.find_all('td')[-7].string
	    img_lien = img_lien[:64] + img_lien[71:]

	    dico[i] = nom_joueur, nb_reception, yards, reception_plus_20, reception_plus_40, tds, img_lien

	return dico