from analysis.loader import load_all
from analysis.hierarchy import analyze_hierarchy
from analysis.lengths import analyze_lengths
from analysis.questions import list_questions
from analysis.overlap import analyze_overlap


if __name__ == "__main__":
    corpus, qa = load_all()
    analyze_hierarchy(corpus)
    analyze_lengths(corpus)
    list_questions(qa)
    analyze_overlap(corpus, qa)
