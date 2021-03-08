import json
import os

# with open("C:/Users/bcl/Desktop/0147.json",'r') as load_f:
#     load_dict = json.load(load_f)
#
# def load_XY(load_dict):
#     for i in range(len(load_dict['shapes'])):
#         return

def compute_k_b(load_dict):
    list = []
    #左线
    left_k = (load_dict['shapes'][1]['points'][0][1] - load_dict['shapes'][0]['points'][0][1]) / (
            load_dict['shapes'][1]['points'][0][0] - load_dict['shapes'][0]['points'][0][0])
    left_b = load_dict['shapes'][1]['points'][0][1] - left_k * load_dict['shapes'][1]['points'][0][0]
    print("左边",left_k,left_b)
    list.append(left_k)
    list.append(left_b)
    #右线
    right_k = (load_dict['shapes'][3]['points'][0][1] - load_dict['shapes'][2]['points'][0][1]) / (
                load_dict['shapes'][3]['points'][0][0] - load_dict['shapes'][2]['points'][0][0])
    right_b = load_dict['shapes'][3]['points'][0][1] - right_k * load_dict['shapes'][3]['points'][0][0]
    print("右边",right_k,right_b)
    list.append(right_k)
    list.append(right_b)
    #水平线
    h_k = (load_dict['shapes'][5]['points'][0][1] - load_dict['shapes'][4]['points'][0][1]) / (
            load_dict['shapes'][5]['points'][0][0] - (load_dict['shapes'][4]['points'][0][0]))
    h_b = load_dict['shapes'][5]['points'][0][1] - h_k * load_dict['shapes'][5]['points'][0][0]
    #print(h_k, h_b)
    list.append(h_k)
    list.append(h_b)

   # print(list)
    return list

def compute_cross(load_dict):
    list = compute_k_b(load_dict)
    left_x = []
    right_x = []
    h_x = []
    h_samples = [ 64,  68,  72,  76,  80,  84,  88,  92,  96, 100, 104, 108, 112,
            116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164,
            168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216,
            220, 224, 228, 232, 236, 240, 244, 248, 252, 256, 260, 264, 268,
            272, 276, 280, 284]

    #list1 = [-2, -2, -2, -2, -2, -2, -2, -2, 499, 484, 470, 453, 435, 418, 400, 374, 346, 318, 290, 262, 235, 207, 179, 151, 123, 96, 68, 40, 12, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
    for i in range(len(h_samples)):
        x_l = (h_samples[i] - list[1]) // list[0]
        x_r = (h_samples[i] - list[3]) // list[2]
        x_h = (h_samples[i] - list[5]) // list[4]
        if x_l > 0 and x_l < 1280:
           left_x.append(x_l)
        elif x_l < 0 or x_l > 1280:
           left_x.append(-2)

        if x_r > 0 and x_r < 1280:
           right_x.append(x_r)
        elif x_r < 0 or x_r > 1280:
           right_x.append(-2)

        if x_h > 0 and x_h < 1280:
           h_x.append(x_h)
        elif x_h < 0 or x_h > 1280:
           h_x.append(-2)
    global num
    raw_file = "C:/Users/bcl/Desktop/image/"+str(num)+".jpg"
    num = num + 1
    item_dict = {"lanes":[left_x,right_x,h_x], "h_samples":h_samples,"raw_file":raw_file}
    #return left_x, right_x, h_x
    print(item_dict, num)
    return item_dict

def list_json(path, item_list):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        print(file_path)
        with open(file_path, 'r') as load_f:
            load_dict = json.load(load_f)
            #left_x, right_x, h_x = compute_cross(load_dict)

            # print("left_x", left_x)
            # print("长度为：", len(left_x))
            #
            # print("right_x", right_x)
            # print("长度为：", len(right_x))
            #
            # print("h_x", h_x)
            # print("长度为：", len(h_x))

            item_dict = compute_cross(load_dict)
            # item_list.append(item_dict)
            # print(item_list)

            with open(r'C:\Users\bcl\Desktop\labels.json', 'a+', encoding='utf-8') as f:
                json.dump(item_dict, f, ensure_ascii=False)
                f.write('\n')

if __name__ == '__main__':
    num = 1
    path = r"C:\Users\bcl\Desktop\json"
    item_list = []
    list_json(path, item_list)

