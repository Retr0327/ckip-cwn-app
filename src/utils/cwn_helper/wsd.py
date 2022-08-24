from typing import List, Tuple
from DistilTag import DistilTag
from CwnSenseTagger import senseTag

tagger = DistilTag()

def disambiguate_word_sense(sentence_list: List[str])-> List[Tuple[str]]:
    """The disambiguate_word_sense function disambiuates the word sense.
    
    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of tuples.
    """
    disambiguate = lambda value: tagger.tag(value)
    return list(map(disambiguate, sentence_list))

def create_cwn_sense_tags(disambiguated_list: List[List[List[tuple]]]):
    create = lambda value: senseTag(value)
    return list(map(create, disambiguated_list))