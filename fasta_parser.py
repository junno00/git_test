import pandas as pd

def parse_fasta(file_path):
    sequences = []
    names = []
    
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
                names.append(line[1:])  # 配列名を保存
            else:
                sequence += line  # 配列を追加
        if sequence:  # 最後の配列を追加
            sequences.append(sequence)

    # DataFrameを作成
    df = pd.DataFrame({'Name': names, 'Sequence': sequences})
    return df

# 使用例
if __name__ == "__main__":
    fasta_file = 'a.txt'  # 解析するFASTAファイルのパス
    df = parse_fasta(fasta_file)
    print(df)
