import textwrap
import sys
import re

label = re.compile(r'^[0-9a-f-]{36}$')
tcode = re.compile(r'^[0-9:.]{12} --> [0-9:.]{12}')
readingtext = False
blanklines = 0
textbuffer = ''

with open(sys.argv[1], 'r') as f:

	if f.readline() == 'WEBVTT\n':
		print('WEBVTT')
	else:
		raise ValueError('not a WEBVTT format file')


	for line in f:
		line = line.strip('\n')
	
		if len(line) == 0:
			# blank line

			# empty the text buffer
			if len(textbuffer) > 0:
				for chunk in textwrap.wrap(textbuffer, 70):
					print(chunk)
			textbuffer = ''
			blanklines += 1
			readingtext = False
			if blanklines < 2:
				print()
			continue

		if line.startswith('NOTE'):
			# discard note
			continue

		blanklines = 0

		if tcode.fullmatch(line):
			# deal with timecode
			print(line)
			readingtext = True
			continue

		if readingtext:
			# accumulate text
			if len(textbuffer) > 0:
				textbuffer += ' '
			textbuffer += line

