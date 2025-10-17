Creating a complete Python application, especially a web application, involves quite a bit of code and multiple components. I'll outline a simplified version using Flask (a web framework) and include critical placeholder components that could act as a foundation for your eco-travel guide application. This program will focus on the structure, integrating route optimization, and recommending sustainable options. Real-world usages would require additional integrations with external APIs, databases, and more.

Below is an example illustrating how you might structure such a project:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder data for demonstration purposes
ACCOMMODATIONS = [
    {"name": "Green Hotel", "location": "City A", "eco_rating": 4.5},
    {"name": "Eco Lodge", "location": "City B", "eco_rating": 4.7}
]

ACTIVITIES = [
    {"name": "Nature Hike", "location": "City A", "eco_friendly": True},
    {"name": "River Cleanup", "location": "City B", "eco_friendly": True}
]

ROUTES = {
    ("City A", "City B"): {"distance": 100, "eco_score": 5},
    ("City A", "City C"): {"distance": 200, "eco_score": 3}
}

# Error handling function
def get_safe_data(data, key, default=None):
    try:
        return data[key]
    except KeyError as e:
        print(f"KeyError: {str(e)}")
        return default


@app.route('/optimize_route', methods=['GET'])
def optimize_route():
    start_city = request.args.get('start')
    end_city = request.args.get('end')
    try:
        route_info = ROUTES[(start_city, end_city)]
        return jsonify({"route": route_info}), 200
    except KeyError:
        return jsonify({"error": "Route not found"}), 404


@app.route('/recommend_accommodation', methods=['GET'])
def recommend_accommodation():
    location = request.args.get('location')
    try:
        accommodations = [acc for acc in ACCOMMODATIONS if acc['location'] == location]
        if accommodations:
            return jsonify(accommodations), 200
        else:
            raise ValueError("No accommodations found")
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route('/recommend_activity', methods=['GET'])
def recommend_activity():
    location = request.args.get('location')
    try:
        activities = [act for act in ACTIVITIES if act['location'] == location and act['eco_friendly']]
        if activities:
            return jsonify(activities), 200
        else:
            raise ValueError("No activities found")
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

1. **Dependencies**: This example uses Flask, which means you need to have Flask installed (`pip install Flask`).

2. **Data Simulation**: We use hardcoded data since there's no database, assuming the role of an external API or database. In a real-world application, this would be replaced with a database call or external API request.

3. **Routes and Functions**:
   - `optimize_route`: Simulated endpoint to get an optimized travel route based on eco-friendly scores.
   - `recommend_accommodation`: Returns a list of eco-friendly accommodations based on location.
   - `recommend_activity`: Provides eco-friendly activities in the requested location.

4. **Error Handling**: 
   - We use `try-except` blocks to handle key errors and custom error messages gracefully.
   - `get_safe_data` is a helper function to safely handle dictionary reads, even though it's not extensively used in this example (mostly for idea illustration).

5. **Running the Application**:
   - Run the script, then navigate to `http://127.0.0.1:5000/` with the appropriate endpoints to test functionality. Gather data by appending applicable endpoints, e.g., `http://127.0.0.1:5000/optimize_route?start=City+A&end=City+B`.

To make this system production-ready, you'd have to:
- Implement a persistent data layer with a database (e.g., PostgreSQL, MySQL).
- Integrate third-party APIs for real-world data fetching.
- Enhance error handling, logging, security measures, and user interface components (potentially using a front-end framework like React).