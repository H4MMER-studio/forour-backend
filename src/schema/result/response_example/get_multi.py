from src.schema.response import ErrorResponseModel, GetResponseModel

result_get_multi_response = {
    "200": {
        "model": GetResponseModel,
        "description": "성공",
        "content": {
            "application/json": {
                "example": {
                    "data": [
                        {
                            "_id": "61c9daa96ed0d4329c8231ed",
                            "images": {
                                "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFJ_%E1%84%85%E1%85%AE%E1%84%91%E1%85%B5%E1%84%82%E1%85%A5%E1%84%89%E1%85%B3.svg",
                                "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFJ.png"
                            },
                            "mbti": "ISFJ",
                            "mbti_title": "용감한 수호자",
                            "mbti_count": 1,
                            "mbti_description": "소중한 이들을 수호하는 데 심혈을 기울이는 혁신적이며 성실한 방어자형",
                            "flower_name": "루피너스",
                            "flower_description": "삶의 욕구",
                            "mbti_relation": [
                                {
                                    "relation": "best",
                                    "mbti": "ENTP",
                                    "_id": "61c9daa96ed0d4329c8231ed",
                                    "mbti_description": "지적인 도전을 두려워 하지 않는 똑똑한 호기심형",
                                    "mbti_title": "뜨거운 논쟁을 즐기는 변론가",
                                    "mbti_count": 0,
                                    "images": {
                                        "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTP_%E1%84%89%E1%85%A1%E1%84%85%E1%85%B3%E1%84%87%E1%85%B5%E1%84%8B%E1%85%A1.svg",
                                        "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTP.png"
                                    },
                                    "flower_name": "샤르비아",
                                    "flower_description": "불타는 열정"
                                },
                                {
                                    "relation": "worst",
                                    "mbti": "ENTJ",
                                    "_id": "61c9daa96ed0d4329c8231ed",
                                    "mbti_description": "대담하면서도 상상력이 풍부한 강한 의지의 소유자로 다양한 방법을 모색하거나 여의치 않을 경우 새로운 방안을 창출하는 리더형",
                                    "mbti_title": "대담한 통솔자",
                                    "mbti_count": 0,
                                    "images": {
                                        "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTJ_%E1%84%8B%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%85%E1%85%B5%E1%84%89%E1%85%B3.svg",
                                        "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTJ.png"
                                    },
                                    "flower_name": "아이리스",
                                    "flower_description": "남 모르게 하는 노력"
                                }
                            ]
                        },
                        {
                            "_id": "61c9da406ed0d4329c8231e4",
                            "images": {
                                "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTP_%E1%84%89%E1%85%A1%E1%84%85%E1%85%B3%E1%84%87%E1%85%B5%E1%84%8B%E1%85%A1.svg",
                                "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ENTP.png"
                            },
                            "mbti": "ENTP",
                            "mbti_title": "뜨거운 논쟁을 즐기는 변론가",
                            "mbti_count": 0,
                            "mbti_description": "지적인 도전을 두려워 하지 않는 똑똑한 호기심형",
                            "flower_name": "샤르비아",
                            "flower_description": "불타는 열정",
                            "mbti_relation": [
                                {
                                    "relation": "best",
                                    "mbti": "ISFJ",
                                    "_id": "61c9da406ed0d4329c8231e4",
                                    "mbti_description": "소중한 이들을 수호하는 데 심혈을 기울이는 혁신적이며 성실한 방어자형",
                                    "mbti_title": "용감한 수호자",
                                    "mbti_count": 1,
                                    "images": {
                                        "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFJ_%E1%84%85%E1%85%AE%E1%84%91%E1%85%B5%E1%84%82%E1%85%A5%E1%84%89%E1%85%B3.svg",
                                        "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFJ.png"
                                    },
                                    "flower_name": "루피너스",
                                    "flower_description": "삶의 욕구"
                                },
                                {
                                    "relation": "worst",
                                    "mbti": "ISFP",
                                    "_id": "61c9da406ed0d4329c8231e4",
                                    "mbti_description": "항시 새로운 것을 찾아 시도하거나 도전할 준비가 되어 있는 융통성 있는 성격의 매력 넘치는 예술가형",
                                    "mbti_title": "호기심 많은 예술가",
                                    "mbti_count": 0,
                                    "images": {
                                        "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFP_%E1%84%85%E1%85%A1%E1%84%82%E1%85%A5%E1%86%AB%E1%84%8F%E1%85%B2%E1%86%AF%E1%84%85%E1%85%A5%E1%84%89%E1%85%B3.svg",
                                        "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ISFP.png"
                                    },
                                    "flower_name": "라넌큘러스",
                                    "flower_description": "매력과 매혹"
                                }
                                ]
                            }
                        ]}}}
    },
    "404": {
        "model": GetResponseModel,
        "description": "존재하지 않는 엔티티",
        "content": {"application/json": {"example": {"data": []}}},
    },
    "422": {
        "model": ErrorResponseModel,
        "description": "유효하지 않은 매개변수 사용",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["query", "skip"],
                            "msg": "field required",
                            "type": "value_error.missing",
                        }
                    ]
                }
            }
        },
    },
}
