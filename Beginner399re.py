N = int(input())
P = list(map(int, input().split()))

rank = {}
for i, x in enumerate(sorted(P, reverse=True), 1):   # 降順でインデックスが１から始まる
    rank.setdefault(x, i)  # 初めて出た位置がそのスコアの順位
    
print("\n".join(str(rank[x]) for x in P))
"""
(str(rank[x]) for x in P)
P を左から順に見て、各得点 x に対応する順位 rank[x] を取り出し、文字列に変換する「ジェネレータ式」です。
例: P = [100, 80, 80, 70], rank = {100:1, 80:2, 70:4} なら、"1", "2", "2", "4" が順に生成されます。
"\n".join(・・・)
生成された文字列たちを改行文字 "\n" で連結して、1つの大きな文字列にします。
上の例だと "1\n2\n2\n4" になります。
"""
