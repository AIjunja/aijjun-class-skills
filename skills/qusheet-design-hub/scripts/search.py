"""Search the bundled Qusheet factual catalog without network or dependencies."""
from pathlib import Path
import argparse, json, re

CATALOG = Path(__file__).resolve().parents[1]/'references/catalog.json'
ALIASES = {
 '푸터':['footer.design'], '하단':['footer.design'], '헤더':['navbar.gallery'], '내비게이션':['navbar.gallery'], '네비게이션':['navbar.gallery'],
 '온보딩':['User Onboard','Page Flows','UI Sources','WWIT','온보딩 페이지'],
 '게임':['Game Ui DB','게임 UIUX'], '브랜딩':['brandingstyleguides','브랜드 디자인'],
 '팔레트':['컬러','COOLORS','Realtime Colors','Happy Hues'], '명암':['컬러','contrast-ratio','Color.review'],
 '대비':['whocanuse','Randoma11y','use contrast','contrast-ratio','Color.review'],
 '투명색':['Alphredo'], '그라데이션':['그라디언트'], '슬라이드':['Deck.gallery','프레젠테이션 디자인'],
 '발표':['Deck.gallery','프레젠테이션 디자인'], '이메일':['email love','Goode Mail Copy','이메일 디자인'],
 '한글':['눈누','원티드','한글 맞춤','한글더미텍스트','한글 입숨'], '서체':['폰트','타이포그라피'],
 '모션':['codrops','Design Spells','use Animations','모션 디자인'],
 '컴포넌트':['Good Practices Design','designsystems.surf','Design Systems','checklist'],
 '상태':['checklist','Good Practices Design','Page Flows'], '목업':['목업'],
 '사진':['사진'], '아이콘':['아이콘'], '로고':['Font in Logo','로고 디자인','simpleicons'],
 '피그마':['피그마'], 'figma':['피그마'], 'sketch':['sketch'], 'lottie':['Lottie'],
 '포토샵':['포토샵'], 'photoshop':['포토샵'], 'ppt':['Deck.gallery','프레젠테이션 디자인'],
 '접근성':['웹 접근성','whocanuse','Randoma11y','use contrast'],
 '한글 더미':['한글더미텍스트','한글 입숨'], '패키지':['패키지 디자인'], '공간':['환경 디자인']
}
FILTER_ALIASES={'figma':'피그마','photoshop':'포토샵','sketch':'sketch','lottie':'Lottie','illustrator':'일러스트','saas':'saas','랜딩페이지':'랜딩 페이지','아이콘 디자인':'아이콘 디자인'}
FIELDS={'field':'fields','resource':'resources','system':'systems','type':'types','tool':'tools','extra':'extras','region':'regions'}

def normal(s):return str(s).strip().casefold()

def filter_value(s):return normal(FILTER_ALIASES.get(normal(s),s))

def rank(row,query):
    if not query:return 1
    name=normal(row['name'])
    tags=' '.join(str(v) for key in FIELDS.values() for v in row[key]).casefold()
    usage=normal(row['application_note'])
    terms=[normal(query)]+[normal(t) for t in re.split(r'\s+',query) if t]
    expanded=[]
    for key,values in ALIASES.items():
        if normal(key) in normal(query):expanded.extend(normal(v) for v in values)
    score=0
    for t in set(terms):
        if t==name:score+=120
        elif t in name:score+=35
        if t in tags:score+=12
        if t in usage:score+=2
    for t in set(expanded):
        if t==name:score+=80
        elif t in name:score+=25
        if t in tags:score+=8
    if len(row['fields'])>15 and score:score-=5
    return max(score,0)

def search(rows,args):
    result=[]
    for row in rows:
        if args.category and args.category.removeprefix('qusheet-') not in row['categories']:continue
        if any(values and not all(any(filter_value(v)==filter_value(tag) for tag in row[key]) for v in values) for option,key in FIELDS.items() if (values:=getattr(args,option))):continue
        score=rank(row,args.query or '')
        if score:result.append((score,row))
    result.sort(key=lambda item:(-item[0],len(item[1]['fields'])>15,item[1]['name'].casefold()))
    return [r for _,r in result]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query',default='')
    parser.add_argument('--category')
    for field in FIELDS:parser.add_argument('--'+field,action='append',default=[])
    parser.add_argument('--limit',type=int,default=8)
    parser.add_argument('--all',action='store_true')
    parser.add_argument('--json',action='store_true')
    parser.add_argument('--list-filters',action='store_true')
    args=parser.parse_args()
    data=json.loads(CATALOG.read_text(encoding='utf-8'));rows=data['records']
    if args.list_filters:
        filters={key:sorted({v for r in rows for v in r[column]}) for key,column in FIELDS.items()}
        filters['category']=sorted({v for r in rows for v in r['categories']})
        print(json.dumps(filters,ensure_ascii=False,indent=2));return
    categories={v for row in rows for v in row['categories']}
    if args.category and args.category.removeprefix('qusheet-') not in categories:
        parser.error('Unknown category; use --list-filters.')
    if args.limit<1:parser.error('--limit must be positive')
    matches=search(rows,args)
    shown=matches if args.all else matches[:args.limit]
    if args.json:
        print(json.dumps({'matched':len(matches),'shown':len(shown),'records':shown},ensure_ascii=False,indent=2));return
    print(f'Found {len(matches)} records; showing {len(shown)}. Snapshot: {data["captured_date"]}.')
    print('Source: https://www.qusheet.com/; external current features and licenses unverified.\n')
    for row in shown:
        print(f'- {row["name"]} | {row["role"]}\n  {row["url"]}\n  {row["application_note"]}\n  category: {", ".join(row["categories"])}\n  source: {row["source_url"]}')
    if not matches:print('No matching records. Inspect --list-filters or broaden only the relevant filter.')

if __name__=='__main__':main()
