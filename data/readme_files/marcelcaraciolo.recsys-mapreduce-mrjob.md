For more information, read the blog post:
http://aimotion.blogspot.com/2012/08/introduction-to-recommendations-with.html

# Python files that aren't in the MRJob file itself need to be uploaded
# separately, so put them in a tarball and use --python-archive
> tar -cvf metrics.tar.gz metrics.py
> python moviesSimilarities.py data/sampling.csv --python-archive data/metrics.tar.gz
