# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for domain generation."""

GENERATE_DOMAIN_PROMPT = """
You are an intelligent assistant that helps a human to analyze the information in a text document.
Given a sample text, help the user by assigning a descriptive domain that summarizes what the text is about.
Example domains are: "Social studies", "Algorithmic analysis", "Medical science", among others.

Text: {input_text}
Domain:"""



GENERATE_DOMAIN_PROMPT_ZH = """
你是一个智能助手，帮助人类分析文本文档中的信息。
给定一个示例文本，通过分配一个描述性域来帮助用户总结文本的内容。
示例领域包括:"社会研究"、"算法分析"、"医学"等。

文字:{input_text}
Domain:"""