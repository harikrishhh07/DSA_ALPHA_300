<h2>Find K Smallest Elements Using Selection Sort</h2>

<img src='https://img.shields.io/badge/Difficulty-Easy--Medium-orange' alt='Difficulty: Easy-Medium' /><hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, find the <strong>k smallest elements</strong> in the array and return them in ascending order.</p>

<p>Use the Selection Sort approach. In each pass, find the smallest element in the remaining unsorted portion and swap it into the next correct position. Stop after placing the first <code>k</code> smallest elements.</p>

<p><strong>Restriction:</strong> Do not use <code>.sort()</code>, <code>sorted()</code>, or <code>min()</code>. Find the minimum manually by scanning the array.</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [7,10,4,3,20,15], k = 3</code></p>
<p><strong>Output:</strong> <code>[3,4,7]</code></p>
<p><strong>Explanation:</strong> The three smallest elements are <code>3</code>, <code>4</code>, and <code>7</code>, returned in ascending order.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [5,2,8,1], k = 1</code></p>
<p><strong>Output:</strong> <code>[1]</code></p>
<p><strong>Explanation:</strong> The smallest element is <code>1</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <code>nums = [9,4,6,2,7], k = 5</code></p>
<p><strong>Output:</strong> <code>[2,4,6,7,9]</code></p>
<p><strong>Explanation:</strong> Since <code>k</code> equals the array length, all elements are returned in ascending order.</p>
</div>

<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= k &lt;= nums.length</code></li>
<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p><strong>Expected Complexity:</strong></p>
<ul>
<li>Time: <code>O(kn)</code></li>
<li>Auxiliary Space: <code>O(1)</code> extra space when modifying the input array in place</li>
</ul>