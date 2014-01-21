#!/usr/local/bin/python

import subprocess, sys, pprint, cgi, string, re
from psd_tools import PSDImage

if len(sys.argv) < 3:
	print 'input PSD file and output type (html or css) are required... exiting'
	exit()

"""
Call ruby command to get JSON representation of PSD file

"""

ruby_cmd = '/Users/pierson/2014/github/cpcbell/python-psd-utils/psd-parse.rb'
output = subprocess.check_output([ruby_cmd, sys.argv[1]])

layer_ary = output.split('{:type=>:layer,')

"""
pprint.pprint(layer_ary)
exit()
text_ary = []
font_ary = []
css_ary = []
"""


def css_display(layer,layer_ct):

	print '.layer' + str(layer_ct) + '{'

	name_re = re.compile(r', \:name\=>\"(.*?)\", ')
	try:
		print "\t" + '/** ' + name_re.search(layer).group(1) + ' */'
	except:
		pass

	font_family_re = re.compile(r', \:css\=>\"font-family\: (.*?)\;')
	try:
		fonts = font_family_re.search(layer).group(1)

		fonts_ary = fonts.split(', ')

		fonts_ary.remove('AdobeInvisFont')

		fonts_ary.append('sans-serif')

		fonts = ', '.join('"{0}"'.format(w) for w in fonts_ary)

		print "\t" + 'font-family: ' + fonts + ' ;'

	except:
		pass

	font_size = None

	font_size_re = re.compile(r'font-size\:\s?(.*?)\;')
	try:
		font_size = font_size_re.search(layer).group(1)

	except:
		pass

	if font_size is not None:

		font_val = float(font_size[:-2])

		font_em = font_val

		if 'px' in font_size:

			px_to_em = 16

			if font_val > px_to_em:
				font_em = font_val / px_to_em
			else:
				font_em = px_to_em / font_val

		if 'pt' in font_size:

			pt_to_em = 11.95

			if font_val > pt_to_em:
				font_em = font_val / pt_to_em
			else:
				font_em = pt_to_em / font_val

		font_em = round(font_em, 2)

		print "\t" + 'font-size: ' + str(font_em) + 'em;'


	font_color_re = re.compile(r'\\ncolor\:\s?(.*?)\;')
	try:
		font_color = font_color_re.search(layer).group(1)

		print "\t" + 'color: ' + font_color + ' ;'
	except:
		pass

	print '}'

	return layer

def html_display(layer,layer_ct):

	text_str = None

	try:
		text_re = re.compile(r':text\=>\{:value\=>\"(.*?)\",\s?')

		text_str = text_re.search(layer).group(1)
	except:
		print '<div class="layer' + str(layer_ct) + '"></div>'
		return None

	try:
		text_str = cgi.escape(text_str)
	except:
		pass

	try:
		uni_re = re.compile(r'(\\u0019)')

		text_str = uni_re.sub('&#39;',text_str)
	except:
		pass

	try:
		quote_re = re.compile(r'(\\")')

		text_str = quote_re.sub('&#34;',text_str)
	except:
		pass

	try:
		white_space_re = re.compile(r'(\\n)')

		text_str = white_space_re.sub(' ',text_str)
	except:
		pass

	try:
		white_space_re = re.compile(r'(\s+)')

		text_str = white_space_re.sub(' ',text_str)
	except:
		pass

	print '<div class="layer' + str(layer_ct) + '">' + text_str + '</div>'

	return layer

layer_ct = 1

for layer in layer_ary:

	if sys.argv[2] == 'css':
		css_display(layer,layer_ct)

	else:
		html_display(layer,layer_ct)

	layer_ct += 1

exit()

