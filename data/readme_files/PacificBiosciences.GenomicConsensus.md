<h1 align="center"><img src="http://www.pacb.com/wp-content/themes/pacific-biosciences/img/pacific-biosciences-logo-mobile.svg"/></h1>
<h1 align="center">GenomicConsensus</h1>
<p align="center">Genome polishing and variant calling.</p>

***

The ``GenomicConsensus`` package provides the ``variantCaller`` tool,
which allows you to apply the Quiver or Arrow algorithm to mapped
PacBio reads to get consensus and variant calls.

## Availability
Latest version can be installed via bioconda package `genomicconsensus`.

Please refer to our [official pbbioconda page](https://github.com/PacificBiosciences/pbbioconda)
for information on Installation, Support, License, Copyright, and Disclaimer.

## Background on Quiver and Arrow

*Quiver* is the legacy consensus model based on a conditional random
field approach.  Quiver enables consensus accuracies on genome
assemblies at accuracies approaching or even exceeding Q60 (one error
per million bases).  If you use the HGAP assembly protocol in
SMRTportal 2.0 or later, Quiver runs automatically as the final
"assembly polishing" step.

Over the years Quiver has proven difficult to train and develop, so we are
phasing it out in favor of the new model, Arrow.  *Arrow* is an
improved consensus model based on a more straightforward hidden Markov
model approach.

Quiver is supported for PacBio RS data.  Arrow is supported for PacBio
Sequel data and RS data with the P6-C4 chemistry.


## Running
-------
Basic usage is as follows:

```sh
% quiver aligned_reads{.cmp.h5, .bam, .fofn, or .xml}    \
>     -r reference{.fasta or .xml} -o variants.gff       \
>     -o consensus.fasta -o consensus.fastq
```

``quiver`` is a shortcut for ``variantCaller --algorithm=quiver``.
Naturally, to use arrow you could use the ``arrow`` shortcut or
``variantCaller --algorithm=arrow``.

in this example we perform haploid consensus and variant calling on
the mapped reads in the ``aligned_reads.bam`` which was aligned to
``reference.fasta``.  The ``reference.fasta`` is only used for
designating variant calls, not for computing the consensus.  The
consensus quality score for every position can be found in the output
FASTQ file.

*Note that 2.3 SMRTanalysis does not support "dataset" input (FOFN
 or XML files); those who need this feature should wait for the forthcoming
 release of SMRTanalysis 3.0 or build from GitHub sources.*


## More documentation

- [More detailed installation and running instructions](./doc/HowTo.rst)
- [FAQ](./doc/FAQ.rst)
- [variants.gff spec](./doc/VariantsGffSpecification.rst)
- [CHANGELOG](./CHANGELOG)

DISCLAIMER
----------
THIS WEBSITE AND CONTENT AND ALL SITE-RELATED SERVICES, INCLUDING ANY DATA, ARE PROVIDED "AS IS," WITH ALL FAULTS, WITH NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTIES OF MERCHANTABILITY, SATISFACTORY QUALITY, NON-INFRINGEMENT OR FITNESS FOR A PARTICULAR PURPOSE. YOU ASSUME TOTAL RESPONSIBILITY AND RISK FOR YOUR USE OF THIS SITE, ALL SITE-RELATED SERVICES, AND ANY THIRD PARTY WEBSITES OR APPLICATIONS. NO ORAL OR WRITTEN INFORMATION OR ADVICE SHALL CREATE A WARRANTY OF ANY KIND. ANY REFERENCES TO SPECIFIC PRODUCTS OR SERVICES ON THE WEBSITES DO NOT CONSTITUTE OR IMPLY A RECOMMENDATION OR ENDORSEMENT BY PACIFIC BIOSCIENCES.
