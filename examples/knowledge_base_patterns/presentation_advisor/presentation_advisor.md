# プレゼンテーション構成アドバイザー

**Pattern 7 実践例**: 知識ベース活用による個別要件対応型プレゼン構成自動生成

## 概要

プレゼンテーション設計のプロフェッショナル知識をデータベース化し、ユーザーの個別要件（聴衆・時間・目的）に基づいて最適なプレゼン構成を自動生成するシステム。

**主な価値**: 
- 熟練プレゼンターの「暗黙知」を「形式知」として活用
- 素人でもプロレベルの構成を短時間で取得
- 個別要件への自動適応

## 使い方

1. **知識読み込み**: プレゼン設計フレームワークを読み込む
2. **要件入力**: テーマ、聴衆、時間、目的を指定
3. **構成生成**: 知識ベースから最適パターンを選択・適用
4. **出力確認**: 具体的なプレゼン構成案を取得

---

## Step 1: 知識ベース読み込み

「=== プレゼン設計知識読み込み ===」と表示してください。

presentation_framework.mdを読み込んで{{presentation_knowledge}}に設定してください。

「プレゼンテーション設計フレームワークを読み込みました」と表示してください。

{{presentation_knowledge}}から以下の主要要素を確認してください：
- 聴衆別アプローチの種類
- 構成パターンの種類  
- 時間別構成ガイド
- スライド設計原則

---

## Step 2: 要件収集

「=== プレゼン要件確認 ===」と表示してください。

以下の質問にお答えください：

**質問1**: プレゼンのテーマは何ですか？
（例：新商品提案、プロジェクト報告、技術説明など）

あなたの回答を{{presentation_theme}}に設定してください。

**質問2**: 聴衆はどのタイプですか？
（経営層/技術者/一般聴衆 のいずれか）

あなたの回答を{{audience_type}}に設定してください。

**質問3**: 発表時間はどのくらいですか？
（5分/15分/30分 のいずれか）

あなたの回答を{{presentation_time}}に設定してください。

**質問4**: 主な目的は何ですか？
（説得/情報共有/提案/報告 のいずれか）

あなたの回答を{{main_purpose}}に設定してください。

「要件確認完了: {{presentation_theme}}（{{audience_type}}向け、{{presentation_time}}、目的：{{main_purpose}}）」と表示してください。

---

## Step 3: 知識適用・構成生成

「=== 最適構成生成 ===」と表示してください。

{{presentation_knowledge}}と収集した要件を統合して、最適なプレゼン構成を生成してください：

### 聴衆別アプローチ選択
{{audience_type}}に基づいて{{presentation_knowledge}}から適切なアプローチを選択し{{approach_style}}に設定してください。

### 構成パターン決定
{{main_purpose}}に基づいて最適な構成パターンを選択し{{structure_pattern}}に設定してください：
- 説得目的 → PREP法
- 提案目的 → 問題解決型
- 報告目的 → ストーリー型

### 時間配分計画
{{presentation_time}}に基づいて{{presentation_knowledge}}の時間別ガイドから時間配分を決定し{{time_allocation}}に設定してください。

「選択されたアプローチ: {{approach_style}}」と表示してください。
「構成パターン: {{structure_pattern}}」と表示してください。
「時間配分: {{time_allocation}}」と表示してください。

---

## Step 4: 具体的構成案出力

「=== 具体的プレゼン構成案作成 ===」と表示してください。

決定されたアプローチ、構成パターン、時間配分を基に、{{presentation_theme}}の具体的なプレゼン構成案を作成してください：

### 構成案生成
以下の形式で詳細な構成案を作成し{{detailed_structure}}に設定してください：

```
# {{presentation_theme}} プレゼン構成案

## 基本情報
- 聴衆: {{audience_type}}
- 時間: {{presentation_time}}
- 目的: {{main_purpose}}
- 構成パターン: {{structure_pattern}}

## 詳細構成
（具体的なスライド構成、各部の内容、時間配分）

## 話し方のコツ
（{{audience_type}}向けの効果的な話し方）

## 注意点・準備事項
（成功のためのポイント）

## スライド設計指針
（視覚的要素と内容の詳細性のガイド）
```

### ファイル出力
{{detailed_structure}}をpresentation_output.mdに保存してください。

「プレゼン構成案をpresentation_output.mdに出力しました」と表示してください。

---

## Step 5: 知識ベース効果確認

presentation_output.mdを読み込んで{{generated_output}}に設定してください。

「=== 知識ベース活用効果確認 ===」と表示してください。

以下を確認してください：

### 知識活用精度
- presentation_framework.mdの知識が構成案に反映されているか
- 聴衆別アプローチが適切に適用されているか
- 構成パターンが正しく選択・実装されているか

### 要件適応度
- ユーザーの要件（テーマ、聴衆、時間、目的）が構成に反映されているか
- 個別要件に応じたカスタマイズができているか

### 実用性評価
- 実際のプレゼンで使える具体性があるか
- 素人でも理解・実行できる明確さがあるか
- プロレベルの構成・アドバイスになっているか

### 知識ベースの価値
- 単純なテンプレート以上の知的な構成ができているか
- プレゼン設計の「暗黙知」が「形式知」として活用できているか
- 経験豊富なプレゼンターの知見が民主化されているか

「プレゼンテーション構成アドバイザー完了: 知識ベース単体の価値を確認しました」と表示してください。

---

## 実行例

### 入力例
- テーマ: 新商品提案
- 聴衆: 経営層
- 時間: 5分
- 目的: 提案

### 期待される出力
- PREP法ベースの構成
- ROI重視の経営層向けアプローチ
- 5分の厳密な時間配分
- 明確な投資判断材料の提示

---

## パターン7での位置づけ

**知識ベース**: プレゼン設計フレームワーク（静的な専門知識）
**環境センシング**: ユーザー要件収集（テーマ、聴衆、時間、目的）
**知識適用**: 要件に基づく最適パターン選択と構成生成

このプログラムは「動的な環境モデル」を持たないシンプルな知識ベース活用例として、Pattern 7の基礎概念を実践できます。