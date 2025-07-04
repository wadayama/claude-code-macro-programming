#!/usr/bin/env python3
import sys
import json

# RAM上の変数ストレージ（辞書）
_variables = {}

def var_set(name, value):
    """変数に値を設定"""
    _variables[name] = value
    print(f"Variable '{name}' set to: {value}")

def var_get(name):
    """変数の値を取得"""
    if name in _variables:
        print(_variables[name])
        return _variables[name]
    else:
        print(f"Variable '{name}' not found")
        return ""

def var_list():
    """全変数を一覧表示"""
    if not _variables:
        print("No variables defined")
    else:
        for name, value in _variables.items():
            # 長い値は省略表示
            display_value = value[:50] + "..." if len(value) > 50 else value
            print(f"{name}: {display_value}")

def var_clear():
    """全変数をクリア"""
    global _variables
    count = len(_variables)
    _variables.clear()
    print(f"Cleared {count} variables")

def var_exists(name):
    """変数の存在確認"""
    exists = name in _variables
    print("true" if exists else "false")
    return exists

def main():
    if len(sys.argv) < 2:
        print("Usage: var <command> [args...]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "set" and len(sys.argv) >= 4:
        var_set(sys.argv[2], sys.argv[3])
    elif command == "get" and len(sys.argv) >= 3:
        var_get(sys.argv[2])
    elif command == "list":
        var_list()
    elif command == "clear":
        var_clear()
    elif command == "exists" and len(sys.argv) >= 3:
        var_exists(sys.argv[2])
    else:
        print("Unknown command or invalid arguments")
        sys.exit(1)

if __name__ == "__main__":
    main()