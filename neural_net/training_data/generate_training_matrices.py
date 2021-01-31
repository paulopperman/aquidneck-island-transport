import itertools
from pyDOE import lhs
import numpy as np


def write_od_file(od_dict, filename, scale=1.0):
	'''
	Write a VISUM style origin-destination file.
	:param od_dict: a dict of the flow.  key is ordered tuple (origin, destination)
	:param filename: the output file
	:param scale: a constant to scale the flows by.  default is 1.00
	:return:
	'''

	with open('./od_files/%s' % filename, 'w+') as f:
		f.write("$OR;D2\n")
		f.write("0.00 \t 1.00\n")
		f.write("{:.2f}\n".format(scale))
		for od_pair in od_dict:
			frm = od_pair[0]
			to = od_pair[1]
			flow = od_dict[od_pair]
			f.write("%s\t%s\t%s\n" % (frm, to, flow))
		f.close()


# list taz ids from the model
taz_ids = [1, 2, 3, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 590, 591,
		   592, 593, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613,
		   614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635,
		   636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654]

od_pairs = list(itertools.product(taz_ids, taz_ids))  # create ordered pairs between each taz
num_factors = len(od_pairs)

samples = 1000  # number of samples per factor for the design matrix.  equals the number of independent sumo simulations
design_matrix = lhs(num_factors, samples=samples)  # latin hypercube sampled design matrix. criterion selection adds significant time

# weight the design matrix based on max aadt flow from a taz
taz_weights = [527.781616, 325.73761, 563.544373, 38.137405, 33.834393, 76.295921, 59.563725, 32.558113, 37.900215,
			   24.886068, 39.549694, 74.731361, 175.710098, 77.775589, 55.181942, 115.814072, 83.126404, 85.860756,
			   131.306976, 41.893452, 19.646582, 22.24085, 563.544373, 27.158676, 169.253586, 1,
			   58.616257, 77.474403, 9.421277, 116.410698, 20.076073, 112.129051, 65.309929, 115.787544, 133.354431,
			   31.713661, 1, 462.791016, 1, 112.134636, 31.868183, 39.719654, 20.976444, 333.83255, 59.94006, 28.77335,
			   60.700512, 375.866394, 22.436918, 20.09548, 57.191509, 380.090851, 9.80699, 56.802017, 54.595867,
			   154.919678, 191.189301, 85.007637, 45.719048, 35.834496, 50.609646, 31.922644, 206.693695, 59.265503,
			   59.131649, 49.796757, 49.158249, 187.8853, 107.439064, 48.641521, 36.24791, 81.013283, 81.591423, 82.6978,
			   10.915609, 54.399651, 116.806564, 527.781616, 93.386177, 42.092995, 109.13726, 118.445641, 83.966866,
			   343.854645]

matrix_weights = np.array(taz_weights).repeat(len(taz_ids))  # upsample array to line up with od pairs

scaled_matrix = matrix_weights * design_matrix  # scale the design matrix

# write runs to matrix files
for i in range(samples):
	sample_dict = dict(zip(od_pairs, scaled_matrix[i, :]))
	write_od_file(sample_dict, "od_sample_{:0>4d}.txt".format(i), 0.25)

