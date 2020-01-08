import random
loop = True
while loop: #otomatis true
    print("masukan calon jodohmu")
    print("1. Masukkan Nama Cowok")
    print("2. Masukkan nama cewek")
    jodoh = input ("Pilih Nomor: ")
    if jodoh=='1':
         pria = input ("masukan nama pria: ")
         print ("nama cowok",pria)
    elif jodoh=='2':
        cewek = input ("masukan nama cewek: ")
        print ("nama cewek",cewek)
    loop = False
    confrim = input ("apakah nama dimasukan sudah benar? y/n :")
    if confrim =="y":
        match = random.randrange(0,100)
        print('peluang mendapat jodoh',match, '%')
        if  match > 80: 
            print ("calon yang tepat")
        elif  match > 60:
            print ("butuh di perjuangkan")
        elif  match > 40:
            print ("coba dipertimbangkan ")
        elif  match > 0:
            print ("tidak cocok")
    tips = input ("maukah mendapatkan tips agar tidak jomblo ? ya/tidak :")
    if tips  =="ya":
        print ("caranya")
        mylist = ["bergerak","mencari", "bermain tiktok"]
        random.shuffle(mylist)
        print(mylist)         
    elif confrim =="n" :
        break

    
    


      
    
                
        


