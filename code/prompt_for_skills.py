import pandas as pd
import json


res = []

df = pd.read_csv("jobdata_preprocessed_with_id.csv")
for index, row in df.iterrows():
    id_value = row['id']
    job_desc = row['工作简介']

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
            "model": "gpt-4o-mini",
            # "model": "gpt-4o",
            "seed": 10370,
            "temperature": 0,
            "stream": False,
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "hardAndSoftSkills",
                    "description": "A response format that includes both hard and soft skills.",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "hard_skills": {
                                "anyOf": [{
                                        "type": "array",
                                        "description": "Hard skills emphasize capabilities directly related to completing daily tasks, characterized by being specific and procedural in nature.",
                                        "items": {
                                            "type": "string",
                                            "enum": [
                                                "写作能力",
                                                "新闻敏感",
                                                "编辑排版",
                                                "研究能力",
                                                "摄影摄像",
                                                "新闻报道",
                                                "播音播报",
                                                "采访调查",
                                                "主持演讲",
                                                "多媒体技术",
                                                "产品管理",
                                                "技术素养",
                                                "视觉设计",
                                                "数据处理",
                                                "内容策略",
                                                "媒体运营",
                                                "网页设计",
                                                "程序设计",
                                                "受众分析"
                                            ],
                                        },
                                    },
                                    {
                                        "type": "string",
                                        "description": "No hard skills found.",
                                        "enum": ["无"]
                                    }
                                ]
                            },
                            "soft_skills": {
                                "anyOf": [{
                                "type": "array",
                                "description": "Soft skills highlight the ability to handle various scenarios and solve different problems, characterized by being abstract and transferable in nature.",
                                "items": {
                                            "type": "string",
                                            "enum": ["个人素养",
                                                "职业道德",
                                                "组织技能",
                                                "抗压能力",
                                                "学科知识",
                                                "其他知识",
                                                "外语能力",
                                                "形象管理",
                                                "交际能力",
                                                "市场管理",
                                                "关系管理",
                                                "领导能力"
                                            ],
                                        }
                                    },
                                    {
                                        "type": "string",
                                        "description": "No soft skills found.",
                                        "enum": ["无"]
                                    }]
                            }
                        },
                        "required": ["hard_skills", "soft_skills"]
                    }
                }
            }
        }
    }

    res.append(json_line_content)

with open("jobdata_preprocessed_with_id.jsonl", "w") as f:
    for line in res:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


SYSTEM_PROMPT = '''
# 识别技能要求的应聘者

## 任务：

职位描述与技能匹配

## 背景：

在招聘平台上存在着大量招聘信息，这些招聘信息会向求职者提出明确的岗位职责与岗位技能要求，这些技能要求往往包含着一些“硬技能”和一些“软技能”，分别要求应聘者掌握技术技能和具备综合素质。正确地将职位描述里提到的要求与硬技能、软技能分别相匹配对于求职者个人的自我提升来说至关重要。

## 你的角色：

你是一个正在找工作的应聘者，你需要精通如何正确地将企业提出的岗位需求归类到对应的技能中。

## 技能要求：

### 19个硬技能：

1. 写作能力 (写作、文案、文字)
2. 新闻敏感 (新闻热点、新闻剖析)
3. 编辑排版 (编辑、排版、Office)
4. 研究能力 (研究方法、社会调查)
5. 摄影摄像 (摄影、镜头、照片)
6. 新闻报道 (新闻报道、专题报道)
7. 播音播报 (播音、主持、普通话)
8. 采访调查 (新闻采访、街头采访)
9. 主持演讲 (即兴表达、即兴演说)
10. 多媒体技术 (影视、画面、音响)
11. 产品管理 (产品管理、产品设计)
12. 技术素养 (交计算机、硬件、技术)
13. 视觉设计 (平面设计、美术、PS)
14. 数据处理 (数据分析、统计、SPSS)
15. 内容策略 (内容策划、广告策划)
16. 媒体运营 (微信、运营、流量)
17. 网页设计 (Web、H5、网页制作)
18. 程序设计 (Python、代码、程序设计)
19. 受众分析 (受众研究、受众定位)

### 12个软技能：

1. 个人素养 (热情、逻辑、批判性思维)
2. 职业道德 (责任心、品德、法律)
3. 组织技能 (活动组织、协调分工)
4. 抗压能力 (抗压性、适应力、毅力)
5. 学科知识 (传播学、理论知识)
6. 其他知识 (计算机科学、心理学)
7. 外语能力 (英语、外语口语、外语读写)
8. 形象管理 (形象气质、化妆、礼仪)
9. 交际能力 (交流、沟通、语言表达)
10. 市场管理 (营销、商务、市场推广)
11. 关系管理 (人脉关系、公共关系)
12. 领导能力 (领导力、团队管理)

## 你的目标：

我会给你提供一段包含岗位职责或工作要求的文本内容，你需要：

1. 仔细阅读并理解文本。
2. 识别我给你提供的“硬技能”“软技能”中是否包含该段文本中对应聘者的技能要求。如果包含，请分类输出所有对应的技能；如果不包含，请输出“无”。
3. 请注意，一段文本可能包含多个硬技能或软技能，也可能不包含硬技能或软技能，请注意甄别。

## 你必须遵守的规则：

所有你可以识别和输出的硬技能必须来自我给你提供的12个硬技能内容，且输出内容必须严格对应。切勿编造任何技能
'''