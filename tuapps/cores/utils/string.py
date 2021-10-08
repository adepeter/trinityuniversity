def truncate_words(sentence, words_count=10, seperator=None):
    return ' '.join(sentence.split(seperator)[:words_count])


def stringify_uuid(uuid: str, remove_dash: bool = False) -> str:
    stringify_uuid4 = str(uuid)
    if remove_dash:
        return ''.join(stringify_uuid4.split('-'))
    return stringify_uuid4
