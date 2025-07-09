# Claude Code 自然言語マクロプログラミングガイド

> 🌐 **English Version Available**: [English documentation is available here](https://github.com/wadayama/claude-code-macro-programming-en)

**Claude Code**を自然言語インタープリタとして活用し、エージェントシステムを構築する手法を示したガイドです。

## ⚡ クイックスタート

変数の保存と参照を試してみましょう：

**変数に保存**:
```
「春をテーマにした俳句を3つ作成して{{haiku}}に保存してください」
```

**変数を参照**:
```
「{{haiku}}の中から最も美しいものを選んで改良してください」
```

Claude Codeで上記をそのまま実行すると、自然言語マクロプログラミングが体験できます。
(注意: CLAUDE.mdにおけるマクロ定義が必要になります)

## 🎯 内容概要

## 🎯 10のデザインパターン

自然言語マクロプログラミングの中核となる10のデザインパターンを、**基本4パターン**と**高度6パターン**に分類して体系化しています。

### 📋 基本4パターン

#### Pattern 1: Sequential Pipeline（順次パイプライン）
タスクを順次実行し、前の処理結果を次の処理に渡す基本的な実行パターン

#### Pattern 2: Parallel Processing（並列処理）
複数のタスクを同時実行し、効率的に処理を完了する並列実行パターン

#### Pattern 3: Conditional Execution（条件分岐）
状況に応じて異なる処理経路を選択する条件分岐パターン

#### Pattern 4: Loop & Modular Programming（繰り返し・モジュール）
TODO-listベースの反復処理とFew-shot Pattern Loopによる効率的な繰り返し制御

### 🚀 高度6パターン

#### Pattern 5: Problem Solving & Recursion（問題解決・再帰）
複雑な問題を段階的に分割し、TODO管理により解決する再帰的アプローチ

#### Pattern 6: Learning from Experience（経験学習・知識蓄積）
過去の実行結果を学習し、改善提案を生成する経験学習パターン

#### Pattern 7: Environment Sensing（環境センシング・知識ベース）
外部環境の情報を取得し、状況に応じた適応的処理を実行

#### Pattern 8: Human-in-the-Loop（人間協調型エージェント）
人間の判断を適切なタイミングで組み込む協調型実行パターン

#### Pattern 9: Error Handling（エラーハンドリング）
エラーを予測し、適切な回復処理を実行する堅牢性向上パターン

#### Pattern 10: Debug & Tracing（デバッグ・トレーシング）
実行状況を可視化し、問題の特定と解決を支援する開発支援パターン

### 🔧 パターンの活用と統合

**構成**: Pattern 1-4（基本パターン）と Pattern 5-10（高度パターン）、さらに Appendix（専門技術）を組み合わせて実用的なシステムを構築できます。

**統合効果**: 複数パターンの組み合わせにより、**A.5俳句生成マルチエージェント**のような高度で実用的なシステムが構築可能になります。

**付録：高度な技術要素と実用化技術**
- A.1: Claude Codeスラッシュコマンドによるシステム制御
- A.2: Event-Driven実行
- A.3: 重要なタスクでのリスク軽減戦略
- A.4: Python Tool Integration（Python ツール統合）
- A.5: マルチエージェント・システム設計（variables.json黒板モデル・俳句生成マルチエージェント実装例）
- A.6: 監査ログシステム（透明性と責任追跡性の確保）
- A.7: LLMベース検証システム（LLMによる実行前静的分析による安全性確保）
- A.8: メタプログラミング（動的マクロ生成・検証・評価・改善による自己適応システム）
- A.9: アンサンブル実行と合意形成（確率的動作への統計的対抗策）
- A.10: 型安全性とスキーマ管理（段階的型安全性強化とスキーマベース体系的データ管理）
- A.11: 並行アクセス制御と楽観的ロック（variables.json並行アクセス制御による安全性確保）
- A.12: LLMベース評価テスト（確率的システムの品質・創造性・論理性評価）
- A.13: 分散変数サーバー（variables.json分散システムによる複数マシン協調動作）

**実践的な応用例**
- 俳句生成マルチエージェントシステム・ブログ作成・投資判断支援システム等
- 業務自動化・並行処理制御への応用手法

## 📚 主要コンテンツ

- **[macro.md](./macro.md)** - メインガイド（10デザインパターン + 付録参照）
- **[Appendix.md](./Appendix.md)** - 付録（高度な技術要素と手法）
- **[examples/](./examples/)** - パターン別実例集 
- **[haiku_direct.md](./haiku_direct.md)** - 実例（俳句生成システム）
- **[CLAUDE.md](./CLAUDE.md)** - マクロ定義ファイル
- **[debugger.md](./debugger.md)** - デバッグモード仕様書


## 📧 お問い合わせ

- **技術的な質問・バグ報告**: [GitHub Issues](../../issues)
- **学術的なお問い合わせ**: wadayama@nitech.ac.jp

## 🛡️ ライセンス

MIT License - 詳細は [LICENSE](./LICENSE) を参照。

## 👥 著者

- **Tadashi Wadayama** - プロジェクト設計・文書作成

---

**Last Updated**: 2025-07-05  
**Author**: Tadashi Wadayama (with assistance from Claude Code)  
**License**: MIT License (2025)