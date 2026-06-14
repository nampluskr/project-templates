---
tags: [project, docs]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# wiki-guide.md

이 프로젝트의 `wiki/` 운영 방식을 설명한다.
사용자가 참조하는 문서이다. 에이전트 행동 규칙은 `_core/rules/wiki-rules.md` 를 참조한다.

## 1. 목적

`wiki/` 는 이 프로젝트 전용 LLM Wiki 지식 저장소이다.

- AI CLI 가 원본 자료를 반복적으로 읽고 답변하는 방식 대신, 지식을 Markdown Wiki 로 누적한다.
- 책 프로젝트의 핵심 개념, 방법, 예시, 용어, 출처 해석을 `wiki/` 에 축적한다.
- Obsidian 에서 그래프, 백링크, 태그, 검색으로 탐색 가능한 지식 그래프를 유지한다.
- `docs/` 의 최종 문서는 `wiki/` 를 기반으로 작성한다.

본 정책은 Andrej Karpathy 의 LLM Wiki 패턴을 참고하되,
전역 개인 지식베이스가 아니라 Repository 단위 책 프로젝트에 맞게 재해석한 것이다.

## 2. wiki/ 와 docs/ 의 관계

`wiki/` 와 `docs/` 는 역할이 다르다.

| 구분 | `wiki/` | `docs/` |
|---|---|---|
| 목적 | 지식 축적 | 출판 |
| 단위 | 개념, 방법, 예시, 용어 | 챕터, 절, 부록 |
| 대상 | AI CLI 와 작성자 | 독자 |
| 상태 | 지속 갱신 | 출판 가능한 정리본 |
| 구조 | 지식 그래프 | 책 목차 |

정보 흐름은 다음과 같다.

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

원칙은 다음과 같다.

- 새로운 정보는 우선 `wiki/` 에 반영한다.
- 최종 문서는 `wiki/` 를 기반으로 `docs/` 에 작성한다.
- `wiki/` 와 `docs/` 내용이 충돌하면 `wiki/` 를 먼저 검토하고 정정한다.
- `docs/` 만 수정한 경우 중요한 내용을 `wiki/` 에 역반영한다.

## 3. wiki/ 권장 구조

```text
wiki/
├── index.md
├── concepts/
│   └── index.md
├── methods/
│   └── index.md
├── examples/
│   └── index.md
├── datasets/
│   └── index.md
├── glossary/
│   └── index.md
├── papers/
│   └── index.md
├── references/
│   └── index.md
└── chapters/
    ├── index.md
    └── book-outline.md
```

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `concepts/` | 핵심 개념, 이론, 수식, 정의 |
| `methods/` | 알고리즘, 모델, 절차, 방법론 |
| `examples/` | 예제, 코드 설명, 실습 아이디어 |
| `datasets/` | 데이터셋 설명, 사용 조건, 전처리 |
| `glossary/` | 용어 정의 |
| `papers/` | 논문 단위 정리 |
| `references/` | 참고 자료 해석, 출처 메모 |
| `chapters/` | 최종 챕터 구성을 위한 설계 메모 |

프로젝트 성격에 따라 폴더는 추가하거나 생략할 수 있다.
단, `wiki/` 가 이 책의 주제 범위를 벗어나지 않도록 유지한다.

## 4. wiki/ 범위 제한

`wiki/` 는 이 Repository 의 책 주제에 한정한다.

- 여러 Repository 가 하나의 중앙 Wiki 를 공유하지 않는다.
- 다른 Repository 의 지식은 직접 복사하지 않는다.
- 필요한 외부 개념은 현재 책의 설명에 필요한 범위까지만 정리한다.
- 필요한 경우 `sources/` 에 참고 자료로 정리한 뒤 현재 프로젝트의 `wiki/` 에 맞게 재해석한다.

## 5. Obsidian 사용 원칙

사용자는 Obsidian 에서 `wiki/` 문서를 확인하고 간단히 수정할 수 있다.

- Obsidian 에서는 주로 `wiki/` 탐색과 간단 수정을 수행한다.
- 대량 생성·수정·정리는 AI CLI 에 위임한다.
- 대규모 구조 변경은 VS Code 와 AI CLI 에서 수행한다.
- Git commit 과 push 는 사용자가 직접 수행한다.

## 6. 초기 폴더 생성

프로젝트 시작 시 `wiki/` 초기 구조 생성 명령은 다음과 같다.

```bash
mkdir -p wiki/{concepts,methods,examples,datasets,glossary,papers,references,chapters}
touch wiki/index.md
touch wiki/concepts/index.md wiki/methods/index.md wiki/examples/index.md
touch wiki/datasets/index.md wiki/glossary/index.md
touch wiki/papers/index.md wiki/references/index.md
touch wiki/chapters/index.md wiki/chapters/book-outline.md
```

## 7. 참조 경로

| 항목 | 경로 |
|---|---|
| wiki/ 에이전트 행동 규칙 | `_core/rules/wiki-rules.md` |
| 프로젝트 구조 가이드 | `_core/docs/project-guide.md` |
