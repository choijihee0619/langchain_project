# LangChain 기초 학습 프로젝트

## 📋 프로젝트 개요

이 프로젝트는 **LangChain**을 활용한 AI 애플리케이션 개발 학습을 위한 포트폴리오입니다. 주식 분석, RAG(Retrieval-Augmented Generation) 시스템, 그리고 AI 소믈리에 서비스를 통해 LangChain의 핵심 개념들을 실습하고 구현하였습니다.

## 🚀 주요 프로젝트

### 1. AI 투자 보고서 생성 서비스 (Streamlit App)
- **파일**: `app.py`, `stock_info.py`, `search.py`, `reporting_service.py`
- **기능**: 
  - 실시간 주식 검색 (MeiliSearch 기반)
  - 회사 기본 정보 및 재무제표 조회 (yfinance API)
  - AI 기반 투자 보고서 자동 생성 (LangChain + OpenAI)
- **기술 스택**: Streamlit, LangChain, OpenAI API, yfinance, MeiliSearch

### 2. RAG 시스템 구현 (Pinecone)
- **파일**: `10_rag_pinecone.ipynb`
- **기능**:
  - Pinecone 벡터 데이터베이스 연동
  - 임베딩 벡터 저장 및 검색
  - 메타데이터 기반 필터링
  - 유사도 검색 구현
- **기술 스택**: Pinecone, LangChain, OpenAI Embeddings

### 3. AI 와인 소믈리에 서비스
- **파일**: `11_rag_소믈리에.ipynb`
- **기능**:
  - 멀티모달 입력 지원 (텍스트 + 이미지)
  - 와인 이미지 분석 및 음식 추천
  - 전문 소믈리에 페르소나 구현
- **기술 스택**: LangChain, OpenAI Vision API, 멀티모달 AI

### 4. 주식 분석 프로젝트
- **파일**: `09_project.ipynb`
- **기능**:
  - Microsoft 주식 분석 예제
  - 재무제표 기반 투자 의견 생성
  - 마크다운 형식 보고서 출력
- **기술 스택**: LangChain, OpenAI API, 금융 데이터 분석

## 🛠 기술 스택

### 핵심 라이브러리
- **LangChain**: AI 애플리케이션 프레임워크
  - `langchain`: 메인 프레임워크
  - `langchain-openai`: OpenAI 모델 연동
  - `langchain-ollama`: Ollama 로컬 모델 지원
  - `langchain-core`: 핵심 컴포넌트

### 외부 서비스 & API
- **OpenAI API**: GPT 모델을 통한 텍스트 생성 및 분석
- **Pinecone**: 벡터 데이터베이스 서비스
- **MeiliSearch**: 실시간 검색 엔진
- **yfinance**: 주식 데이터 API

### 웹 프레임워크 & 도구
- **Streamlit**: 빠른 웹 애플리케이션 개발
- **python-dotenv**: 환경 변수 관리

## 📁 프로젝트 구조

```
langchain_basic/
├── README.md                    # 프로젝트 문서
├── requirements.txt             # 의존성 관리
├── 00_config_test.py           # 환경 설정 테스트
├── test.py                     # OpenAI API 기본 테스트
│
├── # 주식 분석 웹 애플리케이션
├── app.py                      # Streamlit 메인 애플리케이션
├── stock_info.py               # 주식 정보 수집 클래스
├── search.py                   # MeiliSearch 검색 기능
├── reporting_service.py        # AI 투자 보고서 생성
│
├── # Jupyter 노트북 학습 자료
├── 09_project.ipynb            # 주식 분석 프로젝트
├── 10_rag_pinecone.ipynb       # Pinecone RAG 구현
├── 11_rag_소믈리에.ipynb        # AI 소믈리에 서비스
│
├── # 데이터 파일
├── winemag-data-130k-v2.csv    # 와인 데이터셋 (130k 레코드)
├── nasdaq_screener_*.csv       # NASDAQ 주식 목록
│
└── # 설정 및 로그
    ├── data.ms/                # MeiliSearch 데이터
    └── dumps/                  # 백업 및 덤프 파일
```

## 🔧 설치 및 실행

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
`.env` 파일 생성 후 다음 키들을 설정:
```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 3. MeiliSearch 서버 실행
```bash
# MeiliSearch 서버 시작 (로컬)
./meilisearch --master-key="aSampleMasterKey"
```

### 4. Streamlit 애플리케이션 실행
```bash
streamlit run app.py
```

## 📚 학습 성과

### LangChain 핵심 개념 습득
- **Prompt Templates**: 구조화된 프롬프트 설계
- **Chains**: LLM, 프롬프트, 파서 연결
- **Output Parsers**: 응답 형식 표준화
- **Multi-modal Input**: 텍스트와 이미지 동시 처리

### RAG 시스템 구현 경험
- **벡터 데이터베이스**: Pinecone을 활용한 임베딩 저장/검색
- **유사도 검색**: 의미론적 검색 구현
- **메타데이터 필터링**: 조건부 검색 최적화

### 실전 AI 애플리케이션 개발
- **금융 도메인 전문성**: 주식 분석 및 투자 의견 생성
- **멀티모달 AI**: 이미지 기반 와인 분석
- **웹 애플리케이션**: Streamlit을 통한 사용자 인터페이스 구현

### 외부 API 통합
- **금융 데이터**: yfinance를 통한 실시간 주식 정보
- **검색 엔진**: MeiliSearch 실시간 검색 구현
- **클라우드 서비스**: Pinecone 벡터 DB 연동

## 🎯 프로젝트 특징

- **실용성**: 실제 서비스 수준의 주식 분석 도구
- **확장성**: 모듈화된 구조로 기능 확장 용이
- **학습 중심**: 단계별 구현으로 개념 이해 증진
- **멀티모달**: 텍스트와 이미지를 함께 처리하는 AI 서비스

## 📈 향후 개선 계획

1. **성능 최적화**: 캐싱 및 비동기 처리 도입
2. **데이터베이스 연동**: 사용자 히스토리 및 선호도 저장
3. **고급 RAG**: 하이브리드 검색 및 리랭킹 구현
4. **배포**: Docker 컨테이너화 및 클라우드 배포

---