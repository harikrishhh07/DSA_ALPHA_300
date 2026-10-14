<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement/">Longest Repeating Character Replacement</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character at most <code>k</code> times.</p>

<p>Return the length of the longest substring containing the same letter you can get after performing the operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "ABAB", k = 2</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong> Replace the two 'A's with 'B's or the two 'B's with 'A's to make all characters in the string the same.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "AABABBA", k = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong> Replace the one 'A' in the substring "ABBA" to get "ABBB". The longest valid substring has length 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
<li><code>s</code> consists of only uppercase English letters.</li>
<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>