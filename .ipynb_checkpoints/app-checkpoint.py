from flask import Flask, render_template, request, redirect, url_for
# --- SNIP IN ---
import lab5lib as lab5
# --- SNIP OUT ---

app = Flask(__name__, static_folder='docs', static_url_path='/docs')

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to process the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    query = request.form.get('query')

    # TODO: Call your search function in lab5lib to process the query, then pass the ranked list
    # to the lab5lib make_snippets() function and assig the results to a variable named 'results'
    # --- SNIP IN ---
    ranks = lab5.search(query)
    results = lab5.make_snippets(query, ranks)
    # --- SNIP OUT ---
    
    return render_template('form.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)