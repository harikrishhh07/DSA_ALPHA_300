<h2>Count Frequencies of Array Elements</h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>, count the frequency of each distinct element and return the frequencies as key-value pairs, where each key is an element and its value is the number of times it occurs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3,1,4]</span></p>
<p><strong>Output:</strong> <span class="example-io">{1: 2, 2: 2, 3: 1, 4: 1}</span></p>
<p><strong>Explanation:</strong></p>
<p>The element 1 appears twice, 2 appears twice, and 3 and 4 each appear once.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,5,5,5]</span></p>
<p><strong>Output:</strong> <span class="example-io">{5: 4}</span></p>
<p><strong>Explanation:</strong></p>
<p>The element 5 appears four times.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>
<p><strong>Output:</strong> <span class="example-io">{1: 1, 2: 1, 3: 1}</span></p>
<p><strong>Explanation:</strong></p>
<p>Each element appears exactly once.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>