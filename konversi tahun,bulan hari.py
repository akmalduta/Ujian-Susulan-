hari = int(input('jumlah hari yang di inginkan: '))

dalam_tahun = hari//365
dalam_bulan = (hari%365)//30
dalam_minggu = ((hari%365)%30)//7
dalam_hari  = ((hari%365)%30)%7

print(f'Sama dengan {dalam_tahun} tahun, {dalam_bulan} bulan, {dalam_minggu} minggu, {dalam_hari} hari')