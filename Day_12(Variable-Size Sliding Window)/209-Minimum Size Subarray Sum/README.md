<h2><a href="https://leetcode.com/problems/minimum-size-subarray-sum/">Minimum Size Subarray Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return the minimal length of a contiguous subarray whose sum is greater than or equal to <code>target</code>. If there is no such subarray, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 7, nums = [2,3,1,2,4,3]</span></p>
<p><strong>Output:</strong> <span class="example-io">2</span></p>
<p><strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem conditions.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 4, nums = [1,4,4]</span></p>
<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 11, nums = [1,1,1,1,1,1,1,1]</span></p>
<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= target &lt;= 10^9</code></li>
<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
<li><code>1 &lt;= nums[i] &lt;= 10^4</code></li>
</ul>