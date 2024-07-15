# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Utility prompts for low-level LLM invocations."""

JSON_CHECK_PROMPT = """
You are going to be given a malformed JSON string that threw an error during json.loads.
It probably contains unnecessary escape sequences, or it is missing a comma or colon somewhere.
Your task is to fix this string and return a well-formed JSON string containing a single object.
Eliminate any unnecessary escape sequences.
Only return valid JSON, parseable with json.loads, without commentary.

# Examples
-----------
Text: {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: {{"title": "abc", "summary": "def"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: {{"title': "abc", 'summary": "def"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: "{{"title": "abc", "summary": "def"}}"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: [{{"title": "abc", "summary": "def"}}]
Output: [{{"title": "abc", "summary": "def"}}]
-----------
Text: [{{"title": "abc", "summary": "def"}}, {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}]
Output: [{{"title": "abc", "summary": "def"}}, {{"title": "abc", "summary": "def"}}]
-----------
Text: ```json\n[{{"title": "abc", "summary": "def"}}, {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}]```
Output: [{{"title": "abc", "summary": "def"}}, {{"title": "abc", "summary": "def"}}]


# Real Data
Text: {input_text}
Output:"""


JSON_CHECK_PROMPT_ZH = '''
你会得到一个格式错误的JSON字符串，它会在JSON .loads期间抛出错误。
它可能包含不必要的转义序列，或者在某处少了逗号或冒号。
你的任务是修复这个字符串，并返回一个包含单个对象的格式良好的JSON字符串。
消除任何不必要的转义序列。
只返回有效的JSON，可以用JSON解析。负荷，没有评论。

#例子
-----------
Text: {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: {{"title": "abc", "summary": "def"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: {{"title': "abc", 'summary": "def"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: "{{"title": "abc", "summary": "def"}}"
Output: {{"title": "abc", "summary": "def"}}
-----------
Text: [{{"title": "abc", "summary": "def"}}]
Output: [{{"title": "abc", "summary": "def"}}]
-----------
Text: [{{"title": "abc", "summary": "def"}}, {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}]
Output: [{{"title": "abc", "summary": "def"}}, {{"title": "abc", "summary": "def"}}]
-----------
Text: ```json\n[{{"title": "abc", "summary": "def"}}, {{ \\"title\\": \\"abc\\", \\"summary\\": \\"def\\" }}]```
Output: [{{"title": "abc", "summary": "def"}}, {{"title": "abc", "summary": "def"}}]


#真实数据
Text:{input_text}
Output:
'''
