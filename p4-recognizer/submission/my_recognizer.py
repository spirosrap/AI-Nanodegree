import warnings
from asl_data import SinglesData
import arpa
from itertools import permutations


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    test_sequences = list(test_set.get_all_Xlengths().values())
    for test_X,test_Xlength in test_sequences:
      prob = {}
      maxlogLvalue = float("-inf")
      guess = ""
      for word, model in models.items():
        try:
          logLvalue = model.score(test_X, test_Xlength)        
          prob[word] = logLvalue
          if logLvalue > maxlogLvalue:
            guess = word
            maxlogLvalue = logLvalue
        except:
          prob[word] = float("-inf")


      probabilities.append(prob)  
      guesses.append(guess)

    return (probabilities,guesses)

    
def recognize_ngram(models: dict, test_set: SinglesData,probs,BIC_guesses):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []

    model = arpa.loadf("devel-lm-M3.sri.lm")
    lm = model[0]  # ARPA files may contain several models.
    # TODO implement the recognizer
    # return probabilities, guesses
    test_sequences = list(test_set.get_all_Xlengths().values())
    word_keys = list(test_set.get_all_Xlengths().keys())
    i = -1    
    for sentence in test_set.sentences_index.values():
      f = {}
      maxs = float("-inf")
      prob = []
      words = []

      sentenceLength = 0
      for word_index in sentence:
        i+=1
        word = test_set.wordlist[word_index]
        sentenceLength+=1
        try:
          f[word] = probs[word][i]
        except:
          f[word] = float("-inf")
        prob.append(f[word]) ## These are Just the probabilities unchanged from the BIC recognizer.
          
      # Find Six most probable words and generate the possible permutations    
      sixwords = sorted(f,key=f.get,reverse=True)[:6]
      for k in permutations(sixwords, r=sentenceLength):
        l = 0
        for j in range(len(k)):
          l += f[k[j]]
        try:
          sentenceLP = l + 13*lm.log_s(" ".join(k)) ## According to one student in the forum 13 is the best hyperparameter
          if sentenceLP > maxs:                     ## https://discussions.udacity.com/t/slm-data-for-this-asl-dataset/230822/8?u=spiros
            sentence = " ".join(k)
            maxs = sentenceLP
            words = list(k)
        except:
          pass

      if(words == []):
        words = BIC_guesses[len(guesses):len(guesses)+sentenceLength] ## Fall back to BIC guesses
      probabilities.append(prob)  
      guesses += words
    return (probabilities,guesses)
