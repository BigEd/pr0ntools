'''
pr0ntools
Copyright 2011 John McMaster <JohnDMcMaster@gmail.com>
Licensed under the terms of the LGPL V3 or later, see COPYING for details

.pto format?
http://photocreations.ca/panotools/stitch.txt
XXX: use a map instead
'''

'''
# Hugin project file
# generated by Autopano

# Panorama settings:
p w8000 h1200 f2 v250 n"PSD_mask"

# input images:
#-imgfile 2816 2112 "Z:\home\mcmaster\buffer\IC\motorola_mcu_vince\top_metal\5X\0.1\x00000_y00000.jpg"
o f0 y+0.000000 r+0.000000 p+0.000000 u20 d0.000000 e0.000000 v70.000000 a0.000000 b0.000000 c0.000000
'''

import shutil
import os
from pr0ntools.temp_file import ManagedTempFile
from pr0ntools.execute import Execute
from control_point_line import ControlPointLine
from image_line import ImageLine
from variable_line import VariableLine
from mode_line import ModeLine
from panorama_line import PanoramaLine
from util import print_debug
		
'''
class ControlPointLineImage:
	image = None
	x = None
	y = None
	# Index		
	n = None
'''

'''
"autopano-sift-c" "--maxmatches" "0" "--maxdim" "10000" test.pto data/c0_r0.jpg data/c0_r1.jpg
	# Hugin project file generated by APSCpp

	p f2 w3000 h1500 v360  n"JPEG q90"
	m g1 i0

	# i: image file
	# w: width
	# h: height
	# f: field of view, default: 0
	# y: yaw: default 0
	# p: pitch: default 0
	# r: roll, default 90
	i w2816 h2112 f0 a0 b-0.01 c0 d0 e0 p0 r0 v180 y0  u10 n"data/c0_r0.jpg"
	i w2816 h2112 f0 a=0 b=0 c=0 d0 e0 p0 r0 v=0 y0  u10 n"data/c0_r1.jpg"

	v p1 r1 y1

	# automatically generated control points
	# c: control point
	# n0: lowercase n signifies lowercase coord letters
	# N0: uppercase N signifies uppercase coord letters
	# what is t?
	c n0 N1 x1444.778035 y233.742619 X1225.863118 Y967.737131 t0
	c n0 N1 x138.962214 y280.766699 X700.950061 Y337.168418 t0
	c n0 N1 x174.636854 y1506.062901 X409.952583 Y1520.077001 t0
	c n0 N1 x128.111790 y85.436614 X178.862171 Y82.166356 t0
	c n0 N1 x185.913687 y132.074929 X1316.285962 Y258.582828 t0
	c n0 N1 x575.842717 y186.222059 X807.577503 Y201.843139 t0
	c n0 N1 x106.501605 y234.781930 X415.561176 Y260.394812 t0
	c n0 N1 x106.501605 y234.781930 X415.561176 Y260.394812 t0
	c n0 N1 x282.454363 y861.246866 X524.759974 Y796.168031 t0
	c n0 N1 x263.741226 y1023.111056 X507.095358 Y958.025083 t0
	c n0 N1 x255.076623 y1046.452454 X521.642791 Y820.371911 t0
	c n0 N1 x21.128685 y1518.951592 X258.640812 Y1531.902643 t0
	c n0 N1 x154.281249 y1794.318825 X2276.028785 Y629.057778 t0
	c n0 N1 x184.953100 y1459.943702 X420.250084 Y1474.768162 t0
	c n0 N1 x184.953100 y1459.943702 X420.250084 Y1474.768162 t0
	c n0 N1 x176.023646 y1508.324113 X411.531954 Y1522.403846 t0
	c n0 N1 x120.663877 y774.190799 X1884.899395 Y804.325721 t0
	c n0 N1 x151.601649 y1534.284888 X386.385138 Y1549.239989 t0
	c n0 N1 x855.583962 y1992.647570 X1418.183265 Y51.846079 t0
	c n0 N1 x584.941773 y467.957317 X2294.246845 Y658.254045 t0
	c n0 N1 x1217.925413 y935.521381 X1477.978209 Y216.417092 t0
	c n0 N1 x389.932676 y626.473870 X628.094681 Y645.153382 t0
	c n0 N1 x1455.674496 y1538.841677 X1622.255876 Y476.350083 t0

	# :-)


Example file

	p f2 w3000 h1500 v360  n"JPEG q90"
	m g1 i0

	i w2816 h600 f0 a0 b-0.01 c0 d0 e0 p0 r0 v180 y0  u10 n"/tmp/0.6621735916207697.png"
	i w2816 h600 f0 a=0 b=0 c=0 d0 e0 p0 r0 v=0 y0  u10 n"/tmp/0.5022987786350409.png"

	v p1 r1 y1

	# numbers index into above images
	c n0 N1 x983.515978 y31.390674 X860.944595 Y132.080243 t0
	c n0 N1 x652.899413 y71.500283 X807.577503 Y201.843139 t0
	c n0 N1 x474.578071 y154.235865 X107.943696 Y223.202780 t0
	c n0 N1 x774.903103 y186.724081 X1830.890967 Y429.024407 t0
	c n0 N1 x1201.353730 y299.329003 X1269.005225 Y511.798210 t0
	c n0 N1 x1708.592510 y359.149116 X1873.061084 Y499.156064 t0
	c n0 N1 x192.653946 y158.115483 X80.809197 Y254.420106 t0


	# specify variables that should be optimized
	# Seems there is a lone v entry at the end
	# Hugin GUI groups the following by image: y, p, r
	# And these by lens: v, a, b, c, d, e
	# However, .pto specifies them for invidual by image
	v e0 
	v d1 e1 
	v d2 e2 
	v d3 e3 
	v 
'''
class PTOProject:
	def __init__(self):
		# File name, if one exists
		self.file_name = None
		# Raw project text, None is not loaded
		self.text = None
		# If this is a temporary project, have it delete upon destruction
		self.temp_file = None
		# FIXME: not loaded?
		self.image_file_names = None
		# Could be a mix of temp and non-temp, so don't make any ordering assumptions
		self.temp_image_files = set()
	
		# 'p' line
		self.panorama_line = None
		# 'm' line
		self.mode_line = None
		# Those started with #hugin_
		# option_lines = None
		# Raw strings
		self.comment_lines = None
		# c N1 X1225.863118 Y967.737131 n0 t0 x1444.778035 y233.74261
		self.control_point_lines = None
		self.image_lines = None
		'''
		I bet lone v lines can be omitted
		# Variable lines
		v
		v d1 e1 p1 r1 y1
		v d2 e2 p2 r2 y2
		v d3 e3 p3 r3 y3
		v
		'''
		self.variable_lines = None
		# Raw strings, we don't know what these are
		self.misc_lines = list()
	
	def index_to_image(self, index):
		if index >= len(self.image_lines):
			raise IndexError('index: %d, items: %d' % (index, len(self.image_lines)))
		
		return self.image_lines[index]
	
	@staticmethod
	def from_file_name(file_name, is_temporary = False):
		ret = PTOProject()
		ret.file_name = file_name
		if is_temporary:
			ret.temp_file = ManagedTempFile.from_existing(file_name)
		return ret

	@staticmethod
	def from_temp_file(temp_file):
		ret = PTOProject()
		ret.file_name = temp_file.file_name
		ret.temp_file = temp_file
		return ret

	@staticmethod
	def from_text(text):
		ret = PTOProject()
		ret.text = text
		#ret.reparse()
		return ret

	@staticmethod
	def from_blank():
		return PTOProject.from_text('')

	def parse(self):
		'''Parse if not already parsed'''
		self.reparse()

	def reparse(self):
		'''Force a parse'''
		if False:
			print 'WARNING: pto parsing disabled'
			return

		self.panorama_line = None
		self.mode_line = None
		self.comment_lines = list()
		self.variable_lines = list()
		self.control_point_lines = list()
		self.image_lines = list()
		self.misc_lines = list()

		#print self.text
		print_debug('Beginning split on text of len %d' % (len(self.get_text())))
		for line in self.get_text().split('\n'):
			print_debug('Processing line: %s' % line)
			self.parse_line(line)
			print_debug()

	def parse_line(self, line):
		# Ignore empty lines
		if len(line) == 0:
			return
			 
		k = line[0]
		if k == '#':
			# Ignore comments and option lines for now
			# They have position dependencies and usually can be ignored anyway for my purposes
			print 'WARNING: ignoring comment line: %s' % line
		# Panorama line
		elif k == "p":
			self.panorama_line = PanoramaLine(line, self)
		# additional options
		elif k == "m":
			self.mode_line = ModeLine(line, self)
		# Image line
		elif k == "i":
			self.image_lines.append(ImageLine(line, self))
		# Optimization (variable) line
		elif k == "v":
			self.variable_lines.append(VariableLine(line, self))
		# Control point line
		elif k == "c":
			self.control_point_lines.append(ControlPointLine(line, self))
		else:
			print 'WARNING: unknown line type: %s' % line
			self.misc_lines.append(line)
			
	def regen(self):
		self.text = ''
		self.text += '# Generated by pr0ntools\n'

		#print 'Pano line: %s' % self.panorama_line
		self.regen_line(self.panorama_line)
		self.regen_line(self.mode_line)
			
		for line in self.image_lines:
			self.regen_line(line)

		for line in self.variable_lines:
			self.regen_line(line)

		for line in self.control_point_lines:
			self.regen_line(line)

		for line in self.comment_lines:
			self.regen_line(line)

	def regen_line(self, line):
		for comment_line in line.comments:
			self.text += '%s\n' % comment_line
		self.text += '%s\n' % line

	def __repr__(self):
		# Might make this diff from get_text to show parser info at some point
		return self.get_text()

	def get_text(self):
		self.ensure_text_loaded()
		return self.text
		
	def ensure_text_loaded(self):
		if not self.text:
			self.text = open(self.file_name).read()

	def get_a_file_name(self, prefix = None, postfix = None):
		'''If doesn't have a real file, create a temp file'''
		if self.file_name:
			return self.file_name
		if postfix is None:
			postfix = ".pto"
		self.temp_file = ManagedTempFile.get(prefix, postfix)
		self.file_name = self.temp_file.file_name
		self.save()
		return self.file_name

	def set_file_name(self, file_name):
		self.file_name = file_name

	def set_text(self, text):
		self.text = text
		if self.file_name:
			self.save()

	def merge_into(self, others):
		'''Merge project into this one'''
		print 'others: %d' % len(others)
		temp = self.merge(others)
		self.text = temp.__repr__()
		print 'text len: %d' % len(self.text)
		if self.file_name:
			print 'saving'
			self.save()	

	def merge(self, others):
		'''Return a project containing both control points'''
		'''
		Does not allow in place replace, we have to move things around
		
		[mcmaster@gespenst bin]$ pto_merge --help
		pto_merge: merges several project files
		pto_merge version 2010.4.0.854952d82c8f

		Usage:  pto_merge [options] input.pto input2.pto ...

		  Options:
			 -o, --output=file.pto  Output Hugin PTO file.
									Default: <filename>_merge.pto
			 -h, --help			 Shows this help
		'''
		if len(others) == 0:
			print 'WARNING: skipping merge due to no other files'
			raise Exception('Nothing to merge')
			return None
			
		return self.do_merge(others)
		
	def do_merge(self, others):
		pto_temp_file = ManagedTempFile.get(None, ".pto")

		command = "pto_merge"
		args = list()
		
		args.append("--output=%s" % pto_temp_file)

		# Possible this is still empty
		if self.file_name and os.path.exists(self.file_name):
			args.append(self.file_name)
		for other in others:
			 args.append(other.get_a_file_name())
		
		print_debug(args)

		(rc, output) = Execute.with_output(command, args)
		# go go go
		if not rc == 0:
			print
			print
			print
			print 'Output:'
			print output
			print 'rc: %d' % rc
			raise Exception('failed pto_merge')
		return PTOProject.from_temp_file(pto_temp_file)

	def save(self):
		'''
		import traceback
		import sys
		sys.stdout.flush()
		sys.stderr.flush()
		traceback.print_stack()
		sys.stdout.flush()
		sys.stderr.flush()
		'''
		f = open(self.file_name, 'w')
		f.write(self.text)

	def save_as(self, file_name, is_new_filename = False):
		if self.text:
			f = open(file_name, "w")
			f.write(self.text)
		elif self.file_name:
			shutil.copyfile(self.file_name, file_name)
		# empty project?
		else:
			raise Exception("tried to save empty project")
		
		if is_new_filename:
			self.file_name = file_name

	# reload is a builtin...not sure if it would conflict
	def reopen(self):
		f = open(self.file_name, 'r')
		self.text = f.read()

	def get_image_file_names(self):
		return self.image_file_names

	def optimize_xy_only(self):
		# XXX: move this to earlier if possible
		'''
		Added by pto_merge or something
		v Ra0 Rb0 Rc0 Rd0 Re0 Vb0 Vc0 Vd0
		v Eb1 Eev1 Er1
		v Eb2 Eev2 Er2
		v Eb3 Eev3 Er3
		v
		
		
		Need something like (assume image 0 is anchor)
		v d1 e1 
		v d2 e2 
		v d3 e3 
		v 

		
		After saving, get huge i lines
		#-hugin  cropFactor=1
		i w2816 h2112 f-2 Eb1 Eev0 Er1 Ra0 Rb0 Rc0 Rd0 Re0 Va1 Vb0 Vc0 Vd0 Vx-0 Vy-0 a0 b0 c0 d-0 e-0 g-0 p0 r0 t-0 v51 y0  Vm5 u10 n"x00000_y00033.jpg"
		'''
		print_debug('Fixing up v (optimization variable) lines...')
		new_project_text = ''
		new_lines = ''
		for i in range(1, len(self.get_image_file_names())):
			# optimize d (x) and e (y) for all other than anchor
			new_lines += 'v d%d e%d \n' % (i, i)
		new_lines += 'v \n'
		for line in self.text.split('\n'):
			if line == '':
				new_project_text += '\n'				
			elif line[0] == 'v':
				# Replace once, ignore others
				new_project_text += new_lines
				new_lines = ''
			else:
				new_project_text += line + '\n'
		self.text = new_project_text
		print
		print
		print_debug(self.text)
		print
		print


	def hugin_form(self):
		'''
		Something is causing pto_merge to hang, but NOT ptomerge
		Only occurs if I wrap my commands in a script...
		The script doesn't do any fancy I/O redirection			
			clear
			rm -rf /tmp/pr0ntools_*
			pr0nstitch *.jpg out.pto
		pto_merge produces nicer output than ptomerge
		While ptomerge produces the fields I need, it leaves some other junk
		I think pto_merge also calculates width/heigh attributes


		part of Hugin
		[mcmaster@gespenst first]$ pto_merge
		Warning: pto_merge requires at least 2 project files

		pto_merge: merges several project files
		pto_merge version 2010.4.0.854952d82c8f


		part of perl-Panotools-Script
		[mcmaster@gespenst first]$ ptomerge  --help
		cannot read-open --help at /usr/share/perl5/Panotools/Script.pm line 91.		
		man ptomerge
		...
		ptomerge infile1.pto infile2.pto infile3.pto [...] outfile.pto
		...
		'''
		
		# However, this tool also generates an archaic .pto format that pto can parse, but I don't want to
		# pretend to merge into an empty project to force Hugin to clean it up
		# pto_merge --output=temp.pto /dev/null temp.pto
		if False:
			args = list()
			args.append("%s" % self.get_a_file_name())
			args.append("%s" % self.get_a_file_name())
			args.append("%s" % self.get_a_file_name())
		
			(rc, output) = Execute.with_output("ptomerge", args)
		else:
			args = list()
			args.append("--output=%s" % self.get_a_file_name())
			args.append("%s" % self.get_a_file_name())
		
			if False:
				args.append("/dev/null")
			else:
				empty_file = ManagedTempFile.get(None, ".pto")
				open(empty_file.file_name, 'w').write('')
				args.append(empty_file.file_name)

			(rc, output) = Execute.with_output("pto_merge", args)
			
		if not rc == 0:
			print
			print
			print
			print 'output:%s' % output
			raise Exception('Bad rc: %d' % rc)
		
		self.reopen()		

