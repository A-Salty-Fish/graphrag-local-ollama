# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for community report summarization."""

COMMUNITY_REPORT_SUMMARIZATION_PROMPT = """
{persona}

# Goal
Write a comprehensive assessment report of a community taking on the role of a {role}. The content of this report includes an overview of the community's key entities, their legal compliance, technical capabilities,
reputation, and noteworthy claims.

# Report Structure
The report should include the following sections:
- TITLE: community's name that represents its key entities - title should be short but specific. When possible, include representative named entities in the title.
- SUMMARY: An executive summary of the community's overall structure, how its entities are related to each other, and significant threats associated with its entities.
- THREAT SEVERITY RATING: a float score between 0-10 that represents the potential global impact to humanity as posed by entities within the community.
- RATING EXPLANATION: Give a single sentence explanation of the threat severity rating.
- DETAILED FINDINGS: A list of 5-10 key insights about the community. Each insight should have a short summary followed by multiple paragraphs of explanatory text grounded according to the grounding rules below. Be comprehensive.

Return output as a well-formed JSON-formatted string with the following format. Don't use any unnecessary escape sequences. The output should be a single JSON object that can be parsed by json.loads.
    {{
        "title": "<report_title>",
        "summary": "<executive_summary>",
        "rating": <threat_severity_rating>,
        "rating_explanation": "<rating_explanation>"
        "findings": "[{{"summary":"<insight_1_summary>", "explanation": "<insight_1_explanation"}}, {{"summary":"<insight_2_summary>", "explanation": "<insight_2_explanation"}}]"
    }}

# Grounding Rules
After each paragraph, add data record reference if the content of the paragraph was derived from one or more data records. Reference is in the format of [records: <record_source> (<record_id_list>, ...<record_source> (<record_id_list>)]. If there are more than 10 data records, show the top 10 most relevant records.
Each paragraph should contain multiple sentences of explanation and concrete examples with specific named entities. All paragraphs must have these references at the start and end. Use "NONE" if there are no related roles or records.

Example paragraph with references added:
This is a paragraph of the output text [records: Entities (1, 2, 3), Claims (2, 5), Relationships (10, 12)]

# Example Input
-----------
Text:

Entities

id,entity,description
5,ABILA CITY PARK,Abila City Park is the location of the POK rally

Relationships

id,source,target,description
37,ABILA CITY PARK,POK RALLY,Abila City Park is the location of the POK rally
38,ABILA CITY PARK,POK,POK is holding a rally in Abila City Park
39,ABILA CITY PARK,POKRALLY,The POKRally is taking place at Abila City Park
40,ABILA CITY PARK,CENTRAL BULLETIN,Central Bulletin is reporting on the POK rally taking place in Abila City Park

Output:
{{
    "title": "Abila City Park and POK Rally",
    "summary": "The community revolves around the Abila City Park, which is the location of the POK rally. The park has relationships with POK, POKRALLY, and Central Bulletin, all
of which are associated with the rally event.",
    "rating": 5.0,
    "rating_explanation": "The impact rating is moderate due to the potential for unrest or conflict during the POK rally.",
    "findings": [
        {{
            "summary": "Abila City Park as the central location",
            "explanation": "Abila City Park is the central entity in this community, serving as the location for the POK rally. This park is the common link between all other
entities, suggesting its significance in the community. The park's association with the rally could potentially lead to issues such as public disorder or conflict, depending on the
nature of the rally and the reactions it provokes. [records: Entities (5), Relationships (37, 38, 39, 40)]"
        }},
        {{
            "summary": "POK's role in the community",
            "explanation": "POK is another key entity in this community, being the organizer of the rally at Abila City Park. The nature of POK and its rally could be a potential
source of threat, depending on their objectives and the reactions they provoke. The relationship between POK and the park is crucial in understanding the dynamics of this community.
[records: Relationships (38)]"
        }},
        {{
            "summary": "POKRALLY as a significant event",
            "explanation": "The POKRALLY is a significant event taking place at Abila City Park. This event is a key factor in the community's dynamics and could be a potential
source of threat, depending on the nature of the rally and the reactions it provokes. The relationship between the rally and the park is crucial in understanding the dynamics of this
community. [records: Relationships (39)]"
        }},
        {{
            "summary": "Role of Central Bulletin",
            "explanation": "Central Bulletin is reporting on the POK rally taking place in Abila City Park. This suggests that the event has attracted media attention, which could
amplify its impact on the community. The role of Central Bulletin could be significant in shaping public perception of the event and the entities involved. [records: Relationships
(40)]"
        }}
    ]

}}

# Real Data

Use the following text for your answer. Do not make anything up in your answer.

Text:
{{input_text}}
Output:"""



COMMUNITY_REPORT_SUMMARIZATION_PROMPT_ZH = """
{persona}

#目标
撰写一份综合评估报告，评估社区承担的角色。本报告内容包括社区主要实体的概述、它们的法律合规、技术能力、
声誉和值得注意的主张。

#报告结构
报告应包括下列各节:
-标题:代表其关键实体的社区名称-标题应简短但具体。如果可能的话，在标题中包括有代表性的命名实体。
-摘要:社区整体结构的执行摘要，其实体如何相互关联，以及与其实体相关的重大威胁。
—威胁严重等级:0-10之间的浮动分数，表示社区内实体对人类的潜在全球影响。
—评级解释:用一句话解释威胁严重性评级。
-详细的发现:关于社区的5-10个关键见解。每个观点都应该有一个简短的摘要，然后是根据下面的基本规则建立起来的多段解释性文本。是全面的。

返回格式良好的json格式字符串，格式如下。不要使用任何不必要的转义序列。输出应该是一个可以被JSON .loads解析的JSON对象。
    {{
        "title": "<report_title>",
        "summary": "<executive_summary>",
        "rating": <threat_severity_rating>,
        "rating_explanation": "<rating_explanation>"
        "findings": "[{{"summary":"<insight_1_summary>", "explanation": "<insight_1_explanation"}}, {{"summary":"<insight_2_summary>", "explanation": "<insight_2_explanation"}}]"
    }}

#基础规则
在每个段落之后，如果段落的内容来自一个或多个数据记录，则添加数据记录引用。引用的格式为[records: <record_source> (<record_id_list>，…]< record_source > (< record_id_list >)。如果有超过10条数据记录，则显示前10条最相关的记录。
每个段落应包含多句解释和具体的例子与具体的命名实体。所有段落的开头和结尾都必须有这些引用。如果没有相关的角色或记录，请使用NONE。

添加引用的示例段落:
这是输出文本的一段[records: Entities (1, 2, 3)， Claims (2, 5)， Relationships (10, 12)]
#示例输入
-----------
文本:

实体

id、实体描述
5、阿比拉城市公园，阿比拉城市公园是巴控克什米尔集会的地点

的关系

id、源、目标,描述
阿比拉城市公园，巴控克什米尔拉力赛，阿比拉城市公园是巴控克什米尔拉力赛的位置
巴控克什米尔在阿比拉城市公园举行集会
39，阿比拉城市公园，POKRALLY, POKRALLY在阿比拉城市公园举行
阿比拉城市公园，中央公报，中央公报正在报道巴控克什米尔在阿比拉城市公园的集会

输出:
{{
    "title": "阿比拉城市公园和巴控克什米尔集会",
    "summary": "社区围绕着阿比拉城市公园，这是巴控克什米尔集会的地点。公园和巴控克什米尔，巴控拉力赛，中央公报都有关系
与集会活动有关的。",
    "rating": 5.0,
    "rating_explanation": "由于巴控克什米尔集会期间可能发生动乱或冲突，影响评级适中。",
    "findings": [
        {{
            "summary": "阿比拉市公园为中心位置",
            "explanation": "阿比拉城市公园是这个社区的中心实体，是巴控克什米尔集会的地点。这个公园是连接所有其他公园的公共纽带
实体，表明其在社区中的重要性。公园与集会的联系可能会导致公共秩序混乱或冲突等问题，具体取决于
反弹的性质及其引发的反应。[记录:实体(5)，关系(37,38,39,40)]"
        }},
        {{
            "summary": "巴控克什米尔在社会中的角色",
            "explanation": "巴控克什米尔是这个社区的另一个关键实体，是阿比拉城市公园集会的组织者。巴控克什米尔的性质及其反弹可能是一种潜力
威胁的来源，取决于他们的目标和他们引起的反应。巴控克什米尔和公园之间的关系对于理解这个社区的动态至关重要。
[记录:关系(38)]"
        }},
        {{
            "summary": "POKRALLY是一个重要的事件",
            "explanation": "POKRALLY是在Abila城市公园举行的一项重要活动。这个事件是社区动态的一个关键因素，可能是一个潜力
威胁的来源，取决于反弹的性质及其引发的反应。集会和公园之间的关系对于理解这一动态至关重要
社区。[记录:关系(39)]"
        }},
        {{
            "summary": "中央公报的作用",
            "explanation": "中央公报正在报道在阿比拉城市公园举行的巴控克什米尔集会。这表明该活动已经吸引了媒体的关注，这可能
扩大对社区的影响。《中央公报》在塑造公众对这一事件和有关实体的看法方面可以发挥重要作用。【记录:人际关系
(40)]"
        }}
    ]

}}

#真实数据

使用下面的文本作为你的答案。不要在你的回答中编造任何东西。

文本:
{{input_text}}
输出:
"""
