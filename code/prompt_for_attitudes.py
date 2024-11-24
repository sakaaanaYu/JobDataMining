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
            "model": "gpt-4o-mini",
            # "model": "gpt-4o",
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

with open("jobdata_preprocessed_with_id.jsonl", "w") as f:
    for line in res:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")