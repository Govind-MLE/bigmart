from flask import Flask ,request,jsonify
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return "Welcome to my home"
@app.route('/predict',methods=['GET','POST'])
def predict():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)
if __name__=='__main__':
        app.run(port=8080,debug=True)
