# creditos: https://bit.ly/2SwB2YK
# 05/12/2018 - 19:05
# Estre projeto apenas classifica a frase(Caso queira adicionar frases va na def Examples)
import nltk
from nltk.stem import RSLPStemmer

'''Tokenize: essa função serve para quebrarmos nosso texto por palavras,
   criando desse modo um array com todas as palavras contidas dentro do texto.
   Por exemplo, "Eu gosto de Correr" → ["eu","gosto","de","correr"]'''
def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

'''Stemming: essa função serve para diminuirmos a palavra até a sua raiz/base,
   pois assim, conseguimos tratar as palavras originais e suas respectivas derivações de uma mesma maneira.
   Exemplo: As palavras Correr e Corrida quando submetidas à nossa função de Stemming,
   ambas as palavras serão diminuídas até a base Corr.
   Desse modo, se adicionarmos essa função ao algorítimo,
   nosso Chatbot não ficará preso à palavras especificas,
   ele também será capaz de reconhecer derivações ainda não conhecida de palavras bases que ele já aprendeu.'''
def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

'''RemoveStopWords: essa função serve para retiramos dentro do nosso array
   algumas palavras que não são interessantes para contabilizarmos uma pontuação na
   hora de classificar o nosso texto, então mantemos somente as palavras principais.'''
def RemoveStopWords(sentence):
    stopWords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word in sentence:
            if word not in stopWords:
                phrase.append(word)
    return phrase

# Base de exemplos
def Example():
    exampleData = []
    exampleData.append({'classe':'amor', 'frase':'Eu te amo'})
    exampleData.append({'classe':'amor', 'frase':'Você é o amor da minha vida'})
    exampleData.append({'classe':'medo', 'frase':'estou com medo'})
    exampleData.append({'classe':'medo', 'frase':'tenho medo de fantasma'})
    print(f'{len(exampleData)} frases inclusas')
    return exampleData

# Treinando o algoritmo
def Train(exampleData):
    corpusWords =  {} # Armazenara as classes, suas respectivas palavras e o peso de cada uma.
    for data in exampleData:
        frase = data['frase']
        frase = Tokenize(frase)
        frase = Stemming(frase)
        frase = RemoveStopWords(frase)
        className = data['classe'] # Valor da classe
        if className not in list(corpusWords.keys()):
            corpusWords[className] = {}
        for word in frase:
            if word not in list(corpusWords[className].keys()):
                corpusWords[className][word] = 1
            else:
                corpusWords[className][word] += 1
    return corpusWords

def calculatClassScore(sentence, className):
    score = 0 
    sentence = Tokenize(sentence)
    sentence = Stemming(sentence)
    for word in sentence:
        if word in dados[className]:
            score += dados[className][word]
    return score

def calculateScore(sentence):
    highScore = 0
    className = 'default'
    for classe in dados.keys():
        pontos = 0
        pontos = calculatClassScore(sentence, classe)
        if pontos > highScore:
            highScore = pontos
            className = classe
    return className, highScore

dados = Example()
dados = Train(dados)

while True:
    frase = str(input('Sua frase: '))
    print(f'Classificacao: {calculateScore(frase)}')