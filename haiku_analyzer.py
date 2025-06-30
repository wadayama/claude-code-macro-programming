#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俳句データ分析ツール
variables.jsonから俳句データを読み取り、詳細な分析を実行して結果を保存する
Python Tool Integration の実験用ツール
"""

import json
import re
from collections import Counter
from pathlib import Path

def count_morae(text):
    """日本語テキストの音律（モーラ）数を概算で計算"""
    # ひらがな・カタカナ・漢字を1モーラとして計算（簡易版）
    # 実際の俳句分析では更に精密な処理が必要だが、実験目的では十分
    text_cleaned = re.sub(r'[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', '', text)
    return len(text_cleaned)

def analyze_haiku_structure(haiku):
    """俳句の構造分析"""
    lines = haiku.split()
    if len(lines) >= 3:
        line1_morae = count_morae(lines[0]) if len(lines) > 0 else 0
        line2_morae = count_morae(' '.join(lines[1:-1])) if len(lines) > 2 else count_morae(lines[1]) if len(lines) > 1 else 0
        line3_morae = count_morae(lines[-1]) if len(lines) > 0 else 0
        
        return {
            "total_lines": len(lines),
            "line1_morae": line1_morae,
            "line2_morae": line2_morae, 
            "line3_morae": line3_morae,
            "total_morae": line1_morae + line2_morae + line3_morae,
            "structure_score": abs(5 - line1_morae) + abs(7 - line2_morae) + abs(5 - line3_morae)
        }
    else:
        total_morae = count_morae(haiku)
        return {
            "total_lines": len(lines),
            "total_morae": total_morae,
            "structure_score": 100  # 構造が不明確
        }

def analyze_vocabulary(text):
    """語彙分析"""
    # 単語を抽出（簡易版）
    words = re.findall(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]+', text)
    
    # 特徴的な語彙の分類
    nature_words = ['風', '星', '月', '花', '雲', '雨', '雪', '空', '海', '山']
    emotion_words = ['夢', '愛', '悲', '喜', '怒', '哀', '楽', '想', '憂', '希']
    tech_words = ['回路', '抵抗', '電子', '機械', '時計', 'コード', 'データ']
    
    nature_count = sum(1 for word in words if any(n in word for n in nature_words))
    emotion_count = sum(1 for word in words if any(e in word for e in emotion_words))
    tech_count = sum(1 for word in words if any(t in word for t in tech_words))
    
    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "word_list": words,
        "nature_words": nature_count,
        "emotion_words": emotion_count,
        "tech_words": tech_count,
        "vocabulary_diversity": len(set(words)) / len(words) if words else 0
    }

def analyze_creativity(haiku):
    """独創性分析"""
    # 独創的な表現の検出（簡易版）
    creativity_indicators = {
        "擬人法": ["夢見る", "語り", "踊る", "歌う", "泣く", "笑う"],
        "対比表現": ["大小", "明暗", "新旧", "動静"],
        "感覚的表現": ["響き", "調べ", "輝き", "香り", "触れ"],
        "抽象的概念": ["記憶", "時間", "空間", "存在", "無限"]
    }
    
    detected_techniques = {}
    for technique, patterns in creativity_indicators.items():
        count = sum(1 for pattern in patterns if pattern in haiku)
        if count > 0:
            detected_techniques[technique] = count
    
    return {
        "creativity_score": len(detected_techniques),
        "detected_techniques": detected_techniques,
        "is_metaphorical": any(word in haiku for word in ["ように", "みたい", "だらけ", "まみれ"])
    }

def main():
    """メイン処理"""
    try:
        # variables.jsonを読み込み
        variables_path = Path("variables.json")
        if not variables_path.exists():
            result = {
                "error": "variables.json not found",
                "status": "failed"
            }
        else:
            with open(variables_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 俳句データの抽出
            haikus = {}
            for i in range(1, 5):
                key = f"haiku_{i}"
                if key in data:
                    haikus[key] = data[key]
            
            themes = data.get("themes", "")
            best_selection = data.get("best_selection", "")
            
            # 各俳句の分析
            haiku_analyses = {}
            for key, haiku in haikus.items():
                analysis = {
                    "text": haiku,
                    "structure": analyze_haiku_structure(haiku),
                    "vocabulary": analyze_vocabulary(haiku),
                    "creativity": analyze_creativity(haiku)
                }
                haiku_analyses[key] = analysis
            
            # 全体統計
            total_morae = sum(h["structure"]["total_morae"] for h in haiku_analyses.values())
            avg_creativity = sum(h["creativity"]["creativity_score"] for h in haiku_analyses.values()) / len(haiku_analyses)
            
            # 分析結果の作成
            result = {
                "analysis_timestamp": "2025-06-30",
                "total_haikus_analyzed": len(haiku_analyses),
                "themes_analyzed": themes,
                "individual_analyses": haiku_analyses,
                "overall_statistics": {
                    "total_morae_count": total_morae,
                    "average_creativity_score": round(avg_creativity, 2),
                    "most_creative_haiku": max(haiku_analyses.keys(), key=lambda k: haiku_analyses[k]["creativity"]["creativity_score"]),
                    "best_structure_haiku": min(haiku_analyses.keys(), key=lambda k: haiku_analyses[k]["structure"]["structure_score"])
                },
                "recommendations": {
                    "strengths": [],
                    "areas_for_improvement": []
                },
                "status": "completed"
            }
            
            # 推奨事項の生成
            if avg_creativity > 2:
                result["recommendations"]["strengths"].append("高い独創性と表現技法の活用")
            
            structure_issues = sum(1 for h in haiku_analyses.values() if h["structure"]["structure_score"] > 3)
            if structure_issues == 0:
                result["recommendations"]["strengths"].append("優秀な5-7-5音律構造の維持")
            elif structure_issues > 2:
                result["recommendations"]["areas_for_improvement"].append("音律構造の更なる精密化")
        
        # 結果をvariables.jsonに書き戻し
        data["analysis_report"] = result
        
        with open(variables_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("俳句分析が完了しました。結果はvariables.jsonのanalysis_reportに保存されました。")
        print(f"分析対象: {result['total_haikus_analyzed']}句")
        print(f"平均独創性スコア: {result['overall_statistics']['average_creativity_score']}")
        
    except Exception as e:
        error_result = {
            "error": str(e),
            "status": "failed",
            "analysis_timestamp": "2025-06-30"
        }
        
        # エラー情報もvariables.jsonに記録
        try:
            with open("variables.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            data["analysis_report"] = error_result
            with open("variables.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except:
            pass
        
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()