<h2><a href="https://leetcode.com/problems/max-consecutive-ones-iii/">Max Consecutive Ones III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a binary array <code>nums</code> and an integer <code>k</code>, return the maximum number of consecutive <code>1</code>s in the array if you can flip at most <code>k</code> <code>0</code>s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2</span></p>
<p><strong>Output:</strong> <span class="example-io">6</span></p>
<p><strong>Explanation:</strong> [1,1,1,0,0,1,1,1,1,1,1] has 6 consecutive ones after flipping two zeroes.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,0,1,1,1,0,0], k = 0</span></p>
<p><strong>Output:</strong> <span class="example-io">3</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>
