from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# Simulated data for laptops
laptops = [
    {'id': str(uuid4()), 'name': 'Dell XPS 13', 'rating': 4.8, 'price': 1200, 'discount': 10, 'availability': 'In Stock'},
    {'id': str(uuid4()), 'name': 'MacBook Air', 'rating': 4.7, 'price': 1000, 'discount': 5, 'availability': 'In Stock'},
    {'id': str(uuid4()), 'name': 'HP Spectre x360', 'rating': 4.6, 'price': 1100, 'discount': 8, 'availability': 'Out of Stock'},
    {'id': str(uuid4()), 'name': 'Lenovo ThinkPad X1 Carbon', 'rating': 4.5, 'price': 1300, 'discount': 15, 'availability': 'In Stock'},
    {'id': str(uuid4()), 'name': 'Asus ZenBook 13', 'rating': 4.4, 'price': 900, 'discount': 20, 'availability': 'In Stock'}
]

@app.route('/categories/laptops/products', methods=['GET'])
def get_products():
    n = int(request.args.get('n', 10))
    page = int(request.args.get('page', 1))
    sort_by = request.args.get('sort_by')
    order = request.args.get('order', 'asc')

    sorted_laptops = sorted(laptops, key=lambda x: x.get(sort_by, ''), reverse=(order == 'desc')) if sort_by else laptops
    start = (page - 1) * n
    end = start + n
    paginated_laptops = sorted_laptops[start:end]
    
    return jsonify(paginated_laptops)

@app.route('/categories/laptops/products/<product_id>', methods=['GET'])
def get_product_details(product_id):
    product = next((item for item in laptops if item['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)
