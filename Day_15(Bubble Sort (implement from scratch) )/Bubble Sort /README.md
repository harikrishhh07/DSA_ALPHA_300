<h2>Bubble Sort</h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr>

<p>Given an array of integers <code>nums</code>, sort the array in ascending order using the <strong>Bubble Sort algorithm</strong>.</p>

<p>Compare adjacent elements and swap them if the left element is greater than the right element. Repeat this process until the array is sorted.</p>

<p><strong>Restriction:</strong> Do not use <code>.sort()</code> or <code>sorted()</code>. Implement Bubble Sort from scratch using nested loops.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [5,1,4,2,8]</code></p>
<p><strong>Output:</strong> <code>[1,2,4,5,8]</code></p>
<p><strong>Explanation:</strong> Adjacent elements are compared and swapped until the array is sorted in ascending order.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [3,2,1]</code></p>
<p><strong>Output:</strong> <code>[1,2,3]</code></p>
<p><strong>Explanation:</strong> The elements are rearranged into ascending order through adjacent swaps.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [-3,0,-1,5]</code></p>
<p><strong>Output:</strong> <code>[-3,-1,0,5]</code></p>
<p><strong>Explanation:</strong> Negative and positive integers are sorted in ascending order.</p>
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