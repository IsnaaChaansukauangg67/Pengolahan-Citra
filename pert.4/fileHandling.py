#def get_jpeg_size(filename):
#   with open(filename, 'rb') as f:
#       f.seek(0)
#       while True:
 #           byte = f.read(1)
  #          if not byte:
   #             break
    #        # cari marker FF C0 (Start of Frame)
     #       if byte == b'\xFF':
      #          marker = f.read(1)
       #         if marker == b'\xC0':  # SOF0
        #            f.read(3)  # skip 3 bytes
         #           height = int.from_bytes(f.read(2), 'big')
          #          width = int.from_bytes(f.read(2), 'big')
           #         return width, height
  #  return None

#ukuran = get_jpeg_size("mic.bing.jpeg")
#if ukuran:
 #   print("Lebar:", ukuran[0], "px")
  #  print("Tinggi:", ukuran[1], "px")
   # print("Jumlah pixel:", ukuran[0] * ukuran[1])
#else:
 #   print("Ukuran tidak ditemukan")
with open("mic.bing.jpeg", "rb") as f:
    data = f.read()
    print("Ukuran file:", len(data), "byte")
