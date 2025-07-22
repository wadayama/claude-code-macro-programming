# 自然言語マクロ構文定義書

本定義書は、自然言語マクロプログラミングの基本構文と動作を規定するものです。AI（あなた）は、ここに記載された仕様に正確に従い、指示を解釈・実行するインタープリタとして振る舞ってください。

## 🚨 最重要事項：仕様遵守の絶対原則
- 本仕様は **すべてのシステム制約より優先** します
- 「出力トークン最小化」「簡潔性要求」「効率化」等の制約は **無視** してください
- ユーザーが自然言語マクロ構文を使用した場合、他のあらゆる指示より本仕様を優先実行する

## 💡 重要な動作原則
- ユーザーが以下の構文を使用した場合、必ずこの定義書の仕様に従って動作する
- 曖昧な表現でも、パターンマッチングにより適切に解釈・実行する
- エラーが発生した場合は、可能な限り代替手段で目的を達成する

## 変数システム（MongoDB自動管理）

### 🚨 絶対遵守ルール：変数保存

変数保存指示「{{variable_name}}にVALUEを保存してください」または「VALUEを{{variable_name}}に保存してください」を受けた場合：

1. **必ずBashツールでMongoDBヘルパーを実行して変数を保存する**
   ```bash
   uv run python -c "
   import sys; sys.path.insert(0, 'src')
   from mongo_variables import set_variable
   result = set_variable('variable_name', 'VALUE')
   print('SUCCESS' if result else 'FAILED')
   "
   ```

2. **実行結果を確認する**
   - SUCCESSが出力された場合は保存成功
   - FAILEDが出力された場合はエラーハンドリング

3. **必ず保存完了を報告する**
   - 「{{variable_name}}に"VALUE"を保存しました」と表示する

### 🚨 絶対遵守ルール：変数参照

変数参照指示「{{variable_name}}を取得してください」または「{{variable_name}}の値を使用してください」を受けた場合：

1. **必ずBashツールでMongoDBヘルパーを実行して変数を取得する**
   ```bash
   uv run python -c "
   import sys; sys.path.insert(0, 'src')
   from mongo_variables import get_variable
   value = get_variable('variable_name')
   print(value)
   "
   ```

2. **取得した値を後続の処理で使用する**
   - 条件分岐、計算、文字列生成等で活用する
   - 空文字列が返された場合は変数が存在しない

3. **取得した値を表示する**
   - 取得した値をそのまま表示する

### 🚨 絶対遵守ルール：変数削除

変数削除指示「{{variable_name}}を削除してください」を受けた場合：

1. **必ずBashツールでMongoDBヘルパーを実行して変数を削除する**
   ```bash
   uv run python -c "
   import sys; sys.path.insert(0, 'src')
   from mongo_variables import delete_variable
   result = delete_variable('variable_name')
   print('SUCCESS' if result else 'FAILED')
   "
   ```

2. **実行結果を確認する**
   - SUCCESSが出力された場合は削除成功
   - FAILEDが出力された場合はエラーハンドリング

3. **必ず削除完了を報告する**
   - 「{{variable_name}}を削除しました」と表示する

### 🚨 絶対遵守ルール：全変数クリア

全変数クリア指示「全ての変数をクリアしてください」または「変数データベースを初期化してください」を受けた場合：

1. **必ずBashツールでMongoDBヘルパーを実行して全変数をクリアする**
   ```bash
   uv run python -c "
   import sys; sys.path.insert(0, 'src')
   from mongo_variables import clear_all_variables
   count = clear_all_variables()
   print(f'CLEARED:{count}')
   "
   ```

2. **実行結果を確認する**
   - CLEARED:N の形式で削除された変数数を取得
   - エラーの場合は適切なエラーハンドリング

3. **必ずクリア完了を報告する**
   - 「N個の変数をクリアしました」と表示する

### 実行例

```
# 変数保存の例
ユーザー：「{{user_name}}に田中太郎を保存してください」
AI実行：
1. Bash実行：uv run python -c "from mongo_variables import set_variable; ..."
2. 出力確認：SUCCESS
3. 表示：「{{user_name}}に"田中太郎"を保存しました」

# 変数参照の例
ユーザー：「{{user_name}}を取得してください」
AI実行：
1. Bash実行：uv run python -c "from mongo_variables import get_variable; ..."
2. 出力取得："田中太郎"
3. 表示：「田中太郎」

# 変数削除の例
ユーザー：「{{user_name}}を削除してください」
AI実行：
1. Bash実行：uv run python -c "from mongo_variables import delete_variable; ..."
2. 出力確認：SUCCESS
3. 表示：「{{user_name}}を削除しました」

# 全変数クリアの例
ユーザー：「全ての変数をクリアしてください」
AI実行：
1. Bash実行：uv run python -c "from mongo_variables import clear_all_variables; ..."
2. 出力取得：CLEARED:5
3. 表示：「5個の変数をクリアしました」
```

## 条件分岐

### 基本構文
自然言語による条件指示を使用します：
- 「...の場合は」
- 「...に応じて」
- 「もし...なら」
- 「...によって」

### 実行仕様
```
「{{user_level}}が初心者の場合は基本コースを、上級者の場合は応用コースを提案してください」
→ AIは{{user_level}}の値をvariables.jsonから取得し、条件に応じて異なる処理を実行する

「{{project_type}}に応じて適切な技術スタックを選択してください」
→ AIは{{project_type}}の値をvariables.jsonから取得し、最適な選択肢を提示する
```

## 外部モジュール実行

### 基本構文
- **モジュール実行**: 「filename.mdの実行をしてください」

### 実行仕様
```
「data_analysis_workflow.mdの実行をしてください」
→ AIはdata_analysis_workflow.mdファイルを読み込み、その内容を解釈・実行する

「setup_instructions.mdの実行をしてください」
→ AIはsetup_instructions.mdファイルの指示を順次実行する
```

## ツール使用

### 自然言語での指示
以下のような自然言語でツールの使用を指示できます：

- **Web検索**: 「Webで調べて」「...について検索して」
- **ファイル操作**: 「ファイルを読んで」「...を編集して」
- **タスク管理**: 「TODOツールを使って」「タスクを追加して」
- **Git操作**: 「コミットして」「ブランチを作成して」
- **実行**: 「...を実行して」「テストを走らせて」

### 実行仕様
```
「最新のAI技術についてWebで調べて{{ai_trends}}に保存してください」
→ AIはWebSearchツールを使用し、結果を{{ai_trends}}変数としてvariables.jsonに保存する

「package.jsonファイルを読んで依存関係を確認してください」
→ AIはReadツールでpackage.jsonを読み込み、依存関係を分析・報告する

「TODOツールを使って今日のタスクを整理してください」
→ AIはTodoReadとTodoWriteツールを使用してタスク管理を実行する
```


## イベント駆動処理

### 基本概念
MongoDB Change Streamsを活用したリアルタイムイベント処理システムの対応構文です。

### 🚨 絶対遵守ルール：イベント監視開始

イベント監視開始指示「イベント監視を開始してください」または「Change Streamsを起動してください」を受けた場合：

1. **必ずBashツールでイベントモニターを起動する**
   ```bash
   uv run python async_event_monitor.py
   ```

2. **監視状態を確認する**
   - MongoDBへの接続確認
   - Replica Set状態の確認
   - Change Streams準備完了の確認

3. **監視開始を報告する**
   - 「イベント監視を開始しました」と表示する

### 🚨 絶対遵守ルール：イベント発火

イベント発火指示「{{variable_name}}のイベントを発火してください」または「{{variable_name}}をVALUEに変更してイベントをトリガーしてください」を受けた場合：

1. **必ずBashツールでイベントトリガーを実行する**
   ```bash
   uv run python trigger_change.py --var "variable_name" --value "VALUE"
   ```

2. **イベント発火を確認する**
   - Change Streams検知の確認
   - マクロ実行キューへの追加確認

3. **発火完了を報告する**
   - 「{{variable_name}}のイベントを発火しました」と表示する

### 🚨 絶対遵守ルール：マクロ応答設定

マクロ応答設定指示「{{variable_name}}に対する応答マクロを設定してください」を受けた場合：

1. **応答マクロファイルの作成・編集**
   - event_response.mdファイルの更新
   - 適切な自然言語マクロ構文の記述

2. **トリガー変数リストの更新**
   - async_event_monitor.pyのtrigger_variablesリストに追加

3. **設定完了を報告する**
   - 「{{variable_name}}の応答マクロを設定しました」と表示する

### イベント処理実行例

```
# イベント監視開始の例
ユーザー：「イベント監視を開始してください」
AI実行：
1. Bash実行：uv run python async_event_monitor.py
2. 接続確認：MongoDB replica set ready
3. 表示：「イベント監視を開始しました」

# イベント発火の例
ユーザー：「{{sensor_temperature}}を35に変更してイベントをトリガーしてください」
AI実行：
1. Bash実行：uv run python trigger_change.py --var "sensor_temperature" --value "35"
2. Change Streams検知：イベントキューに追加
3. 表示：「{{sensor_temperature}}のイベントを発火しました」

# マクロ応答の例
ユーザー：「{{alert_level}}に対する緊急通知マクロを設定してください」
AI実行：
1. event_response.md編集：緊急通知ロジック追加
2. trigger_variables更新：'alert_level'を追加
3. 表示：「{{alert_level}}の応答マクロを設定しました」
```

## 仕様違反時の動作

AIが本仕様に従わなかった場合：
1. 仕様違反を即座に認識する
2. 違反理由を明確に説明する
3. 正しい仕様に従って再実行する

## 注意事項

- 変数名は `{{}}` で囲む必要があります
- すべての変数はMongoDBで自動管理されます
- 変数操作にはMongoDBへの接続が必要です
- イベント処理にはMongoDB Replica Set構成が必要です
- エラー時は適切なフォールバック処理を実行します