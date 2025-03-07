# thư viện hỗ trợ lấy mã html của trang web thông qua url
import requests

# lấy mã html của một trang web và trả về dạng string
def get_html_source_as_string(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred fetching the URL: {e}")
        return None

# lấy sub links của mỗi trang web và lưu vào một list
def get_sublinks(url) :  
    html_source = get_html_source_as_string(url)
    sublinks = []

    substring = "<div class=\"image cover\">\n												<a href=\""
    len_sub_string = len(substring)

    for i in range(len(html_source)) :
        if (html_source[i] == "<" and html_source[i + 1] == "d") :
            match = True
            j = 0
            while (j < len_sub_string) :
                if (html_source[i + j] != substring[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                sublink = ""
                while (html_source[i + j] != "\"") :
                    sublink += html_source[i + j]
                    i += 1
                sublinks.append(sublink)
                i = i + j + 1
    return sublinks

# xóa tất cả substring của một string
def remove_all_substring(string, substring):
    new_string = ""
    i = 0
    while i < len(string):
        if string[i:].startswith(substring):
            i += len(substring)
        else:
            new_string += string[i]
            i += 1
    return new_string

# lấy data của một trang web thông qua url và ghi vào filepath với số thực tự no và quận district
substring1 = "<h1 class=\"uk-panel-title\"><span>"
len_sub_string1 = len(substring1)

substring2 = "<strong class=\"price\">\n"
len_sub_string2 = len(substring2)

substring3 = "Diện tích:</strong>"
len_sub_string3 = len(substring3)

substring4 = "Phòng ngủ:</strong>"
len_sub_string4 = len(substring4)

substring5 = "Phòng WC:</strong>"
len_sub_string5 = len(substring5)

substring6 = "Địa chỉ:</strong> "
len_sub_string6 = len(substring6)

substring7 = "Ngày đăng:</strong>"
len_sub_string7 = len(substring7)

substring8 = "Nội dung tin đăng</span>"
len_sub_string8 = len(substring8)

def get_data_to_csv(url, file_path, no, district) :
    html_source = get_html_source_as_string(url)

    title = ""
    price = ""
    area = ""
    bedrooms = ""
    WCs = ""
    # address = ""
    postdate = ""
    description = ""

    for i in range(len(html_source)) :
        # get title
        if (html_source[i] == "<" and html_source[i + 1] == "h" and html_source[i + 2] == "1") :
            match = True
            j = 0
            while (j < len_sub_string1) :
                if (html_source[i + j] != substring1[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (html_source[i + j] != "<") :
                    title += html_source[i + j]
                    i += 1
                i = i + j + 1
                
        # get price
        if (html_source[i] == "<" and html_source[i + 1] == "s" and html_source[i + 2] == "t") :
            match = True
            j = 0
            while (j < len_sub_string2) :
                if (html_source[i + j] != substring2[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while ((html_source[i + j] < '0' or html_source[i + j] > '9') and html_source[i + j] != '<') :
                    i += 1
                if (html_source[i + j] != '<') :
                    while (html_source[i + j] != " ") :
                        price += html_source[i + j]
                        i += 1
                if (price == "") :
                    price = "TT"
                i = i + j + 1 

        # get area
        if (html_source[i] == "D" and html_source[i + 1] == "i" and html_source[i + 2] == "ệ") :
            match = True
            j = 0
            while (j < len_sub_string3) :
                if (html_source[i + j] != substring3[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (html_source[i + j] < '0' or html_source[i + j] > '9') :
                    i += 1
                while (html_source[i + j] != " ") :
                    area += html_source[i + j]
                    i += 1
                i = i + j + 1 

        # get bedrooms
        if (html_source[i] == "P" and html_source[i + 1] == "h" and html_source[i + 2] == "ò"
            and html_source[i + 6] == "n") :
            match = True
            j = 0
            while (j < len_sub_string4) :
                if (html_source[i + j] != substring4[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (html_source[i + j] < '0' or html_source[i + j] > '9') :
                    i += 1
                while (html_source[i + j] != " ") :
                    bedrooms += html_source[i + j]
                    i += 1
                i = i + j + 1 
        
        # get WCs
        if (html_source[i] == "P" and html_source[i + 1] == "h" and html_source[i + 2] == "ò"
            and html_source[i + 6] == "W") :
            match = True
            j = 0
            while (j < len_sub_string5) :
                if (html_source[i + j] != substring5[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (html_source[i + j] < '0' or html_source[i + j] > '9') :
                    i += 1
                while (html_source[i + j] != " ") :
                    WCs += html_source[i + j]
                    i += 1
                i = i + j + 1     

        # get postdate
        if (html_source[i] == "N" and html_source[i + 1] == "g" and html_source[i + 2] == "à") :
            match = True
            j = 0
            while (j < len_sub_string7) :
                if (html_source[i + j] != substring7[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (html_source[i + j] < '0' or html_source[i + j] > '9') :
                    i += 1
                while (html_source[i + j] != "\"") :
                    postdate += html_source[i + j]
                    i += 1
                i = i + j + 1   

        # get description    
        if (html_source[i] == "N" and html_source[i + 1] == "ộ" and html_source[i + 2] == "i") :
            match = True
            j = 0
            while (j < len_sub_string8) :
                if (html_source[i + j] != substring8[j]) :
                    match = False
                    break
                j += 1
            if (match) :
                while (i + j + 4 < len(html_source) and (html_source[i + j] != '<' or html_source[i + j + 1] != 'b'
                       or html_source[i + j + 2] != 'r' or html_source[i + j + 3] != ' '
                       or html_source[i + j + 4] != '/')):
                    i += 1
                i = i + 8
                while (i + j + 3 < len(html_source) and (html_source[i + j] != '<' or html_source[i + j + 1] != '/'
                       or html_source[i + j + 2] != 'p' or html_source[i + j + 3] != '>')) :
                    description += html_source[i + j]
                    i += 1
                i = i + j + 1          

                description = remove_all_substring(description, "<br />")
                description = description.replace('\n', '|')
                description = description.replace('\r', ' ')

    with open(file_path, 'a') as f :
        f.write(str(no) + "," + price + ",\"" + title + "\"," + area + "," + bedrooms + ","
            + WCs + ",\"" + district + "\"," + postdate + ",\"" + description + "\"\n")

# cào dữ liệu từ trang web
data_size = 0
districts = ['quan-1', 'quan-2', 'quan-3', 'quan-4', 'quan-5',
            'quan-6', 'quan-7', 'quan-8', 'quan-9', 'quan-10',
            'quan-11', 'quan-12', 'binh-chanh', 'binh-tan', 'binh-thanh',
            'can-gio', 'cu-chi', 'go-vap', 'hoc-mon', 'nha-be', 
            'phu-nhuan', 'tan-binh', 'tan-phu', 'thu-duc']


filepath = "../Data/crawl_data.csv"
with open(filepath, 'w') as f:
    f.write("No,Price,Title,Area,Bedrooms,WCs,District,Postdate,Description\n")
    
for district in districts :
    i = 0
    while (True) : 
        i += 1
        sublinks = get_sublinks("https://batdongsan.vn/ban-nha-" + district + "-ho-chi-minh/p" + str(i))
        if len(sublinks) == 0 :
            break
        for j in range(len(sublinks)) :
            data_size += 1
            get_data_to_csv(sublinks[j], filepath, data_size, district)
            print(f"Record {data_size} is done...")

print("Get dataset done !")