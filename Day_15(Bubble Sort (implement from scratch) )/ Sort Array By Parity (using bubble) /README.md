<h2>Sort Array By Parity Using Bubble Sort</h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr>

<p>Given an integer array <code>nums</code>, rearrange it so that all <strong>even integers appear before odd integers</strong>.</p>

<p>Use Bubble Sort-style adjacent comparisons and swaps to move odd numbers toward the end of the array. The relative order of the even and odd elements does not need to be preserved.</p>

<p><strong>Restriction:</strong> Do not use <code>.sort()</code>, <code>sorted()</code>, or a separate sorted array. Implement the solution using nested loops and manual swaps.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [3,1,2,4]</code></p>
<p><strong>Output:</strong> <code>[2,4,3,1]</code></p>
<p><strong>Explanation:</strong> The even numbers <code>2</code> and <code>4</code> appear before the odd numbers <code>3</code> and <code>1</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [0,1,2]</code></p>
<p><strong>Output:</strong> <code>[0,2,1]</code></p>
<p><strong>Explanation:</strong> The even numbers are moved before the odd number.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [1,3,5]</code></p>
<p><strong>Output:</strong> <code>[1,3,5]</code></p>
<p><strong>Explanation:</strong> All elements are odd, so no swaps are required.</p>
</div>

<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
</ul>

<p><strong>Expected Complexity:</strong></p>
<ul>
<li>Time: <code>O(n²)</code></li>
<li>Auxiliary Space: <code>O(1)</code></li>
</ul>