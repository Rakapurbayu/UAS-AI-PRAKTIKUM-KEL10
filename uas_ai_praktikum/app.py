from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def build_decision_tree():
    decision_tree = {
        'Kepribadian': {
            'terorganisir': 'Visual',
            'kritis': 'Auditory',
            'bertanggung jawab': 'Kinesthetic',
            'konsisten': 'Visual',
            'tenang': 'Kinesthetic',
            'adil': 'Auditory',
            'keras kepala': 'Visual',
            'perfeksionis': 'Kinesthetic',
            'semangat yang tinggi': 'Visual',
            'aktif': 'Kinesthetic',
            'kreatif': 'Auditory',
            'selalu ingin tahu': 'Visual',
            'kurang kooperatif': 'Auditory',
            'individualis': 'Visual',
            'lebih mementingkan logika daripada perasaan': 'Kinesthetic',
            'misterius': 'Visual',
            'memiliki banyak teman': 'Auditory',
            'rasional': 'Visual',
            'suka menolong': 'Kinesthetic',
            'mudah beradaptasi': 'Auditory',
            'tidak tegas': 'Visual',
            'mudah lupa': 'Kinesthetic',
            'sensitif': 'Auditory',
            'empati': 'Visual',
            'baik hati': 'Kinesthetic',
            'pemurah': 'Visual',
            'enerjik': 'Auditory',
            'terbuka': 'Visual',
            'menghargai pendapat orang lain': 'Kinesthetic',
            'mudah terpengaruh oleh orang lain': 'Auditory',
            'kurang fokus': 'Visual',
            'lebih suka menjadi pengikut dibanding pemimpin': 'Kinesthetic'
        }
    }
    return decision_tree

decision_tree = build_decision_tree()

def predict_learning_style(data):
    kepribadian_list = data.get('Kepribadian', [])
    golongan_darah = data.get('Golongan Darah', '')

    result_counts = {
        'Visual': 0,
        'Auditory': 0,
        'Kinesthetic': 0,
        'Tidak Diketahui': 0
    }
    
    for kepribadian in kepribadian_list:
        kepribadian = kepribadian.lower()
        if kepribadian in decision_tree['Kepribadian']:
            result_counts[decision_tree['Kepribadian'][kepribadian]] += 1
        else:
            result_counts['Tidak Diketahui'] += 1

    prediction = max(result_counts, key=result_counts.get)
    
    if result_counts[prediction] == 0:
        return "Tidak Diketahui"
    return prediction

@app.route('/')
def home():
    personality_traits = list(decision_tree['Kepribadian'].keys())
    return render_template('index.html', personality_traits=personality_traits)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    
    if 'Kepribadian' not in data or 'Golongan Darah' not in data:
        return jsonify({'error': 'Missing required keys'}), 400
    
    prediction = predict_learning_style(data)
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
