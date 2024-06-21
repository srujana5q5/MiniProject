from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import os

app = Flask(__name__)

# Load dataset
file_path = "C:/Users/sruja/OneDrive/Desktop/newproj/miniproject(106)ds.1718048096201 (1).csv"  # Update with your dataset path
dataset = pd.read_csv(file_path)

# Function to get weather temperature
def get_weather_temperature():
    response = requests.get(url)
    if response.status_code == 200:
        return data['main']['temp']
    else:
        return None

# Function to find the nearest image, jewelry, and footwear link based on input features
def find_nearest_links(knn_model,input_features):
    encoded_dataset = pd.get_dummies(dataset[['Style', 'SleeveLength']])
    knn_model.fit(encoded_dataset)
    distances, indices = knn_model.kneighbors(input_encoded)
    return dataset.loc[nearest_neighbor_index, ['ImageLink', 'Jewelry', 'footwear']]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explore')
def explore():
    if request.method == 'POST':
        style = request.form['Style']
        sleeve_length = request.form['SleeveLength']
        temperature = get_weather_temperature()

        input_features = {
            'Style': style,
            'Temperature': temperature,
            'SleeveLength': sleeve_length
        }

        knn_model = NearestNeighbors(n_neighbors=1)
        image_link, jewelry_link, footwear_link = find_nearest_links(knn_model, dataset, input_features)

        return render_template('result.html', image_link=image_link, jewelry_link=jewelry_link, footwear_link=footwear_link)

    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)
