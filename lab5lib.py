def search(query):
    return [ 'coffee-guide.doc', 'learn-python.doc', 'recipes.doc', 'running.doc', 'indoor-gardening.doc' ]

def make_snippets(ranks):
    # TODO: Implement snippets for each document in the ranks list by calling snippet() and wrappint the result in HTML. Return a single HTML string.   
    return '''
        <div class="snippet">
        <div class="title">Best <b>Coffee Shops</b> in Downtown Seattle</div>
        <div class="url">www.seattleeats.com/coffee-guide</div>
        <div class="description">
            Discover the top <b>coffee shops</b> in Seattle's downtown area. From artisanal roasts to cozy atmospheres, find your perfect <b>coffee</b> spot near Pike Place Market.
        </div>
    </div>

    <div class="snippet">
        <div class="title"><b>Python Programming</b> Tutorial for Beginners</div>
        <div class="url">www.learncode.com/python-basics</div>
        <div class="description">
            Master <b>Python programming</b> with our comprehensive tutorial. Learn variables, functions, and loops in this beginner-friendly <b>Python</b> course with hands-on examples.
        </div>
    </div>

    <div class="snippet">
        <div class="title">Healthy <b>Meal Prep</b> Ideas for Busy Professionals</div>
        <div class="url">www.healthyeating.org/meal-prep</div>
        <div class="description">
            Save time with these nutritious <b>meal prep</b> recipes. Quick, balanced meals perfect for busy schedules. Includes shopping lists and storage tips for weekly <b>meal prep</b>.
        </div>
    </div>

    <div class="snippet">
        <div class="title">How to Choose the Right <b>Running Shoes</b></div>
        <div class="url">www.runningworld.com/shoe-guide</div>
        <div class="description">
            Find the perfect <b>running shoes</b> for your gait and terrain. Expert advice on cushioning, support, and fit to prevent injuries and improve your <b>running</b> performance.
        </div>
    </div>

    <div class="snippet">
        <div class="title"><b>Home Gardening</b> Tips for Small Spaces</div>
        <div class="url">www.gardenlife.net/small-space-gardens</div>
        <div class="description">
            Transform your apartment into a green oasis with these <b>home gardening</b> ideas. Vertical gardens, herb containers, and indoor plants perfect for small living spaces.
        </div>
    </div>
    '''

def process_query(query):
    # TODO: Implement processing on the query and returl a list of tuples with the original word and stem
    return [ ('coffee', 'coffee'), ('meals',  'meal'), ('gardening', 'garden') ]
    
def snippet(keypairs, docname, max_length=250):
        
    if docname == 'coffee-guide.doc':
        return "Discover the top <b>coffee shops</b> in Seattle's downtown area. From artisanal roasts to cozy atmospheres, find your perfect <b>coffee</b> spot near Pike Place Market."

    if docname == 'learn-python.doc':
        return "Master <b>Python programming</b> with our comprehensive tutorial. Learn variables, functions, and loops in this beginner-friendly <b>Python</b> course with hands-on examples."
    
    if docname == 'recipes.doc':
        return "Save time with these nutritious <b>meal prep</b> recipes. Quick, balanced meals perfect for busy schedules. Includes shopping lists and storage tips for weekly <b>meal prep</b>."
    
    if docname == 'running.doc':
        return "Find the perfect <b>running shoes</b> for your gait and terrain. Expert advice on cushioning, support, and fit to prevent injuries and improve your <b>running</b> performance."
        
    if docname == 'indoor-gardening.doc':
        "Transform your apartment into a green oasis with these <b>home gardening</b> ideas. Vertical gardens, herb containers, and indoor plants perfect for small living spaces."

    return "Unknown document"
