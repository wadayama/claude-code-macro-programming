# 競合調査システム（Parallel Processing - 中級）

## 完全初期化（クリーンスタート）

variables.jsonが存在すれば削除してください
TODOリストをすべてクリアしてください

「=== 並列処理システム開始 ===」と表示してください。

## 調査対象設定
「クラウドサービス市場」の主要企業として以下5社を{{target_companies}}に保存し、
{{target_companies}}をtarget_companies.jsonに保存してください：
- Amazon AWS
- Microsoft Azure  
- Google Cloud Platform
- IBM Cloud
- Oracle Cloud

## 並列企業分析
**以下の5つのタスクをTask toolを利用して並列実行してください：**

{{target_companies}}の各企業について以下を分析してください：

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
戦略的示唆をcompetitive_insights.jsonに保存してください。

