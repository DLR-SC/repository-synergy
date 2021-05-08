[다음영화](http://movie.daum.net)에서 영화/드라마 정보를 가져오는 Plex용 Metadata Agent입니다.

[드라마를 위한 Metadata Agent](https://github.com/hojel/DaumMovieTv.bundle)가 따로 있었으나 통합됨.

설정
==============

1. 영화 ID 덮어쓰기
   - _None_: 다음영화 ID를 유지
   - _IMDB_: [IMDB](http://www.imdb.com) ID를 대신 넘겨줌. OpenSubtitles Agent와 연결에 필요.
2. 드라마 ID 덮어쓰기
   - _None_: 다음영화 ID를 유지
   - _TVDB_: [TVDB](http://www.thetvdb.com) ID를 대신 넘겨줌. OpenSubtitles Agent와 연결에 필요.

OpenSubtitles과의 연결
==============

1. Plex Plug-in folder에서 OpenSubtitles.bundle 을 찾는다.
2. Contents/Code/__init__.py 를 다음과 같이 수정한다.

    \- contributes_to = ['com.plexapp.agents.imdb']  
    \+ contributes_to = ['com.plexapp.agents.imdb', 'com.plexapp.agents.daum_movie']  

    \- contributes_to = ['com.plexapp.agents.thetvdb']  
    \+ contributes_to = ['com.plexapp.agents.thetvdb', 'com.plexapp.agents.daum_movie']  

3. DaumMovie.bundle의 설정에서 영화 ID 덮어쓰기로 _IMDB_, 드라마 ID 덮어쓰기로 _TVDB_를 각각 선택한다.

FanartTV.bundle 에도 사용가능하다.
