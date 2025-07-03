# 監査ログシステム（図書館貸出）

**概要**: 図書館の本貸出システムにおける監査記録の実践。利用者の貸出申請から承認・記録まで、完全な監査証跡をaudit_logとタイムスタンプで管理する。

---

## 完全初期化（クリーンスタート）

variables.jsonが存在すれば削除してください
TODOリストをすべてクリアしてください

「=== 図書館監査システム開始 ===」と表示してください。

## フェーズ1: 基本情報記録と監査開始

### 監査ログ構造の初期化
以下の構造をvariables.jsonに作成してください：

```json
{
  "student_name": "",
  "book_title": "",
  "borrow_type": "",
  "audit_log": []
}
```

### 貸出申請情報の記録
「田中太郎さんがプログラミング入門を借りたい」という申請から：
- 学生名を{{student_name}}に保存してください
- 本のタイトルを{{book_title}}に保存してください

### 監査開始エントリの追加
現在時刻で以下をaudit_logに追加してください：
- timestamp: 現在時刻
- event_type: "borrow_request"
- content: "{{student_name}}による{{book_title}}の貸出申請"
- source: "student"

## フェーズ2: 貸出条件判定と監査記録

### 貸出種別の判定
{{book_title}}に応じて以下を{{borrow_type}}に保存してください：

- {{book_title}}に「プログラミング」が含まれる場合：
  → 「特別貸出（1週間・要承認）」

- {{book_title}}に「入門」が含まれる場合：
  → 「通常貸出（2週間）」

- その他の場合：
  → 「延長貸出（4週間・要返却確認）」

### 判定結果の監査記録
{{borrow_type}}の判定をaudit_logに追加してください：
- timestamp: 現在時刻
- event_type: "type_determination"
- content: "貸出種別決定: {{borrow_type}}"
- source: "system"

### 承認プロセスの記録
{{borrow_type}}に「要承認」が含まれる場合：
- 「司書による承認待ち」をaudit_logに追加してください
- event_type: "approval_pending"

## フェーズ3: 最終決定と監査証跡完成

### 最終貸出記録の作成
{{student_name}}、{{book_title}}、{{borrow_type}}を組み合わせて、完全な貸出記録を{{final_record}}に作成してください

### 完了エントリの追加
以下をaudit_logに追加してください：
- timestamp: 現在時刻
- event_type: "borrow_completed"
- content: {{final_record}}
- source: "librarian"

### 監査証跡の表示
「=== 完全な監査証跡 ===」として以下を表示してください：
1. {{final_record}}の内容
2. audit_logの全エントリ

### 監査の意義説明
以下を表示してください：
「この監査記録により、本の紛失時の責任追跡、貸出期間の管理、利用統計の正確性が確保されます。各エントリのタイムスタンプにより、時系列での検証が可能です。」