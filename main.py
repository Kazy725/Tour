from helpers import *
from flask import  Flask , render_template , request  , redirect 
import random 

app = Flask(__name__)


@app.route("/")
def main():
    if len(request.args) == 0:
        tours = random.sample(list(get_tour_covers()), 8)
        return render_template('index.html', data={'tours': tours, 'tour_heading': f'Лучшие туры'})
    
    keyword = request.args.get('keyword')
    min_price = request.args.get('min-price')
    max_price = request.args.get('max-price')
    print(keyword)
    tours = get_tours()
    print(tours[1])
    result = []
    for tour in tours:
        flag = False
        price_flag = False
        # Ищем только среди названия, описания и страны - индексы этих полей это 1, 2 и 5
        if keyword:
            for i in 1, 3, 5:
                if keyword.lower() in tour[i].lower():
                    flag = True
                    break
        else:
            flag = True 

        if min_price or max_price:
            if min_price:
                min_price = int(min_price)
                if not max_price and tour[2] >= min_price:
                    price_flag = True
                elif max_price and tour[2] >= min_price and tour[2] <= int(max_price):
                    price_flag = True
            elif max_price:
                max_price = int(max_price)
                if not min_price and tour[2] <= max_price:
                    price_flag = True
                elif min_price and tour[2] <= max_price and tour[2] >= int(min_price):
                    price_flag=True
        else:
            price_flag = True
                    
 
        if flag and price_flag:
            result.append(tour)
    
    if len(result) <= 8:
        return render_template('index.html', data={'tours': result, 'tour_heading': f'Результаты по запросу: {keyword}'})
        
    return render_template('index.html', data={'tours': random.sample(tours, 8), 'tour_heading': f'Результаты по запросу: {keyword}'})

@app.route("/tours")
def tours():
    data = get_tours()
    return render_template("tours.html", data = {"tours": data})

@app.route("/tour/<int:id>")
def tour(id):
    t = get_tour_by_id(int(id))
    return render_template("tour.html", data = {"tour": t})

app.run()