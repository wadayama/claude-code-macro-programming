# Claude Code 自然言語マクロプログラミングガイド

**対象読者**: Claude Code初級者～中級者（プログラミング経験不問）  
**学習目標**: 自然言語によるマルチエージェントシステム構築の習得  
**推奨学習時間**: 2-4時間（基本パターン習得まで）

## 🎯 学習内容

1. **自然言語マクロプログラミングの基本概念**
   - マークダウン見出しによる実行制御
   - 変数管理と結果の受け渡し
   - 条件分岐と並列実行の実装

2. **3つの基本デザインパターン**
   - Sequential Pipeline（順次パイプライン）
   - Parallel Processing（並列処理）  
   - Conditional Execution（条件分岐）

3. **実践的なシステム構築能力**
   - 6つの段階別サンプルによる実習
   - 俳句生成システム等の実用例
   - 業務自動化への応用手法

## 📚 学習コンテンツ

### メインガイド
- **[macro.md](./macro.md)** - 完全ガイド（基本概念からパターンまで）
- **[haiku_direct.md](./haiku_direct.md)** - 実践例：俳句生成マルチエージェントシステム

### 段階別サンプル集
- **[examples/](./examples/)** - 6つの実践サンプル

#### Sequential Pipeline（順次パイプライン）
- [ブログ記事作成システム](./examples/sequential/blog_creation.md) - 初級
- [学術調査パイプライン](./examples/sequential/research_pipeline.md) - 中級

#### Parallel Processing（並列処理）
- [市場分析システム](./examples/parallel/market_analysis.md) - 初級  
- [競合調査システム](./examples/parallel/competitive_research.md) - 中級

#### Conditional Execution（条件分岐）
- [適応型学習システム](./examples/conditional/adaptive_tutor.md) - 初級
- [コンテンツ処理システム](./examples/conditional/content_processor.md) - 中級

## 🚀 学習手順

1. **基本概念習得**: [macro.md](./macro.md)の構文・パターンを学習する
2. **実践体験**: [haiku_direct.md](./haiku_direct.md)で統合システムを体験する
3. **段階別練習**: [examples/](./examples/)で各パターンを習得する

## 📝 前提知識

- マークダウン記法の基本理解
- Claude Codeの基本操作
- プログラミング経験は不要

## 🎓 学習パス

### 初級者向け
1. macro.mdの基本構文を理解する
2. haiku_direct.mdで全体像を把握する
3. 各パターンの初級サンプルを実行する

### 中級者向け
1. 各パターンの中級サンプルに挑戦する
2. パターンの組み合わせを試行する
3. 独自のシステム設計に応用する

## 🛡️ ライセンス

MIT License - 詳細は [LICENSE](./LICENSE) を参照。

## 👥 著者

- **Tadashi Wadayama** - プロジェクト設計・文書作成
- **Claude Code (Anthropic Inc.)** - 技術実装・検証

---

**Version**: 1.0  
**Created**: 2025-06-18  
**Last Updated**: 2025-06-18