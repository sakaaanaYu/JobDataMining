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