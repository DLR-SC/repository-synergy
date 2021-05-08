# 공지
epg2xml은 1.2.6 버전을 마지막으로 업데이트가 이루어 지지 않습니다.  
3월 31일 이후로 리포지터리 삭제 예정입니다.

# EPG2XML
이 프로그램은 EPG(Electronic Program Guide)를 웹상의 여러 소스에서 가져와서 XML로 출력하는 프로그램으로 python2.7 및 php5.4.45 이상에서 사용 가능하도록 제작되었다.  
python3과 php 5.4.45 이하에서는 정상적인 작동을 보장하지 못한다.  또한 외부의 소스를 분석하여 EPG 정보를 가공하여 보여주는 것이므로 외부 소스 사이트가 변경되거나 삭제되면 문제가 발생할 수 있다.  

## 개발자 후원하기
https://www.facebook.com/chericface  
페이스북을 사용하신다면 개발자 후원하는 방법이라고 생각해주시고 위의 링크 들어가서 좋아요 눌러주시면 감사하겠습니다.
제가 관련된 곳에서 운영하는 페이스북인데 아직 초기라서 사람이 많이 없습니다. 화학공학 및 소재 관련 사이트입니다.
감사합니다.  

## 필요 모듈

### epg2xml.py
BeautifulSoup(bs4), lxml, requests 모듈이 추가로 필요하다.  
설치 OS별로 모듈을 설치하기 위한 사전 설치 방법이 다를 수도 있으므로 검색해서 설치하도록 한다.  
pip install beautifulsoup4, pip install lxml, pip install requests 로 추가할 수 있다.  
* easy_install로 설치시 모듈이 인식되지 않는 경우가 있으므로 pip로 설치하기를 권한다.  

### epg2xml.php
json, dom, mbstring, openssl, curl 모듈이 필요하다. 일반적으로 PHP가 설치되어 있다면 대부분 설치되어 있는 모듈이나 설치되어 있지 않을 경우 추가로 설치해야 한다.

### epg2xml-web.php
epg2xml.php와 동일하다.

## 설정방법
### epg2xml.json
epg2xml.json 안의 항목이 설정 가능한 항목이다. 
<pre>
MyISP : 사용하는 ISP를 넣는다 .(ALL, KT, LG, SK가 사용가능하다)
MyChannels : EPG 정보를 가져오고자 하는 채널 ID를 넣는다. ("1, 2, 3, 4" 또는 "1,2,3,4")
output : EPG 정보 출력방향 (d: 화면 출력, o: 파일 출력, s:소켓출력)
default_icon_url : 채널별 아이콘이 있는 url을 설정할 수 있다. 아이콘의 이름은 json 파일에 있는 Id.png로 기본설정되어 있다.
default_rebroadcast : 제목에 재방송 정보 출력
default_episode : 제목에 회차정보 출력
default_verbose : EPG 정보 상세 출력
default_xmltvns : 에피소드 정보 표시 방법
default_fetch_limit : EPG 데이터 가져오는 기간.
default_xml_filename : EPG 저장시 기본 저장 이름으로 tvheadend 서버가 쓰기가 가능한 경로로 설정해야 한다.
default_xml_socket   : External XMLTV 사용시 xmltv.sock가 있는 경로로 설정해준다.
</pre>

### Channel.json
Channel.json 파일의 최신버전은 https://github.com/wonipapa/Channel.json 에서 다운받을 수 있다.  
Channel.json 파일을 텍스트 편집기로 열어보면 각채널별 정보가 들어 있다.  

## 옵션 소개
### epg2xml.py, epg2xml.php 옵션
실행시 사용가능한 인수는 --help 명령어로 확인이 가능하다.  
epg2xml.json의 설정을 옵션의 인수를 이용하여 변경할 수 있다.  
<pre>
-h --help : 도움말 출력
--version : 버전을 보여준다.
-i : IPTV 선택 (ALL, KT, SK, LG 선택가능) ex) -i KT
-d --display : EPG 정보를 화면으로 보여준다.
-o --outfile : EPG 정보를 파일로 저장한다. ex) -o xmltv.xml
-s --socket  : EPG 정보를 xmltv.sock로 전송한다. ex) -s /var/run/xmltv.sock
-l --limit : EPG 정보 가져올 기간으로 기본값은 2일이며 최대 7일까지 설정 가능하다. ex) -l 2
--icon : 채널 icon 위치 URL ex) --icon http://www.example.com
--rebroadcast : 제목에 재방송정보 표기 ex) --rebroadcast y
--episode : 제목에 회차정보 표기 ex) --episode y
--verbose : EPG 정보 상세하게 표기 ex) --verbose y
</pre>

### epg2xml-web.php 옵션
실행시 사용가능한 인수는 epg2xml.php?help 명령어로 확인이 가능하다.  
epg2xml.json의 설정을 옵션의 인수를 이용하여 변경할 수 있다.  
ex : http://domain/epg2xml.php?i=ALL&l=2

## 사용방법

### tv_grab_file 사용시 (https://github.com/nurtext/tv_grab_file_synology)
tv_grab_file 안의 cat xmltv.xml 또는 wget 이 있는 부분을 아래와 같이 변경해준다.  
python 경로와 php의 경로는 /usr/bin에 있고, epg2xml 파일은 /home/hts에 있는 것으로 가정했다.  
이 경우 epg2xml.json의 output을 d로 해야 한다.
#### PYTHON의 경우
<pre>
/usr/bin/python /home/hts/epg2xml.py 또는
/home/hts/epg2xml.py
</pre>

#### PHP CLI의 경우
<pre>
/usr/bin/php /home/hts/epg2xml.php 또는
/home/hts/epg2xml.php
</pre>

#### PHP WEB의 경우
<pre>
wget -O - http://www.examle.com/epg2xml-web.php 또는
wget -O - http://www.example.com/epg2xml-web.php?i=ALL&l=2
</pre>

### XMLTV SOCKET 사용시
**xmltv.sock 사용시 socat 등을 사용하지 않고 바로 socket에 쓰기가 가능하다**

#### PYTHON의 경우
<pre>
/usr/bin/python /home/hts/epg2xml.py 또는
/home/hts/epg2xml.py
</pre>

#### PHP CLI의 경우
<pre>
/usr/bin/php /home/hts/epg2xml.php 또는
/home/hts/epg2xml.php
</pre>

#### PHP WEB의 경우
php web 버전은 xmltv.sock을 지원하지 않는다.

## 라이센스
BSD 3-clause "New" or "Revised" License

## WIKI
https://github.com/wonipapa/epg2xml/wiki

## FAQ
https://github.com/wonipapa/epg2xml/wiki/FAQ

## 변경사항
### Version 1.2.6
  - SKB 함수 버그 수정
  - KT, LG, SK, SKB, NAVER 이외의 함수 삭제
### Version 1.2.5
  - SKB 함수 수정
  - SKB 함수 수정(p1)
  - SKY 함수 수정(p2)
  - HCN 함수 삭제(p3)
### Version 1.2.4
  - ISCS 함수 수정
  - SKB 함수 수정(p1)
### Version 1.2.3
  - PHP 버전통합
  - PYTHON 버전 html Parser 변수 추가(libxml지원안하는 기기 편의 지원)
  - everyontv 함수 추가
  - Channel.json Enabled 항목 제거
  - 에피소드 넘버 xmltv_ns 옵션 항목 추가 (epg2xml.json)
  - 가져오는 날짜 최대 7일로 변경
  - KT 함수 수정
  - PHP 버전 socket 사용시 화면에 출력되는 문제 해결(p1)
  - PHP 버전 한글 깨지는 문제 수정(p2)
  - SK 함수 수정(p3)
  - 이터레이션 수정(p4)
  - oksusu함수 추가(p4)
  - PHP 버전 Pooq함수 복구(p5)
### Version 1.2.2
  - My Channel 추가
  - 소스 추가
  - 에피소드 넘버 xmltv_ns 추가
  - PHP 공용함수 분리
  - POOQ 함수 기간에 관계없이 하루만 가져오는 것 수정
  - ISCS 함수 수정
  - HCN 함수 수정
### Version 1.2.1
  - SKB 함수 추가
  - 가져오는 날짜 최대 2일로 변경
  - 타이틀이 1부, 2부 등 을 포함할 때 1부, 2부를 서브타이틀로 이동
  - Channel.json release date 삭제
  - Channel.json 채널 기본 설정 Enalble 0으로 변경
  - Channel 소스 변경
  - GCN 채널 삭제
  - readme.txt Readme.md로 통합
### Version 1.2.0
  - 커넥션 관련 에러 예외 처리 추가
  - 채널 소스 변경
  - Channel.json release date 추가
### Version 1.1.9
  - 언어 버전 사항 체크
  - 필요 모듈 사항 체크
  - 버그 수정
  - php 버전 웹 버전 추가
  - php 버전 file_get_contents를 curl 사용으로 수정
### Version 1.1.8
  - KBS 함수 추가
  - 채널 변경 사항 반영
  - 스카이라이프 url 변경
  - EPG 누락 데이터 수정
### Version 1.1.7
  - PHP 7.0 지원
  - 채널 변경 사항 반영
  - 라디오 채널 추가
### Version 1.1.6
  - iptv 선택 항목에 ALL 추가
  - 에피소드 넘버 출력 수정
  - 시작 시간 에러 출력 수정
  - 타이틀 출력 수정
  - 서브타이틀 추출 수정
  - 데이터 중복 출력 문제 수정
  - php 버전이 5.6.3 이전일 때 DOM access 관련 에러 수정
### Version 1.1.5
  - inline 변수 재추가
### Version 1.1.4
  - epg2xml.json 파일 도입
  - inline 변수 삭제
  - PHP 버전 추가
  - 버그 수정
### Version 1.1.3
  - 제목에 회차정보, 재방송 정보 추가시 오류 수정
### Version 1.1.2
  - 재방송정보, 회차정보 옵션 추가
### Version 1.1.1
  - sk 카테고리 오류 수정
### Version 1.1.0
  - 채널 아이콘 추가
  - 오류 메시지 통합
### Version 1.0.9
  - 소켓파일이 없을 때 오류 추가
  - 채널 변경 사항 반영
### Version 1.0.8
  - 정지 시간 추가
  - 오류 출력 구문 디버그시만 출력으로 변경
  - 채널 소스 변경
### Version 1.0.7
  - urllib2를 requests로 변경
  - User Agent 변경
  - 오류 처리 추가
  - 채널 변경 사항 반영
  - 채널 소스 변경
  - 지역 지상파 채널 추가
### Version 1.0.6
  - urllib를 urllib2로 변경
  - User Agent 추가
  - 채널 변경 사항 반영
### Version 1.0.5
  - epg.co.kr의 epg 정보 못가져오는 것 수정
### Version 1.0.4
  - KODI에서 사용가능하도록 수정
  - 제목에서 서브타이틀 및 회차 분리
  - 서브타이틀 추가
  - 출연, 제작진 개인별로 분리
### Version 1.0.3
  - Channel.json 파일 오류 수정 
  - LG를 소스로 하는 EPG 정보 기간 오류 수정
### Version 1.0.2
  - ISP별 분리된 채널통합
  - 개별 채널별 EPG 정보 수집가능하도록 Enabled 추가
  - getMyChannel 함수 삭제
  - 채널 변경 사항 반영
  - KT TRU TV 채널 삭제
  - ISP 선택 설정 추가
  - EPG 정보 가져오는 기간 설정 추가
  - 채널 아이콘 설정 URL 설정 추가
  - tvheadend 전용 카테고리 추가
### Version 1.0.1
  - EPG 소스 변경
  - 등록된 채널 정보만 EPG 정보 가져오도록 설정
  - IPTV별 개인화
### Version 1.0.0
  - first release
