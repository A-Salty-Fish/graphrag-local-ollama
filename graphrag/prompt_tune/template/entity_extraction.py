# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity extraction."""

GRAPH_EXTRACTION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: an integer score between 1 to 10, indicating strength of the relationship between the source entity and target entity

Format each relationship as ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{{record_delimiter}}** as the list delimiter.

4. When finished, output {{completion_delimiter}}

-Examples-
######################
{examples}

-Real Data-
######################
entity_types: [{entity_types}]
text: {{input_text}}
######################
output:"""

GRAPH_EXTRACTION_JSON_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity output as a JSON entry with the following format:

{{"name": <entity name>, "type": <type>, "description": <entity description>}}

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: an integer score between 1 to 10, indicating strength of the relationship between the source entity and target entity
Format each relationship as a JSON entry with the following format:

{{"source": <source_entity>, "target": <target_entity>, "relationship": <relationship_description>, "relationship_strength": <relationship_strength>}}

3. Return output in English as a single list of all JSON entities and relationships identified in steps 1 and 2.

-Examples-
######################
{examples}

-Real Data-
######################
entity_types: {entity_types}
text: {{input_text}}
######################
output:"""

EXAMPLE_EXTRACTION_TEMPLATE = """
Example {n}:

entity_types: [{entity_types}]
text:
{input_text}
------------------------
output:
{output}
#############################

"""

UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE = """
Example {n}:

text:
{input_text}
------------------------
output:
{output}
#############################

"""


UNTYPED_GRAPH_EXTRACTION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity, first identify all entities needed from the text in order to capture the information and ideas in the text.
Next, report all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: Suggest several labels or categories for the entity. The categories should not be specific, but should be as general as possible.
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
 Format each relationship as ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{{record_delimiter}}** as the list delimiter.

4. When finished, output {{completion_delimiter}}

-Examples-
######################
{examples}

-Real Data-
######################
text: {{input_text}}
######################
output:
"""


GRAPH_EXTRACTION_PROMPT_ZH = """
目标- - - - - -
给定一个可能与该活动相关的文本文档和一组实体类型，从文本中识别出这些类型的所有实体以及识别出的实体之间的所有关系。

步骤,
1. 识别所有实体。对于每个识别出的实体，提取以下信息:
—entity_name:实体名称，首字母大写
—entity_type:以下类型之一:[{entity_types}]
- entity_description:实体属性和活动的综合描述
将每个实体格式化为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

2. 从步骤1中确定的实体中，找出彼此* *明显相关* *的所有对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
—source_entity:源实体的名称，在步骤1中识别
—“target_entity”:目标实体的名称，在步骤1中识别
- relationship_description:解释为什么你认为源实体和目标实体彼此相关
—relationship_strength: 1 ~ 10之间的整数分数，表示源实体和目标实体之间的关系强度

将每个关系格式化为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 将英文输出作为步骤1和步骤2中确定的所有实体和关系的单个列表返回。使用**{{record_delimiter}}**作为列表分隔符。

4. 完成时，输出{{completion_delimiter}}

的例子,
######################
{例子}

无论数据-
######################
entity_types ({entity_types}):
文字:{{input_text}}
######################
输出:"""

GRAPH_EXTRACTION_JSON_PROMPT_ZH = """
目标- - - - - -
给定一个可能与该活动相关的文本文档和一组实体类型，从文本中识别出这些类型的所有实体以及识别出的实体之间的所有关系。

步骤,
1. 识别所有实体。对于每个识别出的实体，提取以下信息:
—entity_name:实体名称，首字母大写
—entity_type:以下类型之一:[{entity_types}]
- entity_description:实体属性和活动的综合描述
使用以下格式将每个实体输出格式化为JSON条目:

{{"name": <实体名称>，"type": <类型>，"description": <实体描述>}}

2. 从步骤1中确定的实体中，找出彼此* *明显相关* *的所有对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
—source_entity:源实体的名称，在步骤1中识别
—“target_entity”:目标实体的名称，在步骤1中识别
- relationship_description:解释为什么你认为源实体和目标实体彼此相关
—relationship_strength: 1 ~ 10之间的整数分数，表示源实体和目标实体之间的关系强度
使用以下格式将每个关系格式化为JSON条目:

{{"source": <source_entity>， "target": <target_entity>， "relationship": <relationship_description>， "relationship_strength": <relationship_strength>}}

3. 返回英文输出，作为步骤1和步骤2中确定的所有JSON实体和关系的单个列表。

的例子,
######################
{例子}

无论数据-
######################
entity_types: {entity_types}
文字:{{input_text}}
######################
输出:

"""

EXAMPLE_EXTRACTION_TEMPLATE_ZH = """
entity_types ({entity_types}):
文本:
{input_text}
------------------------
输出:
{输出}
#############################
"""

UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE_ZH = """
Example {n}:

文本:
{input_text}
------------------------
输出:
{output}
#############################

"""


UNTYPED_GRAPH_EXTRACTION_PROMPT_ZH = """
目标- - - - - -
给定一个可能与该活动相关的文本文档，首先确定文本中所需的所有实体，以便捕获文本中的信息和想法。
接下来，报告已识别实体之间的所有关系。

步骤,
1. 识别所有实体。对于每个识别出的实体，提取以下信息:
—entity_name:实体名称，首字母大写
- entity_type:为实体建议几个标签或类别。类别不应具体，而应尽可能一般。
- entity_description:实体属性和活动的综合描述
将每个实体格式化为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

2. 从步骤1中确定的实体中，找出彼此* *明显相关* *的所有对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
—source_entity:源实体的名称，在步骤1中识别
—“target_entity”:目标实体的名称，在步骤1中识别
- relationship_description:解释为什么你认为源实体和目标实体彼此相关
- relationship_strength:一个数值分数，表示源实体和目标实体之间关系的强度
将每个关系格式化为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 将英文输出作为步骤1和步骤2中确定的所有实体和关系的单个列表返回。使用**{{record_delimiter}}**作为列表分隔符。

4. 完成时，输出{{completion_delimiter}}

的例子,
######################
{例子}

无论数据-
######################
文字:{{input_text}}
######################
输出:
"""
