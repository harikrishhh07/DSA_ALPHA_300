<h2>Sort Characters By Frequency (Manual)</h2>

<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr>

<p>Given a string <code>s</code>, rearrange its characters in <strong>descending order of frequency</strong>.</p>

<p>Count the occurrences of each character manually, then use nested loops and comparisons to arrange the characters by frequency. If two characters have the same frequency, either order is acceptable.</p>

<p><strong>Restriction:</strong> Do not use <code>sorted()</code>, <code>.sort()</code>, or <code>Counter</code>. Implement frequency counting and sorting manually.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>s = "tree"</code></p>
<p><strong>Output:</strong> <code>"eert"</code></p>
<p><strong>Explanation:</strong> The character <code>e</code> occurs twice, while <code>t</code> and <code>r</code> occur once. The most frequent character appears first.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>s = "cccaaa"</code></p>
<p><strong>Output:</strong> <code>"cccaaa"</code> or <code>"aaaccc"</code></p>
<p><strong>Explanation:</strong> Both characters occur three times, so either order is valid.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>s = "Aabb"</code></p>
<p><strong>Output:</strong> <code>"bbAa"</code> or <code>"bbaA"</code></p>
<p><strong>Explanation:</strong> The character <code>b</code> occurs twice, while <code>A</code> and <code>a</code> occur once each. Uppercase and lowercase characters are different.</p>
</div>

<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
<li><code>s</code> contains uppercase and lowercase English letters, digits, or other supported characters.</li>
</ul>

<p><strong>Expected Complexity:</strong></p>
<ul>
<li>Frequency counting: <code>O(n)</code> average time using a dictionary</li>
<li>Manual sorting: <code>O(m²)</code>, where <code>m</code> is the number of distinct characters</li>
</ul>