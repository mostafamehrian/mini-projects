import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

def analyze():  
    files = glob.glob('diarytone/diary/*.txt')
    filenames = Path('/home/mosi/projectbasedpython/projects/megacourse/diarytone/diary/2023-10-21.txt').stem


    analyze = SentimentIntensityAnalyzer()
    diarytone = {}

    for file in sorted(files):
        with open(file,'r') as f:
            diary = f.read()
        
        filenames = Path(file).stem
    
        diaryanalize = analyze.polarity_scores(diary)
        filenames = Path(file).stem
        diarytone[filenames] = diaryanalize
        
    return diarytone
