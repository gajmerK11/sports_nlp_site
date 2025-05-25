from django.shortcuts import render
import spacy

nlp = spacy.load("en_core_web_sm")

def home(request):
    response = None
    if request.method == 'POST':
        question = request.POST.get('question', '')
        doc = nlp(question)

        # TEMP: Just extract named entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        response = f"Entities found: {entities}"

    return render(request, 'sportschat/index.html', {'response': response})


