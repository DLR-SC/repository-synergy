This is an extremely simple Python wrapper for SRILM:
  http://www.speech.sri.com/projects/srilm/

Basically it lets you load a SRILM-format ngram model into memory, and
then query it directly from Python.

Right now this is extremely bare-bones, just enough to do what I
needed, no fancy infrastructure at all. Feel free to send patches
though if you extend it!

Requirements:
  - SRILM
  - Cython

Installation:
  - Edit setup.py so that it can find your SRILM build files.
  - To install in your Python environment, use:
       python setup.py install
    To just build the interface module:
       python setup.py build_ext --inplace
    which will produce srilm.so, which can be placed on your
    PYTHONPATH and accessed as 'import srilm'.
    
Usage:

from srilm import LM

# Use lower=True if you passed -lower to ngram-count. lower=False is
# default.
lm = LM("path/to/model/from/ngram-count", lower=True)

# Compute log10(P(brown | the quick))
#
# Note that the context tokens are in *reverse* order, as per SRILM's
# internal convention. I can't decide if this is a bug or not. If you
# have a model of order N, and you pass more than (N-1) words, then
# the first (N-1) entries in the list will be used. (I.e., the most
# recent (N-1) context words.)
lm.logprob_strings("brown", ["quick", "the"])

# We can also compute the probability of a sentence (this is just
# a convenience wrapper):
#   log10 P(The | <s>)
#   + log10 P(quick | <s> The)
#   + log10 P(brown | <s> The quick)
lm.total_logprob_strings(["The", "quick", "brown"])

# Internally, SRILM interns tokens to integers. You can convert back
# and forth using the .vocab attribute on an LM object:
idx = lm.vocab.intern("brown")
print idx
assert lm.vocab.extern(idx) == "brown"
# .extern() returns None if an idx is unused for some reason.

# There's a variant of .logprob_strings that takes these directly,
# which is probably not really any faster, but sometimes is more
# convenient if you're working with interned tokens anyway:
lm.logprob(lm.vocab.intern("brown"),
           [lm.vocab.intern("quick"),
            lm.vocab.intern("the"),
           ])

# There are detect "magic" tokens that don't actually represent anything
# in the input stream, like <s> and <unk>. You can detect them like
assert lm.vocab.is_non_word(lm.intern("<s>"))
assert not lm.vocab.is_non_word(lm.intern("brown"))

# Sometimes it's handy to have two models use the same indices for the
# same words, i.e., share a vocab table. This can be done like:
lm2 = LM("other/model", vocab=lm.vocab)

# This gives the index of the highest vocabulary word, useful for
# iterating over the whole vocabulary. Unlike the Python convention
# for describing ranges, this is the *inclusive* maximum:
lm.vocab.max_interned()

# And finally, let's put it together with an example of how to find
# the max-probability continuation:
#   argmax_w P(w | the quick)
# by querying each word in the vocabulary in turn:
context = [lm.vocab.intern(w) for w in ["quick", "the"]]
best_idx = None
best_logprob = -1e100
# Don't forget the +1, because Python and SRILM disagree about how
# ranges should work...
for i in xrange(lm.vocab.max_interned() + 1):
    logprob = lm.logprob(i, context)
    if logprob > best_logprob:
        best_idx = i
        best_logprob = logprob
best_word = lm.vocab.extern(best_idx)
print "Max prob continuation: %s (%s)" % (best_word, best_logprob)
