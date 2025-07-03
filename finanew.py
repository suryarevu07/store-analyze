from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import joblib
import traceback

app = Flask(__name__)


def load_artifacts():
    model_path = r"D:\model (1).pkl"
    scaler_path = r"D:\scaler (9).pkl"
    print(f"Checking {model_path}, {scaler_path}")
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        print("Artifacts loaded successfully")
        return model, scaler
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        return None, None

model, scaler = load_artifacts()
selected_features = ['Dept', 'Size', 'Type', 'Store', 'Week', 'CPI', 'Unemployment', 'Temperature']

def get_average_size(df, store, dept):
    mask = (df['Store'] == store) & (df['Dept'] == dept)
    return df[mask]['Size'].mean() if mask.any() else df['Size'].mean()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            store = int(request.form['store'])
            dept = int(request.form['dept'])
            type_val = int(request.form['type'])
            week = int(request.form['week'])
            cpi = float(request.form['cpi'])
            unemployment = float(request.form['unemployment'])
            temperature = float(request.form['temperature'])

       
            df = pd.DataFrame()  
            size = 0 
            if not df.empty:
                size = get_average_size(df, store, dept)
                if np.isnan(size):
                    size = df['Size'].mean()

            pred_data = {
                'Dept': [dept],
                'Size': [size],
                'Type': [type_val],
                'Store': [store],
                'Week': [week],
                'CPI': [cpi],
                'Unemployment': [unemployment],
                'Temperature': [temperature]
            }
            pred_df = pd.DataFrame(pred_data)
            X_pred = pred_df[selected_features]
            X_scaled = scaler.transform(X_pred)
            pred_log = model.predict(X_scaled)
            predicted_sales = np.expm1(pred_log)[0]

            return redirect(url_for('results', sales=f"${predicted_sales:,.2f}"))
        except Exception as e:
            print(f"Error in prediction: {traceback.format_exc()}")
            return jsonify({'error': f"An error occurred: {str(e)}"}), 500

    return render_template('index.html')

@app.route('/results')
def results():
    sales = request.args.get('sales', 'N/A')
    return render_template('results.html', sales=sales)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



