<h2><a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/">Find All Anagrams in a String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given two strings <code>s</code> and <code>p</code>, return an array of all the start indices of <code>p</code>'s anagrams in <code>s</code>. You may return the answer in any order.</p>

<p>An anagram is a string formed by rearranging the letters of another string, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "cbaebabacd", p = "abc"</span></p>
<p><strong>Output:</strong> <span class="example-io">[0,6]</span></p>
<p><strong>Explanation:</strong> The substring starting at index 0 is "cba", which is an anagram of "abc". The substring starting at index 6 is "bac", which is also an anagram of "abc".</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abab", p = "ab"</span></p>
<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10^4</code></li>
<li><code>s</code> and <code>p</code> consist of lowercase English letters.</li>
</ul>