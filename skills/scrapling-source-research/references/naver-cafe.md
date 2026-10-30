# Naver Cafe handling

## Two separate gates

1. **Viewing gate:** 네이버 도움말상 `전체공개` 글은 비회원도 읽을 수 있다. `멤버공개` 글은 원칙적으로 멤버용이며, 검색·공유 설정에 따라 제한적으로 외부 노출될 수 있다.
2. **Collection gate:** 공개 화면이라고 해서 자동 수집 허가가 생기지는 않는다. 네이버 이용약관은 사전 허락 없는 자동화 도구를 이용한 게시물 수집과 기술적 조치 우회를 제한한다.

그래서 이 스킬은 네이버 URL에 다음 순서를 강제한다.

- 명시적 허가 증거 없음: 네트워크 수집 중단, `PLATFORM_PERMISSION_REQUIRED` 기록.
- 사용자가 저장한 공개 HTML 제공: 로컬 파일만 분석.
- 사이트 소유자 또는 플랫폼의 서면 허가 있음: 사용자가 근거 식별자·확인일·범위·도메인·만료일을 permission manifest에 기록한 뒤 낮은 요청량으로 실행. 도구는 이 진술의 법적 유효성을 독립 검증하지 않는다.
- 로그인·멤버 전용·권한 없음 신호: 즉시 `LOGIN_REQUIRED` 또는 `RESTRICTED`로 분류하며 우회하지 않음.
- 내부망 주소, 비표준 포트, URL 인증정보, 위험한 리다이렉트, robots.txt 금지 경로: 네트워크 요청 전 또는 다음 요청 전에 차단.

## Public-post selectors

로컬 HTML 또는 허가된 페이지에서 다음 본문 후보를 순서대로 확인한다.

- `.se-main-container p`
- `.article_viewer p`
- `#postViewArea p`
- `.ContentRenderer p`

셀렉터가 맞지 않으면 페이지 전체 텍스트를 무리하게 수집하지 말고 `UNCERTAIN`으로 남긴다.

## Primary references

- 네이버 카페 공개 설정: https://help.naver.com/service/5622/contents/15206?lang=ko&osType=PC
- 게시글 공개 범위: https://help.naver.com/service/5622/contents/15342?lang=ko&osType=PC
- 네이버 검색 노출 안내: https://help.naver.com/service/5626/contents/22937?lang=ko&osType=COMMONOS
- 네이버 이용약관: https://policy.naver.com/rules/service.html
