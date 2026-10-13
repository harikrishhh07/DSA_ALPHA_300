<h2><a href="https://leetcode.com/problems/contains-duplicate-ii/">Contains Duplicate II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if there are two distinct indices <code>i</code> and <code>j</code> in the array such that <code>nums[i] == nums[j]</code> and <code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1], k = 3</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,1,1], k = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1,2,3], k = 2</span></p>
<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
<li><code>-10^9 &lt;= nums[i] &lt;= 10^9</code></li>
<li><code>0 &lt;= k &lt;= 10^5</code></li>
</ul>