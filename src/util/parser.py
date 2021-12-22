from typing import Tuple

from src.core import get_settings


def compare_answers(answers: str, pair: Tuple[str, str]) -> str:
    first_value_count = answers.count(pair[0])
    second_value_count = answers.count(pair[1])

    if first_value_count > 3:
        raise ValueError
    elif second_value_count > 3:
        raise ValueError

    if first_value_count > second_value_count:
        return pair[0]
    elif first_value_count < second_value_count:
        return pair[1]
    else:
        raise ValueError


def answers_parser(answers: str) -> str:
    if len(answers) != 12:
        raise ValueError

    answer = ""

    for pair in get_settings().MBTI_PAIR:
        answer += compare_answers(answers=answers, pair=pair)

    return answer
