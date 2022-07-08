﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruth")
define k = Character("Nathan")
define i = Character("Rachel")
define a = Character("Anton")
define n = Character("Narrator")

default rachelgood = False
default nathangood = False
default antongood = False
default ruthgood = False

default qtecount = 1
default qtepoint= 0

transform fullsize:
        size (1920,1080)
        on show:
            yalign 0.5 xalign 0.5

image rrumah = "dragon_afro.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rumah

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "Di suatu hari yang cerah, hiduplah satu keluarga kecil."

    n "keluarga itu terdiri dari 4 orang yaitu ayah, ibu dan kedua anaknya."

    show anton happy

    n "Anton merupakan kepala rumah tangga dari keluarga tersebut."

    n "Ayah berumur 49 tahun ini memiliki kepribadan yang rajin dan juga memiliki semangat yang tinggi untuk menafkahi keluarganya."

    n "Akan tetapi,"

    n "Anton memiliki sifat buruk yang selalu ada disaat ia mengerjakan sesuatu"

    n "Sifat buruk itu adalah..."

    n "T E L E D O R."

    n "Sifat buruk ini juga menurun ke salah satu anaknya."

    n "terlepas dari itu, sifat teledornya dengan mudah tertutupi oleh sifat baik yang dimiliki Anton"

    hide anton happy

    show rachel happy

    n "Rachel, sang ibu, pengayom dan penyayang keluarganya."

    n "Sama seperti suaminya, Rachel juga memiliki semangat yang tinggi untuk membahagiakan keluarganya."

    n "Meskipun sudah menginjak usia 50 tahun, Rachel masih memiliki tekad yang kuat dalam beraktivitas sehari-hari."

    n "Rachel cenderung lebih mengutamakan orang lain dibanding dirinya."

    n "Dari sifat tersebut, Rachel selalu memaksa dirinya untuk selalu kelihatan tangguh."

    n "Hal tersebut dilakukan agar tidak mengkhawatirkan keluarganya."

    hide rachel happy

    show nathan happy

    n "Nathan, anak pertama dari Anton dan Rachel."

    n "Ia memiliki minat dalam dunia otomotif serta bakat dalam memperbaiki kendaraan seperti motor dan mobil di umur 21 tahun."

    n "Dibalik minat dan bakatnya, Nathan merupakan orang yang teledor seperti ayahnya."

    n "Terlebih lagi saat dia lelah."

    n "Nathan cenderung melupakan hal yang sangat penting saat dia lelah."

    hide nathan happy

    show ruth happy

    n "Ruth merupakan anak bungsu di keluarga tersebut."

    n "Anak berumur 18 tahun ini memiliki semangat dan ambisi yang tinggi untuk meraih prestasi di sekolahnya."

    n "Ruth selalu mengerjakan tugas dan belajar untuk ujian agar memperoleh nilai tinggi."

    n "Tetapi karena ambisinya itu juga, ruth sering melakukan begadang yang merusak jam tidurnya."

    hide ruth happy

    n "Keluarga kecil tersebut akan bertamasya ke pulau bali."

    n "Hari ini merupakan 1 hari sebelum mereka berangkat ke bali."


    scene kamar ruth

    show Ruth ngantuk

    r "Hoaaammm...."

    r "Sekarang jam berapa ya...?"

    scene jam

    r "Whoa masih jam 6"

    r "Mau balik tidur lagi deh."

    scene kamar ruth

    show ruth ngantuk

    scene merem

    with fade

    r "Hmmmmmmm..."

    r "Susah banget balik tidur.."

    scene kamar ruth

    show ruth ngantuk

    with fade

    r "Ambil minum dulu dibawah kali ya..."

    scene ruang makan

    show ruth ngantuk

    n "Saat hendak mengambil minum, ruth melihat ibunya sedang memasak di pagi hari."

    scene dapur

    show ibu serius

    i "hm.."

    i "Oh... pakai bumbu ini..."

    i "Nanti direbus..."

    scene ruang makan

    show ruth bingung

    with fade

    menu:

        "Membantu ibu memasak." :
            scene dapur
            show rachel kesusahan
            show ruth happy at right with moveinright
            r "Ibu! sini aku bantu masaknya!"
            hide rachel kesusahan
            show rachel happy
            i "Ruth, udah nggak apa-apa."
            i "Ibu bisa sendiri kok!"
            r "Gapapa kok, aku juga mau belajar masak hehehe"
            # MINIGAME

            $ rachelgood = True

        "Mengambil air, lalu membantu ibu memasak sebentar." :
            scene ruang makan
            show ruth ngantuk
            r "Hmmm... nanti dulu deh masih capek.."
            n "Ruth meminum air, kemudian ia hendak membantu ibunya sedikit."
            scene dapur
            show ruth ngantuk at right with moveinright
            show rachel kesusahan
            r "Bu, aku bantu-bantu dikit gapapa ya."
            i "Ah iya gapapa kok."
            i "Ibu udah susah motong-motong sekarang.."
            r "Iya, Aku aja yang motong."
            # MINIGAME

        "Menyapa ibu, mengambil air dan kembali tidur." :
            scene ruang makan
            show ruth happy
            r "Selamat pagi ibu!"
            i "Iya selamat pagi Ruth!"



    scene ruang makan

    n "waktu menunjukkan pukul 8."

    n "Keluarga kecil itu menyantap sarapan yang telah dihidangkan sambil bersenda gurau."

    scene ruang keluarga
    with fade

    show nathan bingung

    k "Hm... apa nanti aku lulus jadi pembalap aja ya.."

    k "Gajinya gede sih.. resikonya tinggi juga.."

    hide nathan bingung

    show nathan sombong

    k "Tapi tetep gajinya gede!"

    i "Nathan."

    hide nathan sombong

    show nathan malu

    k "He... iya bu?!"

    show nathan malu at left with move
    show ibu happy at right with moveinright

    show nathan happy at left

    i "Kamu mulai tata barang-barang kamu dulu.."

    i "Besok kan kita mau berangkat, nanti kalo mepet-mepet, celananya ketinggalan."

    hide ibu happy
    show ibu sombong at right

    hide nathan happy
    show nathan malu at left

    i "Kayak tahun lalu~"

    i "Ibu inget banget kamu turun gunung pakai sarungnya ayah, abis it-"

    k "IYA BU IYAA!"

    hide nathan malu with moveoutleft

    scene kamar nathan

    show nathan serius

    k "Hmm..."

    k "Butuh apa aja ya...?"

    hide nathan serius
    show nathan kesusahan

    k "Duh sakit kepala lagi gara-gara main hp kelamaan.."

    hide nathan kesusahan
    show nathan sombong

    k "Oh iya!"

    k "Hehehehe"

    scene kamar ruth

    show ruth happy

    with fade

    r "Ini loncat kesini.."

    r "Ayo!"

    r "Yes! akhirnya bisa santai-santai setelah sekian lama-"

    hide ruth happy
    show ruth bingung

    k "RUUUUUUTTHHHHHHHHH!"

    show ruth bingung at right with move
    show nathan happy at left with moveinleft

    r "Apa- apa- kenapa?!"

    k "Ruth, bantuin aku beres-beres yaaaa"

    hide ruth bingung
    show ruth marah at right


    r "Iiiih kakak lagian gak beres-beres dari kemarin disuruh ibu!"

    hide nathan happy
    show nathan sedih at left
    k "Ya kan kakak kuliah..."

    k "Banyak tugas..."

    k "Trus kegiatan juga banyak..."

    k "Bantuin ya..."

    menu:

        "Meninggalkan game dan langsung menolong kakak dalam menyusun perlengkapan barang." :
            hide ruth bingung
            show ruth happy at right
            r "Ayo kak kita susun sekarang!"
            hide nathan sedih
            show nathan happy at left
            k "Yeeeeyyy ayooo!"
            scene kamar nathan
            show ruth serius at right
            show nathan happy at left
            r "Oh... okeokee bisa kok ini!"
            k "Makasih banget ya adekku yang cantik~"
            #MINIGAME
            scene kamar nathan
            show ruth serius at right
            show nathan happy at left
            r "Kak jangan lupa lho ini inhaler."
            hide nathan happy
            show nathan malu at left
            k "Ohiya hehe aku lupa..."
            $ nathangood = True


        "Menolong kakak setelah selesai bermain game." :
            hide ruth bingung
            show ruth serius at right
            r "Kakak duluan aja nanti aku nyusul."
            hide nathan sedih
            show nathan happy at left
            k "Oh iyaa? okee aku tunggu yaaaa!"
            hide nathan happy with moveoutleft
            scene kamar ruth
            "*10 menit berlalu*"
            show ruth happy
            r "Oke waktunya bantu kakak."
            scene kamar nathan
            show nathan kesusahan at left
            show ruth happy at right with moveinright
            r "Ayo kak sini aku bantuin!"
            hide nathan kesusahan
            show nathan happy at left
            k "Akhirnya dateng juga!"
            #MINIGAME

        "Lanjut bermain game dan membiarkan kakak menyusun perlengkapan sendiri." :
            hide ruth bingung
            show ruth marah at right

            r "Kakak Beresin sendiri aja ihhhhh"
            r "Aku lagi santai-santai ini udah lama gak main game!"
            k "Hmmm yaudah deh..."

    n "Kemudian barang-barang Nathan berhasil tersusun."

    scene kamar nathan

    n "Langit yang berwarna jingga menunjukkan sore hari."

    show nathan ngantuk

    n "Nathan hendak tidur setelah menyusun barang-barangnya untuk berpergian besok."

    "*KRINGGGGG*"

    k "Hm.?"

    "*KRINGGGGGG*"

    k "Halo?"

    a "Kakak."

    k "Ah iya kenapa yah?"

    a "Bisa tolong bantu ayah?"

    hide nathan ngantuk
    show nathan bingung

    a "Jadi mobil lagi rusak..."

    a "Besok kan mau dibawa buat jalan-jalan."

    a "Bisa tolong bantu ayah merbaikin nggak?"

    menu:
        "Bergegas menolong ayah." :
            k "Oke ayah.. aku ke garasi ya!"
            scene garasi
            show anton happy
            show nathan happy at right with moveinright
            k "Ayoo ayah! kita perbaikin bareng-bareng!"
            a "Oke nak, Makasih banyak ya!"
            $ qtepoint = 10
            jump qte
            label goodqte:
            $ antongood = True

        "Berbaring sebentar untuk mengumpulkan nyawa, baru menolong ayah" :
            k "Sebentar ya ayah... aku tiduran dulu..."
            a "Baik nak, ayah di garasi ya nanti."
            "*20 menit berlalu*"
            scene garasi
            show ayah kesusahan
            show nathan serius at right with moveinright
            k "Yang kurang dimana ayah?"
            a "Oh ini tinggal bagian bawah mesin aja.."
            k "Oke sini aku bantu."
            $ qtepoint = 5
            jump qte
            label badqte:

        "Kembali tidur karena masih mengantuk." :
            k "Aku masih capek yah.. gabisa fokus nanti..."
            a "Ooh oke deh nak, maaf ya ganggu tidurnya..."

    scene kamar nathan

    n "Setelah mobil sudah diperbaiki, tidak terasa hari sudah menuju malam."

    n "Sudah saatnya keluarga kecil itu untuk beristirahat."

    n "Akan tetapi..."

    show nathan happy

    k "Eh nanti aja diomongin di kampus biar semua pada ngumpul"

    k "Gaenak kalo disini masi-"

    hide nathan happy
    show nathan bingung

    r "TIDAAAAAAAKKKKK!!"

    k "Duh kenapa si Ruth teriak-teriak, udah malem juga"

    scene kamar ruth

    show ruth kesusahan

    show nathan bingung at left with moveinleft

    k "Kamu kenapa teriak-teriak sih udah malem juga."

    k "untung bukan ayah yang kesini."

    r "Duhh kakkkkkk!"

    r "Aku lupa hari ini ujian online..."

    r "Mana susah banget lagi ini.."

    menu:

        "Inisiatif membantu adiknya dan berhenti mengobrol dengan teman online" :
            hide nathan bingung
            show nathan serius at left
            k "Oke sini kakak bantuin kamu"
            hide ruth kesusahan
            show ruth happy
            r "WIIII BENERAN YA KAK?!"
            k "Iyaa"
            $ hangmanGame("asean","asosiasi negara asia tenggara")
            $ hangmanGame("manila","ibukota filipina")
            $ hangmanGame("vietnam","Negeri naga biru")
            $ hangmanGame("brunei","Letak istana negara terbesar di dunia")
            $ hangmanGame("indonesia","Negara terbesar di asean")
            scene kamar ruth
            show nathan serius at left
            show ruth serius
            k "Terus jawab yang ini... selesai!"
            hide ruth serius
            show ruth happy
            r "YEEEEYYY SELESAIII!"
            r "Makasih banyak kakkk! hihihi"
            r "Nanti aku traktir deh di balii~"
            hide nathan serius
            show nathan happy at left
            k "Bener ya? hehehe"
            $ ruthgood = True

        "Membantunya nanti karena masih mengobrol dengan teman online." :
            hide nathan bingung
            show nathan serius at left
            k "Yaudah aku bantu, tapi nanti aku mau ngobrol sebentar."
            r "Ah iya kak?!"
            k "Iya tapi kamu kerjain sendiri dulu sebentar"
            hide nathan serius with moveoutleft
            r "Iya iya.. makasih ya kak!"
            "*30 menit telah berlalu*"
            scene kamar ruth
            show ruth kesusahan at right
            show nathan sombong at left with moveinleft
            k "Sini sini sini aku bantu."
            hide ruth kesusahan
            show ruth happy
            r "Yeaaayyy!"
            $ hangmanGame("bintang","Lambang sila pertama pancasila")
            $ hangmanGame("yogyakarta","Ibukota Indonesia tahun 1949")
            $ hangmanGame("habibie","Presiden ke-3 indonesia")
            $ hangmanGame("kalimantan","pulau terbesar ke-2 di indonesia")
            $ hangmanGame("borobudur","candi terbesar di indonesia")



        "Kembali mengobrol dengan teman." :
            hide nathan bingung
            show nathan serius at left
            k "Yaudah jangan berisik ya aku lagi sama temen-temen."
            hide ruth kesusahan
            show ruth sedih
            r "Iya... maaf ya kak..."


    scene rumah
    n "Saatnya keluarga kecil itu hendak berangkat di hari yang cerah ini."

    n "Semua sudah disiapkan satu persatu untuk berlibur di pulau bali nanti."

    #################ENDING#################

    label ending:
    if rachelgood == True and nathangood == True and antongood == True and ruthgood == True:
        jump goodend
    elif rachelgood == False:
        jump rachelbad
    elif nathangood == False:
        jump nathanbad
    elif antongood == False:
        jump antonbad
    elif ruthgood == False:
        jump ruthbad


    label goodend:
    scene mobil
    n "Keluarga kecil itupun berangkat ke dermaga agar bisa ke Bali."
    scene goodend
    n "Sesampainya di Bali, mereka dapat menikmati waktu liburannya sampai di hari terakhir."
    n "Hal seperti ini yang menjadi buah dari sifat saling tolong menolong antar anggota keluarga."
    "GOOD END"
    return

    label rachelbad:
        scene rachel bad
    n "Rachel terbaring sakit karena demam."

    n "Hal ini disebabkan oleh Rachel yang memaksakan dirinya untuk memasak di pagi buta."

    show rachel sedih at left
    i "Maafin ibu ya nak.. jadinya liburan kita diundur..."
    show ruth sedih at center
    show nathan sedih at right

    k "Udah bu gapapa... bukan salah ibu juga.."

    r "Iya bu.. maafin ruth ya... harusnya aku bantu ibu kemarin..."

    hide rachel sedih
    hide ruth sedih
    hide nathan sedih
    show anton sedih

    a "Udah nak.. kita masih bisa pergi, tapi diundur aja."

    scene blackscreen

    "BAD END."

    return

    label nathanbad:
        scene mobil jalan

        n "Keluarga kecil itu di tengah jalan ke dermaga untuk menaiki kapal feri ke bali."

        n "namun di tengah perjalanan..."

        scene nathan bad
        show nathan kesusahan
        k "*uhuk**uhuk*"
        k "*uhuk**uhuk**uhuk**uhuk*"
        k "*uhuk**uhuk**uhuk*"
        show ruth bingung at right
        r "Kakak kenapa kak"
        k "*uhuk**uhuk*"
        show rachel bingung at left
        i "Ruth tolong ambilkan inhaler kakak ada di tasnya."
        r "Gaada bu!"
        k "*uhuk**uhuk**uhuk**uhuk*"
        hide ruth bingung
        show ruth sedih at right
        r "Aduuuhhhh gimana ini"
        i "Ayah kita cari apotek dulu ya."
        k "*uhuk**uhuk**uhuk**uhuk*"
        hide nathan kesusahan
        show anton sedih
        a "Hm.. gaada yang deket kalo disini apoteknya..."
        a "Terpaksa kita harus pulang dulu.."
        a "Kita tunda dulu aja perginya... biarkan nathan istirahat dulu."
        scene blackscreen
        "BAD END"
        return
    label antonbad:

        scene mobil
        n "Keluarga kecil itu siap berangkat ke dermaga menggunakan mobil."

        n "Namun, Anton merasakan ada hal yang aneh saat ia membawa mobil itu."

        "*krkrkrkrk*"

        show anton bingung

        a "hm?"

        hide anton bingung

        "*BRRR KRKRKRK BRRRRK*"

        "*CSSSSSSS*"

        show rachel bingung at left

        i "Ayah, kenapa mobilnya?"

        show anton bingung

        a "Aduhhh"

        show nathan sedih at right

        k "Yah mogok ya...."

        a "Ah... iya mogok..."

        show anton serius

        hide anton bingung

        a "Coba ayah liat dulu."

        show nathan serius at right

        k "Aku ikut ayah."

        scene anton bad

        show anton sedih
        show nathan sedih at left

        k "Yah.... ini harus dibawa ke bengkel..."

        a "Iya... ayah juga gabawa perlengkapan buat merbaikin disini..."

        a "Yaudah deh nak gapapa, kita cari bengkel dulu aja."

        a "Sementara kita tunda aja dulu liburannya."

        a "Masih ada hari lain kok."
        scene blackscreen
        "BAD END"
        return


    label ruthbad:

        scene kamar ruth
        show ruth kesusahan
        r "Aduh... masih belom selesai ujiannya..."
        a "Ruth! ayo turun! kita mau jalan lho!"
        scene ruth bad
        r "Ayah maaf, aku gabisa ikut deh kayaknya...."
        a "Lah kenapa?"
        r "Aku masih harus ngejar ujianku..."
        r "Ruth jaga rumah aja gapapa ya.."
        r "Soalnya beneran harus selesai ini..."
        a "Yaudah, kita perginya ke rumah sodara aja besok.."
        a "Biar semua bisa pergi bareng-bareng."
        scene blackscreen
        "BAD END"
        return

    ########MINIGAME#########
    label pnc:
        scene rak dapur


    label dnd:
        scene lantai koper



        label qte:
            scene mesin at fullsize

    $ cont = 0 #variabel continue

    call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # Memanggil Fungsi qte_setup

    while cont == 1 and qtecount < qtepoint: # Fungsi pengulangan
        call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        $ qtecount += 1 #increment

    if qtecount == 10 and qtepoint == 10: #Jika mencapai 10 ronde
        "COMPLETED"
        jump goodqte

    elif qtecount == 5 and qtepoint == 5: #Jika mencapai 5 ronde
        "COMPLETED"
        jump badqte

    else:   #jika player salah klik/waktu habis
        play sound "sounds/miss.mp3"
        "{b}GAME OVER{/b}"
        $ qtecount = 1
        jump qte


label qte_setup(time_start, time_max, interval, x_align, y_align):  #fungsi game QTE

    $ time_start = time_start   #Waktu
    $ time_max = time_max       #waktu max
    $ interval = interval       #Jarak pengurangan waktu
    $ x_align = x_align         #koordinat lokasi X
    $ y_align = y_align         #Koordinat lokasi Y

    call screen qte_button #memanggil qte_button di qte.rpy

    $ cont = _return # return 1 jika tombol tertekan dengan tepat waktu dan 0 jika tidak



init python:
    #first we define our images of hangman 0 - 4 (5 images) (take out the comments when you put your own images in )
    #    for i in range(5):
    #        #images are named slide0.png...slide9.png
    #        renpy.image('hangman%d' % i, 'hangman%d.png' % i)

        def hangmanGame( word, hint ):        #membuat fungsi hangman
            hintword = hint                   #hint
            finishedWord = word               #kata yang ingin dimasukkan
            finishedWord = finishedWord.upper() #.upper membuat string menjadi uppercase
            lettersUsed = ""
            i = 0
            myString = ""
            while (i < len(finishedWord)):  #Fungsi pengulangan simbol * agar setara dengan panjang kata
                myString += "*"
                i+=1
            lettersUsed = ""

            while(finishedWord != myString) :
                ui.text("Your word:" + myString + " \nLetters Used so Far: " + lettersUsed + "\n Guesses Left:" +str(5 - len(lettersUsed)) + " \nHint: " + hintword )
                newLetter = renpy.input("What letter whould you like to get?", "", length=1)
                newLetter = newLetter.upper()
                foundSomething = False;
                i = 0
                while( i < len(finishedWord)) :
                    if(finishedWord[i] == newLetter[0]):
                        myString = myString[0:i] + newLetter[0]+ myString[i+1:]
                        foundSomething = True
                    i+=1
                if(foundSomething == False):
                    lettersUsed += newLetter[0]
                    # This is where I would show a new graphic if I had graphic files to show
                    # renpy.show('hangman%d' % len(lettersUsed))
                    if(len(lettersUsed) >= 5):
                        renpy.jump('lose')
            renpy.jump('win')





    # This ends the game.
            return
