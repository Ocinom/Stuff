# Let's find out about algorithms to find pi to the nth digit and apply it to python

# There are a number of ways to do it. You can try to understand the algorithm that goes behind it, or you can
# just scrape data off something like https://www.piday.org/million/ and pick a digit(albeit up to 1 million) with scrapy

# With anything that has no limits, a generator object help tremendously if it can be figured out for something as chaotic as pi.

# The Bailey-Borwein-Plouffe(BBP) solution looks very neat as well (https://web.archive.org/web/20150627225748/http://en.literateprograms.org/Pi_with_the_BBP_formula_%28Python%29)
# In fact, this is probably the way to go. Let's make a generator using integer arithmetic.

# Because the generated digit gets more precise the further down pi, some amount of precision and rational arithmetic is required.
