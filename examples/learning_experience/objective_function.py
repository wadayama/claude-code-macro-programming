#!/usr/bin/env python3
"""
秘密の2次元目的関数評価プログラム
LLMからは関数形も最適解位置も見えない完全ブラインド探索用

使用方法:
python objective_function.py <x> <y>

出力:
関数値のみを標準出力に返す
"""

import sys
import math
import random

# ユーザが設定する秘密パラメータ（LLMからは見えない）
# 最適解の位置
X0 = 1.0
Y0 = -2.8

# 関数の複雑さパラメータ
OSCILLATION_STRENGTH = 20.0
NOISE_LEVEL = 0.05  # 小さなノイズを追加

def objective_function(x, y):
    """
    秘密の2次元目的関数
    実際の最適解は (X0, Y0) にある
    """
    # 座標変換（秘密のシフト）
    dx = x - X0
    dy = y - Y0
    
    # 複雑な2次元関数
    # 二次項 + 振動項 + 相互作用項
    quadratic_term = dx**2 + dy**2
    oscillation_term = OSCILLATION_STRENGTH * (math.sin(dx)**2 + math.sin(dy)**2)
    interaction_term = 5.0 * math.sin(dx) * math.sin(dy)
    
    base_value = quadratic_term + oscillation_term + interaction_term
    
    # 少量のノイズを追加（現実的な評価環境をシミュレート）
    noise = random.gauss(0, NOISE_LEVEL)
    
    return base_value + noise

def main():
    if len(sys.argv) != 3:
        print("Error: 引数が不正です", file=sys.stderr)
        print("使用方法: python objective_function.py <x> <y>", file=sys.stderr)
        sys.exit(1)
    
    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    except ValueError:
        print("Error: x, y は数値である必要があります", file=sys.stderr)
        sys.exit(1)
    
    # 定義域チェック
    if not (-5 <= x <= 5 and -5 <= y <= 5):
        print("Error: x, y は [-5, 5] の範囲内である必要があります", file=sys.stderr)
        sys.exit(1)
    
    # 関数評価
    result = objective_function(x, y)
    
    # 結果を標準出力に出力（小数点以下6桁）
    print(f"{result:.6f}")

if __name__ == "__main__":
    # ランダムシードを設定（再現性のため）
    random.seed(42)
    main()