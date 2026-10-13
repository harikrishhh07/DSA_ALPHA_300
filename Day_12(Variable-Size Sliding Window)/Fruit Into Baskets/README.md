<h2><a href="https://leetcode.com/problems/fruit-into-baskets/">Fruit Into Baskets</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are visiting a farm with a row of fruit trees represented by the integer array <code>fruits</code>, where <code>fruits[i]</code> is the type of fruit produced by the <code>i</code>th tree.</p>

<p>You want to collect as much fruit as possible. You have two baskets, and each basket can only hold a single type of fruit. You can start at any tree and move right, picking exactly one fruit from each tree until you reach the end or encounter a tree whose fruit cannot fit into your baskets.</p>

<p>Return the maximum number of fruits you can collect.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">fruits = [1,2,1]</span></p>
<p><strong>Output:</strong> <span class="example-io">3</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">fruits = [0,1,2,2]</span></p>
<p><strong>Output:</strong> <span class="example-io">3</span></p>
<p><strong>Explanation:</strong> The subarray [1,2,2] contains two types of fruit and has length 3.</p>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">fruits = [1,2,3,2,2]</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong> The subarray [2,3,2,2] contains two types of fruit and has length 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= fruits.length &lt;= 10^5</code></li>
<li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>