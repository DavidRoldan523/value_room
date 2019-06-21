import requests
if __name__ == '__main__':
    url2 = "https://api.semrush.com/" \
           "?type=domain_adwords" \
           "&key=b1915aca05c569c0d3c48205c7e673be" \
           "&display_limit=200" \
           "&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Vu,Tr,Tc,Co,Nr,Td" \
           "&domain=tigo.com.sv" \
           "&display_sort=po_asc" \
           "&database=us"
    response_videos = requests.get(url2)
    print(response_videos.text)


