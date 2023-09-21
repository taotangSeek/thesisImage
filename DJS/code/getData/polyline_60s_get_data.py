import csv


def extract_data_from_csv(filename, start_row, num_rows, isChange = True):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        for row in rows[start_row:start_row + num_rows]:
            data_0 = float(row[0])
            if isChange == False:
                data_0 /= 1000
            data.append(data_0)  # Assuming there's only one column in the CSV
    return data


def get_bandwidth_by_n():
    num_rows = 61
    k_3G = 10
    k_4G = 11198
    k_CS = 304650
    k_NYU = 77995
    k_5G = 110649
    filename_3G = "E:/work/webrtc/thesisImage/DJS/data/bandwidth/3G_bandwidth.csv"
    filename_4G = "E:/work/webrtc/thesisImage/DJS/data/bandwidth/4G_bandwidth.csv"
    filename_CS = "E:/work/webrtc/thesisImage/DJS/data/bandwidth/CTAM_total.csv"
    filename_NYU = "E:/work/webrtc/thesisImage/DJS/data/bandwidth/NYU_dataset.csv"
    filename_5G = "E:/work/webrtc/thesisImage/DJS/data/bandwidth/5G_bandwidth.csv"

    extracted_data_3G = extract_data_from_csv(filename_3G, k_3G, num_rows)
    extracted_data_4G = extract_data_from_csv(filename_4G, k_4G, num_rows)
    extracted_data_CS = extract_data_from_csv(filename_CS, k_CS, num_rows, False)
    extracted_data_NYU = extract_data_from_csv(filename_NYU, k_NYU, num_rows)
    extracted_data_5G = extract_data_from_csv(filename_5G, k_5G, num_rows)

    return [extracted_data_3G, extracted_data_4G, extracted_data_CS, extracted_data_NYU, extracted_data_5G]
