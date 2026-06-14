---
tags: [project, rules]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# wiki-rules.md

`wiki/` 지식 저장소의 운영 규칙을 정의한다.
에이전트는 `wiki/` 작업 시 이 규칙을 따른다.

본 정책은 Andrej Karpathy 의 LLM Wiki 패턴을 참고하되,
전역 개인 지식베이스가 아니라 Repository 단위 책 프로젝트에 맞게 재해석한 것이다.

## 1. 목적

LLM Wiki 운영 목적은 다음과 같다.

- AI CLI 가 원본 자료를 반복적으로 읽고 다시 답변하는 방식에서 벗어나, 지식을 Markdown Wiki 로 누적한다.
- 책 프로젝트의 모든 핵심 개념, 방법, 예시, 용어, 출처 해석을 `wiki/` 에 축적한다.
- Obsidian 에서 그래프, 백링크, 태그, 검색을 통해 `wiki/` 를 탐색할 수 있게 한다.
- `docs/` 의 최종 문서는 `wiki/` 를 기반으로 작성한다.

## 2. 핵심 원칙

### 2.1. Repository 단위 Wiki

하나의 Repository 는 하나의 독립적인 `wiki/` 를 가진다.
여러 Repository 가 하나의 중앙 Wiki 를 공유하지 않는다.

### 2.2. Wiki 는 책 프로젝트의 SSOT

- 새로운 개념은 먼저 `wiki/` 에 정리한다.
- `docs/` 는 `wiki/` 를 기반으로 작성한다.
- `docs/` 에서 중요한 개념이 새로 정리되면 `wiki/` 에 역반영한다.
- `wiki/` 와 `docs/` 가 충돌할 경우 `wiki/` 를 먼저 검토한다.

### 2.3. Wiki 는 Obsidian 호환 지식 그래프

`wiki/` 는 Obsidian 에서 열람·탐색·수정할 수 있어야 한다.
이를 위해 다음을 유지한다.

- YAML frontmatter
- Obsidian 내부 링크 `[[...]]`
- `## Related` 섹션
- `tags`, `aliases`
- `wiki/index.md` 및 하위 폴더별 `index.md`

## 3. 정보 흐름

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

| 단계 | 폴더 | 역할 |
|---|---|---|
| Capture | `inbox/` | 정리 전 임시 자료 수집 |
| Source Management | `sources/` | 출처가 확인된 원본 자료 정리 |
| Knowledge Distillation | `wiki/` | 책 주제에 맞게 지식 정제 |
| Publication | `docs/` | 최종 출판 문서 작성 |

## 4. wiki/ 권장 구조

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

## 5. 문서 유형

`wiki/` 문서는 다음 유형 중 하나로 분류한다.

| type | 의미 | 위치 예시 |
|---|---|---|
| `concept` | 개념, 이론, 수식, 정의 | `wiki/concepts/` |
| `method` | 알고리즘, 모델, 절차, 방법론 | `wiki/methods/` |
| `dataset` | 데이터셋 설명, 전처리, 사용 조건 | `wiki/datasets/` |
| `paper` | 논문 단위 정리 | `wiki/papers/` |
| `example` | 예제, 코드 설명, 실습 아이디어 | `wiki/examples/` |
| `glossary` | 용어 정의 | `wiki/glossary/` |
| `reference` | 참고 자료 해석 | `wiki/references/` |
| `chapter-note` | 챕터 설계 메모 | `wiki/chapters/` |

## 6. 문서 상태

`status` 는 다음 중 하나를 사용한다.

| status | 의미 |
|---|---|
| `draft` | 초안 |
| `review` | 검토 필요 |
| `stable` | 현재 기준 안정 상태 |
| `deprecated` | 더 이상 권장하지 않는 내용 |

## 7. YAML Frontmatter 표준

모든 `wiki/` 문서는 다음 YAML frontmatter 를 포함한다.

```yaml
---
title: 문서 제목
type: concept
status: draft
tags:
  - wiki
aliases: []
related: []
source: []
docs: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

필드 의미는 다음과 같다.

| 필드 | 의미 |
|---|---|
| `title` | 사람이 읽는 문서 제목 |
| `type` | 문서 유형 |
| `status` | 문서 작성 상태 |
| `tags` | Obsidian 검색 및 분류용 태그 |
| `aliases` | 한글명, 약어, 대체 표현 |
| `related` | 관련 wiki 문서의 파일명 |
| `source` | 근거가 되는 `sources/` 경로 |
| `docs` | 반영되었거나 반영 예정인 `docs/` 경로 |
| `created` | 최초 생성일 |
| `updated` | 마지막 수정일 |

## 8. Obsidian 링크 규칙

기본 링크 형식은 다음과 같다.

```markdown
[[target-file-name]]
[[target-file-name|표시명]]
```

링크 생성 기준은 다음과 같다.

- 상위·하위 개념 연결
- 같은 방법론 계열 연결
- 비교 대상 연결
- 같은 챕터에서 함께 설명될 개념 연결
- 실습 예제와 개념 연결

링크 과잉 방지 원칙은 다음과 같다.

- 단순 단어 일치만으로 링크하지 않는다.
- 의미적 관계가 명확할 때만 링크한다.
- 한 문서 안에서 동일 링크를 반복 삽입하지 않는다.
- 모든 `wiki/` 문서는 최소 1개 이상의 기존 문서와 연결한다.

## 9. Related 및 Missing Links 섹션

모든 `wiki/` 문서는 가능한 경우 `## Related` 섹션을 가진다.

```markdown
## Related

- [[gradient-descent]]
- [[chain-rule]]
```

필요한 개념이 있지만 아직 문서가 없는 경우 `## Missing Links` 섹션에 기록한다.

```markdown
## Missing Links

- `computational-graph`: Backpropagation 설명에 필요하나 아직 문서가 없음
```

## 10. Tags 및 Aliases 규칙

Tags 원칙은 다음과 같다.

- 태그는 소문자와 하이픈을 사용한다.
- 태그 수는 문서당 3~7개를 권장한다.
- 문서 유형은 태그가 아니라 `type` 필드에 기록한다.
- 모든 wiki 문서에는 `wiki` 태그를 부여할 수 있다.

Aliases 원칙은 다음과 같다.

- 파일명은 영어 소문자와 하이픈을 사용한다.
- 한글명, 약어, 대체 표현은 `aliases` 에 기록한다.

## 11. Index 문서 관리

에이전트는 `wiki/` 문서를 생성·삭제·이동·이름 변경할 때 관련 index 문서를 갱신한다.

관리 대상은 다음과 같다.

- `wiki/index.md`
- 각 하위 폴더의 `index.md`
- `wiki/chapters/book-outline.md`

Index 문서는 Obsidian 탐색 시작점이자 AI CLI 의 다음 작업 기준이다.

## 12. 문서 템플릿

새로운 `wiki/` 문서는 다음 템플릿을 따른다.

```markdown
---
title: 문서 제목
type: concept
status: draft
tags:
  - wiki
aliases: []
related: []
source: []
docs: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# 문서 제목

## Summary

핵심 요약을 작성한다.

## Definition

정의 또는 기본 설명을 작성한다.

## Details

세부 설명을 작성한다.

## Formula

필요한 경우 수식을 작성한다.

## Example

예제를 작성한다.

## Related

- [[관련-문서]]

## Sources

- `sources/...`

## Docs Usage

- `docs/contents/chapXX/index.md`

## Missing Links

- `개념명`: 필요한 이유
```

## 13. Docs 반영 원칙

- `docs/` 는 독자 중심 설명 흐름을 따른다.
- `wiki/` 의 여러 문서를 하나의 챕터로 통합할 수 있다.
- `wiki/` 의 Obsidian 링크 `[[...]]` 는 `docs/` 에 그대로 복사하지 않는다.
- `docs/` 에서는 MyST/Jupyter Book 호환 Markdown 링크를 우선 사용한다.
- `docs/` 에서 새롭게 정리된 중요한 개념은 `wiki/` 에 역반영한다.

## 14. AI CLI 작업 순서

AI CLI 는 `wiki/` 작업 시 다음 순서를 따른다.

1. 관련 `sources/` 확인
2. 관련 `wiki/` 문서 검색
3. 새 문서 생성 또는 기존 문서 갱신
4. YAML frontmatter 작성 또는 갱신
5. `## Related` 섹션 및 Obsidian 내부 링크 추가
6. `tags`, `aliases` 보완
7. index 문서 갱신
8. `docs/` 반영 필요 여부 기록

## 15. 파일명 규칙

- 영어 소문자와 하이픈을 사용한다.
- 한글 표현은 `aliases` 에 기록한다.
- 동일 개념의 중복 파일을 생성하지 않는다.

## 16. 품질 기준

좋은 Wiki 문서는 다음 조건을 만족한다.

- 하나의 문서가 하나의 핵심 주제를 다룬다.
- 제목, 파일명, aliases 가 일관된다.
- 최소 1개 이상의 관련 문서와 연결된다.
- 출처가 명확하다.
- docs 반영 여부가 기록된다.
- Obsidian 그래프에서 고립되지 않는다.
