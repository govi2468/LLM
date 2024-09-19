
from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('langchain_model.pkl','rb'))


@app.route('/ans_predict', methods=['POST'])
def ans_predict():
    if request.method == 'POST':
        query = str(request.form['query_input'])
        prediction = model.predict([[query]])
        return render_template('index.html', prediction_text="The Predicted salary in Rs. {} lakhs".format(prediction[0]))



if __name__ == '__main__':
    app.run(debug=True)