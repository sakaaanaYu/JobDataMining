import pandas as pd
import json


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
            # "model": "gpt-4o-mini",
            "model": "gpt-4o",
            "seed": 10370,
            "temperature": 0,
            "stream": False,
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "differentOpinions",
                    "description": "A response format that includes several concluded opinions.",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "opinion1": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that journalism students are more likely to find jobs in new media-related positions and content creation positions.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that journalism students are more likely to find jobs in new media-related positions and content creation positions.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion2": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that there are more job opportunities in big or first-tier cities.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that there are more job opportunities in big or first-tier cities.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion3": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that work experience is important for the employment of journalism students.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that work experience is important for the employment of journalism students.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion4": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that eduation degree is not important for the employment of journalism students.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that eduation degree is not important for the employment of journalism students.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion5": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that people with lower degree can also gain high salaries.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that people with lower degree can also gain high salaries..",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion6": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that the higher education degree, the higher salaries.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that the higher education degree, the higher salaries.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion7": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that the more work experiences, the higher salaries.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that the more work experiences, the higher salaries.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion8": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that jobs like product manager, marketing and digital marketing provide higer salaries.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that jobs like product manager, marketing and digital marketing provide higer salaries.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion9": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that mastering skills like media operations, visual design, data processing, and content strategy can gain a higher salary.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that mastering skills like media operations, visual design, data processing, and content strategy can gain a higher salary.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },

                            "opinion10": {
                                "anyOf": [{
                                        "type": "string",
                                        "description": "Agree that mastering skills like organization, social, personal qualities, and market management can gain a higher salary.",
                                        "enum": ['1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "Disagree that mastering skills like organization, social, personal qualities, and market management can gain a higher salary.",
                                        "enum": ['-1']
                                    },
                                    {
                                        "type": "string",
                                        "description": "No matching opinion found.",
                                        "enum": ["0"]
                                    }
                                ]
                            },
                        },
                        "required": ["opinion1", "opinion2", "opinion3", "opinion4", "opinion5", "opinion6", "opinion7", "opinion8", "opinion9", "opinion10"]
                    }
                }
            }
        }
    }

    res.append(json_line_content)


SYSTEM_PROMPT = '''
# 观点分析师

## 任务

新闻传播专业就业前景观点分析

## 背景：

在互联网上，用户围绕着某一问题作出的讨论可以被总结和分割为若干不同的观点。正确地将用户讨论的文本信息与这些观点对应对于分析公众对于某一话题的想法至关重要。本任务聚焦于“新闻传播专业就业前景”这一话题，旨在将用户评论文本与预设的观点进行匹配，分析用户在评论中表达的内容是否支持/反对预设观点，或是对预设观点没有提及。

## 你的角色

你是一位观点分析专家，专长于将社交媒体用户的评论内容归类并对应到相应的观点中。你将基于被提供的文本信息，将其与以下关于新闻传播专业就业前景的预设观点进行匹配。

## 任务目标

1. 阅读理解：仔细阅读理解被提供的文本内容。
2. 观点匹配：分析文本内容是否提及了所给出的预设观点，如果提及，分析文本内容对该观点持”同意“还是”不同意“的态度。

## 预设观点

1. 新闻专业学生更容易找到新媒体相关岗位和内容创作类岗位的工作

2. 一线城市的就业机会更多

3. 工作经验对于新闻专业学生的就业来说很重要

4. 个人学历对于新闻专业学生的就业来说不重要

5. 低学历者也能获得高薪

6. 学历越高，赚的钱越多

7. 工作经验越多，赚的钱越多

8. 产品经理、市场营销、新媒体运营等岗位更赚钱

9. 掌握媒体运营、视觉设计、数据处理、内容策略等技能更赚钱

10. 具备组织技能、交际能力、个人素养、市场管理等技能更赚钱

## 注意事项

1. 观点来源：所有被纳入考虑范围的观点必须来自上述”预设观点“，不得编造任何观点。
2. 多观点匹配：每条评论可能对应到零个或多个观点，请注意甄别。


'''


with open("jobdata_preprocessed_with_id.jsonl", "w") as f:
    for line in res:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")