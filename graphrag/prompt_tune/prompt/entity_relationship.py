# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity relationship generation."""

ENTITY_RELATIONSHIPS_GENERATION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity, include the parenthesis at the beginning and end, as ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)
for example: ("entity"{{tuple_delimiter}}"Microsoft"{{tuple_delimiter}}"organization"{{tuple_delimiter}}"Microsoft is a technology company")

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: an integer score between 1 to 10, indicating strength of the relationship between the source entity and target entity
Format each relationship, include the parenthesis at the beginning and end, as ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)
for example: ("relationship"{{tuple_delimiter}}"company A"{{tuple_delimiter}}"person A"{{tuple_delimiter}}"company A is currently owned by person A"{{tuple_delimiter}}8)

3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{{record_delimiter}}** as the list delimiter.

4. When finished, output {{completion_delimiter}}.

-Real Data-
######################
entity_types: {entity_types}
text: {input_text}
######################
output:
"""

ENTITY_RELATIONSHIPS_GENERATION_JSON_PROMPT = """
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

-Real Data-
######################
entity_types: {entity_types}
text: {input_text}
######################
output:
"""

UNTYPED_ENTITY_RELATIONSHIPS_GENERATION_PROMPT = """
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

######################
-Examples-
######################
Text:
The Fed is scheduled to meet on Tuesday and Wednesday, with the central bank planning to release its latest policy decision on Wednesday at 2:00 p.m. ET, followed by a press conference where Fed Chair Jerome Powell will take questions. Investors expect the Federal Open Market Committee to hold its benchmark interest rate steady in a range of 5.25%-5.5%.
######################
Output:
("entity"{{tuple_delimiter}}FED{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}The Fed is the Federal Reserve, which is setting interest rates on Tuesday and Wednesday)
{{record_delimiter}}
("entity"{{tuple_delimiter}}JEROME POWELL{{tuple_delimiter}}PERSON{{tuple_delimiter}}Jerome Powell is the chair of the Federal Reserve)
{{record_delimiter}}
("entity"{{tuple_delimiter}}FEDERAL OPEN MARKET COMMITTEE{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}The Federal Reserve committee makes key decisions about interest rates and the growth of the United States money supply)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}JEROME POWELL{{tuple_delimiter}}FED{{tuple_delimiter}}Jerome Powell is the Chair of the Federal Reserve and will answer questions at a press conference{{tuple_delimiter}}9)
{{completion_delimiter}}
######################
Text:
Arm's (ARM) stock skyrocketed in its opening day on the Nasdaq Thursday. But IPO experts warn that the British chipmaker's debut on the public markets isn't indicative of how other newly listed companies may perform.

Arm, a formerly public company, was taken private by SoftBank in 2016. The well-established chip designer says it powers 99% of premium smartphones.
######################
Output:
("entity"{{tuple_delimiter}}ARM{{tuple_delimiter}}ORGANIZATION, COMPANY{{tuple_delimiter}}Arm is a stock now listed on the Nasdaq which powers 99% of premium smartphones)
{{record_delimiter}}
("entity"{{tuple_delimiter}}SOFTBANK{{tuple_delimiter}}ORGANIZATION, COMPANY{{tuple_delimiter}}SoftBank is a firm that previously owned Arm)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}ARM{{tuple_delimiter}}SOFTBANK{{tuple_delimiter}}SoftBank formerly owned Arm from 2016 until present{{tuple_delimiter}}5)
{{completion_delimiter}}
######################
-Real Data-
######################
Text: {input_text}
######################
Output:
"""


# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity relationship generation."""

ENTITY_RELATIONSHIPS_GENERATION_PROMPT_ZH = """
目标- - - - - -
给定一个可能与该活动相关的文本文档和一组实体类型，从文本中识别出这些类型的所有实体以及识别出的实体之间的所有关系。

步骤,
1. 识别所有实体。对于每个识别出的实体，提取以下信息:
—entity_name:实体名称，首字母大写
—entity_type:以下类型之一:[{entity_types}]
- entity_description:实体属性和活动的综合描述
格式化每个实体，包括在开始和结束的括号，作为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)
例如:("entity"{{tuple_delimiter}}"Microsoft"{{tuple_delimiter}}"organization"{{tuple_delimiter}}"Microsoft是一家技术公司")

2. 从步骤1中确定的实体中，找出彼此* *明显相关* *的所有对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
—source_entity:源实体的名称，在步骤1中识别
—“target_entity”:目标实体的名称，在步骤1中识别
- relationship_description:解释为什么你认为源实体和目标实体彼此相关
—relationship_strength: 1 ~ 10之间的整数分数，表示源实体和目标实体之间的关系强度
格式化每个关系，包括在开始和结束的括号，作为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)
例如:("relationship"{{tuple_delimiter}}"company A"{{tuple_delimiter}}"person A"{{tuple_delimiter}}"公司A目前属于person A"{{tuple_delimiter}}8)

3. 将英文输出作为步骤1和步骤2中确定的所有实体和关系的单个列表返回。使用**{{record_delimiter}}**作为列表分隔符。

4. 完成后，输出{{completion_delimiter}}。

无论数据-
######################
entity_types: {entity_types}
文字:{input_text}
######################
输出:
"""

ENTITY_RELATIONSHIPS_GENERATION_JSON_PROMPT_ZH = """
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

无论数据-
######################
entity_types: {entity_types}
文字:{input_text}
######################
输出:
"""

UNTYPED_ENTITY_RELATIONSHIPS_GENERATION_PROMPT_ZH = """
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

######################
的例子,
######################
文本:
美联储定于周二和周三举行会议，计划在周三美国东部时间下午2点公布最新政策决定，之后将举行新闻发布会，美联储主席鲍威尔将回答记者提问。投资者预计，联邦公开市场委员会(fomc)将维持基准利率在5.25%-5.5%的区间不变。
######################
输出:
(“entity”{{tuple_delimiter}}FED{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}美联储是美联储，它将在周二和周三设定利率)
{{record_delimiter}}
(“entity”{{tuple_delimiter}}JEROME POWELL{{tuple_delimiter}}PERSON{{tuple_delimiter}} JEROME POWELL是美联储主席)
{{record_delimiter}}
(“entity”{{tuple_delimiter}}联邦公开市场委员会(FEDERAL OPEN MARKET COMMITTEE) {{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}联邦储备委员会(FEDERAL Reserve COMMITTEE)对利率和美国货币供应量的增长做出关键决定)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}JEROME POWELL{{tuple_delimiter}}FED{{tuple_delimiter}} JEROME POWELL是美联储主席，将在新闻发布会上回答问题{{tuple_delimiter}}9)
{{completion_delimiter}}
######################
文本:
周四，Arm的股票在纳斯达克上市首日大涨。但IPO专家警告说，这家英国芯片制造商在公开市场的首次亮相并不能预示其他新上市公司的表现。

Arm曾是一家上市公司，2016年被软银(SoftBank)私有化。这家知名的芯片设计师表示，99%的高端智能手机都采用了这种芯片。
######################
输出:
(“entity”{{tuple_delimiter}}ARM{{tuple_delimiter}}组织，公司{{tuple_delimiter}}ARM是目前在纳斯达克上市的股票，它支持99%的高级智能手机)
{{record_delimiter}}
(“entity”{{tuple_delimiter}}软银{{tuple_delimiter}}组织，公司{{tuple_delimiter}}软银是一个以前拥有Arm的公司)
{{record_delimiter}}
(“relationship”{{tuple_delimiter}}ARM{{tuple_delimiter}}SOFTBANK{{tuple_delimiter}}软银从2016年起一直拥有ARM{{tuple_delimiter}} 5)
{{completion_delimiter}}
######################
无论数据-
######################
文字:{input_text}
######################
输出:
"""
