# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

SUMMARIZE_PROMPT = """
You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

SUMMARIZE_PROMPT_ZH ='''
您是一个有用的助理，负责生成以下提供的数据的全面摘要。
给定一个或两个实体，以及一组描述，它们都与同一个实体或实体组相关。
请将所有这些连接成一个单一的、全面的描述。确保包含从所有描述中收集的信息。
如果提供的描述是矛盾的，请解决矛盾，并提供一个单一的，连贯的总结。
确保它是用第三人称写的，并包括实体名称，以便我们有完整的上下文。

# # # # # # #
拼,
实体:{entity_name}
描述列表:{description_list}
# # # # # # #
输出:
'''
