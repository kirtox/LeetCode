# Coding Problem Tracker

用途：記錄每一題是否完成、完成品質、是否需要重刷，以及卡住的原因。

## 狀態怎麼填

| 狀態 | 什麼時候使用 | 下一步 |
| --- | --- | --- |
| Todo | 還沒開始 | 依照計畫安排時間做 |
| Solved | 能獨立完成，解法清楚，能說明複雜度 | 把 `完成` 改成 `☑` |
| Review | 有看提示、解答或討論後才完成 | 把 `完成` 和 `重刷` 都改成 `☑` |
| Stuck | 超過 35-45 分鐘沒有方向，或實作完全卡住 | 先把 `重刷` 改成 `☑`，看解法後寫下卡點 |
| Redo | 已經排定要再做一次 | 保留 `重刷` 為 `☑`，重做成功後改成 `Solved` |

## 建議填寫規則

- `完成`：做完就把 `☐` 改成 `☑`。
- `重刷`：需要再做一次就把 `☐` 改成 `☑`。
- `狀態`：用 `Todo`、`Solved`、`Review`、`Stuck`、`Redo` 表示目前品質。
- `耗時`：大概即可，例如 `18m`、`42m`、`60m+`。
- `卡點 / 筆記`：只寫一句重點，例如 `忘記 left pointer 何時收縮`。
- 如果一題重刷後真的會了，把狀態改成 `Solved`，並把 `重刷` 改回 `☐`。

## 10 月

| 順序 | LeetCode | 題目 | 難度 | 題型 | 完成 | 重刷 | 狀態 | 耗時 | 卡點 / 筆記 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | Two Sum | Easy | Hash Table | ☑ | ☐ | Solved | 10m | 忽然忘記key, value放啥 |
| 2 | 217 | Contains Duplicate | Easy | Hash Set | ☑ | ☐ | Solved | 1m | N/A |
| 3 | 242 | Valid Anagram | Easy | Hash Table | ☑ | ☐ | Solved | 8m | 忘記如果扣到0後應該要return False / Follow-Up沒試 |
| 4 | 49 | Group Anagrams | Medium | Hash Table | ☑ | ☑ | Stuck | 40m | 卡在整理得word dict不知道怎麼塞到另一個dict的key |
| 5 | 125 | Valid Palindrome | Easy | Two Pointers | ☑ | ☑ | Solved | 15m | Space O(1)的方法一開始沒想到 |
| 6 | 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers | ☑ | ☑ | Solved | 6m | Sorted array 是 two pointer 的提示 |
| 7 | 15 | 3Sum | Medium | Two Pointers | ☑ | ☑ | Solved | 40m+ | 用了一個TLE solution解太久 應該用two pointer |
| 8 | 11 | Container With Most Water | Medium | Two Pointers | ☑ | ☑ | Solved | 8m+ | left & right 相同時小卡了一下 |
| 9 | 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window | ☑ | ☐ | Solved | 11m+ | N/A |
| 10 | 3 | Longest Substring Without Repeating Characters | Medium | Sliding Window | ☑ | ☑ | Review | 30m+ | Sliding Window的left不應該直接跳到right |
| 11 | 21 | Merge Two Sorted Lists | Easy | Linked List | ☑ | ☐ | Solved | 5m+ |  |
| 12 | 206 | Reverse Linked List | Easy | Linked List | ☑ | ☐ | Solved | 7m+ |  |
| 13 | 876 | Middle of the Linked List | Easy | Linked List | ☑ | ☑ | Solved | 3m+ |  |
| 14 | 150 | Evaluate Reverse Polish Notation | Medium | Stack | ☑ | ☐ | Solved | 13m+ | 忘記Python如何truncates toward zero |
| 15 | 704 | Binary Search | Easy | Binary Search | ☑ | ☐ | Solved | 7m+ |  |
| 16 | 33 | Search in Rotated Sorted Array | Medium | Binary Search | ☑ | ☑ | Stuck | 30m+ | 卡在怎麼區分左右part |
| 17 | 104 | Maximum Depth of Binary Tree | Easy | Tree / DFS | ☑ | ☐ | Solved | 7m+ | 複習深度怎麼紀錄 / C++複習pair怎麼使用 |
| 18 | 226 | Invert Binary Tree | Easy | Tree / DFS | ☑ | ☑ | Review | 10m+ | 不熟悉 |
| 19 | 102 | Binary Tree Level Order Traversal | Medium | Tree / BFS | ☑ | ☑ | Review | 11m+ | 一開始用了DFS做 雖然AC 但還要嘗試BFS! |
| 20 | 200 | Number of Islands | Medium | DFS / BFS | ☐ | ☐ | Todo |  |  |
| 21 | 22 | Generate Parentheses | Medium | Backtracking | ☐ | ☐ | Todo |  |  |
| 22 | 46 | Permutations | Medium | Backtracking | ☐ | ☐ | Todo |  |  |

## 11 月

| 順序 | LeetCode | 題目 | 難度 | 題型 | 完成 | 重刷 | 狀態 | 耗時 | 卡點 / 筆記 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23 | 100 | Same Tree | Easy | Tree / DFS | ☐ | ☐ | Todo |  |  |
| 24 | 98 | Validate Binary Search Tree | Medium | Tree / DFS | ☐ | ☐ | Todo |  |  |
| 25 | 235 | Lowest Common Ancestor of a Binary Search Tree | Medium | Tree | ☐ | ☐ | Todo |  |  |
| 26 | 230 | Kth Smallest Element in a BST | Medium | Tree / Inorder | ☐ | ☐ | Todo |  |  |
| 27 | 199 | Binary Tree Right Side View | Medium | Tree / BFS | ☐ | ☐ | Todo |  |  |
| 28 | 543 | Diameter of Binary Tree | Easy | Tree / DFS | ☐ | ☐ | Todo |  |  |
| 29 | 133 | Clone Graph | Medium | Graph / BFS / DFS | ☐ | ☐ | Todo |  |  |
| 30 | 994 | Rotting Oranges | Medium | BFS | ☐ | ☐ | Todo |  |  |
| 31 | 207 | Course Schedule | Medium | Topological Sort | ☐ | ☐ | Todo |  |  |
| 32 | 210 | Course Schedule II | Medium | Topological Sort | ☐ | ☐ | Todo |  |  |
| 33 | 684 | Redundant Connection | Medium | Union Find | ☐ | ☐ | Todo |  |  |
| 34 | 547 | Number of Provinces | Medium | Union Find / DFS | ☐ | ☐ | Todo |  |  |
| 35 | 695 | Max Area of Island | Medium | DFS / BFS | ☐ | ☐ | Todo |  |  |
| 36 | 703 | Kth Largest Element in a Stream | Easy | Heap | ☐ | ☐ | Todo |  |  |
| 37 | 215 | Kth Largest Element in an Array | Medium | Heap / Quickselect | ☐ | ☐ | Todo |  |  |
| 38 | 347 | Top K Frequent Elements | Medium | Heap / Bucket | ☐ | ☐ | Todo |  |  |
| 39 | 56 | Merge Intervals | Medium | Interval | ☐ | ☐ | Todo |  |  |
| 40 | 57 | Insert Interval | Medium | Interval | ☐ | ☐ | Todo |  |  |
| 41 | 435 | Non-overlapping Intervals | Medium | Greedy | ☐ | ☐ | Todo |  |  |
| 42 | 153 | Find Minimum in Rotated Sorted Array | Medium | Binary Search | ☐ | ☐ | Todo |  |  |
| 43 | 74 | Search a 2D Matrix | Medium | Binary Search | ☐ | ☐ | Todo |  |  |
| 44 | 875 | Koko Eating Bananas | Medium | Binary Search on Answer | ☐ | ☐ | Todo |  |  |
| 45 | 981 | Time Based Key-Value Store | Medium | Hash Table / Binary Search | ☐ | ☐ | Todo |  |  |
| 46 | 238 | Product of Array Except Self | Medium | Prefix / Suffix | ☐ | ☐ | Todo |  |  |
| 47 | 560 | Subarray Sum Equals K | Medium | Prefix Sum | ☐ | ☐ | Todo |  |  |
| 48 | 973 | K Closest Points to Origin | Medium | Heap / Sorting | ☐ | ☐ | Todo |  |  |

## 12 月

| 順序 | LeetCode | 題目 | 難度 | 題型 | 完成 | 重刷 | 狀態 | 耗時 | 卡點 / 筆記 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49 | 70 | Climbing Stairs | Easy | DP | ☐ | ☐ | Todo |  |  |
| 50 | 198 | House Robber | Medium | DP | ☐ | ☐ | Todo |  |  |
| 51 | 213 | House Robber II | Medium | DP | ☐ | ☐ | Todo |  |  |
| 52 | 322 | Coin Change | Medium | DP | ☐ | ☐ | Todo |  |  |
| 53 | 300 | Longest Increasing Subsequence | Medium | DP / Binary Search | ☐ | ☐ | Todo |  |  |
| 54 | 1143 | Longest Common Subsequence | Medium | 2D DP | ☐ | ☐ | Todo |  |  |
| 55 | 139 | Word Break | Medium | DP | ☐ | ☐ | Todo |  |  |
| 56 | 55 | Jump Game | Medium | Greedy / DP | ☐ | ☐ | Todo |  |  |
| 57 | 45 | Jump Game II | Medium | Greedy | ☐ | ☐ | Todo |  |  |
| 58 | 78 | Subsets | Medium | Backtracking | ☐ | ☐ | Todo |  |  |
| 59 | 39 | Combination Sum | Medium | Backtracking | ☐ | ☐ | Todo |  |  |
| 60 | 79 | Word Search | Medium | Backtracking / DFS | ☐ | ☐ | Todo |  |  |
| 61 | 417 | Pacific Atlantic Water Flow | Medium | DFS / BFS | ☐ | ☐ | Todo |  |  |
| 62 | 721 | Accounts Merge | Medium | Union Find / DFS | ☐ | ☐ | Todo |  |  |
| 63 | 128 | Longest Consecutive Sequence | Medium | Hash Set | ☐ | ☐ | Todo |  |  |
| 64 | 424 | Longest Repeating Character Replacement | Medium | Sliding Window | ☐ | ☐ | Todo |  |  |
| 65 | 76 | Minimum Window Substring | Hard | Sliding Window | ☐ | ☐ | Todo |  |  |
| 66 | 295 | Find Median from Data Stream | Hard | Two Heaps | ☐ | ☐ | Todo |  |  |
| 67 | 124 | Binary Tree Maximum Path Sum | Hard | Tree / DFS | ☐ | ☐ | Todo |  |  |
| 68 | 23 | Merge k Sorted Lists | Hard | Heap / Linked List | ☐ | ☐ | Todo |  |  |
| 69 | 152 | Maximum Product Subarray | Medium | DP | ☐ | ☐ | Todo |  |  |
| 70 | 53 | Maximum Subarray | Medium | DP / Kadane | ☐ | ☐ | Todo |  |  |
| 71 | 739 | Daily Temperatures | Medium | Monotonic Stack | ☐ | ☐ | Todo |  |  |
| 72 | 853 | Car Fleet | Medium | Stack / Sorting | ☐ | ☐ | Todo |  |  |
| 73 | 909 | Snakes and Ladders | Medium | BFS | ☐ | ☐ | Todo |  |  |
| 74 | 146 | LRU Cache | Medium | Design | ☐ | ☐ | Todo |  |  |
| 75 | 155 | Min Stack | Medium | Design / Stack | ☐ | ☐ | Todo |  |  |
| 76 | 208 | Implement Trie | Medium | Trie / Design | ☐ | ☐ | Todo |  |  |
