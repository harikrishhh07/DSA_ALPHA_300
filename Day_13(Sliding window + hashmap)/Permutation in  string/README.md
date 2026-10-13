<h2><a href="https://leetcode.com/problems/permutation-in-string/">Permutation in String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a permutation of <code>s1</code>, or <code>false</code> otherwise.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>'s permutations is a substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s1 = "ab", s2 = "eidbaooo"</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
<p><strong>Explanation:</strong> The substring "ba" is a permutation of "ab".</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s1 = "ab", s2 = "eidboaoo"</span></p>
<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s1.length, s2.length &lt;= 10^4</code></li>
<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>