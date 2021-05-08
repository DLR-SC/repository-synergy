# CARTMANGO
![CARTMANGO](https://thumbs.gfycat.com/ComfortableTidyBighornedsheep-size_restricted.gif)

흩어져 있는 장바구니와 위시리스트에 지치셨나요?
카트망고와 함께라면 어디서든 물건을 담고 모아서 볼 수 있습니다.
태그와 리스트로 쉽게 분류하고 공유할 수 있습니다.

Pull Request로 개발 과정에 직접 참여하세요!

## 지원
- Chrome Extension
- iOS APP (In development)
- Android APP (In development)

## 환경
python version: 3.4.3
django version: 1.10.1

## 로컬 환경 세팅
1. virtualenv로 파이썬 3.4.3 버전 가상환경을 만든다.
2. `pip install -r requirements.txt`로 파이썬 패키지 설치
3. `npm install`, `bower update`로 프론트엔드 의존성 설치
4. `python manage.py migrate`로 디비 마이그레이션
5. `./manage.py createsuperuser`로 슈퍼유저 만들기
6. SECRET_KEY, Facebook OAuth key는 [jayjin](mailto:jayjinjay@gmail.com)이 가지고 있으므로 secret.json파일을 요청한다.

## 서버 띄우기
1. `gulp`명령어로 less파일을 css로 컴파일, minify한다.
2. `python manage.py runserver`로 서버를 띄운다.

## Chrome Extension storage
물품 아이디는 `Math.floor(Date.now() / 1000)` 로 타임스탬프 찍는다.
```json
{
  username: 'foo'
  product_list: [
     {
      url: 'http://www.gsshop.com/prd/prd.gs?prdid=24926497',
      title: '[더망고] 필리핀 카라바오 망고 5kg 20과',
      price: 38900,
      shop: 'GSSHOP',
      img: 'http://image.gsshop.com/image/24/92/24926497_L1.jpg',
      timestamp: '1492327941'
    }
  ]
}
```
