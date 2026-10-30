# AI쭌 수업용 스킬 모음

Claude Code 수업에서 바로 설치해서 쓰는 스킬 모음입니다.
설치하면 Claude Code에서 `/스킬이름`으로 부를 수 있어요.

## 들어 있는 스킬

| 스킬 | 하는 일 |
|---|---|
| `jh-landing-page` | 상품·서비스 하나를 중심으로 랜딩 페이지를 만들거나 고칩니다 |
| `jh-design` | 레퍼런스를 분석해서 웹사이트·웹앱 디자인을 정돈합니다 |
| `scrapling-source-research` | 공개 웹페이지를 낮은 요청량으로 읽어 출처가 남는 조사 자료로 정리합니다 |
| `qusheet-design-hub` | 디자인 큐시트 공개 디렉터리에서 자료를 찾아 알맞은 디자인 스킬로 연결합니다 |
| `qusheet-*` (10개) | 허브가 연결하는 분야별 디자인 스킬 (웹 UI, 앱 UX, 브랜드, 타이포, 컬러, 편집, 모션, 아이콘, 목업, 디자인 시스템) |

`qusheet-design-hub`는 `qusheet-*` 10개와 같은 폴더에 함께 설치해야 제대로 동작합니다.

## 설치 · Claude Code에 붙여넣기

Claude Code 새 대화에 아래를 그대로 붙여넣으세요.

```text
다음 공개 GitHub 저장소의 README를 먼저 읽어 줘.
https://github.com/AIjunja/aijjun-class-skills

skills 폴더의 스킬들을 내 Claude Code에 전역으로 설치해 줘.
설치 전에 어디에 설치되는지 먼저 보여 줘.
scrapling-source-research는 파이썬 패키지도 필요하니 같이 설치해 줘.
```

설치가 끝나면 Claude Code를 다시 열고 `/`를 입력해 목록에 뜨는지 확인합니다.

## 설치 · 직접 하기

Windows PowerShell:

```powershell
git clone https://github.com/AIjunja/aijjun-class-skills.git
cd aijjun-class-skills
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

macOS · Linux:

```bash
git clone https://github.com/AIjunja/aijjun-class-skills.git
cd aijjun-class-skills
bash ./install.sh
```

기본 설치 위치는 `~/.claude/skills` (전역)입니다.
한 프로젝트 안에서만 쓰려면 그 프로젝트 폴더의 `.claude/skills`에 복사하세요.

`scrapling-source-research`를 쓰려면 파이썬 패키지가 필요합니다.

```bash
python -m pip install "scrapling[fetchers]"
```

## 지켜 주세요

- `scrapling-source-research`는 robots.txt를 먼저 확인하고, 한 번에 최대 20개 URL을 1.5초 이상 간격으로 읽습니다. 로그인·유료·차단 우회 수집은 하지 않습니다. 사이트 이용약관을 확인하고 쓰세요.
- 레퍼런스 사이트는 구조와 원리를 참고하는 용도입니다. 남의 디자인·문구·이미지를 그대로 베끼지 마세요.
- 큐시트 디렉터리 정보는 2026-10-28에 공개 페이지에서 확인한 사실 정보(이름·주소·분류)입니다. 외부 사이트의 현재 기능·가격·라이선스는 쓸 때 직접 확인하세요.

## 라이선스

스킬 문서와 스크립트는 MIT 라이선스입니다. 포함된 Gmarket Sans 폰트는 SIL Open Font License를 따릅니다 (`skills/jh-design/assets/fonts/OFL.txt`). 외부 라이브러리와 서비스는 각자의 라이선스를 따릅니다. 자세한 내용은 [NOTICE.md](NOTICE.md)를 보세요.
