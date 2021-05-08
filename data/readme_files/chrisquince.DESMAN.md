# DESMAN _De novo_ Extraction of Strains from MetAgeNomes

![alt tag](desmans.jpg)

## Table of Contents

[Overview](#overview)  

[Installation](#installation)

[Simple example](#simple_example)  

[Complete example](complete_example/README.md)  

[Using the desmanflow automated workflow](#desmanflow)  

## Overview

The DESMAN pipeline is described in the [bioRxiv preprint](http://biorxiv.org/content/early/2016/09/06/073825). The software 
itself enables strain inference from frequency counts on contigs across multiple samples. 
[Installation](#installation) and a [Simple example](#simple_example) are 
described below. Generating contig bins, and counts on those contigs in 
order to run DESMAN is rather an involved process. We propose two typical strategies 
for a DESMAN run:

1. If you are processing a well studied organism, for which a core gene set can be determined, then we suggest you adapt this analysis in [Complete example](complete_example/README.md). Which is a complete run  
including validation of results from this synthetic *E. coli* data set. We also 
provide two strategies two automate this entire process:

* A snakemake pipeline: [Complete snakemake example](complete_example_snakemake/README.md)

* A nextflow pipeline: [desmanflow](#desmanflow)

2. Alternatively for an environmental data set, when most organisms are novel without 
multiple cultured representatives then you will just use the 36 single-copy core genes that are universal to all species. This strategy is detailed in the associated repository [Complex synthetic community](https://github.com/chrisquince/StrainMetaSim). 


<a name="installation"/>

## Installation

To install simply type:
```bash
sudo ./setup.py install
```
These items are prerequisities for the installation of desman:

1. *Python 3*
2. *gcc*
3. *gsl*

The installation procedure varies on different systems, 
and described in this README is only how to proceed with a linux (ubuntu) distribution.

The first item, Python 3, should be installed on a modern Ubuntu distribution. 
A c-compiler, e.g. gcc, is needed to compile the c parts of concoct that uses the 
GNU Scientific Library gsl. For linux (ubuntu) this is installed through:

```bash
sudo apt-get install build-essential libgsl0-dev
```

For convenience we also recommend adding the scripts directory to your path:

```bash
export PATH=$HOME/myinstalldir/DESMAN/bin:$HOME/myinstalldir/DESMAN/scripts:$PATH
```

Obviously replacing myinstalldir as appropriate and adding this to your .bash_profile file.

<a name="simple_example"/>

## Simple example

To illustrate the actual strain inference algorithm we will start with a simple example using base frequencies 
that have been pre-prepared. Below we also give [a complete example](#complete_example) including 
pre-processing. The starting point for a Desman analysis is a csv file with base frequencies e.g.: 

[Strain mock community frequencies for COG0015](data/contig_6or16_genesL_scgCOG0015.freq)

This has the following format:

    Contig,Position,SampleName1-A,SampleName1-C,SampleName1-G,SampleName1-T,...,SampleNameN-A,SampleNameN-C,SampleNameN-G,SampleNameN-T

where SampleName1,...,SampleNameN gives the names of the different samples in the analysis. Followed 
by one line for each position with format:

    gene name, position, freq. of A in sample 1, freq. of C in 1,freq. of G in 1,freq. of T in 1,..., freq. of A in sample N, freq. of C in N,freq. of G in N,freq. of T in N 


### Finding variant positions for the test data set

The first step is to identify variant positions. This is performed by the desman script Variant_Filter.py. 
Start assuming you are in the DESMAN repo directory by making a test folder.

```bash
mkdir test
cd test
```

Then run the example data file which corresponds to a single COG from the mock community data set 
described in the manuscript. This COG0015 has 933 variant positions. The input file is in the data 
folder. We run the variant filtering as follows:
```bash
Variant_Filter.py ../../data/contig_6or16_genesL_scgCOG0015.freq -o COG0015_out -p
```

The variant filtering has a number of optional parameters to see them run:
```bash
Variant_Filter.py -h
```  

They should all be fairly self explanatory. We recommend always using the 
the '-p' flag for one dimenisonal optimisition of individual base frequencies if it is not 
too time consuming. The '-o' option is a file stub; all output files will be generated with this prefix.
A log file will be generated 'COG0015_out_log.txt' and output files: 

1. COG0015_outp_df.csv: This gives p-values for each position.

2. COG0015_outq_df.csv: This gives q-values for each position.

3. COG0015_outr_df.csv: This gives log-ratio statistics for each position.

4. COG0015_outsel_var.csv: This is the file of selected variants.

5. COG0015_outtran_df.csv: A matrix of estimated error rates.

### Inferring haplotypes and abundances for the test data set

Having found the variant positions we will now the run the program for inferring haplotypes and their abundance:

```bash
desman COG0015_outsel_var.csv -g 5 -e COG0015_outtran_df.csv -o COG0015_out_g5 -i 50 
```

These parameters specify the variants file. Then number of haplotypes as five '-g 5', an initial 
estimate for the error transition matrix taken from the variant detection '-e COG0015_outtran_df.csv', 
an output directory '-o COG0015_out_g5' and the number of iterations, '-i 50'.
The program takes the selected variants and infers haplotypes and their abundances using the Gibbs sampler given 
the assumption that five strains are present. All output files will be generated in the directory COG0015_out_g5. 
Once the program has finished running a few minutes on a typical computer it will generate the following 
files inside the output directory:

1. log_file.txt: This logs the progress of the program through the three stages: 
NTF initialisation, 'burn-in' Gibbs sampler and the sampling itself. 

2. Eta_star.csv: Prediction for error transition matrix (rows true bases, columns observed probabilities) taken 
from sample with largest log posterior.

3. Eta_mean.csv: Prediction for error transition matrix (rows true bases, columns observed probabilities) as the posterior mean 
calculated over all samples.						

4. Filtered_Tau_star.csv: Prediction for strain haplotypes. Each row of comma separated file contains:

```
gene name, position, haplotype1-A,  haplotype1-C,  haplotype1-G,  haplotype1-T,..., haplotypeG-A,  haplotypeG-C,  haplotypeG-G,  haplotypeG-T  
```

where 1 indicates the base present in that haplotype at that position.

5. Tau_mean.csv: As above but the posterior mean. This can lead to non-discrete haplotypes. This 
can be viewed as posterior probability of assignments. Prior to analysis results 
should be discretised.

6. Gamma_star.csv: This gives the relative frequency of each haplotye in each sample using the sample with 
largest log posterior. One row for each sample.

7. Gamma_mean.csv: As above but posterior mean.

8. Selected_variants.csv: Variants used for strain calling if filtering applied.

9. fit.txt: Statistics evaluating fit as number of haplotypes, number of non-degenerate haplotypes inferred, log maximum posterior probability, mean posterior deviance (-2.0\*Log likelihood)
10. fitF.txt: Statistics evaluating fit of assigned haplotypes (not in random subsample) as number of haplotypes, number of non-degenerate haplotypes inferred, log maximum posterior probability, mean posterior deviance (-2.0\*Log likelihood). Only generated if -r option used.

<a name="desmanflow"/>

## The desmanflow automated workflow

desmanflow automates the use of desman on individual machines or compute clusters.
It builds upon the nextflow workflow language, which has support for parallel execution on multi-core machines or via cluster resource schedulers such as SGE, PBS, slurm, and others.

To reconstruct strain genomes with desmanflow, you will first need to assemble your metagenome, call the species bins using e.g. CONCOCT, and then provide the original metagenome assembly, the list of species contig IDs, and a directory of FastQ files as input to desmanflow. The FastQ files are expected to be paired-end gzipped, in separate files ending with the suffix `.r1.fq.gz` and `.r2.fq.gz`. The desmanflow workflow produces a contig-level strain binning, rather than gene-level. Thus, if chimeric contigs exist in the assembly the accuracy of the resulting strain bins will potentially be reduced. 

### Installation of the desmanflow automated workflow

The following series of commands will install desman onto a clean Debian/Ubuntu system. These commands can take an hour or more to complete.

```bash
# install some programs systemwide (can be skipped if these already exist)
sudo apt install git python3-pip libgsl-dev liblapack-dev liblapacke-dev default-jre samtools bwa r-base

# install nextflow to the user's account
mkdir -p ~/bin
curl -fsSL get.nextflow.io | bash
mv nextflow ~/bin
chmod 755 ~/bin/nextflow
export PATH=$PATH:~/bin

# install some required python3 modules
pip3 install --user cython numpy
pip3 install --user biopython

# install DESMAN
git clone https://github.com/chrisquince/DESMAN.git
cd DESMAN
python3 setup.py install --user
export DESMANHOME=`pwd`
```

### Obtain a test dataset

A test dataset is available which consists of a metagenomic assembly generated by megahit, a list of contigs from the assembly that were assigned to the species, and a directory of FastQ files. The test dataset can be downloaded and unpacked on the command-line:

```bash
curl -fsSL https://cloudstor.aarnet.edu.au/plus/index.php/s/7DH5qMuM5jMbcUc/download > testdata.tar
tar xf testdata.tar
```



### Running the desmanflow automated workflow

First we run desmanflow to estimate the number of strains for this species:

```bash
./scripts/desmanflow.nf --speciescontigs=testdata/species_contigs.txt --assembly=testdata/testasm.fa --inputreads=testdata/fastq
```

This produces a PDF figure in `out/Dev.pdf` that shows the posterior mean deviance for each strain count.
We pick four strains as it looks like the knee in the curve, and now run desmanflow again, this time specifying the number of strains and requesting that it resume computation where the last run left off:

```bash
./scripts/desmanflow.nf --speciescontigs=testdata/species_contigs.txt --assembly=testdata/testasm.fa --inputreads=testdata/fastq -resume --straincount=4
```

The final output of the workflow is now in the `out/` directory and includes a FastA file for each predicted strain, along with posterior probability values for contig membership in the strains and SNV presence in the contigs.

Note that the output location defaults to `out`, but can be changed to another directory with the `--output=` command-line option to `desmanflow.nf`. The FastQ file name extensions default to `.r1.fastq.gz` and `.r2.fastq.gz`, but can be changed with the `--r12extglob=` option. For example to change them to `.R1.fastq` and `.R2.fastq` you would pass `--r12extglob=".R{1,2}.fastq"` on the command-line.

Once the workflow has completed it is safe to delete the `work/` directory, which contains data generated at the intermediate steps of the workflow.

This workflow uses a collection of 37 genes from bacteria and archaea to identify single copy regions of the assembly. The workflow can also be applied in situations where a different or larger set of single copy regions has been manually identified, as may be required when analysing viruses or eukarya. In this situation, a bed file specifying those regions can be given with the `--singlecopybed=` option.
