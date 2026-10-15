BFS + queue 的核心概念：跟 code_1.py 的 DFS stack 解法不同，BFS 是「一層一層」處理，天生順序就是對的，不需要用 dict/map 分組。

引導幾個問題，你可以先想想：

1. 資料結構選擇：Python 沒有內建高效的 queue（list.pop(0) 是 O(n)），你會用什麼結構來當 queue？（提示：collections 裡有一個模組專門做雙端佇列，頭尾操作都是 O(1)）

2. 初始化：root 要先放進 queue，對吧？要放的是單純 node，還是要像 DFS 版那樣額外存 depth？（BFS 其實不需要存 depth，為什麼？）

3. 外層迴圈：while queue 不是空的，每一輪迴圈代表處理「一層」。但 queue 裡同時會有這一層 + 之後加進去的下一層節點，要怎麼知道「這一層有幾個」，讓 for 迴圈只處理這一層、不會把下一層也吃進來？（提示：在進 for 迴圈前先記錄一個數字）

4. 內層迴圈：對這一層的每個節點，做三件事：
    - 從 queue 左邊 pop 出來
    - 把它的 val 存進這一層的暫存 list
    - 把它的 left/right（若存在）加進 queue 的右邊，準備下一層

5. 收尾：這一層跑完後，把暫存 list 丟進最終結果 list。