# Future-Self Chat App — Product Spec

一句話：把「日記 + 反思 + 情境推演」做成對話式體驗，讓使用者能跟 **未來的自己** 對談，同時召喚一群「歷史名人顧問」用不同世界觀幫你拆解盲點、給行動建議。

> 注意：這些顧問人格是**創作式模擬**，不是本人，也不是專業醫療／法律／投資建議。

## 目錄

1. [產品定位](#產品定位)
2. [核心概念](#核心概念)
3. [主要使用情境](#主要使用情境)
4. [功能需求](#功能需求)
5. [非目標](#非目標)
6. [角色與體驗設計](#角色與體驗設計)
7. [資料模型](#資料模型)
8. [AI 編排與 Prompt 規格](#ai-編排與-prompt-規格)
9. [安全、倫理、與風險控管](#安全倫理與風險控管)
10. [架構建議](#架構建議)
11. [事件追蹤與指標](#事件追蹤與指標)
12. [驗收標準](#驗收標準)
13. [Roadmap](#roadmap)
14. [Repo 結構建議](#repo-結構建議)

## 產品定位

### 目標使用者

- 想提升決策品質、情緒調節、長期行動一致性的人。
- 會寫日記/做復盤，但很難持續、很難把洞察變成行動的人。
- 喜歡多視角思辨（不同價值觀的「反對者」）來校正偏誤的人。

### 核心價值

- 把「反思」從抽象變成對話引導（不是空泛雞湯）。
- 把「未來後悔」提前搬到現在做壓力測試。
- 用「多角色顧問團」讓你聽到不同腦迴路的建議（避免只被自己同溫層說服）。

## 核心概念

### Future Self（未來自我）

不是預言家，而是：在你提供的資料上，用「回顧口吻」做推演：

- 「如果你照現在的習慣走下去，三個月後你可能會怎樣？」
- 「你未來最可能後悔的是哪個選擇？」

### Historical Counsel（歷史名人顧問）

- 每位顧問是一組「價值觀 + 推理風格 + 問題偏好」。
- 顧問人格只是一種「思考工具」：幫你看見盲點，而非權威真理。

### Session Output（每次對話都要落地）

一次對話結束必產出：

1. 1 句「洞察結論」。
2. 1～3 個「可執行行動」。
3. 1 個「要避免的自我欺騙」。
4. 1 個「下次回來驗證的問題」。

## 主要使用情境

### 決策前壓力測試

- 例：換工作、投資、創業、關係、重大購買。
- 需求：用未來視角檢查盲點與後悔點。

### 情緒波動時的重置

- 例：焦慮、挫折、憤怒、失望。
- 需求：先穩住，再找出下一步最小行動（而不是腦內開戰）。

### 週回顧 / 月回顧

- 需求：把日常碎片整成策略（我到底在累積什麼？）。

## 功能需求

### 4.1 MVP（第一版必做）

**A. 會話模式**

- Future-Self Chat：你 ↔ 未來的你。
- Counsel Panel：你 ↔ 顧問（單一名人）。
- Triad：你 ↔ 未來的你 ↔ 顧問（輪流發言）。

**B. 時間視角**

- 選擇未來視角：3 個月 / 1 年 / 3 年 / 10 年。
- 不同時間視角會影響：語氣（短期務實 vs 長期價值）、建議粒度（行動 vs 原則）。

**C. Session 結果卡**

- 自動生成「結論/行動/盲點/驗證問題」。
- 一鍵保存到「洞察庫」。

**D. 使用者脈絡（最低限度）**

Onboarding 問卷（5 分鐘內完成）：

- 目前最關注的領域：健康/關係/事業/財務/心態。
- 近期最大困擾與目標。
- 禁忌與敏感話題（可選）。
- 允許使用者在聊天中「補充背景」並可被引用（可開關）。

### 4.2 V1（提升留存與黏性）

- Letter to Future Self：寫信給未來（可設定開啟日，但不必真的推播，先做內容封存）。
- Memory Timeline：把洞察卡按時間線排列（可搜尋）。
- Theme Packs：主題模板（創業焦慮、關係溝通、拖延、價值觀衝突…）。
- Mentor Switching：同一議題一鍵切換不同顧問視角（快速對照）。

### 4.3 V2（更像「個人策略系統」）

- 定期回顧儀表板（本週最常出現的困擾、最常自我欺騙句型）。
- 行動追蹤（只追蹤「承諾過的 1～3 個行動」，不做複雜 TODO）。
- 可選：匯入日記/筆記（但這是隱私與風險大頭，見安全章節）。

## 非目標

- 不做心理治療或診斷（有需要要導向專業資源）。
- 不做投資/法律的具體指令型建議（只做思考框架與風險提醒）。
- 不做重度社群（避免變成情緒宣洩場 + 管理成本爆炸）。
- 不做「假裝真的能通靈名人」的設定（信任會崩）。

## 角色與體驗設計

### 6.1 顧問人選（建議預設 6–10 位）

原則：以「思考風格差異」選人，而不是以名氣選人。

| 顧問 | 核心風格 | 擅長情境 | 禁忌/限制（系統約束） |
| --- | --- | --- | --- |
| 蘇格拉底 | 連續追問、拆定義 | 概念混亂、價值衝突 | 不給一錘定音，偏用提問逼近本質 |
| 馬可·奧理略 | 斯多葛、情緒去災難化 | 焦慮、失望、挫折 | 不許道德綁架、避免冷血語氣 |
| 孔子 | 關係倫理、角色責任 | 人際、職場溝通 | 不用「你應該」壓迫，用情境權衡 |
| 孫子 | 策略、資源配置、風險控管 | 商業決策、談判 | 不鼓勵傷害、詐騙或操控 |
| 李奧納多·達文西 | 好奇心、跨域聯想、原型思維 | 創作、創業點子 | 不飄，要落回可測試假設 |
| 瑪麗·居禮 | 科學方法、證據、實驗設計 | 做決策驗證、學習計畫 | 不做權威口吻；強制列出不確定性 |

> 盲點提醒：顧問越多越容易變「角色扮演遊戲」而不是自我成長工具；建議先 6 位做到極致，再擴。

## 資料模型

### 7.1 Core Entities

- User
- Session
- Message
- InsightCard
- MentorProfile
- UserContext（可選：使用者提供的背景摘要）

### 7.2 JSON Schema（簡化版）

```json
{
  "Session": {
    "id": "uuid",
    "userId": "uuid",
    "mode": "future_self | counsel | triad",
    "timeHorizon": "3m | 1y | 3y | 10y",
    "mentorId": "optional_uuid",
    "createdAt": "iso8601",
    "summary": "string",
    "insightCardId": "uuid"
  },
  "InsightCard": {
    "id": "uuid",
    "sessionId": "uuid",
    "insight": "string",
    "actions": ["string"],
    "selfDeceptionToAvoid": "string",
    "nextVerificationQuestion": "string",
    "tags": ["string"]
  },
  "MentorProfile": {
    "id": "uuid",
    "name": "string",
    "styleGuide": "string",
    "do": ["string"],
    "dont": ["string"]
  }
}
```

## AI 編排與 Prompt 規格

### 8.1 角色分層（建議）

- **System**：安全規則 + 行為邊界（不冒充真人、不做高風險指令）。
- **Developer**：本產品的輸出格式要求（一定要產出 InsightCard）。
- **User**：使用者訊息 + 選擇的模式/顧問/時間視角。
- **Context（可選）**：使用者背景摘要（使用者可關閉）。

### 8.2 Future Self 的行為規格

- 用「回顧口吻」而非預言口吻。
- 必須顯式標注不確定性（至少一句）。
- 回答結構固定：
  - 我看到的模式
  - 最可能的後悔點
  - 你下一步最小行動
  - InsightCard

### 8.3 Mentor 的行為規格（Style Guide 片段）

每位 mentor 需要一個 styleGuide，包含：

- 語氣（短句/長句、是否反問）。
- 偏好框架（策略、倫理、科學、創作…）。
- 禁止事項（例如不能給醫療處方、不能用羞辱語）。
- 禁止做「精準模仿原文」（避免變成仿作/引言機器），只能使用「精神與思路」。

### 8.4 輸出格式（強制）

- 模型輸出最後必須帶一段可 parse 的 JSON（InsightCard）。
- UI 顯示用自然語言，儲存用 JSON。

## 安全、倫理、與風險控管

### 9.1 必備 UI 告知

- 「歷史名人」為模擬人格，不代表本人觀點。
- 內容僅供反思與教育用途。
- 若涉及自傷/他傷/危機：提供求助資源與緊急建議（依地區）。

### 9.2 高風險內容策略

**醫療/法律/投資：**

- 可提供「提問清單」「風險框架」「尋求專業的建議」。
- 禁止：具體處方、具體投資標的指令、法律結論。

### 9.3 另一種可能性（雙向校正）

- 產品很容易變成「逃避現實的對話成癮」。
  - 對策：每次 Session 限制輸出行動數（最多 3 個），並鼓勵去做而不是再聊。
- 也可能變成「名人權威崇拜」。
  - 對策：顧問必須列出反例與不確定性；鼓勵使用者用自己價值觀做終審。

## 架構建議

### 10.1 客戶端

- iOS 優先（若要跨平台可 React Native / Flutter）。
- 主要頁面：
  - Onboarding
  - Chat（含模式切換）
  - Insight Library
  - Mentor Select

### 10.2 後端

- API：Session / Message / InsightCard CRUD。
- AI Orchestrator：
  - prompt 組裝
  - 內容安全過濾
  - response 解析（抓 JSON）
- 儲存：Postgres（結構化）+ Object Storage（可選，放長文本）。

### 10.3 Observability

- request id、latency、token usage、fail rate。
- 模型輸出 parse 失敗要可回放（匿名化）。

## 事件追蹤與指標

### 11.1 事件（Events）

- onboarding_completed
- session_started
- mode_selected
- mentor_selected
- insight_card_saved
- return_visit_d1/d7
- action_marked_done（若有行動追蹤）

### 11.2 北極星指標（NSM）

- **Weekly Saved Insight Cards per Active User**
- 理由：代表使用者真的得到可保存的洞察，而不是只聊天爽。

## 驗收標準

### 12.1 MVP 驗收

- 使用者可在 3 種模式中任選，完成一段對話。
- 每個 Session 都產出 InsightCard（含 4 欄位）。
- InsightCard 可保存並在 Library 查閱。
- 切換顧問後，語氣與框架顯著不同（至少可由測試用例辨識）。
- 高風險內容觸發時，能做安全回應（不提供違規指令）。

### 12.2 品質門檻（建議）

- InsightCard JSON parse 成功率 ≥ 99%。
- 首次完成一個 session 的時間 ≤ 2 分鐘（不含深聊）。

## Roadmap

- **MVP（2–4 週）**：三種模式 + 6 位顧問 + InsightCard + Library。
- **V1（4–8 週）**：主題模板 + 切換顧問對照 + 簡易搜尋/標籤。
- **V2（8–12 週）**：行動追蹤 + 回顧儀表板 + 可選匯入筆記（需隱私設計）。

## Repo 結構建議

```
/
  apps/
    ios/                 # iOS app
    web/                 # (optional) web client
  services/
    api/                 # REST API (sessions, messages, insights)
    ai-orchestrator/     # prompt assembly, safety, parsing
  packages/
    shared/              # types, schemas, utils
  docs/
    product/             # this spec + UX flows
    prompts/             # mentor style guides
  scripts/
    seed_mentors.ts      # seed mentor profiles
```

---

## 你可以直接拿去做的下一步（建議）

- 先做 MVP 的 6 位顧問（風格差異拉到最大），不用急著塞 30 位。
- 把「InsightCard」做成你們產品的靈魂：沒有卡＝沒有價值。
- 先把「輸出格式穩定」做到 99%（parse/落地/可回顧），再談花俏 UI。

要不要我再幫你把「6 位顧問的 styleGuide（do/don’t + 語氣規則 + 回覆模板）」完整寫成 `docs/prompts/*.md`，你們工程可以直接丟進 orchestrator 用？
