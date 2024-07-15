# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity types generation."""

ENTITY_TYPE_GENERATION_PROMPT = """
The goal is to study the connections and relations between the entity types and their features in order to understand all available information from the text.
The user's task is to {task}.
As part of the analysis, you want to identify the entity types present in the following text.
The entity types must be relevant to the user task.
Avoid general entity types such as "other" or "unknown".
This is VERY IMPORTANT: Do not generate redundant or overlapping entity types. For example, if the text contains "company" and "organization" entity types, you should return only one of them.
Don't worry about quantity, always choose quality over quantity. And make sure EVERYTHING in your answer is relevant to the context of entity extraction.
And remember, it is ENTITY TYPES what we need.
Return the entity types in as a list of comma sepparated of strings.
=====================================================================
EXAMPLE SECTION: The following section includes example output. These examples **must be excluded from your answer**.

EXAMPLE 1
Task: Determine the connections and organizational hierarchy within the specified community.
Text: Example_Org_A is a company in Sweden. Example_Org_A's director is Example_Individual_B.
RESPONSE:
organization, person
END OF EXAMPLE 1

EXAMPLE 2
Task: Identify the key concepts, principles, and arguments shared among different philosophical schools of thought, and trace the historical or ideological influences they have on each other.
Text: Rationalism, epitomized by thinkers such as René Descartes, holds that reason is the primary source of knowledge. Key concepts within this school include the emphasis on the deductive method of reasoning.
RESPONSE:
concept, person, school of thought
END OF EXAMPLE 2

EXAMPLE 3
Task: Identify the full range of basic forces, factors, and trends that would indirectly shape an issue.
Text: Industry leaders such as Panasonic are vying for supremacy in the battery production sector. They are investing heavily in research and development and are exploring new technologies to gain a competitive edge.
RESPONSE:
organization, technology, sectors, investment strategies
END OF EXAMPLE 3
======================================================================

======================================================================
REAL DATA: The following section is the real data. You should use only this real data to prepare your answer. Generate Entity Types only.
Task: {task}
Text: {input_text}
RESPONSE:
{{<entity_types>}}
"""

ENTITY_TYPE_GENERATION_JSON_PROMPT = """
The goal is to study the connections and relations between the entity types and their features in order to understand all available information from the text.
The user's task is to {task}.
As part of the analysis, you want to identify the entity types present in the following text.
The entity types must be relevant to the user task.
Avoid general entity types such as "other" or "unknown".
This is VERY IMPORTANT: Do not generate redundant or overlapping entity types. For example, if the text contains "company" and "organization" entity types, you should return only one of them.
Don't worry about quantity, always choose quality over quantity. And make sure EVERYTHING in your answer is relevant to the context of entity extraction.
Return the entity types in JSON format with "entities" as the key and the entity types as an array of strings.
=====================================================================
EXAMPLE SECTION: The following section includes example output. These examples **must be excluded from your answer**.

EXAMPLE 1
Task: Determine the connections and organizational hierarchy within the specified community.
Text: Example_Org_A is a company in Sweden. Example_Org_A's director is Example_Individual_B.
JSON RESPONSE:
{{"entity_types": [organization, person] }}
END OF EXAMPLE 1

EXAMPLE 2
Task: Identify the key concepts, principles, and arguments shared among different philosophical schools of thought, and trace the historical or ideological influences they have on each other.
Text: Rationalism, epitomized by thinkers such as René Descartes, holds that reason is the primary source of knowledge. Key concepts within this school include the emphasis on the deductive method of reasoning.
JSON RESPONSE:
{{"entity_types": [concept, person, school of thought] }}
END OF EXAMPLE 2

EXAMPLE 3
Task: Identify the full range of basic forces, factors, and trends that would indirectly shape an issue.
Text: Industry leaders such as Panasonic are vying for supremacy in the battery production sector. They are investing heavily in research and development and are exploring new technologies to gain a competitive edge.
JSON RESPONSE:
{{"entity_types": [organization, technology, sectors, investment strategies] }}
END OF EXAMPLE 3
======================================================================

======================================================================
REAL DATA: The following section is the real data. You should use only this real data to prepare your answer. Generate Entity Types only.
Task: {task}
Text: {input_text}
JSON response:
{{"entity_types": [<entity_types>] }}
"""

ENTITY_TYPE_GENERATION_PROMPT_ZH = """
目标是研究实体类型及其特征之间的联系和关系，以便理解文本中所有可用的信息。
用户的任务指向{task}。
作为分析的一部分，您需要识别以下文本中出现的实体类型。
实体类型必须与用户任务相关。
避免使用一般的实体类型，如“其他”或“未知”。
这非常重要:不要生成冗余或重叠的实体类型。例如，如果文本包含"company"和"organization"实体类型，则应该只返回其中一个。
不要担心数量，总是选择质量而不是数量。并确保你的答案中的所有内容都与实体提取的上下文相关。
记住，我们需要的是实体类型。
以逗号分隔的字符串列表的形式返回实体类型。
=====================================================================
示例部分:以下部分包括示例输出。这些例子**必须从你的答案中排除**。

示例1
任务:确定指定社区内的联系和组织层次结构。
Example_Org_A是瑞典的一家公司。Example_Org_A的主管是Example_Individual_B。
回应:
组织的人
例1结束

示例2
任务:识别不同哲学思想流派之间共享的关键概念、原则和论点，并追踪它们彼此之间的历史或思想影响。
以René笛卡儿等思想家为代表的理性主义认为，理性是知识的主要来源。这个学派的主要概念包括强调推理的演绎方法。
回应:
概念，人，思想流派
例2结束

示例3
任务:确定间接影响问题的所有基本力量、因素和趋势。
松下(Panasonic)等行业领袖正在争夺电池生产领域的霸主地位。它们在研发方面投入巨资，并在探索新技术以获得竞争优势。
回应:
组织、技术、部门、投资策略
例3结束
======================================================================

======================================================================
真实数据:以下部分为真实数据。你应该只使用这些真实数据来准备你的答案。只生成实体类型。
任务:{任务}
文字:{input_text}
回应:
{{< entity_types >}}
"""

ENTITY_TYPE_GENERATION_JSON_PROMPT_ZH = """
目标是研究实体类型及其特征之间的联系和关系，以便理解文本中所有可用的信息。
用户的任务指向{task}。
作为分析的一部分，您需要识别以下文本中出现的实体类型。
实体类型必须与用户任务相关。
避免使用一般的实体类型，如“其他”或“未知”。
这非常重要:不要生成冗余或重叠的实体类型。例如，如果文本包含"company"和"organization"实体类型，则应该只返回其中一个。
不要担心数量，总是选择质量而不是数量。并确保你的答案中的所有内容都与实体提取的上下文相关。
返回JSON格式的实体类型，以“entities”为键，实体类型为字符串数组。
=====================================================================
示例部分:以下部分包括示例输出。这些例子**必须从你的答案中排除**。

示例1
任务:确定指定社区内的联系和组织层次结构。
Example_Org_A是瑞典的一家公司。Example_Org_A的主管是Example_Individual_B。
JSON响应:
{{"entity_types":[组织，人]}}
例1结束

示例2
任务:识别不同哲学思想流派之间共享的关键概念、原则和论点，并追踪它们彼此之间的历史或思想影响。
以René笛卡儿等思想家为代表的理性主义认为，理性是知识的主要来源。这个学派的主要概念包括强调推理的演绎方法。
JSON响应:
{{"entity_types":[概念，人，学派]}}
例2结束

示例3
任务:确定间接影响问题的所有基本力量、因素和趋势。
松下(Panasonic)等行业领袖正在争夺电池生产领域的霸主地位。它们在研发方面投入巨资，并在探索新技术以获得竞争优势。
JSON响应:
{{"entity_types":[组织，技术，部门，投资策略]}}
例3结束
======================================================================

======================================================================
真实数据:以下部分为真实数据。你应该只使用这些真实数据来准备你的答案。只生成实体类型。
任务:{任务}
文字:{input_text}
JSON响应:
{{"entity_types": [<entity_types>]}}
"""
