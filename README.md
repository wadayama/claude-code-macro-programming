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

**10のデザインパターン**
- 基本処理パターン（順次・並列・条件分岐・繰り返し）
- 高度なパターン（問題解決・経験活用・環境理解・人間協調・エラーハンドリング・デバッグ）

**付録：高度な技術要素と実用化技術**
- A.1: Claude Codeスラッシュコマンドによるシステム制御
- A.2: Event-Driven実行
- A.3: 重要なタスクでのリスク軽減戦略
- A.4: Python Tool Integration（Python ツール統合）
- A.5: マルチエージェント・システム設計（variables.json黒板モデル）
- A.6: 監査ログシステム（透明性と責任追跡性の確保）
- A.7: LLMベース検証システム（LLMによる実行前静的分析による安全性確保）
- A.8: メタプログラミング（動的マクロ生成・検証・評価・改善による自己適応システム）
- A.9: アンサンブル実行と合意形成（確率的動作への統計的対抗策）
- A.10: 型安全性とスキーマ管理（段階的型安全性強化とスキーマベース体系的データ管理）

**実践的な応用例**
- 俳句生成・ブログ作成・投資判断支援システム等
- 業務自動化への応用手法

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