# POPONG Crawlers

Just some minor web crawlers.<br>
**Pull requests are always welcome.**

## License
[Affero GPL v3.0](http://choosealicense.com/licenses/agpl/)

- Required: License and copyright notice + State Changes + Disclose Source
- Permitted: Commercial Use + Modification + Distribution
- Forbidden: Hold Liable + Sublicensing

## Descriptions

### Production

#### bills
Get bill data from the [National Assembly](http://likms.assembly.go.kr/bill/jsp/main.jsp) and structurize to json formats. ([See attributes](https://github.com/teampopong/crawlers/wiki/Attributes-of-National-Assembly-Bills))

    pip install -U celery-with-redis    # Install dependencies
    cd bills
    cp settings.py.sample settings.py   # Input data directory
    python main.py

#### commentable_bills
Get commentable bills from [국회입법예고](http://pal.assembly.go.kr/law/mainView.do)

    cd commentable_bills
    python crawl.py     # open and set datadir first

#### committee_list
Get committee list data from the [위원회 현황](http://www.assembly.go.kr/assm/assemact/committee/committee01/assmCommittee/committeeUserList.do)

    cd committee_list
    python get.py       # To get data files

#### election_commission
Get Korean politicians' data from [Korea Election Commission (중앙선거관리위원회)](http://www.nec.go.kr/).<br>
This data contains the list of all people that have run for office in the National Asssmbly.

    cd election_commission
    python main.py -h

#### glossary
Get and merge data for [POPONG Glossary](http://popong.com/glossary) from:<br>
 `committee`: [Standing committee and Special Committee (국회상임위원회 및 특별위원회)](http://committee.na.go.kr/),<br>
 `likms`: [Integrated Legislation Knowledge Management System (입법통합지식관리시스템)](http://likms.assembly.go.kr/),<br>
 `nas`: [National Assembly Secretaritat (국회사무처)](http://http://nas.na.go.kr/).

    python get.py       # To get source data files
    python merge.py     # To create glossary.csv

#### google
Get Google search counts.

    cd google
    python ndocs.py

#### meetings
Get [National Assembly meetings](http://likms.assembly.go.kr/record/).

    cd meetings
    python crawl.py

#### meetings_calendar
Get [National Assembly meetings calendar](http://www.assembly.go.kr/renew10/anc/schedule/assm/assemact/council/council0101/assmSchCal/assemSchCal.do).

    cd meetings_calendar
    python get.py 2014-11-01 2014-11-11     # To get meetings schedule from 2014-11-01 to 2014-11-11 or 
    python get.py 2014-11-01                # To get meetings schedule at 2014-11-01

#### national_assembly
Get member information from the [Korean National Assembly](http://www.assembly.go.kr/).

    pip install Scrapy>=0.22.2
    cd national_assembly
    python crawl.py

#### naver_news
Get news articles for recent bills from Naver News.

    pip install psycopg2 lxml
    cd naver_news
    cp settings.py.sample settings.py
    vi settings.py                      # fill in values
    python crawl.py

#### peoplepower
Get [People Power 21 (열려라국회)](http://watch.peoplepower21.org) webpages. (*Currently broken*)

    cd peoplepower
    scrapy crawl peoplepower21

#### pledges
Get pledges from [NEC (선거관리위원회)](http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml?electionId=0020120411&requestURI=%2Felectioninfo%2F0020120411%2Fep%2Fepei01.jsp&topMenuId=EP&secondMenuId=EPEI01&menuId=&statementId=EPEI01_%232&electionCode=2&cityCode=0&proportionalRepresentationCode=0&x=17&y=11) for 19th National Assembly officials.

    cd pledges
    python crawler.py

#### rokps
Get Korean politicians' data from [ROKPS(헌정회)](http://www.rokps.or.kr).

    cd rokps
    python crawler.py
    python parser.py

#### wikipedia
Get Korean lastnames from Wikipedia.

    cd wikipedia
    python wiki_lastnames.py

Get Wikipedia links for assembly members.

    cd wikipedia
    python assembly_members.py

### Metrics

#### twitter
Get Twitter follower lists for specified handles.

    make twitter_setup
    python twitter/followers.py
