## One more month left to win $100,000! The second round of Chia Network's VDF competition ends July 4th.

NEW! Our reference Pentium G4500 system for the “SIMD and GPU optimizations not allowed” track 2 is online for testing with vdf_bot. To access, use the judge_nosimd command from your Keybase private channel:

/vdf judge_nosimd keybase://team/chia_network.TEAM/track2

For the “SIMD and GPU optimizations allowed” track 1, as before, you can test on our Xeon W-2123 system (dual AVX-512/no turboboost and RTX 2080 GPU) with the judge_speed command:

/vdf judge_speed keybase://team/chia_network.TEAM/track1

NB: vdf_bot is OPTIONAL and is provided as assistance to help teams test their entries on real reference hardware. We can’t guarantee availability or uptime so please test early if you plan to take advantage of this resource.

## Overview

This is the reference implementation for the VDF contest.
It includes our source code, as well as our install and run scripts.

The install.sh script is run by the server to install any dependencies, and/or compile the code. For example, for ours we are installing the GMP library and the FLINT library.

The run.sh file is what is executed to run the VDF. It takes two arguments:
* A discriminant in hex
* The number of iterations, in decimal

The script should output the result of the VDF (but not the proof), encoded as a, b of the final classgroup element.


## VDF v2

This implementation is written in C/C++ and is based on the results of the first round of the VDF competition.
During that round we were made aware of a more efficient algorithm for squaring binary quadratic forms, called NUDUPL. [Akashnil](https://github.com/Akashnil/chia-vdf-competition/tree/master/Entry1) also came up with a more efficient way of reducing the forms by using integer approximation.
We use the [GMP](https://gmplib.org) and [FLINT](http://www.flintlib.org) libraries for their big number arithmetic and other functions, such as GCD.

A NUDUPL implementation is described in the paper [Computational Aspects of NUCOMP](https://www.researchgate.net/publication/221451638_Computational_aspects_of_NUCOMP). Our implementation is based on the work of [bulaiden](https://github.com/Chia-Network/vdftrack1results/tree/master/bulaiden/entry) during the last round.

Also of particular note from the last round is [Sundersoft's entry](https://github.com/sundersoft2/chia-vdf) which used assembly encoding and SIMD instructions. It also contains written thoughts on how to improve the implementation further.

As well as the [old reference implementation](https://github.com/Chia-Network/oldvdf-competition), new contestants may find our [guide to classgroups](https://github.com/Chia-Network/vdf-competition/blob/master/classgroups.pdf) a useful resource.
You can also find all of the entries to the last round of the competition [here](https://github.com/Chia-Network/vdftrack1results).


## Hardware

We will be judging the SIMD/GPU track entries on a Xeon W-2123 CPU, which supports AVX-512 instructions, and a RTX 2080 GPU which supports the Cuda API.

The non-SIMD/non-GPU track entries will be judged on a Pentium G4500 system with no AVX support and no external GPU.

Every submission will be ran on a fresh install of Ubuntu Linux with super user privileges.


## Tracks

We have split the competition into two tracks:
1. SIMD and GPU optimizations allowed
2. SIMD and GPU optimizations not allowed

This is to help us separate the different kinds of optimizations - however if somebody from track 2 is confident about their entry they can submit their code to both as there is no necessity for a track 1 submission to use those techniques.

The prize will be $50,000 for the winner of each track.


---

## Entry Forms

An Entry may be submitted by a team of individuals working collaboratively (a “Team Contestant”), in which case, each individual member of the team must complete the Entry Form and all members of the Team Contestant must designate the same point of contact to receive official Challenge correspondence.

To enter the competition, send a completed version of the [Entry Form](../Application%20Form.pdf) and a signed version of the [Rules and Disclosures Agreement](../Rules%20and%20Disclosures.pdf) to [ali@chia.net](mailto:ali@chia.net).



Have any questions? Join [Chia's public Keybase group](https://keybase.io/team/chia_network.public)
