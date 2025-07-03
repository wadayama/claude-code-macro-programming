# 監査ログシステム（基本）

**概要**: variables.json拡張による監査ログ記録の実践システム。業務操作のリスクレベル判定から監査要件決定、完全な証跡記録までを自動化し、透明性と責任追跡性を確保する。

---

## 完全初期化（クリーンスタート）

variables.jsonが存在すれば削除してください
TODOリストをすべてクリアしてください

「=== 監査ログシステム開始 ===」と表示してください。

## フェーズ1: 基本監査環境の構築

### 監査ログ構造の初期化
以下のaudit_log構造をvariables.jsonに作成してください：

```json
{
  "current_data": {},
  "audit_log": []
}
```

### 業務操作の記録
「顧客データベースを更新、リスクレベル中」という操作情報から：
- 実行操作を{{action}}に保存してください
- リスクレベルを{{risk_level}}に保存してください

### 監査エントリの追加
現在時刻で以下の監査エントリをaudit_logに追加してください：
- event_type: "operation_start"
- content: {{action}}の内容
- source: "system"
- risk_level: {{risk_level}}

## フェーズ2: リスク評価による監査要件決定

### 監査要件ロジック
{{risk_level}}の値に応じて以下を{{audit_requirements}}に保存してください：

- {{risk_level}}が「高」の場合：
  → 「詳細監査+承認者記録+システム管理者通知+実行前承認」

- {{risk_level}}が「中」の場合：
  → 「標準監査+タイムスタンプ+操作者記録+事後報告」

- {{risk_level}}が「低」の場合：
  → 「基本ログ+実行記録のみ」

### 承認プロセスの記録
{{risk_level}}が「高」または「中」を含む場合：
- 「承認待ち: {{audit_requirements}}」をaudit_logに追加してください

## フェーズ3: 監査証跡の完成

### 最終監査レポート作成
{{action}}、{{risk_level}}、{{audit_requirements}}を組み合わせて、完全な監査証跡レポートを{{audit_report}}に作成してください

### 監査ログエントリの完了記録
以下の完了エントリをaudit_logに追加してください：
- event_type: "audit_complete"
- content: {{audit_report}}の要約
- source: "audit_system"

### 結果表示
「=== 監査証跡レポート ===」として、{{audit_report}}を表示してください

最終的なaudit_logの全内容を表示してください