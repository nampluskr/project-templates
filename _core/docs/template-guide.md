---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# template-guide.md

이 워크스페이스에서 관리하는 3개 템플릿의 구조와 용도를 설명한다.

## 1. 템플릿 선택 기준

프로젝트 상황에 맞는 템플릿 선택 기준은 다음과 같다.

| 상황 | 권장 템플릿 |
|---|---|
| 기술 가이드, 매뉴얼, 설정 문서 작성 | `project-docs-template` |
| 장기 지식 노트와 최종 문서를 함께 관리 | `project-wiki-template` |
| Python 코드, 노트북, 실험, 문서를 함께 관리 | `project-coding-template` |

## 2. `project-docs-template`

### 2.1. 용도

문서 작성 중심의 가장 단순한 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- 사용 가이드, 기술 매뉴얼
- 설정 문서, 프로세스 문서
- 경량 Jupyter Book 프로젝트

### 2.2. 루트 구조

```text
project-docs-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _core/
├── inbox/
├── sources/
├── docs/
└── outputs/
```

### 2.3. 폴더 역할

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 미분류 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 내보내기, 빌드 결과 |

## 3. `project-wiki-template`

### 3.1. 용도

지식 베이스와 최종 문서를 함께 관리하는 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- 장기 학습 노트, 책 집필
- 연구 문서, 논문 기반 작업
- Obsidian 호환 위키 시스템

### 3.2. 루트 구조

```text
project-wiki-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _core/
├── inbox/
├── sources/
├── wiki/
├── docs/
└── outputs/
```

### 3.3. 폴더 역할

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 미분류 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `wiki/` | 작업 중 지식 베이스, 개념 노트, 참조 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 내보내기, 빌드 결과 |

### 3.4. 정보 흐름

자료는 다음 흐름으로 처리한다.

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

## 4. `project-coding-template`

### 4.1. 용도

코드 중심 프로젝트에 구조화된 문서를 함께 관리하는 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- PyTorch 딥러닝 프로젝트
- NumPy 수치 해석 프로젝트
- MATLAB → Python 알고리즘 검증
- 실험 관리, 노트북 기반 분석
- 테스트 가능한 Python 패키지

### 4.2. 루트 구조

```text
project-coding-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── _core/
├── data/
├── src/
├── scripts/
├── notebooks/
├── tests/
├── configs/
├── experiments/
├── docs/
└── outputs/
```

### 4.3. 폴더 역할

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `data/` | 데이터 경로 또는 설명 |
| `src/` | 소스 코드 루트 |
| `scripts/` | 실행 가능한 스크립트 |
| `notebooks/` | Jupyter 노트북 |
| `tests/` | 테스트 코드 |
| `configs/` | 설정 파일 |
| `experiments/` | 실험 기록 및 실행 메타데이터 |
| `docs/` | 프로젝트 문서 |
| `outputs/` | 모델, 그래프, 예측, 내보내기 결과 |

## 5. 템플릿 비교

각 템플릿의 주요 폴더 포함 여부는 다음과 같다.

| 폴더 | Docs | Wiki | Coding |
|---|---|---|---|
| `docs/` | 필수 | 필수 | 필수 |
| `wiki/` | 없음 | 필수 | 없음 |
| `src/` | 없음 | 없음 | 필수 |
| `notebooks/` | 없음 | 없음 | 필수 |
| `tests/` | 없음 | 없음 | 필수 |
| `data/` | 없음 | 없음 | 필수 |
| `outputs/` | 권장 | 권장 | 필수 |
