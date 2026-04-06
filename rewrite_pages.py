from pathlib import Path

pages = {
    'bubble_sort.html': '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>氣泡排序法視覺化</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * { box-sizing: border-box; }
        body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; min-height: 100vh; margin: 0; background: radial-gradient(circle at 20% 50%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 40% 80%, rgba(255, 182, 193, 0.3) 0%, transparent 50%), linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #263445; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; }
        body::before { content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); z-index: -1; }
        nav { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); width: 100%; padding: 20px 0; text-align: center; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); position: sticky; top: 0; z-index: 10; border-bottom: 1px solid rgba(255, 255, 255, 0.2); }
        nav a { color: #4a5568; text-decoration: none; margin: 0 12px; font-weight: 600; font-size: 16px; padding: 12px 20px; border-radius: 50px; transition: all 0.3s ease; position: relative; overflow: hidden; }
        nav a:hover::before { left: 100%; }
        nav a.active, nav a:hover { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
        nav a::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.2), transparent); transition: left 0.5s; }
        .page { width: 100%; max-width: 980px; padding: 28px 20px 42px; }
        .hero { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-radius: 32px; padding: 40px 40px 32px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.3); text-align: center; margin-top: 32px; position: relative; overflow: hidden; }
        .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c); }
        .badge { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; font-size: 0.85rem; letter-spacing: 0.1em; padding: 10px 20px; border-radius: 50px; margin-bottom: 20px; font-weight: 600; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3); animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        h1 { font-size: 3.2rem; margin: 0; letter-spacing: 0.02em; color: #1a202c; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; }
        .subtitle { color: #4a5568; font-size: 1.1rem; line-height: 1.7; max-width: 720px; margin: 20px auto 0; font-weight: 400; }
        .explanation { background: rgba(255, 255, 255, 0.9); border-radius: 28px; padding: 32px; margin-top: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.35); }
        .explanation h2, .explanation h3 { color: #1a202c; }
        .explanation p { line-height: 1.8; color: #4a5568; }
        .explanation ul, .explanation ol { line-height: 1.7; color: #4a5568; padding-left: 20px; }
        .explanation li { margin-bottom: 10px; font-size: 1.05rem; }
        .explanation pre { background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; overflow-x: auto; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05); position: relative; }
        .explanation pre::before { content: 'Python'; position: absolute; top: 12px; right: 16px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .bar { width: 36px; margin: 0 6px; background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: center; align-items: flex-end; color: #ffffff; font-size: 13px; padding-bottom: 8px; border-radius: 12px 12px 0 0; box-shadow: 0 8px 25px rgba(255, 107, 157, 0.3); position: relative; font-weight: 600; }
        .bar:hover { transform: translateY(-4px) scale(1.05); box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4); }
        .bar:hover::after { opacity: 1; }
        .bar::after { content: ''; position: absolute; top: -4px; left: 50%; transform: translateX(-50%); width: 20px; height: 4px; background: rgba(255, 255, 255, 0.3); border-radius: 2px; opacity: 0; transition: opacity 0.3s ease; }
        .comparing { background: linear-gradient(180deg, #f093fb 0%, #f5576c 100%) !important; animation: comparing 1s ease-in-out infinite alternate; }
        @keyframes comparing { 0% { transform: scale(1); } 100% { transform: scale(1.1); } }
        .sorted { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%) !important; }
        .controls { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; margin-bottom: 50px; }
        button { min-width: 160px; padding: 14px 32px; font-size: 16px; cursor: pointer; border: none; border-radius: 50px; transition: all 0.3s ease; font-weight: 600; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; text-transform: uppercase; letter-spacing: 0.5px; }
        button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: rgba(255, 255, 255, 0.2); transition: left 0.4s ease; }
        button:hover::before { left: 100%; }
        .btn-start { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; }
        .btn-reset { background: #ffffff; color: #4a5568; }
        .btn-reset:hover { background: #eef2ff; }
    </style>
</head>
<body>
    <nav>
        <a href="bubble_sort.html" class="active">氣泡排序</a>
        <a href="selection_sort.html">選擇排序</a>
        <a href="insertion_sort.html">插入排序</a>
        <a href="merge_sort.html">合併排序</a>
        <a href="quick_sort.html">快速排序</a>
        <a href="heap_sort.html">堆積排序</a>
    </nav>
    <main class="page">
        <section class="hero">
            <span class="badge">排序演算法集錦</span>
            <h1>氣泡排序 (Bubble Sort)</h1>
            <p class="subtitle">逐步比較相鄰元素並交換位置，讓最大值或最小值像氣泡般飄到序列一端。</p>
        </section>
        <section class="explanation">
            <h2>操作原理</h2>
            <p>氣泡排序每回合比較相鄰的兩個元素，若前者比後者大則交換，最後將最大的元素移至右側。</p>
            <ol>
                <li>從序列第一個元素開始，依序比較相鄰元素</li>
                <li>若前者較大，則交換兩個元素</li>
                <li>重複比較直到序列尾端，完成一回合後最大值會移到右側</li>
                <li>將回合範圍縮小，直到整個序列排序完成</li>
            </ol>
            <h3>Python 代碼實現</h3>
            <pre><code>def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)</code></pre>
            <h3>複雜度分析</h3>
            <ul>
                <li><strong>時間複雜度：</strong>最壞 O(n²)，平均 O(n²)，最佳 O(n)</li>
                <li><strong>空間複雜度：</strong>O(1)</li>
                <li><strong>穩定性：</strong>穩定排序</li>
                <li><strong>原地排序：</strong>是</li>
            </ul>
        </section>
        <div id="container"></div>
        <div class="controls">
            <button class="btn-start" onclick="startSort()" id="startBtn">開始排序</button>
            <button class="btn-reset" onclick="resetArray()">重置數組</button>
        </div>
    </main>
    <script>
        const container = document.getElementById('container');
        let array = [];
        const SIZE = 12;
        function resetArray() {
            container.innerHTML = '';
            array = [];
            for (let i = 0; i < SIZE; i++) {
                const value = Math.floor(Math.random() * 90) + 10;
                array.push(value);
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.height = `${value * 2.5}px`;
                bar.innerText = value;
                bar.id = `bar-${i}`;
                container.appendChild(bar);
            }
            document.getElementById('startBtn').disabled = false;
        }
        const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
        async function startSort() {
            const bars = document.getElementsByClassName('bar');
            document.getElementById('startBtn').disabled = true;
            for (let i = 0; i < array.length; i++) {
                for (let j = 0; j < array.length - i - 1; j++) {
                    bars[j].classList.add('comparing');
                    bars[j + 1].classList.add('comparing');
                    await sleep(180);
                    if (array[j] > array[j + 1]) {
                        [array[j], array[j + 1]] = [array[j + 1], array[j]];
                        bars[j].style.height = `${array[j] * 2.5}px`;
                        bars[j].innerText = array[j];
                        bars[j + 1].style.height = `${array[j + 1] * 2.5}px`;
                        bars[j + 1].innerText = array[j + 1];
                    }
                    bars[j].classList.remove('comparing');
                    bars[j + 1].classList.remove('comparing');
                }
                bars[array.length - i - 1].classList.add('sorted');
            }
        }
        resetArray();
    </script>
</body>
</html>
''',
    'insertion_sort.html': '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>插入排序法視覺化</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * { box-sizing: border-box; }
        body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; min-height: 100vh; margin: 0; background: radial-gradient(circle at 20% 50%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 40% 80%, rgba(255, 182, 193, 0.3) 0%, transparent 50%), linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #263445; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; }
        body::before { content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); z-index: -1; }
        nav { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); width: 100%; padding: 20px 0; text-align: center; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); position: sticky; top: 0; z-index: 10; border-bottom: 1px solid rgba(255, 255, 255, 0.2); }
        nav a { color: #4a5568; text-decoration: none; margin: 0 12px; font-weight: 600; font-size: 16px; padding: 12px 20px; border-radius: 50px; transition: all 0.3s ease; position: relative; overflow: hidden; }
        nav a:hover::before { left: 100%; }
        nav a.active, nav a:hover { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
        nav a::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.2), transparent); transition: left 0.5s; }
        .page { width: 100%; max-width: 980px; padding: 28px 20px 42px; }
        .hero { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-radius: 32px; padding: 40px 40px 32px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.3); text-align: center; margin-top: 32px; position: relative; overflow: hidden; }
        .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c); }
        .badge { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; font-size: 0.85rem; letter-spacing: 0.1em; padding: 10px 20px; border-radius: 50px; margin-bottom: 20px; font-weight: 600; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3); animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        h1 { font-size: 3.2rem; margin: 0; letter-spacing: 0.02em; color: #1a202c; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; }
        .subtitle { color: #4a5568; font-size: 1.1rem; line-height: 1.7; max-width: 720px; margin: 20px auto 0; font-weight: 400; }
        .explanation { background: rgba(255, 255, 255, 0.9); border-radius: 28px; padding: 32px; margin-top: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.35); }
        .explanation h2, .explanation h3 { color: #1a202c; }
        .explanation p { line-height: 1.8; color: #4a5568; }
        .explanation ul, .explanation ol { line-height: 1.7; color: #4a5568; padding-left: 20px; }
        .explanation li { margin-bottom: 10px; font-size: 1.05rem; }
        .explanation pre { background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; overflow-x: auto; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05); position: relative; }
        .explanation pre::before { content: 'Python'; position: absolute; top: 12px; right: 16px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .bar { width: 36px; margin: 0 6px; background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: center; align-items: flex-end; color: #ffffff; font-size: 13px; padding-bottom: 8px; border-radius: 12px 12px 0 0; box-shadow: 0 8px 25px rgba(255, 107, 157, 0.3); position: relative; font-weight: 600; }
        .bar:hover { transform: translateY(-4px) scale(1.05); box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4); }
        .bar:hover::after { opacity: 1; }
        .bar::after { content: ''; position: absolute; top: -4px; left: 50%; transform: translateX(-50%); width: 20px; height: 4px; background: rgba(255, 255, 255, 0.3); border-radius: 2px; opacity: 0; transition: opacity 0.3s ease; }
        .comparing { background: linear-gradient(180deg, #f093fb 0%, #f5576c 100%) !important; animation: comparing 1s ease-in-out infinite alternate; }
        @keyframes comparing { 0% { transform: scale(1); } 100% { transform: scale(1.1); } }
        .sorted { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%) !important; }
        .controls { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; margin-bottom: 50px; }
        button { min-width: 160px; padding: 14px 32px; font-size: 16px; cursor: pointer; border: none; border-radius: 50px; transition: all 0.3s ease; font-weight: 600; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; text-transform: uppercase; letter-spacing: 0.5px; }
        button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: rgba(255, 255, 255, 0.2); transition: left 0.4s ease; }
        button:hover::before { left: 100%; }
        .btn-start { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; }
        .btn-reset { background: #ffffff; color: #4a5568; }
        .btn-reset:hover { background: #eef2ff; }
    </style>
</head>
<body>
    <nav>
        <a href="bubble_sort.html">氣泡排序</a>
        <a href="selection_sort.html">選擇排序</a>
        <a href="insertion_sort.html" class="active">插入排序</a>
        <a href="merge_sort.html">合併排序</a>
        <a href="quick_sort.html">快速排序</a>
        <a href="heap_sort.html">堆積排序</a>
    </nav>
    <main class="page">
        <section class="hero">
            <span class="badge">排序演算法集錦</span>
            <h1>插入排序 (Insertion Sort)</h1>
            <p class="subtitle">將當前元素插入已排序部分，像整理手中的牌那樣逐一排好。</p>
        </section>
        <section class="explanation">
            <h2>操作原理</h2>
            <p>插入排序將序列視為已排序和未排序兩部分，從未排序部分取出元素後插入到已排序部分的正確位置。</p>
            <ol>
                <li>從第二個元素開始，將該元素作為「待插入元素」</li>
                <li>向左比較已排序部分，當待插入元素小於前一個元素時，將前一個元素往右移動</li>
                <li>直到找到正確位置後插入待插入元素</li>
                <li>重複上述步驟，直到所有元素都處理完成</li>
            </ol>
            <h3>Python 代碼實現</h3>
            <pre><code>def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)</code></pre>
            <h3>複雜度分析</h3>
            <ul>
                <li><strong>時間複雜度：</strong>最壞 O(n²)，平均 O(n²)，最佳 O(n)</li>
                <li><strong>空間複雜度：</strong>O(1)</li>
                <li><strong>穩定性：</strong>穩定排序</li>
                <li><strong>原地排序：</strong>是</li>
            </ul>
        </section>
        <div id="container"></div>
        <div class="controls">
            <button class="btn-start" onclick="startSort()" id="startBtn">開始排序</button>
            <button class="btn-reset" onclick="resetArray()">重置數組</button>
        </div>
    </main>
    <script>
        const container = document.getElementById('container');
        let array = [];
        const SIZE = 12;
        function resetArray() {
            container.innerHTML = '';
            array = [];
            for (let i = 0; i < SIZE; i++) {
                const value = Math.floor(Math.random() * 90) + 10;
                array.push(value);
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.height = `${value * 2.5}px`;
                bar.innerText = value;
                bar.id = `bar-${i}`;
                container.appendChild(bar);
            }
            document.getElementById('startBtn').disabled = false;
        }
        const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
        async function startSort() {
            const bars = document.getElementsByClassName('bar');
            document.getElementById('startBtn').disabled = true;
            for (let i = 1; i < array.length; i++) {
                let key = array[i];
                let j = i - 1;
                bars[i].classList.add('comparing');
                await sleep(180);
                while (j >= 0 && array[j] > key) {
                    array[j + 1] = array[j];
                    bars[j + 1].style.height = `${array[j + 1] * 2.5}px`;
                    bars[j + 1].innerText = array[j + 1];
                    bars[j].classList.add('comparing');
                    await sleep(180);
                    bars[j].classList.remove('comparing');
                    j--; 
                }
                array[j + 1] = key;
                bars[j + 1].style.height = `${key * 2.5}px`;
                bars[j + 1].innerText = key;
                bars[i].classList.remove('comparing');
            }
            for (let idx = 0; idx < array.length; idx++) bars[idx].classList.add('sorted');
        }
        resetArray();
    </script>
</body>
</html>
''',
    'merge_sort.html': '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>合併排序法視覺化</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * { box-sizing: border-box; }
        body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; min-height: 100vh; margin: 0; background: radial-gradient(circle at 20% 50%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 40% 80%, rgba(255, 182, 193, 0.3) 0%, transparent 50%), linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #263445; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; }
        body::before { content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); z-index: -1; }
        nav { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); width: 100%; padding: 20px 0; text-align: center; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); position: sticky; top: 0; z-index: 10; border-bottom: 1px solid rgba(255, 255, 255, 0.2); }
        nav a { color: #4a5568; text-decoration: none; margin: 0 12px; font-weight: 600; font-size: 16px; padding: 12px 20px; border-radius: 50px; transition: all 0.3s ease; position: relative; overflow: hidden; }
        nav a:hover::before { left: 100%; }
        nav a.active, nav a:hover { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
        nav a::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.2), transparent); transition: left 0.5s; }
        .page { width: 100%; max-width: 980px; padding: 28px 20px 42px; }
        .hero { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-radius: 32px; padding: 40px 40px 32px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.3); text-align: center; margin-top: 32px; position: relative; overflow: hidden; }
        .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c); }
        .badge { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; font-size: 0.85rem; letter-spacing: 0.1em; padding: 10px 20px; border-radius: 50px; margin-bottom: 20px; font-weight: 600; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3); animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        h1 { font-size: 3.2rem; margin: 0; letter-spacing: 0.02em; color: #1a202c; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; }
        .subtitle { color: #4a5568; font-size: 1.1rem; line-height: 1.7; max-width: 720px; margin: 20px auto 0; font-weight: 400; }
        .explanation { background: rgba(255, 255, 255, 0.9); border-radius: 28px; padding: 32px; margin-top: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.35); }
        .explanation h2, .explanation h3 { color: #1a202c; }
        .explanation p { line-height: 1.8; color: #4a5568; }
        .explanation ul, .explanation ol { line-height: 1.7; color: #4a5568; padding-left: 20px; }
        .explanation li { margin-bottom: 10px; font-size: 1.05rem; }
        .explanation pre { background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; overflow-x: auto; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05); position: relative; }
        .explanation pre::before { content: 'Python'; position: absolute; top: 12px; right: 16px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .bar { width: 36px; margin: 0 6px; background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: center; align-items: flex-end; color: #ffffff; font-size: 13px; padding-bottom: 8px; border-radius: 12px 12px 0 0; box-shadow: 0 8px 25px rgba(255, 107, 157, 0.3); position: relative; font-weight: 600; }
        .controls { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; margin-bottom: 50px; }
        button { min-width: 160px; padding: 14px 32px; font-size: 16px; cursor: pointer; border: none; border-radius: 50px; transition: all 0.3s ease; font-weight: 600; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; text-transform: uppercase; letter-spacing: 0.5px; }
        button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: rgba(255, 255, 255, 0.2); transition: left 0.4s ease; }
        button:hover::before { left: 100%; }
        .btn-start { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; }
        .btn-reset { background: #ffffff; color: #4a5568; }
        .btn-reset:hover { background: #eef2ff; }
    </style>
</head>
<body>
    <nav>
        <a href="bubble_sort.html">氣泡排序</a>
        <a href="selection_sort.html">選擇排序</a>
        <a href="insertion_sort.html">插入排序</a>
        <a href="merge_sort.html">合併排序</a>
        <a href="quick_sort.html">快速排序</a>
        <a href="heap_sort.html" class="active">堆積排序</a>
    </nav>
    <main class="page">
        <section class="hero">
            <span class="badge">排序演算法集錦</span>
            <h1>堆積排序 (Heap Sort)</h1>
            <p class="subtitle">先建立最大堆，然後將堆頂元素取出並重建堆，最壞情況仍保證 O(n log n)。</p>
        </section>
        <section class="explanation">
            <h2>操作原理</h2>
            <p>堆積排序先將輸入資料轉換成最大堆，然後反覆將堆頂元素取出放到序列末端，再調整堆結構。</p>
            <ol>
                <li>建立最大堆，讓最大元素位於堆頂</li>
                <li>將堆頂最大元素與序列末端元素交換</li>
                <li>減少堆的大小，對剩餘元素進行 heapify</li>
                <li>重複以上步驟直到所有元素排序完成</li>
            </ol>
            <h3>Python 代碼實現</h3>
            <pre><code>def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))</code></pre>
            <h3>複雜度分析</h3>
            <ul>
                <li><strong>時間複雜度：</strong>最壞 O(n log n)，平均 O(n log n)，最佳 O(n log n)</li>
                <li><strong>空間複雜度：</strong>O(1)</li>
                <li><strong>穩定性：</strong>不穩定排序</li>
                <li><strong>原地排序：</strong>是</li>
            </ul>
        </section>
        <div id="container"></div>
        <div class="controls">
            <button class="btn-start" onclick="startSort()" id="startBtn">開始排序</button>
            <button class="btn-reset" onclick="resetArray()">重置數組</button>
        </div>
    </main>
    <script>
        const container = document.getElementById('container');
        let array = [];
        const SIZE = 12;
        function resetArray() {
            container.innerHTML = '';
            array = [];
            for (let i = 0; i < SIZE; i++) {
                const value = Math.floor(Math.random() * 90) + 10;
                array.push(value);
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.height = `${value * 2.5}px`;
                bar.innerText = value;
                bar.id = `bar-${i}`;
                container.appendChild(bar);
            }
            document.getElementById('startBtn').disabled = false;
        }
        const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
        async function heapify(n, i) {
            const bars = document.getElementsByClassName('bar');
            let largest = i;
            const l = 2 * i + 1;
            const r = 2 * i + 2;
            if (l < n) { bars[l].classList.add('comparing'); await sleep(120); bars[l].classList.remove('comparing'); }
            if (r < n) { bars[r].classList.add('comparing'); await sleep(120); bars[r].classList.remove('comparing'); }
            bars[i].classList.add('heap-root');
            await sleep(120);
            if (l < n && array[l] > array[largest]) largest = l;
            if (r < n && array[r] > array[largest]) largest = r;
            if (largest !== i) {
                await swap(i, largest);
                bars[i].classList.remove('heap-root');
                await heapify(n, largest);
            }
            bars[i].classList.remove('heap-root');
        }
        async function swap(i, j) {
            [array[i], array[j]] = [array[j], array[i]];
            const barA = document.getElementById(`bar-${i}`);
            const barB = document.getElementById(`bar-${j}`);
            const heightA = barA.style.height;
            const heightB = barB.style.height;
            const textA = barA.innerText;
            const textB = barB.innerText;
            barA.style.height = heightB;
            barB.style.height = heightA;
            barA.innerText = textB;
            barB.innerText = textA;
        }
        async function startSort() {
            document.getElementById('startBtn').disabled = true;
            const n = array.length;
            for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
                await heapify(n, i);
            }
            for (let end = n - 1; end > 0; end--) {
                await swap(0, end);
                document.getElementById(`bar-${end}`).classList.add('sorted');
                await heapify(end, 0);
            }
            document.getElementById('bar-0').classList.add('sorted');
        }
        resetArray();
    </script>
</body>
</html>
''',
    'selection_sort.html': '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>排序演算法集錦 - 選擇排序</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * { box-sizing: border-box; }
        body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; min-height: 100vh; margin: 0; background: radial-gradient(circle at 20% 50%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%), radial-gradient(circle at 40% 80%, rgba(255, 182, 193, 0.3) 0%, transparent 50%), linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #263445; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; }
        body::before { content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); z-index: -1; }
        nav { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); width: 100%; padding: 20px 0; text-align: center; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); position: sticky; top: 0; z-index: 10; border-bottom: 1px solid rgba(255, 255, 255, 0.2); }
        nav a { color: #4a5568; text-decoration: none; margin: 0 12px; font-weight: 600; font-size: 16px; padding: 12px 20px; border-radius: 50px; transition: all 0.3s ease; position: relative; overflow: hidden; }
        nav a:hover::before { left: 100%; }
        nav a.active, nav a:hover { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
        nav a::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.2), transparent); transition: left 0.5s; }
        .page { width: 100%; max-width: 980px; padding: 28px 20px 42px; }
        .hero { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-radius: 32px; padding: 40px 40px 32px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.3); text-align: center; margin-top: 32px; position: relative; overflow: hidden; }
        .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c); }
        .badge { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; font-size: 0.85rem; letter-spacing: 0.1em; padding: 10px 20px; border-radius: 50px; margin-bottom: 20px; font-weight: 600; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3); animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        h1 { font-size: 3.2rem; margin: 0; letter-spacing: 0.02em; color: #1a202c; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; }
        .subtitle { color: #4a5568; font-size: 1.1rem; line-height: 1.7; max-width: 720px; margin: 20px auto 0; font-weight: 400; }
        .explanation { background: rgba(255, 255, 255, 0.9); border-radius: 28px; padding: 32px; margin-top: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.35); }
        .explanation h2, .explanation h3 { color: #1a202c; }
        .explanation p { line-height: 1.8; color: #4a5568; }
        .explanation ul, .explanation ol { line-height: 1.7; color: #4a5568; padding-left: 20px; }
        .explanation li { margin-bottom: 10px; font-size: 1.05rem; }
        .explanation pre { background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; overflow-x: auto; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05); position: relative; }
        .explanation pre::before { content: 'Python'; position: absolute; top: 12px; right: 16px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .bar { width: 36px; margin: 0 6px; background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: center; align-items: flex-end; color: #ffffff; font-size: 13px; padding-bottom: 8px; border-radius: 12px 12px 0 0; box-shadow: 0 8px 25px rgba(255, 107, 157, 0.3); position: relative; font-weight: 600; }
        .controls { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; margin-bottom: 50px; }
        button { min-width: 160px; padding: 14px 32px; font-size: 16px; cursor: pointer; border: none; border-radius: 50px; transition: all 0.3s ease; font-weight: 600; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; text-transform: uppercase; letter-spacing: 0.5px; }
        button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: rgba(255, 255, 255, 0.2); transition: left 0.4s ease; }
        button:hover::before { left: 100%; }
        .btn-start { background: linear-gradient(135deg, #667eea, #764ba2); color: #ffffff; }
        .btn-reset { background: #ffffff; color: #4a5568; }
        .btn-reset:hover { background: #eef2ff; }
    </style>
</head>
<body>
    <nav>
        <a href="bubble_sort.html">氣泡排序</a>
        <a href="selection_sort.html" class="active">選擇排序</a>
        <a href="insertion_sort.html">插入排序</a>
        <a href="merge_sort.html">合併排序</a>
        <a href="quick_sort.html">快速排序</a>
        <a href="heap_sort.html">堆積排序</a>
    </nav>
    <main class="page">
        <section class="hero">
            <span class="badge">排序演算法集錦</span>
            <h1>選擇排序 (Selection Sort)</h1>
            <p class="subtitle">每回合找出最小元素並放到左側，觀察排序過程更具邏輯。</p>
        </section>
        <section class="explanation">
            <h2>操作原理</h2>
            <p>選擇排序是一種簡單的排序演算法，其基本思想是從未排序的區間中找到最小元素，然後與當前位置交換，逐步擴大已排序區間。</p>
            <ol>
                <li>從未排序區間找到最小元素</li>
                <li>將該最小元素與未排序區間開頭交換</li>
                <li>對剩餘未排序區間重複上述步驟</li>
                <li>直到整個序列排序完成</li>
            </ol>
            <h3>Python 代碼實現</h3>
            <pre><code>def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))</code></pre>
            <h3>複雜度分析</h3>
            <ul>
                <li><strong>時間複雜度：</strong>最壞 O(n²)，平均 O(n²)，最佳 O(n²)</li>
                <li><strong>空間複雜度：</strong>O(1)</li>
                <li><strong>穩定性：</strong>不穩定排序</li>
                <li><strong>原地排序：</strong>是</li>
            </ul>
        </section>
        <div id="container"></div>
        <div class="controls">
            <button class="btn-start" onclick="selectionSort()" id="startBtn">開始排序</button>
            <button class="btn-reset" onclick="reset()">重置數組</button>
        </div>
    </main>
    <script>
        const container = document.getElementById('container');
        let array = [];
        const SIZE = 12;
        function reset() {
            container.innerHTML = '';
            array = [];
            for (let i = 0; i < SIZE; i++) {
                const value = Math.floor(Math.random() * 90) + 10;
                array.push(value);
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.height = `${value * 2.5}px`;
                bar.innerText = value;
                bar.id = `bar-${i}`;
                container.appendChild(bar);
            }
            document.getElementById('startBtn').disabled = false;
        }
        const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
        async function selectionSort() {
            const bars = document.getElementsByClassName('bar');
            document.getElementById('startBtn').disabled = true;
            for (let i = 0; i < array.length; i++) {
                let min = i;
                bars[min].classList.add('comparing');
                for (let j = i + 1; j < array.length; j++) {
                    bars[j].classList.add('comparing');
                    await sleep(180);
                    if (array[j] < array[min]) {
                        bars[min].classList.remove('comparing');
                        min = j;
                        bars[min].classList.add('comparing');
                    }
                    bars[j].classList.remove('comparing');
                }
                if (min !== i) {
                    [array[i], array[min]] = [array[min], array[i]];
                    bars[i].style.height = `${array[i] * 2.5}px`;
                    bars[i].innerText = array[i];
                    bars[min].style.height = `${array[min] * 2.5}px`;
                    bars[min].innerText = array[min];
                }
                bars[min].classList.remove('comparing');
                bars[i].classList.add('sorted');
            }
        }
        reset();
    </script>
</body>
</html>
'''
}

for name, content in pages.items():
    Path(name).write_text(content, encoding='utf-8')
