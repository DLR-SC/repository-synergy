fec-standardizer
================

An experiment to standardize individual donor names in campaign finance data using simple graph theory and machine learning.

## Basics

The objective of this project is to build an entirely automated workflow that can identify canonical individual donors in an arbitrary set
of campaign finance data. In order to test its accuracy, this experiment uses federal campaign finance data that has already had its donors
standardized by the Center for Responsive Politics. In order to measure the accuracy of the process, this workflow is designed to show how
often an automated process' judgment matches CRP's, which is considered the gold standard.

## Results

Using a set of 100,000 random individual contributions selected from CRP's data, this workflow identified the same canonical donors as CRP's
combination of human and automated classifiers between 96 and 98 percent of the time.

## More details

The whole process is documented in detail in the [wiki](https://github.com/cjdd3b/fec-standardizer/wiki) of this repo. Here's the table of contents:

- [Home](https://github.com/cjdd3b/fec-standardizer/wiki/)
- [Preprocessing](https://github.com/cjdd3b/fec-standardizer/wiki/Preprocessing)
- [Matching and classifying donors](https://github.com/cjdd3b/fec-standardizer/wiki/Matching-donors)
- [Defining donor clusters](https://github.com/cjdd3b/fec-standardizer/wiki/Defining-donor-clusters)
- [Applications and next steps](https://github.com/cjdd3b/fec-standardizer/wiki/Applications-and-next-steps)

## Questions or comments

At best, I'm an amateur when it comes to a lot of the techniques used here. I'm sure I made some mistakes and did some stupid things. If so, I'd love to hear about them!

If you have any questions or comments, feel free to leave them in the wiki or contact chase.davis@gmail.com. Thanks for your interest!
