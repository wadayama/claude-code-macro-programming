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

## 🎯 10のデザインパターン

自然言語マクロプログラミングの中核となる10のデザインパターンを、**基本4パターン**と**高度6パターン**に分類して体系化しています。

### 📋 基本4パターン - [macro.md](./macro.md)

- **[Pattern 1: Sequential Pipeline（順次パイプライン）](./macro.md#pattern-1-sequential-pipeline順次パイプライン)** - タスクを順次実行し、前の処理結果を次の処理に渡す基本的な実行パターン
- **[Pattern 2: Parallel Processing（並列処理）](./macro.md#pattern-2-parallel-processing並列処理)** - 複数のタスクを同時実行し、効率的に処理を完了する並列実行パターン
- **[Pattern 3: Conditional Execution（条件分岐）](./macro.md#pattern-3-conditional-execution条件分岐)** - 状況に応じて異なる処理経路を選択する条件分岐パターン
- **[Pattern 4: Loop & Modular Programming（繰り返し・モジュール）](./macro.md#pattern-4-loop--modular-programming繰り返しモジュール)** - TODO-listベースの反復処理とFew-shot Pattern Loopによる効率的な繰り返し制御

### 🚀 高度6パターン - [macro.md](./macro.md)

- **[Pattern 5: Problem Solving & Recursion（問題解決・再帰）](./macro.md#pattern-5-problem-solving--recursion動的問題解決再帰的分割)** - 複雑な問題を段階的に分割し、TODO管理により解決する再帰的アプローチ
- **[Pattern 6: Learning from Experience（経験学習・知識蓄積）](./macro.md#pattern-6-learning-from-experience経験学習知識蓄積記憶管理)** - 過去の実行結果を学習し、改善提案を生成する経験学習パターン
- **[Pattern 7: Environment Sensing, Knowledge-base & Environment Model（環境センシング・知識ベース・環境モデル）](./macro.md#pattern-7-environment-sensing-knowledge-base-and-environment-model環境センシング知識ベース環境モデル)** - 外部環境の情報を取得し、知識体系を構築し、状況に応じた適応的処理を実行
- **[Pattern 8: Human-in-the-Loop（人間協調型エージェント）](./macro.md#pattern-8-human-in-the-loophitl-人間協調型エージェント設計)** - 人間の判断を適切なタイミングで組み込む協調型実行パターン
- **[Pattern 9: Error Handling（エラーハンドリング）](./macro.md#pattern-9-error-handlingエラーハンドリング)** - エラーを予測し、適切な回復処理を実行する堅牢性向上パターン
- **[Pattern 10: Debug & Tracing（デバッグ・トレーシング）](./macro.md#pattern-10-debug--tracingデバッグトレーシング)** - 実行状況を可視化し、問題の特定と解決を支援する開発支援パターン

### 🔧 パターンの活用と統合

**構成**: Pattern 1-4（基本パターン）と Pattern 5-10（高度パターン）、さらに Appendix（専門技術）を組み合わせて実用的なシステムを構築できます。

**統合効果**: 複数パターンの組み合わせにより、**A.4俳句生成マルチエージェント**のような協調型システムが構築可能になります。

### 📖 付録（高度な技術）- [Appendix.md](./Appendix.md)

- **[A.1: イベント駆動実行](./Appendix.md#a1-イベント駆動実行)** - 非同期処理とリアルタイム応答システム
- **[A.2: 4層の防御戦略](./Appendix.md#a2-4層の防御戦略)** - 4層防御戦略による安全な運用手法  
- **[A.3: Python ツール統合](./Appendix.md#a3-python-ツール統合)** - SQLite変数管理システム連携によるPythonエコシステム活用
- **[A.4: マルチエージェント・システム設計](./Appendix.md#a4-マルチエージェントシステム設計)** - 共有黒板モデルによる協調エージェントシステム（俳句生成マルチエージェント実装例含む）
- **[A.5: 監査ログシステム](./Appendix.md#a5-監査ログシステム)** - SQLite変数管理拡張による透明性と責任追跡性の確保
- **[A.6: LLMベース実行前検査](./Appendix.md#a6-llmベース実行前検査)** - LLMによる実行前静的分析によるセキュリティと品質の確保
- **[A.7: メタプログラミング](./Appendix.md#a7-メタプログラミング)** - 動的マクロ生成・検証・評価・改善による自己適応システム
- **[A.8: アンサンブル実行と合意形成](./Appendix.md#a8-アンサンブル実行と合意形成)** - 確率的動作への統計的対抗策
- **[A.9: 型安全性とスキーマ管理](./Appendix.md#a9-型安全性とスキーマ管理)** - 段階的型安全性強化とスキーマベース体系的データ管理
- **[A.10: LLMベース実行後評価](./Appendix.md#a10-llmベース実行後評価)** - 確率的システムの品質・創造性・論理性評価
- **[A.11: 変数管理の永続化とスケーリング](./Appendix.md#a11-変数管理の永続化とスケーリングデータベースの活用)** - データベースによる堅牢な状態管理
- **[A.12: ベクトルデータベースとRAG活用](./Appendix.md#a12-ベクトルデータベースとrag活用)** - 知識ベース・経験学習による動的知識システム
- **[A.13: ゴール指向アーキテクチャと自律的プランニング](./Appendix.md#a13-ゴール指向アーキテクチャと自律的プランニング)** - 4段階フロー・PDCAサイクルによる完全自律システム
- **[A.14: Pythonオーケストレーション型ハイブリッドアプローチ](./Appendix.md#a14-pythonオーケストレーション型ハイブリッドアプローチ)** - Python + 自然言語マクロによる高速・低コストシステム
- **[A.15: SQLiteベース変数管理](./Appendix.md#a15-sqliteベース変数管理)** - SQLiteデータベースによる堅牢な変数管理システム・パフォーマンス向上
- **[A.16: LLMエージェント協調マクロ自動生成](./Appendix.md#a16-llmエージェント協調マクロ自動生成)** - 宣言的仕様から手続き的マクロへの自動変換手法とデザインパターン活用

## 📚 主要コンテンツ

- **[macro.md](./macro.md)** - メインガイド（10デザインパターン + 付録参照）
- **[Appendix.md](./Appendix.md)** - 付録（高度な技術要素と手法）
- **[examples/](./examples/)** - パターン別実例集
- **[multi-haiku/](./multi-haiku/)** - マルチエージェント俳句生成システム（SQLiteベース実装例）
- **[SQLite/](./SQLite/)** - SQLiteベース変数管理システムの実装コードとツール
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

**Last Updated**: 2025-07-22  
**Author**: Tadashi Wadayama (with assistance from Claude Code)  
**License**: MIT License (2025)