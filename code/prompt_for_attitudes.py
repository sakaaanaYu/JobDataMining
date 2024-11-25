import pandas as pd
import json

opinion = [
  {
    "id": "journalism-favors-new-media-jobs",
    "content": "新闻专业学生更容易找到新媒体相关岗位和内容创作类岗位的工作"
  },
  {
    "id": "tier-1-cities-offer-more-jobs",
    "content": "一线城市的就业机会更多"
  },
  {
    "id": "experience-matters-significantly",
    "content": "工作经验对于新闻专业学生的就业来说很重要"
  },
  {
    "id": "education-level-matters-little",
    "content": "个人学历对于新闻专业学生的就业来说不重要"
  },
  {
    "id": "low-education-can-earn-high",
    "content": "低学历者也能获得高薪"
  },
  {
    "id": "higher-education-earns-more",
    "content": "学历越高，赚的钱越多"
  },
  {
    "id": "more-experience-earns-more",
    "content": "工作经验越多，赚的钱越多"
  },
  {
    "id": "pm-marketing-roles-pay-better",
    "content": "产品经理、市场营销、新媒体运营等岗位更赚钱"
  },
  {
    "id": "tech-skills-earn-more",
    "content": "掌握媒体运营、视觉设计、数据处理、内容策略等技能更赚钱"
  },
  {
    "id": "soft-skills-earn-more",
    "content": "具备组织技能、交际能力、个人素养、市场管理等技能更赚钱"
  }
]


SYSTEM_PROMPT = f'''
# 观点分析师
## 任务
新闻传播专业就业前景观点分析

## 背景：
在互联网上，用户围绕着某一问题作出的讨论可以被总结和分割为若干不同的观点。正确地将用户讨论的文本信息与这些观点对应对于分析公众对于某一话题的想法至关重要。本任务聚焦于“新闻传播专业就业前景”这一话题，旨在将用户评论文本与预设的观点进行匹配，分析用户在评论中表达的内容是否支持/反对预设观点，或是对预设观点没有提及。

## 你的角色
你是一位观点分析专家，专长于将社交媒体用户的评论内容归类并对应到相应的观点中。你将基于被提供的文本信息，将其与以下关于新闻传播专业就业前景的预设观点进行匹配。

## 任务目标
1. 阅读理解：仔细阅读理解被提供的文本内容。
2. 观点匹配：分析文本内容是否提及了所给出的预设观点，如果提及，分析文本内容对该观点持“同意”还是“不同意”的态度。

## 预设观点
```json
{json.dumps(opinion, ensure_ascii=False, indent=2)}
```
'''.strip()


res = []

df = pd.read_csv("attitudes_zhihu_with_id.xlsx")
for index, row in df.iterrows():
    id_value = row['id']
    job_desc = row['content']

    json_line_content = {
        "custom_id": id_value,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "messages": [{
                "role": "system",
                "content": SYSTEM_PROMPT
            }, {
                "role": "user",
                "content": job_desc
            }],
            "model": "gpt-4o",
            "seed": 10370,
            "temperature": 0,
            "stream": False,
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "opinion_analysis",
                    "description": "Opinion analysis for journalism students' employment prospects.",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "agree": {
                                "type": "array",
                                "description": "Opinions that the user agrees with.",
                                "items": {
                                    "type": "string",
                                    "additionalProperties": False,
                                    "enum": [op['id'] for op in opinion]
                                }
                            },
                            "disagree": {
                                "type": "array",
                                "description": "Opinions that the user disagrees with.",
                                "items": {
                                    "type": "string",
                                    "additionalProperties": False,
                                    "enum": [op['id'] for op in opinion]
                                }
                            },
                            "neutral": {
                                "type": "array",
                                "description": "Opinions that the user doesn't mention.",
                                "items": {
                                    "type": "string",
                                    "additionalProperties": False,
                                    "enum": [op['id'] for op in opinion]
                                }
                            }
                        },
                        "required": ["agree", "disagree", "neutral"]
                    }
                }
            }
        }
    }

    res.append(json_line_content)