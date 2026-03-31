# Legal-RAG-Bench 데이터셋 분석 보고서

**데이터셋**: `isaacus/legal-rag-bench` (HuggingFace)
**분석 일자**: 2026-03-26

---

## 개요

| 항목 | 값 |
|------|-----|
| Corpus 패시지 수 | 4,876 |
| QA 질문 수 | 100 |
| 커버 범위 | 빅토리아주 형사법 (호주) |

---

## 1. Corpus 계층 구조 분석

패시지 ID 형식: `{chapter}-c{chapter_num}-s{section_num}`
예: `7.3.1.2-c4-s10` → depth 4 (점 구분자 개수 기준)

### Depth 분포

| Depth | 레이블 | 패시지 수 | 고유 섹션 수 |
|-------|--------|----------|------------|
| 0 | (비정규 ID) | 100 | 100 |
| 1 | chapter | 11 | 1 |
| 2 | subchapter | 1,305 | 87 |
| 3 | sub-subchapter | 1,688 | 259 |
| 4 | depth-4 | 1,758 | 355 |
| 5 | depth-5 | 14 | 7 |

- 대부분의 패시지(약 72%)는 depth 3–4에 집중 → 상당히 세분화된 계층 구조
- Depth 0의 100개 패시지는 비정규 ID (QA 연결 패시지로 추정)

### 최상위 챕터별 패시지 수

| 챕터 | 패시지 수 | 비율 |
|------|---------|------|
| Chapter 7 | 2,828 | 58.0% |
| Chapter 4 | 582 | 11.9% |
| Chapter 8 | 496 | 10.2% |
| Chapter 5 | 246 | 5.0% |
| Chapter 3 | 178 | 3.6% |
| Chapter 9 | 157 | 3.2% |
| 기타 (1,2,6,10,11,B6-B9) | 389 | 8.0% |

**Chapter 7** (형사법 실체 조항)이 전체의 58%를 차지하며 압도적으로 크다.

---

## 2. 패시지 길이 및 섹션 분포 분석

### 단어 수 통계

| 통계량 | 값 |
|--------|-----|
| count | 4,876 |
| min | 2 |
| p25 | 110 |
| median | 209 |
| p75 | 310 |
| p90 | 360 |
| max | 452 |
| mean | 209.1 |
| std | 114.0 |

### 단어 수 히스토그램

```
   2-  46 | ███████████████                 349
  47-  91 | ██████████████████████████      578
  92- 136 | ██████████████████████████████  665  ← 최고점
 137- 181 | █████████████████████████       559
 182- 226 | ██████████████████████          493
 227- 271 | ██████████████████████          488
 272- 316 | ████████████████████████████    623
 317- 361 | █████████████████████████████   653  ← 이중 피크
 362- 406 | █████████████████               384
 407- 451 | ███                              83
 452- 496 |                                   1
```

- **이중 피크(bimodal) 구조**: 짧은 패시지(92–136 단어)와 긴 패시지(317–361 단어) 두 그룹이 존재
- 짧은 패시지: 정의/규정 단편 (법령 조항 한 항)
- 긴 패시지: 복합 법리 설명 (판례 + 해석 포함)

### 섹션당 패시지 수

| 통계량 | 값 |
|--------|-----|
| 총 섹션 수 | 809 |
| min | 1 |
| median | 4 |
| max | 48 |
| mean | 6.0 |

### 패시지가 가장 많은 섹션 Top 10

| 섹션 | 패시지 수 |
|------|---------|
| 4.12 | 48 |
| 7.7.1 | 45 |
| 4.6 | 44 |
| 7.6.1 | 43 |
| 4.21 | 36 |
| 3.9 | 35 |
| 4.11 | 35 |
| 8.9 | 35 |
| 1.7 | 34 |
| 7.3.1.2 | 34 |

---

## 3. QA 질문 유형 분석

총 100개 질문. 모두 빅토리아주 형사법 시나리오 기반.

### 질문 유형 분류 (수동 분류 기준)

| 분류 | 설명 | 예시 QA ID |
|------|------|-----------|
| **[A] Factual / definition** | 정의·용어·법령 조항 확인 | 89 ("What is a good?"), 88, 72, 81, 98 |
| **[B] Procedural** | 절차·단계 질문 | 7, 8, 39 |
| **[C] Conditional / scenario** | 가상 시나리오 적용 | 대부분 (1, 5, 19, 20, 41, …) |
| **[D] Comparative** | 비교·구분 | 88, 92 |
| **[E] Causal / reason-why** | 왜 그런지 이유 설명 | 2, 49, 62 |
| **[F] Eligibility / permission** | 허용·금지·자격 판단 | 4, 16, 17, 33 |
| **[G] Other** | 인용 찾기, 빈칸 채우기 등 | 77, 84, 91, 93, 96, 98, 100 |

> **주목할 패턴**: 대부분의 질문이 실제 인물 이름과 구체적 상황이 포함된 시나리오형([C])이다. 이는 법령 텍스트와의 직접적 어휘 겹침을 낮추는 주요 원인.

---

## 4. 질문-패시지 어휘 중복 (Jaccard) 분석

스탑워드 제거 후 질문과 관련 패시지 간 Jaccard 유사도 측정.

### Jaccard 점수 통계

| 통계량 | 값 |
|--------|-----|
| count | 100 |
| min | 0.0000 |
| p25 | 0.0333 |
| median | 0.0521 |
| p75 | 0.0779 |
| max | 0.2394 |
| mean | 0.0586 |

### 해석

- **전반적으로 매우 낮은 Jaccard** (중앙값 0.052): 질문이 패시지 어휘를 거의 그대로 쓰지 않음
- 이는 **단순 BM25/TF-IDF 기반 검색의 한계**를 시사 → semantic retrieval 필요성 높음

### Hard Cases (Jaccard ≤ 0.0333, 하위 25%) — 25개

검색이 가장 어려운 질문들:

| QA ID | Passage | Score | 비고 |
|-------|---------|-------|------|
| 36 | 4.16-c3-s1 | 0.0000 | 크리스마스 파티 시나리오 |
| 72 | 7.3.2-c5-s1 | 0.0000 | 성별 관련 법률 정의 |
| 76 | 7.4.8-c3-s5 | 0.0000 | 인용문 형식 질문 |
| 89 | 7.5.10-c2-s1 | 0.0000 | "What is a good?" (매우 단순) |
| 96 | 7.6.1-c3-s7 | 0.0097 | 마약 거래 케이스 |
| 75 | 7.4.8-c3-s2 | 0.0101 | 폭행 시나리오 |
| 12 | 3.12-c1-s1 | 0.0112 | 이중위험금지 법 존재 여부 |

#### Hard Case 예시 — QA #36 (Jaccard = 0.0000)

**질문 (Q):**
> Kim and Frank are at a Christmas party and are watching a news story about a recent drive-by shooting. Kim thinks the car looks like Frank's and asks, "That's not your car, is it?" Frank stays silent. A few minutes later, the police shut down the party due to noise complaints. Later, Frank is on trial for offences related to the same drive-by shooting. **Why is it important to the defence that the party was loud?**

**관련 패시지 (4.16-c3-s1):**
> **Admissibility**
>
> A statement made in the accused's presence will only be admissible if, in all the circumstances, it is open to the jury to conclude that:
> - The accused heard the statement and had the opportunity to respond;
> - The occasion was one in which the accused might **reasonably have been expected to respond**; and
> - By his or her silence the accused has substantially admitted the truth of the statement in whole or in part, or has shown a consciousness of guilt.
>
> *(R v Salahattin [1983] VR 521; R v MMJ (2006) 166 A Crim R 501)*

**왜 어려운가?**
- 질문의 핵심 단어: *Christmas party*, *loud*, *noise complaints*, *Frank*, *Kim*, *car*
- 패시지의 핵심 단어: *admissibility*, *accused*, *reasonably expected to respond*, *silence*, *consciousness of guilt*
- 공유 어휘가 **전무** → 질문이 "시끄러운 장소에서 침묵이 합리적 응답 기대를 충족하지 못함"이라는 법리를 우회적으로 묻고 있음
- BM25로는 완전히 미스. **법적 개념 이해(semantic)** 또는 **그래프 추론** 없이 검색 불가

### Easy Cases (Jaccard ≥ 0.0779, 상위 25%) — Top 10

| QA ID | Passage | Score |
|-------|---------|-------|
| 57 | 7.2.2-c4-s1 | **0.2394** |
| 68 | 7.3.2-c3-s1 | 0.1573 |
| 56 | 7.2.2-c2-s1 | 0.1250 |
| 22 | 4.9-c2-s1 | 0.1250 |
| 71 | 7.3.2-c4-s2 | 0.1233 |
| 70 | 7.3.2-c4-s2 | 0.1233 |
| 44 | 6.2-c9-s1 | 0.1231 |
| 82 | 7.4.12-c2-s5 | 0.1150 |
| 69 | 7.3.2-c4-s1 | 0.1071 |
| 42 | 5.2-c8-s1 | 0.1047 |

---

## 5. GraphRAG 설계 관련 시사점

| 관찰 | 시사점 |
|------|--------|
| Chapter 7이 58% 차지, 최대 depth 5 | 계층 구조를 그래프 엣지로 표현할 때 Chapter 7 노드의 팬아웃 관리 필요 |
| 이중 피크 길이 분포 | 패시지 청킹 전략 재검토 — 짧은 패시지와 긴 패시지에 다른 처리 가능 |
| 중앙값 Jaccard 0.052 (매우 낮음) | Sparse retrieval(BM25) 단독 사용 부적합, Dense/Graph 기반 retrieval 필수 |
| Hard cases 25개 (score ≈ 0) | 이 케이스들은 법령 용어가 아닌 개념 추론 필요 → GraphRAG의 관계 탐색이 핵심 |
| 섹션당 평균 6개 패시지, 최대 48개 | 섹션 레벨 집계 노드(summary node) 활용 시 검색 커버리지 향상 기대 |
