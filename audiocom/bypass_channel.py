import math
import numpy
import matplotlib.pyplot as p
import graphs
import random

class BypassChannel:
    def __init__(self, noise, lag, h):
        self.noise = noise
        self.lag = lag
        self.h = h
        #DO NOT modify the following lines.
        numpy.random.seed()
        random.seed()

    def xmit_and_recv(self, tx_samples):
        #raise NotImplementedError, "xmit_and_recv"
	# Convolve tx_samples with h
	conv = numpy.convolve(tx_samples, self.h)
	# Prepend lag samples of value 0
	lag_samples = numpy.zeros(conv.size + self.lag)
	lag_samples[self.lag:] = conv
	# Add gaussian random variable with 0 mean and self.noise variance
	return numpy.random.normal(lag_samples, self.noise)
