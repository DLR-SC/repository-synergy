Bedfellows
===================

Bedfellows is a Python library that uses Federal Election Commission data of political action committee contributions to other committees to calculate seven scores measuring the length and breadth of the relationship between donors and recipients. It also provides a way to see similar donors, recipients or pairs. It is intended as reporting tool for journalists and researchers interested in federal campaign finance data.

Bedfellows is a command-line tool, and requires a local or remote MySQL database (it defaults to local, but users can change the connection string in `main.py`). It also requires three tables from the FEC: candidates, committees and the committee-to-committee transaction file. These files should match the layouts from the FEC with the exception of an additional `cycle` field that users need to add. Bedfellows expects these tables to be named fec_candidates, fec_committees and fec_committee_contributions. When computing the scores, Bedfellows will create a number of tables in the database; most of them are not large.

In addition to the expected database tables, Bedfellows comes with several files listing campaign contribution limits, score weights and super PACs (which are excluded from the analysis since they do not make contributions to candidates). Of these, the list of super PACs may need to be updated depending on when the library is used.

### Requirements

In addition to MySQL, Bedfellows makes use of Python packages numpy, scipy and pandas. Full list in [requirements.txt](requirements.txt). You should use a tool like virtualenv to maintain control over your Python environment.

### Installation

Clone this repository and create a virtualenv in that directory. Then, `pip install -r requirements.txt`.

### Usage

Bedfellows is a command-line application:

```
    python main.py <Flag: 'overall' or 'cycle'> <Name of Database>

    Examples:
    python main.py overall fec
    python main.py cycle new
```

Note that it is required that a database containing tables fec_committee_contributions, fec_candidates and fec_committees be specified as the  third parameter. To assist users, we've provided versions of each with data for the 2010, 2012 and 2014 cycles. Download SQL dump files here:

* [fec_candidates](https://www.strongspace.com/shared/wka39lhqsc)
* [fec_committees](https://www.strongspace.com/shared/82w6oib687)
* [fec_committee_contributions](https://www.strongspace.com/shared/sv45ey3o8c) (zipped)

The `main.py` file simply calls `overall.py` or `groupedbycycle.py` as specified by the second paramater (which must be either `overall` or `cycle`).

Choosing `overall` will give you the option of computing scores, analyzing existing scores, or both for all cycles, while choosing `cycle` will do the same, prompting for a specific even-numbered cycle:

```
    Do you want to compute scores or perform a similarity analysis of scores already computed? Enter 'compute', 'analyze' or 'both' accordingly.

```

Entering `compute` will result in the script creating and populating any needed tables, and may take several minutes. For `analyze` the user will be prompted to enter a donor or recipient's FEC ID (usually the committee ID for donors and either committee or candidate ID for recipients, depending on how your table is populated), or both when looking at pairs.


### CONTRIBUTORS

Bedfellows was developed by Nikolas Iubel during an internship with the Interactive News team at The New York Times, and is edited by Derek Willis of The Times.

### LICENSE

Bedfellows is licensed under the MIT License. See [LICENSE](LICENSE) for details.
