#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Miguel Vaz on 2010-04-06.
Copyright (c) 2010 mvaz.net. All rights reserved.
"""

import sys
import os, re
import urllib, urllib2
from BeautifulSoup import BeautifulSoup

def main():
	d = dict( boardType='dep',
	disableEquivs='yes',
	input='Frankfurt (Main) Saalburg-/Wittelsbacherallee#3001517',
	maxJourneys='10',
	selectDate='today',
	showAdvancedProductMode='yes',
	showStBoard='yes',
	start='Anzeigen',
	time='now',
	uid='')
	
	params = urllib.urlencode( d )
	print params
	url = 'http://www.rmv.de/auskunft/bin/jp/stboard.exe/dn?L=vs_rmv'
	f = urllib2.urlopen(url, params)
	
	data = f.read()
	f.close()
	
	soup = BeautifulSoup(data)
	for i in soup.findAll('tr', {'class': re.compile('^depboard')} ):
		row = i.findAll('td')
		print row[0].contents[0], row[2].a.span.contents[0], row[3].span.a.contents[0]

if __name__ == '__main__':
	main()

