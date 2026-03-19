import os

TARGET_ID = "REDACTED" 
REPLACEMENT = "0"

def clean_files():
    count = 0
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if TARGET_ID in content:
                new_content = content.replace(TARGET_ID, REPLACEMENT)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已清理: {filename}")
                count += 1
    print(f"--- 完成！共清理 {count} 個檔案 ---")

if __name__ == "__main__":
    clean_files()
