import sqlite3
import os

# 数据库路径
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

try:
    # 连接数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 列出所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("数据库中的表:")
    for table in tables:
        print(f"- {table[0]}")
        
        # 获取每个表的结构
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        print("  列:")
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")
        
        # 获取每个表的行数
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cursor.fetchone()[0]
        print(f"  行数: {count}")
        print("")
    
except sqlite3.Error as e:
    print(f"数据库错误: {e}")
finally:
    if conn:
        conn.close() 