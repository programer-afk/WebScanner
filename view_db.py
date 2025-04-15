import sqlite3

def view_database():
    conn = sqlite3.connect(r'Web-Scanner-master\db.sqlite3')
    cursor = conn.cursor()
    
    # 获取所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("数据库中的表：")
    for table in tables:
        table_name = table[0]
        print(f"\n表名: {table_name}")

        
        # # 获取表结构
        # cursor.execute(f"PRAGMA table_info({table_name});")
        # columns = cursor.fetchall()
        # print("表结构:")
        # for col in columns:
        #     print(f"  {col[1]} ({col[2]})")
        
        # # 获取表内容
        # cursor.execute(f"SELECT * FROM {table_name};")
        # rows = cursor.fetchall()
        # print("\n前5条数据:")
        # for row in rows:
        #     print(f"  {row}")
    
    conn.close()

if __name__ == "__main__":
    view_database() 