# Learning from Experience サンプル

Claude Code自然言語マクロプログラミングにおける「Learning from Experience」パターンの実践的サンプル集です。

## 🎯 サンプル構成

### 1. 基礎サンプル
- **[writing_style_learning.md](./writing_style_learning.md)** - 文章スタイル分析・改善システム
  - JSON永続化による文章経験の記録・蓄積
  - 文体分析と改善ポイントの発見
  - 過去経験を活用した文章品質向上

### 2. 中級サンプル
- **[prompt_improvement_learning.md](./prompt_improvement_learning.md)** - プロンプト継続改良システム
  - Loop Pattern + Learning from Experience の統合実践
  - 評価駆動による段階的プロンプト最適化
  - ブログタイトル生成品質の継続改善

### 3. 上級サンプル  
- **[blind_optimization_learning.md](./blind_optimization_learning.md)** - 完全ブラインド最適化学習システム
  - 真のブラインド探索環境（関数形・最適解位置を完全非開示）
  - 外部Python評価プログラム連携
  - データ駆動推論による最適解発見
  - 早期停止条件付き効率的探索

- **[objective_function.py](./objective_function.py)** - 秘密の目的関数評価プログラム
  - LLMからは完全に隠蔽された関数形・最適解位置
  - 複雑な2次元関数（二次項+振動項+相互作用項+ノイズ）
  - コマンドライン評価インターフェース

## 🚀 実行方法

### 基礎サンプル
```bash
# Claude Codeで以下のマクロを実行
claude code run writing_style_learning.md
```

### 中級サンプル
```bash
# Claude Codeでプロンプト継続改良システムを実行
claude code run prompt_improvement_learning.md
```

### 上級サンプル
```bash
# 秘密の最適解位置をobjective_function.pyで設定
# X0, Y0の値をユーザが任意に変更可能

# Claude Codeで完全ブラインド最適化を実行
claude code run blind_optimization_learning.md
```

## 🔍 学習ポイント

### Learning from Experienceパターンの核心
1. **JSON永続化**: `{{variable_name}}をfilename.jsonに保存して永続化してください`
2. **経験蓄積**: 過去の試行結果を体系的に記録
3. **知見活用**: 蓄積された経験からの論理的推論
4. **継続学習**: Loop Patternとの組み合わせによる反復改善

### プロンプト改良システムの革新性
- **評価駆動改良**: 客観的評価指標による改良方向の決定
- **段階的最適化**: 過去履歴から学習した改良戦略の適用
- **収束判定**: 効率的な改良プロセスの自動終了
- **実用的統合**: Loop Pattern + Learning from Experienceの実践的融合

### ブラインド最適化の革新性
- **真の未知環境**: LLMが関数形を一切知らない状態での探索
- **チート防止**: 外部プログラムによる完全な情報隠蔽
- **データ駆動推論**: 評価結果のみからの戦略的意思決定
- **効率的収束**: 早期停止条件による実践的最適化

## 🎓 応用可能性

- **プロンプトエンジニアリング自動化**
- **コンテンツ品質継続改善**
- **機械学習ハイパーパラメータ調整**
- **A/Bテスト結果分析**
- **製品開発プロセス最適化**
- **個人学習記録・改善システム**
- **業務プロセス継続改善**
- **マーケティングメッセージ最適化**

## 📚 関連資料

- [macro.md](../../macro.md) - 全体設計思想とパターン解説
- [Pattern 6: Learning from Experience](../../macro.md#pattern-6-learning-from-experience) - 詳細理論