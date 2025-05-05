from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text_input', '')
        # Redirect to the 'result' view and pass the text as a URL parameter
        return redirect(f'/result/?text={text}')
    return render(request, 'home.html')

def result(request):
    # Get the text from URL parameter
    text = request.GET.get('text', '')
    return render(request, 'result.html', {'text': text})
