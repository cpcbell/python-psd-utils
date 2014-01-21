python-psd-utils
================

Python parsing wrapper utilities for ruby psd gem and in the future other python PSd packages.

The goal is to save a ton of time and create some usable HTML and CSS from PSD files.

Currently this will give you HTML divs with all the text layers and CSS that goes with them.

In the next revision I'm hoping it will also provide where it can dimension CSS for the divs in
case its helpful for saving more time.

I would like this to be pure ruby but I know python regex so for now its both ruby and python.

You will need at the very least:  gem install psd   and possibly gem install psd-enginedata and of course python.

The psd-parse.rb script simply runs psd with a full path to the PSD and returns the parsed data.

The psd_parse.py script takes 2 arguments, the full path to the PSD and an output type ( html or css ) for example:

python psd_parse.py /full/path/to/my.psd html

will output divs for each layer and if the layer has text data, text divs.

python psd_parse.py /full/path/to/my.psd css

will output CSS for those divs

I hope this saves you some time :D

-C
