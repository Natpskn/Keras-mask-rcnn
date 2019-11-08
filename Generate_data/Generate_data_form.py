import json
import pandas as pd

from glob import glob


files = glob('./data_json/*.json')

df = pd.DataFrame()


for file in files:
    with open(file) as f:
        data = json.load(f)
        # print(data)

        try:
            path = data['imagePath']
        except:
            data = data[-1]
            path = data['imagePath']

        viz_path = "./data_json/"+ path.split('.')[0] + '_json/label_viz.png'
        ori_path = "./data_json/"+ path.split(',')[0]
        objs = data['shapes']

        for obj in objs:
            label = obj['label']
            points = obj['points']
            x, y = [], []

            for pair in points:
                x.append(pair[0])
                y.append(pair[1])

            x_min, x_max = min(x), max(x)
            y_min, y_max = min(y), max(y)

            rows = {
                "path": [path],
                "x_min": [x_min],
                "y_min": [y_min],
		"x_max": [x_max],
                "y_max": [y_max],
                "label": [label],
                "viz": [viz_path],
                "ori": [ori_path]
            }
            df = df.append(pd.DataFrame.from_dict(rows))
            
sorted_columns = ['ori', 'x_min', 'y_min', 'x_max', 'y_max', 'label', 'viz']

df[sorted_columns].to_csv('./result.csv', header=False, index=False)
