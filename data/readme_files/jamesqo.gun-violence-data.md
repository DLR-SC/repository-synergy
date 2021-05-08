# Gun Violence Data

## What is this repository?

This repository contains data for all recorded gun violence incidents in the US between January 2013 and March 2018, inclusive.

## Why was it created?

There's currently a lack of large and easily-accessible amounts of detailed data on gun violence. This project aims to change that; we make a record of more than 260k gun violence incidents, with detailed information about each incident, available in CSV format. We hope that this will make it easier for data scientists and statisticians to study gun violence and predict future trends.

## Where did you get the data?

The data was downloaded from [Gun Violence Archive's website](http://www.gunviolencearchive.org/). From the organization's description:

> Gun Violence Archive (GVA) is a not for profit corporation formed in 2013 to provide free online public access to accurate information about gun-related violence in the United States. GVA will collect and check for accuracy, comprehensive information about gun-related violence in the U.S. and then post and disseminate it online.

All credits for the data go to Gun Violence Archive.

## How did you get the data?

Because GVA limits the number of incidents that are returned from a single query, and because the website's "Export to CSV" functionality was missing crucial fields, it was necessary to obtain this dataset using web scraping techniques.

**Stage 1:** For each date between 1/1/2013 and 3/31/2018, a Python script queried all incidents that happened at that particular date, then scraped the data and wrote it to a CSV file. Each month got its own CSV file, with the exception of 2013, since not many incidents were recorded from then.

**Stage 2:** Each entry was augmented with additional data not directly viewable from the query results page, such as participant information, geolocation data, etc.

**Stage 3:** The entries were sorted in order of increasing date, then merged into a single CSV file.

**[Click here]** to download the tarball the data is stored in. You can decompress the tarball using the [7-Zip] utility on Windows, or via the `tar` executable on macOS/Linux.

[Click here]: DATA_01-2013_03-2018.tar.gz?raw=true
[7-Zip]: https://www.7-zip.org/

## Data format

The data is stored in a single CSV file sorted by increasing date. It has the following fields:

| field                   | type         | description                                                               | required? |
|-----------------------------|------------------|-------------------------------------------------------------------------------|---------------|
| incident_id                 | int              |                 gunviolencearchive.org ID for incident                        | yes           |
| date                        | str              |                           date of occurrence                                  | yes           |
| state                       | str              |                                                                               | yes           |
| city_or_county              | str              |                                                                               | yes           |
| address                     | str              | address where incident took place                                             | yes           |
| n_killed                    | int              | number of people killed                                                       | yes           |
| n_injured                   | int              | number of people injured                                                      | yes           |
| incident_url                | str              | link to gunviolencearchive.org webpage containing details of incident         | yes           |
| source_url                  | str              | link to online news story concerning incident                                 | no            |
| incident_url_fields_missing | bool             | ignore, always False                                                          | yes           |
| congressional_district      | int              |                                                                               | no            |
| gun_stolen                  | dict[int, str] | key: gun ID, value: 'Unknown' or 'Stolen'                                     | no            |
| gun_type                    | dict[int, str] | key: gun ID, value: description of gun type                                   | no            |
| incident_characteristics    | list[str]        | list of incident characteristics                                              | no            |
| latitude                    | float            |                                                                               | no            |
| location_description        | str              | description of location where incident took place                             | no            |
| longitude                   | float            |                                                                               | no            |
| n_guns_involved             | int              | number of guns involved                                                       | no            |
| notes                       | str              | additional notes about the incident                                           | no            |
| participant_age             | dict[int, int] | key: participant ID                                                           | no            |
| participant_age_group       | dict[int, str] | key: participant ID, value: description of age group, e.g. 'Adult 18+'        | no            |
| participant_gender          | dict[int, str] | key: participant ID, value: 'Male' or 'Female'                                | no            |
| participant_name            | dict[int, str] | key: participant ID                                                           | no            |
| participant_relationship    | dict[int, str] | key: participant ID, value: relationship of participant to other participants | no            |
| participant_status          | dict[int, str] | key: participant ID, value: 'Arrested', 'Killed', 'Injured', or 'Unharmed'    | no            |
| participant_type            | dict[int, str] | key: participant ID, value: 'Victim' or 'Subject-Suspect'                     | no            |
| sources                     | list[str]        | links to online news stories concerning incident                              | no            |
| state_house_district        | int              |                                                                               | no            |
| state_senate_district       | int              |                                                                               | no            |

Important notes:

- Each list is encoded as a string with separator `||`. For example, `"a||b"` represents `['a', 'b']`.
- Each dict is encoded as a string with outer separator `||` and inner separator `::`. For example, `0::a, 1::b` represents `{0: 'a', 1: 'b'}`.
- The "gun ID" and "participant ID" are numbers specific to a given incident that refer to a particular gun/person involved in that incident. For example, this:

  ```
  participant_age_group = 0::Teen 12-17||1::Adult 18+
  participant_status = 0::Killed||1::Injured
  participant_type = 0::Victim||1::Victim
  ```

  corresponds to this:

  |                    | Age Group | Status | Type |
  |--------------------|---------------|------------|----------|
  | **Participant #0** | Teen 12-17    | Killed     | Victim   |
  | **Participant #1** | Adult 18+     | Injured    | Victim   |

### Example

The incident described [here](http://www.gunviolencearchive.org/incident/1081561) resulted in the following fields:

| incident_id | date | state | city_or_county | address | n_killed | n_injured | incident_url | source_url | incident_url_fields_missing | congressional_district | gun_stolen | gun_type | incident_characteristics | latitude | location_description | longitude | n_guns_involved | notes | participant_age | participant_age_group | participant_gender | participant_name | participant_relationship | participant_status | participant_type | sources | state_house_district | state_senate_district |
|-------------|------|-------|----------------|---------|----------|-----------|--------------|------------|-----------------------------|------------------------|------------|----------|--------------------------|----------|----------------------|-----------|-----------------|-------|-----------------|-----------------------|--------------------|------------------|--------------------------|--------------------|------------------|---------|----------------------|-----------------------|
| 1081561 | 3/29/2018 | Colorado | Pueblo | 617 W Northern Ave | 0 | 0 | http://www.gunviolencearchive.org/incident/1081561 | https://www.chieftain.com/news/crime/pueblo-sheriff-seizes-illegal-guns-drugs-cash-in-bessemer-building/article_436d713a-4be6-565f-a919-747ab83e66df.html | False | 3 | 0::Stolen\|\|1::Unknown\|\|2::Unknown\|\|3::Unknown\|\|4::Unknown\|\|5::Unknown\|\|6::Unknown\|\|7::Unknown\|\|8::Unknown\|\|9::Unknown\|\|10::Unknown\|\|11::Unknown\|\|12::Unknown\|\|13::Unknown\|\|14::Unknown\|\|15::Unknown\|\|16::Unknown\|\|17::Unknown\|\|18::Unknown\|\|19::Unknown\|\|20::Unknown\|\|21::Unknown\|\|22::Unknown\|\|23::Unknown\|\|24::Unknown | 0::Handgun\|\|1::Handgun\|\|2::Unknown\|\|3::Unknown\|\|4::Unknown\|\|5::Unknown\|\|6::Unknown\|\|7::Unknown\|\|8::Unknown\|\|9::Unknown\|\|10::Unknown\|\|11::Unknown\|\|12::Unknown\|\|13::Unknown\|\|14::Unknown\|\|15::Unknown\|\|16::Unknown\|\|17::Unknown\|\|18::Unknown\|\|19::Unknown\|\|20::Unknown\|\|21::Unknown\|\|22::Unknown\|\|23::Unknown\|\|24::Unknown | Non-Shooting Incident\|\|Drug involvement\|\|ATF/LE Confiscation/Raid/Arrest\|\|Possession (gun(s) found during commission of other crimes)\|\|Possession of gun by felon or prohibited person\|\|Stolen/Illegally owned gun{s} recovered during arrest/warrant | 38.2442 | Bessemer | -104.618 | 25 | Guns and drugs recovered from residence. | 0::43 | 0::Adult 18+ | 0::Male | 0::Phillip W. Key |  | 0::Unharmed, Arrested | 0::Subject-Suspect | https://www.chieftain.com/news/crime/pueblo-sheriff-seizes-illegal-guns-drugs-cash-in-bessemer-building/article_436d713a-4be6-565f-a919-747ab83e66df.html | 46 | 3 |

## Additional notes

- The list of incidents from 2013 is not exhaustive; only 279 incidents from that year were catalogued.
- 2 incidents were manually removed from the dataset: the [Las Vegas mass shooting incident](http://www.gunviolencearchive.org/download/las-vegas-shooting.pdf) and [incident 1081885](http://www.gunviolencearchive.org/incident/1081885).
  - The Las Vegas mass shooting had to be removed because information about the incident was stored in a PDF, which caused scraping to fail since the scraper expects an HTML webpage.
  - Incident 1081885 had to be removed because the location details were not parsing nicely.
  - PRs to manually add back either/both of these incidents are welcome. (Please edit the `stage1` files in `intermediate/`)
- Known issue: the `address` field should be required, but is missing for ~16k incidents.
- Please provide credit to and notify Gun Violence Archive if you intend to use this dataset in your project. [Read their terms here.](http://www.gunviolencearchive.org/about)

  > All we ask is to please provide proper credit for use of Gun Violence Archive data and advise us of its use.

## Contact us

If you're interested in using this dataset for your research, feel free to contact us and ask questions / let us know about your work at gunviolencedata@gmail.com. Please note that we are not affiliated with gunviolencearchive.org in any way.
