<h2>Bubble Sort with Early-Exit Optimization</h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr>

<p>Given an array of integers <code>nums</code>, sort the array in ascending order using an <strong>optimized Bubble Sort algorithm</strong>.</p>

<p>Use a flag to track whether any swaps occur during a pass. If no swaps occur, the array is already sorted, so terminate the algorithm early.</p>

<p><strong>Restriction:</strong> Do not use <code>.sort()</code> or <code>sorted()</code>. Implement nested loops, manual swaps, and the early-exit condition yourself.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [1,2,3,4,5]</code></p>
<p><strong>Output:</strong> <code>[1,2,3,4,5]</code></p>
<p><strong>Explanation:</strong> The array is already sorted. No swaps occur in the first pass, so the algorithm terminates early.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [5,1,4,2,8]</code></p>
<p><strong>Output:</strong> <code>[1,2,4,5,8]</code></p>
<p><strong>Explanation:</strong> The algorithm sorts the array and stops when a complete pass requires no swaps.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [2,1]</code></p>
<p><strong>Output:</strong> <code>[1,2]</code></p>
<p><strong>Explanation:</strong> One swap sorts the array. The next pass detects that no swaps are needed.</p>
</div>

<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p><strong>Expected Complexity:</strong></p>
<ul>
<li>Best-case Time: <code>O(n)</code></li>
<li>Worst-case Time: <code>O(n²)</code></li>
<li>Auxiliary Space: <code>O(1)</code></li>
</ul>