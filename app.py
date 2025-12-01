from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import random
from pathlib import Path
import json

app = Flask(__name__)
app.secret_key = "supersecretkey"

dictionary = {
    "rizz": "Charm or attractiveness 🥰💫",
    "sus": "Suspicious or acting shady 🤔🚨",
    "bet": "Used to agree or confirm something 👍💯",
    "slay": "To do something amazing or look fabulous 💃🔥",
    "cap": "A lie; 'No cap' means no lie 🧢❌",
    "simp": "Someone who does too much for someone they like 😍🙈",
    "lit": "Amazing, exciting, or fun 🔥🎉",
    "tea": "Gossip or juicy news ☕👀",
    "yeet": "To throw something with force 🚀😂",
    "drip": "Cool, fashionable style 👟💎",
    "mid": "Mediocre, average, or not that great 😐📉",
    "fire": "Awesome, excellent, or top-tier 🔥💯",
    "vibe": "A feeling, mood, or atmosphere ✨😎",
    "periodt": "Used to end a statement with emphasis 💅✅",
    "stan": "An extreme fan who supports someone a lot 🫶🌟",
    "mood": "Something relatable or expressing how you feel 😭👌",
    "salty": "Bitter or upset over something small 🧂😤",
    "flex": "To show off or brag 💪💎",
    "ghost": "To ignore someone suddenly 👻🙅‍♀️",
    "lowkey": "Quietly or secretly; not too obvious 🤫",
    "highkey": "Very obvious or not hiding something 🔊🔥",
    "bussin": "Really good, especially food 🍔😋",
    "goat": "Greatest of all time 🐐👑",
    "fit": "Short for outfit 👕🧢",
    "vibe check": "Judging the mood or energy of something 🪩💭",
    "boujee": "Luxurious or high-class lifestyle 💄💅",
    "no cap": "For real, no lie 🧢✋",
    "based": "Being true to yourself and not caring what others think 💯🧠",
    "ratio": "Used on social media to show disagreement (more replies/likes than original post) 🔢📱",
    "fr": "For real or seriously 🙌😤",
    "idc": "I don’t care 😎✌️",
    "idk": "I don’t know 🤷‍♀️🤷‍♂️",
    "ngl": "Not gonna lie 😅🫣",
    "iykyk": "If you know, you know 😉🔍",
    "ok boomer": "Sarcastic reply to older people out of touch 🧓😂",
    "valid": "Cool, acceptable, or makes sense ✅🔥",
    "cringe": "Embarrassing or awkward 😬🙈",
    "glow up": "A big positive transformation ✨💅",
    "savage": "Bold, unapologetic, or brutally honest 😎🔥",
    "pressed": "Annoyed or upset 😤💢",
    "main character": "When someone acts like the star of the story 🎬🌟",
    "aura": "Your personal vibe or energy 💫🔮",
    "delulu": "Being delusional, usually in a funny way 🤪💭",
    "it’s giving": "Used to describe the energy or impression something gives 🌈🪩",
    "skibidi": "Silly or chaotic energy (from meme culture) 🕺🤣",
    "fanum tax": "When someone takes a bit of your food 🍟😅",
    "core": "Aesthetic or vibe of a trend (e.g., cottagecore, goblincore) 🍃🏡",
    "slaps": "Something really good, especially music 🎶🔥",
    "dead": "Something so funny it “killed” you with laughter 💀😂",
    "sneaky link": "A secret hookup or relationship 🤫💋",
    "bruh": "Expression of disbelief, frustration, or disappointment 😐🤦‍♂️",
    "gyatt": "Expression when someone sees something attractive 👀🔥",
    "sheesh": "Used to hype something or someone up 😤🙌",
    "op": "Overpowered or too good (from gaming) 🎮💥",
    "npc": "A boring or basic person with no main character energy 🧍‍♂️💀",
    "caught in 4k": "Got caught doing something wrong with proof 📸😂",
    "sus af": "Extremely suspicious 😳🚨",
    "bffr": "Be for real 😭🙄",
    "mid af": "Extremely average 😐📉",
    "gatekeep": "Keeping something cool a secret so not everyone knows 🚪🙊",
    "slumped": "Extremely tired or asleep 😴💤",
    "sigma": "Independent, confident, and cool in their own way 🧠😎",
    "glitch": "Something weird or unexpected happened 🤖⚡",
    "vibing": "Chilling, enjoying the moment 🎧🌈",
    "brainrot": "When you watch or do something dumb for too long 📱💀",
    "core memory": "A special or unforgettable moment 🧠💖",
    "touch grass": "Go outside and get off the internet 🌿😆",
    "suspect": "Untrustworthy or suspicious person 🕵️‍♂️🤨",
    "drained": "Feeling exhausted emotionally or mentally 😮‍💨🫠",
    "lag": "Being slow or delayed (in games or life) 🕹️🐢",
    "slayed": "Did amazing or looked fabulous 💅🔥",
    "fyp": "For You Page, on TikTok 🎥📱",
    "aesthetic": "Visually pleasing or stylish 🎨✨"
}


quiz_questions = {
 
    "easy": [
        {
            "question": "What does 'rizz' mean?",
            "options": ["Charm or attractiveness", "Suspicious", "Lie"],
            "answer": "Charm or attractiveness"
        },
        {
            "question": "What does 'sus' mean?",
            "options": ["Suspicious", "Sleepy", "Funny"],
            "answer": "Suspicious"
        },
        {
            "question": "What does 'lit' mean?",
            "options": ["Amazing or exciting", "Dark", "Boring"],
            "answer": "Amazing or exciting"
        },
        {
            "question": "What does 'cap' mean?",
            "options": ["A lie", "A hat", "A joke"],
            "answer": "A lie"
        },
        {
            "question": "What does 'tea' mean?",
            "options": ["Gossip or news", "A drink", "A joke"],
            "answer": "Gossip or news"
        }
    ],

    "medium": [
        {
            "question": "What does 'drip' mean in Gen Z slang?",
            "options": ["Fashionable style", "A leak", "Something boring"],
            "answer": "Fashionable style"
        },
        {
            "question": "What does 'simp' mean?",
            "options": ["Someone who does too much for someone they like", "Someone cool", "A funny person"],
            "answer": "Someone who does too much for someone they like"
        },
        {
            "question": "What does 'slay' mean?",
            "options": ["To look amazing or do something perfectly", "To fail", "To hide"],
            "answer": "To look amazing or do something perfectly"
        },
        {
            "question": "What does 'no cap' mean?",
            "options": ["No lie / For real", "No hat", "Stop talking"],
            "answer": "No lie / For real"
        },
        {
            "question": "What does 'vibe' mean?",
            "options": ["Mood or atmosphere", "Sound", "Clothing"],
            "answer": "Mood or atmosphere"
        }
    ],

    "hard": [
        {
            "question": "What does 'delulu' mean?",
            "options": ["Being delusional in a funny way", "Being lazy", "Being smart"],
            "answer": "Being delusional in a funny way"
        },
        {
            "question": "What does 'based' mean in Gen Z culture?",
            "options": ["Being true to yourself", "Following trends", "Being shy"],
            "answer": "Being true to yourself"
        },
        {
            "question": "What does 'NPC' mean?",
            "options": ["A person who acts basic or unoriginal", "A video game character", "A hacker"],
            "answer": "A person who acts basic or unoriginal"
        },
        {
            "question": "What does 'bussin' mean?",
            "options": ["Really good, especially food", "Terrible", "Average"],
            "answer": "Really good, especially food"
        },
        {
            "question": "What does 'caught in 4k' mean?",
            "options": ["Got caught doing something with proof", "Being famous", "Watching a movie"],
            "answer": "Got caught doing something with proof"
        }
    ]
}

    





@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dictionary')
def dictionary_page():
    return render_template('dictionary.html')

@app.route('/search', methods=['POST'])
def search():
    word = request.form['word'].lower()
    meaning = dictionary.get(word)
    if meaning:
        return render_template('result.html', word=word, meaning=meaning)
    else:
        return render_template('notfound.html', word=word)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    if request.method == "POST":
        level = request.form['level']
        session['level'] = level
        session['current'] = 0
        session['answers'] = []
        session['questions'] = quiz_questions[level]
        return redirect(url_for('quiz_question'))
    return render_template('quiz.html')


@app.route('/quiz_question', methods=['GET', 'POST'])
def quiz_question():
    if 'current' not in session or 'questions' not in session:
        return redirect(url_for('quiz_page'))

    current_index = session['current']
    questions = session['questions']

    if request.method == "POST":
        
        selected = request.form.get('answer')
        session['answers'].append(selected)
        session['current'] += 1
        current_index = session['current']

       
        if current_index >= len(questions):
            return redirect(url_for('quiz_result'))

   
    if current_index < len(questions):
        question = questions[current_index]
        return render_template('quiz_question.html', q=question, index=current_index + 1, total=len(questions))


@app.route('/quiz_result')
def quiz_result():
    questions = session.get('questions', [])
    user_answers = session.get('answers', [])
    score = 0
    for ua, q in zip(user_answers, questions):
        if ua == q['answer']:
            score += 1

    
    session.pop('current', None)
    session.pop('questions', None)
    session.pop('answers', None)
    session.pop('level', None)

    return render_template('quiz_result.html', score=score, total=len(questions))



@app.route('/mini_game', methods=['GET', 'POST'])
def mini_game():
    words = list(dictionary.keys())
    
    if request.method == "POST":
        scrambled = request.form['scrambled']
        correct_word = request.form['correct_word']
        user_guess = request.form['guess'].lower()
        if user_guess == correct_word.lower():
            result = "🎉 Correct! Well done!"
        else:
            result = f"❌ Wrong! The correct word was '{correct_word}'."
       
        new_word = random.choice(words)
        new_scrambled = ''.join(random.sample(new_word, len(new_word)))
        return render_template("mini_game.html", scrambled=new_scrambled, word=new_word, result=result)
  
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    return render_template("mini_game.html", scrambled=scrambled, word=word, result=None)



# -------------------- GEN-Z BROWSER --------------------



DICTIONARY_PATH = Path("data/dictionary.json")

def load_dictionary():
    if DICTIONARY_PATH.exists():
        with open(DICTIONARY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {} 
    
@app.route("/genz_browser")
def genz_browser():
    dictionary_data = load_dictionary()  # Your JSON dictionary file

    grouped = {}
    for word in dictionary_data.keys():
        letter = word[0].upper()
        grouped.setdefault(letter, []).append(word)

    # Sort words alphabetically in each letter
    for k in grouped:
        grouped[k].sort()

    return render_template("genz_browser.html", grouped=grouped)
@app.route("/get_meaning")
def get_meaning():
    word = request.args.get("word")
    dictionary_data = load_dictionary()
    meaning = dictionary_data.get(word, "Meaning not found")
    return jsonify({"word": word, "meaning": meaning})



if __name__ == "__main__":
    app.run(debug=True)
