from django.shortcuts import render
import spacy

nlp = spacy.load("en_core_web_sm")

def home(request):
    response = None
    if request.method == 'POST':
        question = request.POST.get('question', '')
        doc = nlp(question)

        # here we are extracting named entities from text inputed by user like names of people, places, organizations, dates, etc.
        # the output of following code will look like: [('Barcelona', 'GPE'), ('tonight', 'DATE')]
        ''' We have used list of tuples here because:
        1. We use tuples to store things that belong together and won’t change, like ("Barcelona", "GPE").
        2. It makes clear that each pair is one fixed unit (an entity and its type).
        3. In a list of lists, it looks like you might want to change the data later — which you usually don't.
        '''
        # here label is like label_ because in spacy ent.label gives you the numeric iD of the label like 26 and ent.label_ gives you the readable string label like 'GPE'
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        response = f"Entities found: {entities}"

    return render(request, 'sportschat/index.html', {'response': response})


