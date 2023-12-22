### Simple Flask web application to visualize data ###
    
# First we need to install flask in our environment
#pip install flask
    
# Create a Flask App
from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__, template_folder = 'template')

# Load the cleaned and preprocessed data
orders_df = pd.read_csv('..\Dataset\Orders.csv')
merged_df = pd.read_csv('..\Dataset\cleaned_data.csv')

@app.route('/dashboard')
def dashboard():
    # Visualization 1: Order Status Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x='order_status', data=orders_df)
    plt.title('Order Status Distribution')
    img_order_status_path = 'order_status_distribution.png'
    plt.savefig(img_order_status_path)
    plt.close()

    # Visualization 2: Product Category Distribution
    plt.figure(figsize=(25, 25))
    sns.countplot(x='product_category_name', data=merged_df, order=merged_df['product_category_name'].value_counts().index)
    plt.xticks(rotation=90)
    plt.title('Product Category Distribution')
    img_product_category_path = 'product_category_distribution.png'
    plt.savefig(img_product_category_path)
    plt.close()

    return render_template('dashboard.html')

@app.route('/data')
def data():
    return render_template('data.html', tables=[merged_df.to_html(classes='table table-striped')], titles=[''])

if __name__ == '__main__':
    app.run(debug=True)