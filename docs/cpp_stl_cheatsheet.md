# C++ STL 常用容器操作備忘 (vector / unordered_set / unordered_map)

## vector<T>
- 新增: `v.push_back(x)` (尾插), `v.emplace_back(args...)` (就地構造), `v.insert(v.begin()+i, x)` (插入指定位置)
- 刪除: `v.pop_back()` (刪尾), `v.erase(v.begin()+i)` (刪指定位置), `v.erase(v.begin()+i, v.begin()+j)` (刪範圍), `v.clear()` (清空)
- 修改: `v[i] = x` 或 `v.at(i) = x` (at 有邊界檢查，較安全但慢)
- 查找: `find(v.begin(), v.end(), x)` (回傳 iterator，需要 `<algorithm>`；找不到回傳 `v.end()`)，沒有 O(1) 查找，vector 查找是 O(n)
- 其他常用: `v.size()`, `v.empty()`, `v.front()`, `v.back()`, `sort(v.begin(), v.end())`, `reverse(v.begin(), v.end())`

## unordered_set<T>
- 初始化: `unordered_set<int> s;` (空集合), `unordered_set<int> s = {1, 2, 3};` (initializer list), `unordered_set<int> s(v.begin(), v.end());` (用 vector/array 等容器的 iterator 範圍建立，會自動去重), `unordered_set<int> s2(s1);` (複製建構)
- 新增: `s.insert(x)` (回傳 pair<iterator, bool>，bool 表示是否真的插入)
- 刪除: `s.erase(x)` (用 value 刪，回傳刪除數量 0 或 1), `s.erase(it)` (用 iterator 刪), `s.clear()`
- 修改: 沒有直接修改，需先 `erase` 舊值再 `insert` 新值 (set 元素本身不可變)
- 查找: `s.find(x)` (回傳 iterator，找不到為 `s.end()`), `s.count(x)` (回傳 0 或 1，常用來判斷是否存在) → 推薦用 `s.count(x)` 或 C++20 的 `s.contains(x)`
- 其他: `s.size()`, `s.empty()`

## unordered_map<K, V>
- 新增: `m[key] = value` (若不存在會自動建立，value 預設初始化), `m.insert({key, value})` (已存在則不覆蓋), `m.emplace(key, value)`
- 刪除: `m.erase(key)` (用 key 刪), `m.erase(it)` (用 iterator 刪), `m.clear()`
- 修改: `m[key] = newValue` (直接覆蓋), 或透過 `m.at(key) = newValue` (key 不存在會丟例外，比 `[]` 安全，因為 `[]` 查找時若不存在會自動插入預設值)
- 查找: `m.find(key)` (回傳 iterator，找不到為 `m.end()`，避免用 `m[key]` 來查找因為會意外插入), `m.count(key)` (0 或 1)
- 遍歷: `for (auto& [k, v] : m)` (C++17 結構化綁定)
- 其他: `m.size()`, `m.empty()`

## list<T> (雙向鏈表)
- 新增: `l.push_back(x)` / `l.push_front(x)` (頭尾插入皆 O(1)), `l.insert(it, x)` (任意位置 O(1)，但找到 it 要 O(n))
- 刪除: `l.pop_back()` / `l.pop_front()`, `l.erase(it)` (O(1)), `l.remove(x)` (刪除所有等於 x 的元素), `l.clear()`
- 修改: `*it = x` (透過 iterator 改值)
- 查找: `find(l.begin(), l.end(), x)` (`<algorithm>`，O(n))，沒有 `[]` 隨機存取
- 其他: `l.size()`, `l.empty()`, `l.front()`, `l.back()`, `l.sort()` (成員函式，自己的排序，因為不支援隨機存取無法用 std::sort), `l.splice(...)` (O(1) 接合另一個 list)
- 特性: 沒有隨機存取 (`l[i]` 不支援)，任意位置插入/刪除都是 O(1)（前提已有 iterator）

## deque<T> (雙端佇列)
- 新增: `d.push_back(x)` / `d.push_front(x)` (頭尾皆 O(1)), `d.insert(d.begin()+i, x)` (中間 O(n))
- 刪除: `d.pop_back()` / `d.pop_front()` (皆 O(1)), `d.erase(d.begin()+i)` (中間 O(n)), `d.clear()`
- 修改: `d[i] = x` / `d.at(i) = x` (支援隨機存取，O(1))
- 查找: `find(d.begin(), d.end(), x)` (O(n))
- 其他: `d.size()`, `d.empty()`, `d.front()`, `d.back()`, `sort(d.begin(), d.end())` (支援 std::sort)
- 特性: 支援隨機存取且頭尾插入刪除都是 O(1)，是 vector 和 list 的折衷（常用來實作 queue/stack 的底層容器，或滑動窗口）

## 常見陷阱
- 用 `map[key]` 做查找會意外插入預設值，查找請用 `find` 或 `count`/`contains`
- vector 的 `erase`/`insert` 在中間位置操作是 O(n)，頻繁操作考慮用 list 或 deque
- unordered_set/map 不保證順序，需要排序請用 set/map (紅黑樹版本，O(log n))
- list 不支援隨機存取 (`l[i]` 編譯錯誤)，也不能用 `std::sort`（iterator 不是 random access），要排序用 `l.sort()`
- deque 的頭尾插入刪除不會使現有元素的 reference 失效，但會使 iterator 失效；中間插入刪除兩者都會失效（和 vector 類似）
- 需要頻繁頭尾操作選 deque；需要頻繁中間插入/刪除且不需要隨機存取選 list

## 型別轉換 (string / char / int / double)

### string → int / long / double
- `stoi(s)` → int, `stol(s)` → long, `stoll(s)` → long long, `stod(s)` → double, `stof(s)` → float
- 轉換失敗(非數字開頭)會丟 `invalid_argument`，數字超出範圍會丟 `out_of_range`
- 可接受字串前面的空白與正負號，遇到非數字字元會停止轉換（不會整串報錯），例如 `stoi("123abc")` → 123
- `stoi` 第二參數可取得轉換用了幾個字元: `size_t idx; int n = stoi(s, &idx);`

### int / double → string
- `to_string(x)` → 直接把數字轉成 string，支援 int/long/long long/float/double 等

### char → int (數字字元)
- `c - '0'` (字元 '0'~'9' 轉成對應數字，最常用也最快，不需要額外 include)
- 注意：`(int)c` 拿到的是 ASCII 碼，不是數字本身 (例如 `(int)'5'` 是 53，不是 5)

### int → char (數字轉字元)
- `char c = n + '0'` (n 為 0~9)

### char 大小寫轉換 / 判斷 (`<cctype>`)
- `isdigit(c)`, `isalpha(c)`, `isalnum(c)`, `isspace(c)`, `isupper(c)`, `islower(c)`
- `toupper(c)`, `tolower(c)` (回傳 int，若要存回 char 需要 `(char)toupper(c)`)

### string 與 char 陣列互轉
- `string s(cstr)` / `s = cstr` (`const char*` → string，自動轉換)
- `s.c_str()` (string → `const char*`)
- `vector<char> v(s.begin(), s.end())` / `string s(v.begin(), v.end())` (string 與 vector<char> 互轉)

### 其他常用轉換
- `static_cast<int>(d)` (double → int，無條件捨去小數部分，不建議用舊式 `(int)d` C-style cast)
- `static_cast<double>(n)` (int → double，常用於避免整數除法，例如 `static_cast<double>(a) / b`)
- stringstream 轉換（適合格式較複雜或一次要解析多個數字）:
  ```cpp
  #include <sstream>
  stringstream ss(s);
  int a, b;
  ss >> a >> b; // 以空白分隔自動解析
  ```

### 常見陷阱
- `stoi` 遇到完全無法轉換的字串（如 `"abc"`）會丟例外，記得包 `try/catch` 或先用 `isdigit` 檢查
- `char - '0'` 只適用於 ASCII 數字字元 '0'~'9'，其他字元結果無意義
- 整數除法 `a / b` 兩個 int 相除結果還是 int（捨去小數），要得到浮點數需先轉型其中一個運算元
