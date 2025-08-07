# Hotel Booking Dashboard

An interactive dashboard built with **Streamlit** and **Plotly** for exploring and analyzing hotel booking data. This app enables users to filter bookings by hotel type, year, and customer type, and provides key metrics and visualizations to gain insights into booking trends, cancellation rates, average daily rates, and customer segments.

## Features

* Filterable views by hotel, year, and customer type
* Key Performance Indicators (KPIs) including total bookings, cancellation rate, average daily rate (ADR), and lead time
* Visualizations: monthly bookings, cancellation rates by market segment, ADR distribution, and customer type breakdown
* Uses cached data loading for improved performance

## Technologies

* Python
* Streamlit
* Pandas
* Plotly Express

## Usage

1. Clone the repo
2. Install dependencies with `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. Upload your cleaned hotel booking data as `cleaned_hotel_data.csv`
