# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

CLAIM_EXTRACTION_PROMPT = """
-Target activity-
You are an intelligent assistant that helps a human analyst to analyze claims against certain entities presented in a text document.

-Goal-
Given a text document that is potentially relevant to this activity, an entity specification, and a claim description, extract all entities that match the entity specification and all claims against those entities.

-Steps-
1. Extract all named entities that match the predefined entity specification. Entity specification can either be a list of entity names or a list of entity types.
2. For each entity identified in step 1, extract all claims associated with the entity. Claims need to match the specified claim description, and the entity should be the subject of the claim.
For each claim, extract the following information:
- Subject: name of the entity that is subject of the claim, capitalized. The subject entity is one that committed the action described in the claim. Subject needs to be one of the named entities identified in step 1.
- Object: name of the entity that is object of the claim, capitalized. The object entity is one that either reports/handles or is affected by the action described in the claim. If object entity is unknown, use **NONE**.
- Claim Type: overall category of the claim, capitalized. Name it in a way that can be repeated across multiple text inputs, so that similar claims share the same claim type
- Claim Status: **TRUE**, **FALSE**, or **SUSPECTED**. TRUE means the claim is confirmed, FALSE means the claim is found to be False, SUSPECTED means the claim is not verified.
- Claim Description: Detailed description explaining the reasoning behind the claim, together with all the related evidence and references.
- Claim Date: Period (start_date, end_date) when the claim was made. Both start_date and end_date should be in ISO-8601 format. If the claim was made on a single date rather than a date range, set the same date for both start_date and end_date. If date is unknown, return **NONE**.
- Claim Source Text: List of **all** quotes from the original text that are relevant to the claim.

Format each claim as (<subject_entity>{tuple_delimiter}<object_entity>{tuple_delimiter}<claim_type>{tuple_delimiter}<claim_status>{tuple_delimiter}<claim_start_date>{tuple_delimiter}<claim_end_date>{tuple_delimiter}<claim_description>{tuple_delimiter}<claim_source>)

3. Return output in English as a single list of all the claims identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

4. When finished, output {completion_delimiter}

-Examples-
Example 1:
Entity specification: organization
Claim description: red flags associated with an entity
Text: According to an article on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B. The company is owned by Person C who was suspected of engaging in corruption activities in 2015.
Output:

(COMPANY A{tuple_delimiter}GOVERNMENT AGENCY B{tuple_delimiter}ANTI-COMPETITIVE PRACTICES{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}Company A was found to engage in anti-competitive practices because it was fined for bid rigging in multiple public tenders published by Government Agency B according to an article published on 2022/01/10{tuple_delimiter}According to an article published on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B.)
{completion_delimiter}

Example 2:
Entity specification: Company A, Person C
Claim description: red flags associated with an entity
Text: According to an article on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B. The company is owned by Person C who was suspected of engaging in corruption activities in 2015.
Output:

(COMPANY A{tuple_delimiter}GOVERNMENT AGENCY B{tuple_delimiter}ANTI-COMPETITIVE PRACTICES{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}Company A was found to engage in anti-competitive practices because it was fined for bid rigging in multiple public tenders published by Government Agency B according to an article published on 2022/01/10{tuple_delimiter}According to an article published on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B.)
{record_delimiter}
(PERSON C{tuple_delimiter}NONE{tuple_delimiter}CORRUPTION{tuple_delimiter}SUSPECTED{tuple_delimiter}2015-01-01T00:00:00{tuple_delimiter}2015-12-30T00:00:00{tuple_delimiter}Person C was suspected of engaging in corruption activities in 2015{tuple_delimiter}The company is owned by Person C who was suspected of engaging in corruption activities in 2015)
{completion_delimiter}

-Real Data-
Use the following input for your answer.
Entity specification: {entity_specs}
Claim description: {claim_description}
Text: {input_text}
Output:"""


CONTINUE_PROMPT = "MANY entities were missed in the last extraction.  Add them below using the same format:\n"
LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES {tuple_delimiter} NO if there are still entities that need to be added.\n"


CLAIM_EXTRACTION_PROMPT_ZH = '''
-----目标活动-----
您是一个智能助手，可以帮助人类分析师分析针对文本文档中出现的某些实体的声明。

----目标----
给定与此活动潜在相关的文本文档、实体规范和声明描述，提取与实体规范匹配的所有实体以及针对这些实体的所有声明。

----步骤----,
1. 抽取与预定义实体规范匹配的所有命名实体。实体说明可以是实体名称的列表，也可以是实体类型的列表。
2. 对于步骤1中识别的每个实体，提取与该实体关联的所有声明。声明需要与指定的声明描述匹配，并且实体应该是声明的主题。
对于每个声明，提取以下信息:
-主体:声明主体的实体名称，大写。主体实体是指执行请求中描述的行为的实体。Subject需要是步骤1中标识的命名实体之一。
-对象:作为声明对象的实体名称，大写。对象实体是一个报告/处理或受声明中描述的操作影响的实体。如果对象实体是未知的，使用**NONE**。
-声明类型:声明的总体类别，大写。以一种可以在多个文本输入中重复的方式命名它，以便相似的声明共享相同的声明类型
声明状态:**TRUE**, **FALSE**, or **SUSPECTED**。TRUE意味着主张被证实，FALSE意味着主张被发现是错误的，suspect意味着主张没有被证实。
-声明说明:对声明原因的详细说明，以及所有相关的证据和参考文献。
-声明日期:声明发生的时间(起始日期，结束日期)。开始日期和结束日期都应该是ISO-8601格式。如果声明是针对单个日期而不是日期范围，则为start_date和end_date设置相同的日期。如果date未知，则返回**NONE**。
-声明源文本:原始文本中与声明相关的**所有**引用的列表。

将每个权利要求格式为(<subject_entity>{tuple_delimiter}<object_entity>{tuple_delimiter}<claim_type>{tuple_delimiter}<claim_status>{tuple_delimiter}<claim_start_date>{tuple_delimiter}<claim_end_date>{tuple_delimiter}<claim_description>{tuple_delimiter}<claim_source>)

3. 返回英文输出，作为步骤1和步骤2中确定的所有声明的单个列表。使用**{record_delimiter}**作为列表分隔符。

4. 完成时，输出{completion_delimiter}

----例子----,
示例1:
实体规范:组织
声明说明:与实体相关联的标志
根据2022/01/10的一篇文章，A公司在参与政府机构b公布的多次公开招标时，因串通投标而被罚款。该公司的所有者是在2015年涉嫌从事腐败活动的人C。
输出:根据2022/01/10发表的一篇文章{tuple_delimiter}， A公司被发现从事反竞争行为，因为它在政府机构B发布的多个公开招标中串谋投标被罚款。A公司多次参与政府机构b公布的公开招标，因串通投标被罚款。)
{completion_delimiter}

示例2:
实体规范:A公司，C人
声明说明:与实体相关联的标志
根据2022/01/10的一篇文章，A公司在参与政府机构b公布的多次公开招标时，因串通投标而被罚款。该公司的所有者是在2015年涉嫌从事腐败活动的人C。
输出:

根据2022/01/10发表的一篇文章{tuple_delimiter}， A公司被发现从事反竞争行为，因为它在政府机构B发布的多个公开招标中串谋投标被罚款。A公司多次参与政府机构b公布的公开招标，因串通投标被罚款。)
{record_delimiter}
(PERSON C{tuple_delimiter}NONE{tuple_delimiter}CORRUPTION{tuple_delimiter} suspect {tuple_delimiter}2015-01-01T00:00:00{tuple_delimiter}2015-12-30T00:00:00{tuple_delimiter} PERSON C涉嫌在2015年从事腐败活动{tuple_delimiter}该公司为涉嫌在2015年从事腐败活动的人C所有)
{completion_delimiter}

--真实数据--
使用下面的输入作为你的答案。
实体规范:{entity_specs}
声明描述:{claim_description}
文字:{input_text}
输出:
'''

CONTINUE_PROMPT_ZH = "许多实体在最后一次提取中被遗漏了。使用相同的格式在下面添加它们:\n"
LOOP_PROMPT_ZH = "似乎仍有一些实体被遗漏了。如果仍然有需要添加的实体，请回答YES {tuple_delimiter}，如果没有，请回答NO\n"

