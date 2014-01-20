#!/usr/local/bin/python

import subprocess,sys,pprint,cgi,string
from psd_tools import PSDImage

if len(sys.argv) < 2:
	print 'input PSD file and output file name are required... exiting'
	exit()

"""
Call ruby command to get JSON representation of PSD file

"""

ruby_cmd = '/Users/pierson/2014/github/cpcbell/python-psd-utils/psd-parse.rb'
output = subprocess.check_output([ ruby_cmd, sys.argv[1] ])


layer_ary = output.split('{:type=>:layer,')

pprint.pprint(layer_ary)
exit()

text_ary = []
font_ary = []
css_ary = []

for layer in layer_ary:

	text_ary.append( layer.split(', :text=>{:value=>"') )
	font_ary.append( layer.split(':font=>') )
	css_ary.append( layer.split(':css=>') )

for the_text in css_ary:
	print the_text

exit()

for font in font_ary:

	print font

	css_ary = font.split(':css=>')

	print css_ary[0]

exit()

psd = PSDImage.load(sys.argv[1])

for layer in psd.layers:

	print layer.name

	if layer.bbox:
		pprint.pprint(layer.bbox)

	text_str = None
	if layer.text_data:

		pprint.pprint(layer.text_data)

		text_str = str(pprint.pformat(layer.text_data.text))

		try:

			text_str = cgi.escape(text_str).encode('ascii','xmlcharrefreplace')
		except:
			print 'failed to decode/encode'
			pass

		text_str = "</div><div>".join(text_str.split("\\r"))

		text_str = '<div>' + text_str + '</div>'

	if text_str is not None:
		print text_str
