# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for community reporter role generation."""

GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT = """
{persona}
Given a sample text, help the user by creating a role definition that will be tasked with community analysis.
Take a look at this example, determine its key parts, and using the domain provided and your expertise, create a new role definition for the provided inputs that follows the same pattern as the example.
Remember, your output should look just like the provided example in structure and content.

Example:
A technologist reporter that is analyzing Kevin Scott's "Behind the Tech Podcast", given a list of entities
that belong to the community as well as their relationships and optional associated claims.
The report will be used to inform decision-makers about significant developments associated with the community and their potential impact.


Domain: {domain}
Text: {input_text}
Role:"""

GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT_ZH = """
{persona}
给定一个示例文本，通过创建角色定义来帮助用户，该角色将负责社区分析。
看一下这个示例，确定其关键部分，并使用提供的域和您的专业知识，为提供的输入创建一个新的角色定义，该定义遵循与示例相同的模式。
请记住，你的输出在结构和内容上应该与所提供的示例一样。

例子:
一名技术记者正在分析凯文·斯科特的《科技播客背后》，给出了一个实体列表
属于社区以及他们的关系和可选的相关声明。
该报告将用于向决策者通报与社区相关的重大发展及其潜在影响。


域:{domain}
文字:{input_text}
角色:"""
