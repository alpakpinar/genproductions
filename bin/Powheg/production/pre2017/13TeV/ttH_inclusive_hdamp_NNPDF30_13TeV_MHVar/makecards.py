#!/usr/bin/env python

import argparse

masswidth = (
 (110, 0.00285),
 (115, 0.00312),
 (120, 0.00351),
 (123, 0.00382),
 (124, 0.00394),
 (125, 0.00407),
 (126, 0.00421),
 (127, 0.00436),
 (130, 0.00491),
 (135, 0.00618),
 (140, 0.00817),
 (145, 0.0114),
 (150, 0.0173),
 (155, 0.0309),
 (160, 0.0831),
 (165, 0.246),
 (170, 0.38),
 (175, 0.501),
 (180, 0.631),
 (190, 1.04),
 (200, 1.43),
 (210, 1.85),
 (230, 2.82),
 (250, 4.04),
 (270, 5.55),
 (300, 8.43),
 (350, 15.2),
 (400, 29.2),
 (450, 46.8),
 (500, 68.0),
 (550, 93.0),
 (600, 123.0),
 (700, 199.0),
 (750, 247.0),
 (800, 304.0),
 (900, 449.0),
 (1000, 647.0),
 (1500, 750.0),
 (2000, 1000.0),
 (2500, 1250.0),
 (3000, 1500.0),
)

# Read the mass points from the command line
parser = argparse.ArgumentParser()
parser.add_argument('mass_points', help='List of mass points for which the cards will be generated.', nargs='*', type=int)
args = parser.parse_args()

mass_points = args.mass_points

# Automatically to be appended to the end of powheg input file
endfile = '''
rwl_group_events 2000
lhapdf6maxsets 50
rwl_file 'pwg-rwl.dat'
rwl_format_rwgt 1
'''

template_filename = 'ttH_inclusive_hdamp_NNPDF30_13TeV_template.input'

with open(template_filename) as f:
  template = f.read()

for mass, width in masswidth:
  if mass not in mass_points:
    continue
  print "creating cards for mass", mass 
  with open("ttH_inclusive_hdamp_NNPDF30_13TeV_M{mass}.input".format(mass=mass), "w") as f:
    f.write(template.format(mass=mass, width=width))

    f.write(endfile)
