---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# template-guide.md

이 워크스페이스에서 관리하는 3개 템플릿의 구조와 용도를 설명한다.

## 1. 상속 구조

3개 템플릿은 `shared/` 에 정의된 공통 기반을 공유한다.

```text
shared/  (공통 기반)
    |
    +--[wiki/ 추가]-----------> project-wiki-template
    |
    +--[코딩 도구 추가]---------> project-coding-template
    |
    +-(추가 없음)--------------> project-docs-template
```

`project-docs-template` 은 공통 기반 그 자체이다.

## 2. 공통 기반 (shared/)

3개 템플릿 모두에 포함되는 공통 파일은 다음과 같다.

```text
README.md
.gitignore
_core/
inbox/
sources/
docs/
outputs/
```

`AGENTS.md` 와 `CLAUDE.md` 는 공유하지 않는다. 각 템플릿이 독립적으로 관리한다.

## 3. 템플릿 선택 기준

| 상황 | 권장 템플릿 |
|---|---|
| 기술 가이드, 매뉴얼, 설정 문서 작성 | `project-docs-template` |
| 경량 Jupyter Book 프로젝트 | `project-docs-template` |
| 장기 학습 노트와 최종 문서를 함께 관리 | `project-wiki-template` |
| 연구 문서, 논문 기반 작업 | `project-wiki-template` |
| Obsidian 호환 위키 + 최종 문서 | `project-wiki-template` |
| Python 스크립트, 노트북, 테스트 | `project-coding-template` |
| PyTorch 딥러닝 프로젝트 | `project-coding-template` |
| NumPy 수치 해석 프로젝트 | `project-coding-template` |
| 실험 관리, 노트북 기반 분석 | `project-coding-template` |

## 4. `project-docs-template`

### 4.1. 용도

문서 작성 중심의 가장 단순한 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- 사용 가이드, 기술 매뉴얼
- 설정 문서, 프로세스 문서
- 경량 Jupyter Book 프로젝트

### 4.2. 루트 구조

```text
project-docs-template/
├── README.md               # shared
├── AGENTS.md               # docs-specific
├── CLAUDE.md               # docs-specific
├── .gitignore              # shared
├── _core/                  # shared
├── inbox/                  # shared
├── sources/                # shared
├── docs/                   # shared
└── outputs/                # shared
```

### 4.3. 폴더 역할

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 미분류 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 내보내기, 빌드 결과 |

### 4.4. 정보 흐름

```text
inbox/ → sources/ → docs/ → outputs/
```

### 4.5. 예시 프로젝트

```text
wsl-cuda-setup-guide
vscode-codex-usage-guide
jupyter-book-build-guide
github-submodule-guide
```

## 5. `project-wiki-template`

### 5.1. 용도

지식 베이스와 최종 문서를 함께 관리하는 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- 장기 학습 노트, 책 집필
- 연구 문서, 논문 기반 작업
- Obsidian 호환 위키 시스템

### 5.2. 루트 구조

```text
project-wiki-template/
├── README.md               # shared
├── AGENTS.md               # wiki-specific
├── CLAUDE.md               # wiki-specific
├── .gitignore              # shared
├── _core/                  # shared
├── inbox/                  # shared
├── sources/                # shared
├── wiki/                   # wiki-specific
├── docs/                   # shared
└── outputs/                # shared
```

### 5.3. 폴더 역할

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 미분류 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `wiki/` | 작업 중 지식 베이스, 개념 노트, 참조 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 내보내기, 빌드 결과 |

### 5.4. 정보 흐름

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

### 5.5. 예시 프로젝트

```text
display-anomaly-detection-wiki
deep-learning-from-scratch-book
oled-color-science-notes
papers-to-book-workspace
```

## 6. `project-coding-template`

### 6.1. 용도

코드 중심 프로젝트에 구조화된 문서를 함께 관리하는 템플릿이다.

적합한 프로젝트 유형은 다음과 같다.

- PyTorch 딥러닝 프로젝트
- NumPy 수치 해석 프로젝트
- MATLAB → Python 알고리즘 검증
- 실험 관리, 노트북 기반 분석
- 테스트 가능한 Python 패키지

### 6.2. 루트 구조

```text
project-coding-template/
├── README.md               # shared
├── AGENTS.md               # coding-specific
├── CLAUDE.md               # coding-specific
├── .gitignore              # shared
├── pyproject.toml          # coding-specific
├── requirements.txt        # coding-specific
├── _core/                  # shared
├── data/                   # coding-specific
├── src/                    # coding-specific
├── scripts/                # coding-specific
├── notebooks/              # coding-specific
├── tests/                  # coding-specific
├── configs/                # coding-specific
├── experiments/            # coding-specific
├── docs/                   # shared
└── outputs/                # shared
```

### 6.3. 폴더 역할

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `data/` | 데이터 경로 또는 설명 |
| `src/` | 소스 코드 루트 (내부 구조는 프로젝트별 결정) |
| `scripts/` | 실행 가능한 스크립트 |
| `notebooks/` | Jupyter 노트북 |
| `tests/` | 테스트 코드 |
| `configs/` | 설정 파일 |
| `experiments/` | 실험 기록 및 실행 메타데이터 |
| `docs/` | 프로젝트 문서 |
| `outputs/` | 모델, 그래프, 예측, 내보내기 결과 |

### 6.4. 예시 프로젝트

```text
mnist-from-scratch-mlp
oled-anomaly-detection
gan-training-framework
numpy-numerical-analysis
pytorch-classification-template
```

## 7. 템플릿 비교

| 항목 | Docs | Wiki | Coding |
|---|:---:|:---:|:---:|
| `README.md` `.gitignore` `_core/` | O | O | O |
| `inbox/` `sources/` `docs/` `outputs/` | O | O | O |
| `wiki/` | - | O | - |
| `pyproject.toml` `requirements.txt` | - | - | O |
| `data/` `src/` `scripts/` | - | - | O |
| `notebooks/` `tests/` `configs/` `experiments/` | - | - | O |
