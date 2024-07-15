# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License
"""A file containing prompts definition."""

COMMUNITY_REPORT_PROMPT = """
You are an AI assistant that helps a human analyst to perform general information discovery. Information discovery is the process of identifying and assessing relevant information associated with certain entities (e.g., organizations and individuals) within a network.

# Goal
Write a comprehensive report of a community, given a list of entities that belong to the community as well as their relationships and optional associated claims. The report will be used to inform decision-makers about information associated with the community and their potential impact. The content of this report includes an overview of the community's key entities, their legal compliance, technical capabilities, reputation, and noteworthy claims.

# Report Structure

The report should include the following sections:

- TITLE: community's name that represents its key entities - title should be short but specific. When possible, include representative named entities in the title.
- SUMMARY: An executive summary of the community's overall structure, how its entities are related to each other, and significant information associated with its entities.
- IMPACT SEVERITY RATING: a float score between 0-10 that represents the severity of IMPACT posed by entities within the community.  IMPACT is the scored importance of a community.
- RATING EXPLANATION: Give a single sentence explanation of the IMPACT severity rating.
- DETAILED FINDINGS: A list of 5-10 key insights about the community. Each insight should have a short summary followed by multiple paragraphs of explanatory text grounded according to the grounding rules below. Be comprehensive.

Return output as a well-formed JSON-formatted string with the following format:
    {{
        "title": <report_title>,
        "summary": <executive_summary>,
        "rating": <impact_severity_rating>,
        "rating_explanation": <rating_explanation>,
        "findings": [
            {{
                "summary":<insight_1_summary>,
                "explanation": <insight_1_explanation>
            }},
            {{
                "summary":<insight_2_summary>,
                "explanation": <insight_2_explanation>
            }}
        ]
    }}

# Grounding Rules

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (1), Entities (5, 7); Relationships (23); Claims (7, 2, 34, 64, 46, +more)]."

where 1, 5, 7, 23, 2, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.


# Example Input
-----------
Text:

Entities

id,entity,description
5,VERDANT OASIS PLAZA,Verdant Oasis Plaza is the location of the Unity March
6,HARMONY ASSEMBLY,Harmony Assembly is an organization that is holding a march at Verdant Oasis Plaza

Relationships

id,source,target,description
37,VERDANT OASIS PLAZA,UNITY MARCH,Verdant Oasis Plaza is the location of the Unity March
38,VERDANT OASIS PLAZA,HARMONY ASSEMBLY,Harmony Assembly is holding a march at Verdant Oasis Plaza
39,VERDANT OASIS PLAZA,UNITY MARCH,The Unity March is taking place at Verdant Oasis Plaza
40,VERDANT OASIS PLAZA,TRIBUNE SPOTLIGHT,Tribune Spotlight is reporting on the Unity march taking place at Verdant Oasis Plaza
41,VERDANT OASIS PLAZA,BAILEY ASADI,Bailey Asadi is speaking at Verdant Oasis Plaza about the march
43,HARMONY ASSEMBLY,UNITY MARCH,Harmony Assembly is organizing the Unity March

Output:
{{
    "title": "Verdant Oasis Plaza and Unity March",
    "summary": "The community revolves around the Verdant Oasis Plaza, which is the location of the Unity March. The plaza has relationships with the Harmony Assembly, Unity March, and Tribune Spotlight, all of which are associated with the march event.",
    "rating": 5.0,
    "rating_explanation": "The impact severity rating is moderate due to the potential for unrest or conflict during the Unity March.",
    "findings": [
        {{
            "summary": "Verdant Oasis Plaza as the central location",
            "explanation": "Verdant Oasis Plaza is the central entity in this community, serving as the location for the Unity March. This plaza is the common link between all other entities, suggesting its significance in the community. The plaza's association with the march could potentially lead to issues such as public disorder or conflict, depending on the nature of the march and the reactions it provokes. [Data: Entities (5), Relationships (37, 38, 39, 40, 41,+more)]"
        }},
        {{
            "summary": "Harmony Assembly's role in the community",
            "explanation": "Harmony Assembly is another key entity in this community, being the organizer of the march at Verdant Oasis Plaza. The nature of Harmony Assembly and its march could be a potential source of threat, depending on their objectives and the reactions they provoke. The relationship between Harmony Assembly and the plaza is crucial in understanding the dynamics of this community. [Data: Entities(6), Relationships (38, 43)]"
        }},
        {{
            "summary": "Unity March as a significant event",
            "explanation": "The Unity March is a significant event taking place at Verdant Oasis Plaza. This event is a key factor in the community's dynamics and could be a potential source of threat, depending on the nature of the march and the reactions it provokes. The relationship between the march and the plaza is crucial in understanding the dynamics of this community. [Data: Relationships (39)]"
        }},
        {{
            "summary": "Role of Tribune Spotlight",
            "explanation": "Tribune Spotlight is reporting on the Unity March taking place in Verdant Oasis Plaza. This suggests that the event has attracted media attention, which could amplify its impact on the community. The role of Tribune Spotlight could be significant in shaping public perception of the event and the entities involved. [Data: Relationships (40)]"
        }}
    ]
}}


# Real Data

Use the following text for your answer. Do not make anything up in your answer.

Text:
{input_text}

The report should include the following sections:

- TITLE: community's name that represents its key entities - title should be short but specific. When possible, include representative named entities in the title.
- SUMMARY: An executive summary of the community's overall structure, how its entities are related to each other, and significant information associated with its entities.
- IMPACT SEVERITY RATING: a float score between 0-10 that represents the severity of IMPACT posed by entities within the community.  IMPACT is the scored importance of a community.
- RATING EXPLANATION: Give a single sentence explanation of the IMPACT severity rating.
- DETAILED FINDINGS: A list of 5-10 key insights about the community. Each insight should have a short summary followed by multiple paragraphs of explanatory text grounded according to the grounding rules below. Be comprehensive.

Return output as a well-formed JSON-formatted string with the following format:
    {{
        "title": <report_title>,
        "summary": <executive_summary>,
        "rating": <impact_severity_rating>,
        "rating_explanation": <rating_explanation>,
        "findings": [
            {{
                "summary":<insight_1_summary>,
                "explanation": <insight_1_explanation>
            }},
            {{
                "summary":<insight_2_summary>,
                "explanation": <insight_2_explanation>
            }}
        ]
    }}

# Grounding Rules

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (1), Entities (5, 7); Relationships (23); Claims (7, 2, 34, 64, 46, +more)]."

where 1, 5, 7, 23, 2, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.

Output:"""


COMMUNITY_REPORT_PROMPT_ZH = """
你是一个人工智能助手，帮助人类分析师执行一般信息发现。信息发现是识别和评估网络中与某些实体(例如，组织和个人)相关的信息的过程。

#目标
写一份关于社区的全面报告，列出属于社区的实体以及它们的关系和可选的相关声明。该报告将用于向决策者提供与社区有关的信息及其潜在影响。本报告内容包括社区主要实体的概述，它们的法律合规性、技术能力、声誉和值得注意的声明。

#报告结构

报告应包括下列各节:

-标题:代表其关键实体的社区名称-标题应简短但具体。如果可能的话，在标题中包括有代表性的命名实体。
-概要:社区的整体结构、实体之间的关系以及与实体相关的重要信息的概要。
—影响严重等级:0-10之间的浮动分数，表示社区内实体的影响严重程度。影响力是一个社区的重要性得分。
—评级解释:用一句话解释影响严重性评级。
-详细的发现:关于社区的5-10个关键见解。每个观点都应该有一个简短的摘要，然后是根据下面的基本规则建立起来的多段解释性文本。是全面的。

返回一个格式良好的json字符串，格式如下:
    {{
        "title": <report_title>,
        "summary": <executive_summary>,
        "rating": <impact_severity_rating>,
        "rating_explanation": <rating_explanation>,
        "findings": [
            {{
                "summary":<insight_1_summary>,
                "explanation": <insight_1_explanation>
            }},
            {{
                "summary":<insight_2_summary>,
                "explanation": <insight_2_explanation>
            }}
        ]
    }}

#基础规则

由数据支持的点应列出其数据来源如下:

“这是一个由多个数据引用支持的示例句子[数据:<数据集名称>(记录ids);<数据集名称>(记录id)] "

不要在单个引用中列出超过5个记录id。相反，列出前5个最相关的记录id，并添加“+more”表示还有更多。

例如:
“X是Y公司的所有者，受到许多不当行为的指控[数据:报告(1)，实体(5,7);关系(23);声明(7、2、34、64、46 +)]。”

其中1、5、7、23、2、34、46和64表示相关数据记录的id(不是索引)。

如果没有提供支持的证据，请不要包含这些信息。

#示例输入
-----------
文本:

实体

id、实体描述
5、青翠绿洲广场，青翠绿洲广场是统一进行曲的位置
6、“和谐集会”是一个在绿洲广场举行游行的组织

关系

id、源、目标,描述
37、青翠绿洲广场，统一游行，青翠绿洲广场是统一游行的地点
38、绿洲绿洲广场，和谐集会，和谐集会在绿洲绿洲广场举行游行
39、绿洲绿洲广场，统一游行，统一游行正在绿洲绿洲广场举行
40、青翠绿洲广场，论坛聚焦，论坛聚焦正在报道在青翠绿洲广场发生的团结游行
41，青绿洲广场，贝利·阿萨迪，贝利·阿萨迪在青绿洲广场就游行发表讲话
43、和谐集会，团结游行，和谐集会正在组织团结游行

输出:
{{
    "title": "青翠绿洲广场和团结游行",
    "summary": "社区围绕着青翠的绿洲广场，这是团结游行的地点。广场与和谐集会、团结游行、聚焦论坛都有关系，所有这些都与游行活动有关。”",
    "rating": 5.0,
    "rating_explanation": "由于在统一游行期间可能发生动乱或冲突，影响严重性评级为中度。",
    "findings": [
        {{
            "summary": "以绿洲广场为中心位置",
            "explanation": "青翠绿洲广场是这个社区的中心实体，是团结游行的地点。这个广场是连接所有其他实体的共同纽带，体现了它在社区中的意义。广场与游行的联系可能会导致公共秩序混乱或冲突等问题，这取决于游行的性质及其引发的反应。[数据:实体(5)，关系(37,38,39,40,41 +)]"
        }},
        {{
            "summary": "和谐大会在社区中的作用",
            "explanation": "和谐集会是这个社区的另一个关键实体，是在青翠绿洲广场游行的组织者。“和谐集会”及其游行的性质可能是一个潜在的威胁来源，这取决于他们的目标和他们引起的反应。和谐集会和广场之间的关系对于理解这个社区的动态至关重要。[数据:实体(6)，关系(38,43)]"
}},
        {{
            "summary": "团结进行曲是重大事件",
            "explanation": "团结大游行是在绿洲广场举行的一项重要活动。这一事件是社区动态的一个关键因素，也可能是一个潜在的威胁来源，取决于游行的性质和它引起的反应。游行和广场之间的关系对于理解这个社区的动态至关重要。[数据:关系(39)]"
        }},
        {{
            "summary": "聚焦论坛的角色",
            "explanation": "聚焦论坛报道了在青翠的绿洲广场发生的团结游行。这表明，该活动吸引了媒体的关注，这可能会扩大其对社区的影响。《聚焦论坛》在塑造公众对事件和相关实体的看法方面发挥了重要作用。[数据:关系(40)]"
        }}
    ]
}}

#真实数据

使用下面的文本作为你的答案。不要在你的回答中编造任何东西。

文本:
{input_text}

报告应包括下列各节:

-标题:代表其关键实体的社区名称-标题应简短但具体。如果可能的话，在标题中包括有代表性的命名实体。
-概要:社区的整体结构、实体之间的关系以及与实体相关的重要信息的概要。
—影响严重等级:0-10之间的浮动分数，表示社区内实体的影响严重程度。影响力是一个社区的重要性得分。
—评级解释:用一句话解释影响严重性评级。
-详细的发现:关于社区的5-10个关键见解。每个观点都应该有一个简短的摘要，然后是根据下面的基本规则建立起来的多段解释性文本。是全面的。

返回一个格式良好的json字符串，格式如下:
    {{
        "title": <report_title>,
        "summary": <executive_summary>,
        "rating": <impact_severity_rating>,
        "rating_explanation": <rating_explanation>,
        "findings": [
            {{
                "summary":<insight_1_summary>,
                "explanation": <insight_1_explanation>
            }},
            {{
                "summary":<insight_2_summary>,
                "explanation": <insight_2_explanation>
            }}
        ]
    }}

#基础规则

由数据支持的点应列出其数据来源如下:

“这是一个由多个数据引用支持的示例句子[数据:<数据集名称>(记录ids);<数据集名称>(记录id)] "

不要在单个引用中列出超过5个记录id。相反，列出前5个最相关的记录id，并添加“+more”表示还有更多。

例如:
“X是Y公司的所有者，受到许多不当行为的指控[数据:报告(1)，实体(5,7);关系(23);声明(7、2、34、64、46 +)]。”

其中1、5、7、23、2、34、46和64表示相关数据记录的id(不是索引)。

如果没有提供支持的证据，请不要包含这些信息。

输出:"""