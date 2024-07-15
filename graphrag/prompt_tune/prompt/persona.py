# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for persona generation."""

GENERATE_PERSONA_PROMPT = """
You are an intelligent assistant that helps a human to analyze the information in a text document.
Given a specific type of task and sample text, help the user by generating a 3 to 4 sentence description of an expert who could help solve the problem.
Use a format similar to the following:
You are an expert {{role}}. You are skilled at {{relevant skills}}. You are adept at helping people with {{specific task}}.

task: {sample_task}
persona description:"""

GENERATE_PERSONA_PROMPT_ZH = """
你是一个智能助手，帮助人类分析文本文档中的信息。
给定一个特定类型的任务和示例文本，通过生成3到4个句子描述可以帮助用户解决问题的专家。
使用类似下面的格式:
你是一个专家{{role}}。你擅长{{相关技能}}。你擅长帮助别人完成{{特定任务}}。

任务:{sample_task}
角色描述:"""
