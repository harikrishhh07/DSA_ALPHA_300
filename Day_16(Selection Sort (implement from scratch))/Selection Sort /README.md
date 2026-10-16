<h2>Selection Sort</h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr>

<p>Given an array of integers <code>nums</code>, sort the array in ascending order using the <strong>Selection Sort algorithm</strong>.</p>

<p>For each position, scan the remaining unsorted portion of the array to find the smallest element. Swap it with the first element of the unsorted portion.</p>

<p><strong>Restriction:</strong> Do not use <code>.sort()</code>, <code>sorted()</code>, or <code>min()</code>. Find the smallest element by scanning manually and perform the swap yourself.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [64,25,12,22,11]</code></p>
<p><strong>Output:</strong> <code>[11,12,22,25,64]</code></p>
<p><strong>Explanation:</strong> The smallest element from the unsorted portion is selected in each pass and placed at its correct position.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [5,4,3,2,1]</code></p>
<p><strong>Output:</strong> <code>[1,2,3,4,5]</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [-2,5,0,-1]</code></p>
<p><strong>Output:</strong> <code>[-2,-1,0,5]</code></p>
</div>

<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p><strong>Expected Complexity:</strong></p>
<ul>
<li>Time: <code>O(n²)</code></li>
<li>Auxiliary Space: <code>O(1)</code></li>
</ul>