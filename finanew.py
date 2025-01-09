import streamlit as st
import numpy as np
import pandas as pd
import joblib  # To load the trained model

# Load the pre-trained model (replace 'model.pkl' with your trained model's file path)
model = joblib.load("random_forest_model.pkl")
df=pd.read_csv('sale_pre.csv')

# Feature names used in the model
feature_names = [
    'holiday_sales_boost', 
    'dept_size_interaction', 
    'size_bin', 
    'Dept',
    'total_markdown', 
    'total_markdown_avg', 
    'month',
    'markdown_holiday_impact'
]

# Descriptions for each feature
feature_descriptions = {
    'holiday_sales_boost': 'Sales boost during holidays (e.g., Christmas, Black Friday).',
    'dept_size_interaction': 'Size of interaction in the department (e.g., number of visits or transactions).',
    'size_bin': 'Categorical variable representing different size bins of the products.',
    'Dept': 'Department ID (e.g., 1 for Electronics, 2 for Clothing).',
    'total_markdown': 'Total markdown amount applied to products.',
    'total_markdown_avg': 'Average markdown amount applied across different periods.',
    'month': 'Month in which sales are recorded.',
    'markdown_holiday_impact': 'Impact of markdowns during holidays on sales.'
}

# Streamlit App Starts Here
st.title("Sales Prediction App")
st.write("Enter values for the features below to get a prediction:")

# Create a form for user input
with st.form("prediction_form"):
    st.subheader("Enter Input Values")

    # Dynamic input fields with tooltips and descriptions
    user_input = {}
    for feature in feature_names:
        st.write(f"### {feature.replace('_', ' ').capitalize()}")
        st.info(feature_descriptions[feature])

        if feature in ['holiday_sales_boost', 'total_markdown', 'total_markdown_avg', 'markdown_holiday_impact']:
            user_input[feature] = st.number_input(
                f"Enter {feature.replace('_', ' ').capitalize()}",
                min_value=0.0,
                format="%.2f"
            )
        elif feature in ['Dept', 'size_bin']:
            user_input[feature] = st.selectbox(
                f"Select {feature.replace('_', ' ').capitalize()}",
                options=sorted(df[feature].unique())
            )
        else:
            user_input[feature] = st.number_input(
                f"Enter {feature.replace('_', ' ').capitalize()}",
                min_value=0,
                step=1
            )

    # Submit button st.form_submit_button() 
    submitted = st.form_submit_button("Predict")

# When the user clicks the predict button
if submitted:
    # Prepare the input data for prediction
    user_data = pd.DataFrame([list(user_input.values())], columns=feature_names)
    st.write("Your Input Data:")
    st.dataframe(user_data)

    # Predict
    try:
        prediction = model.predict(user_data)[0]
        st.subheader("Prediction Result")
        st.success(f"Predicted Sales: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error occurred during prediction: {e}")
