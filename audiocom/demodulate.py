#demodulate workfile: 6.02 PS 4,5,6
import numpy
import sendrecv
import math

def avgfilter(samples_in, window):
    #raise NotImplementedError, "avgfilter"
    return numpy.array([numpy.mean(samples_in[i:min(i+window,len(samples_in))]) for i in range(len(samples_in))])

def lpfilter(samples_in, omega_cut):
    raise NotImplementedError, "lpfilter"

def envelope_demodulator(samples, sample_rate, carrier_freq, spb):
    #raise NotImplementedError, "envelope_demodulator"
    window = int(sample_rate / (carrier_freq * 2))
    return avgfilter([abs(s) for s in samples], window)

def avg_demodulator(samples, sample_rate, carrier_freq, spb):
    raise NotImplementedError, "avg_demodulator"

def quad_demodulator(samples, sample_rate, carrier_freq, spb, channel_gap = 500):
    raise NotImplementedError, "avg_demodulator"
