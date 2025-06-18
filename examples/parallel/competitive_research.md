# 競合調査システム（Parallel Processing - 中級）

- `##` マークダウン見出し：順次実行するメインタスク
- `###` マークダウン見出し：Task toolを利用して並列実行されるサブタスク
- 条件分岐: 自然言語による条件指示（「...の場合は」「...に応じて」など）
- `{{variable_name}}`：結果参照
- 結果保存：「...を{{variable_name}}に保存してください」
- 永続化保存：「{{variable_name}}をfilename.jsonに保存して永続化してください」
- ファイル読み込み：「filename.jsonを読み込んで{{variable_name}}に設定してください」
- 外部モジュール実行：「filename.mdの実行をしてください」
- ツール使用：自然言語で指示（例：「Webで調べて」「ファイルを読んで」）

---


## 調査対象設定
「クラウドサービス市場」の主要企業として以下5社を{{target_companies}}に保存し、
{{target_companies}}をtarget_companies.jsonに保存して永続化してください：
- Amazon AWS
- Microsoft Azure  
- Google Cloud Platform
- IBM Cloud
- Oracle Cloud

## 並列企業分析
{{target_companies}}の各企業について以下を同時実行：

### AWS分析
Amazon AWSの事業戦略、技術的優位性、市場シェア、最新サービスを分析し{{aws_analysis}}に保存してください。

### Azure分析  
Microsoft Azureの事業戦略、エンタープライズ重点、Office365連携、成長戦略を分析し{{azure_analysis}}に保存してください。

### GCP分析
Google Cloud Platformの技術革新、AI/ML特化戦略、データ分析強みを分析し{{gcp_analysis}}に保存してください。

### IBM分析
IBM Cloudのハイブリッド戦略、企業向けソリューション、AI Watson活用を分析し{{ibm_analysis}}に保存してください。

### Oracle分析
Oracle Cloudのデータベース強み、エンタープライズ顧客基盤、統合戦略を分析し{{oracle_analysis}}に保存してください。

## 競合比較マトリックス作成
{{aws_analysis}}、{{azure_analysis}}、{{gcp_analysis}}、{{ibm_analysis}}、{{oracle_analysis}}を比較し、
以下の観点での競合マトリックスを作成して{{comparison_matrix}}に保存してください：
- 市場シェア
- 技術的優位性
- 価格競争力
- 顧客満足度
- 成長性

## 戦略的インサイト抽出
{{comparison_matrix}}を基に、市場における競争構造と今後の展開予測を分析し、
戦略的示唆をcompetitive_insights.jsonに保存して永続化してください。

---

**学習ポイント**:
- 5つの並列タスクによるスケーラブルな設計
- 各企業の特徴に応じた個別分析視点
- 複数の分析結果の体系的比較手法
- 戦略的インサイトの抽出プロセス
- ファイル永続化による重要情報の保存
- より複雑な並列処理システムの構築