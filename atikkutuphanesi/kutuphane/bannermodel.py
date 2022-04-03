


class Banner2:
     def __init__(self,urlname = "", whatisit = "",whyimportant ="",whereaccurs="",howunderstand="",mainname ="") -> None:

          self.urlname = urlname
          self.whatisit = whatisit
          self.whyimportant = whyimportant
          self.whereaccurs = whereaccurs
          self.howunderstand = howunderstand
          self.mainname = mainname

#tıbbi atık 
s = "Öncelikle atığın insan veya hayvan sağlığına müdahale amacıyla ve/veya bu amaca yönelik bir tanı, teşhis, tedavi, araştırma vb. süreç esnasında mı oluştuğunu dikkate almalısınız. \nAtık herhangi bir sağlık hizmeti verilmesi (dövme ve akupunktur gibi kan ile temas içeren müdahaleler de dahildir) veya buna yönelik bir araştırma esnasında oluşmamışsa tıbbi atık değildir.\nAtık kaynağı teyit edildikten sonra atığın kesici-delici özellikte olup olmadığına bakılabilir. Atık, kesici-delici bir özellik taşıyor ise tıbbi atıktır. Atık, içerisinde herhangi bir kimyasal işlem görmemiş patolojik ögeler barındırıyor ise (doku-organ parçaları, fetüs vb.) tıbbi atıktır. Son olarak atık, enfeksiyon yapıcı etkenleri taşıdığı bilinen veya taşıması muhtemel maddeleri içeriyor ise veya bu maddeler ile bulaşmış ise yine tıbbi atıktır. "
tibbi_atik = Banner2()
tibbi_atik.urlname = "Tıbbi Atık"
tibbi_atik.whatisit = "Tıbbi atıklar sağlık hizmeti verilen, sağlık hizmetlerine yönelik araştırmalar yapılan yerler veya dövme, akupunktur gibi hijyenik hizmetler sunan yerlerde oluşan kesici-delici, patolojik ve/veya enfeksiyon yapıcı atıklardır. "
tibbi_atik.whyimportant = "Tıbbi atıklar, eğer doğru yönetilmez ise, insanlara ve hayvanlara hastalık bulaşmasına ve salgınlara yol açabilir. "
tibbi_atik.whereaccurs ="İnsan ve hayvan sağlığına yönelik hizmet veren servisler; hastaneler başta olmak üzere, revirler, diyaliz merkezi, fizik tedavi merkezi, poliklinik, kan merkezi, acil müdahale birimleri, mikrobiyoloji laboratuvarları, diş hekimliği, veteriner klinikleri vb. özel klinikler, insan ve hayvan sağlığına yönelik araştırmalar yapan kuruluşlar (üniversiteler, laboratuvarlar, araştırma merkezleri), dövme salonları, akupunktur merkezlerinde oluşur."
tibbi_atik.howunderstand = s
tibbi_atik.mainname = "TIBBİ ATIK"

#atık lastik 
atik_lastik = Banner2()
atik_lastik.urlname = "Atık Lastik"
atik_lastik.whatisit = "Atık lastik veya ömrünü tamamlamış lastik (ÖTL), faydalı ömrünü tamamladığı sonucuna varılarak araçlardan sökülen, bir daha kullanılamayacak durumda olan, ve üretimi esnasında ortaya çıkan ıskarta atıklarıdır. "
atik_lastik.whyimportant = "OLUŞAN ATIK LASTİKLERİN; HAVA, SU, TOPRAK, BİTKİ VE HAYVANLARA ZARAR VERMEDEN VE ÇEVREYİ ETKİLEYECEK HERHANGİ BİR OLUMSUZLUK BULUNMADAN GERİ KAZANIMI VE BERTARAFI ESASTIR. YÖNETMELİĞE GÖRE; ÖTL’LER DOLGU MALZEMESİ OLARAK KULLANILMAMALI, KATI ATIK DEPOLAMA TESİSLERİNE KABÜLÜ VE DEPOLANMASI, ISINMADA KULLANILMASI VE HERHANGİ BİR BAŞKA AMAÇLA YAKILMASI YASAKTIR. BELİRLENEN YÖNTEMLERE UYULMADIĞI TAKDİRDE ÇEVRESEL SORUNLARA NEDEN OLABİLİR. DAHASI; DÜZENLİ DEPOLAMA SAHALARINDA BERTARAF YÖNTEMİ UYGULANDIĞINDA, ZEHİRLİ GAZLAR OLUŞMASI MUHTEMELDİR. OLUŞAN BU ZEHİRLİ GAZLAR İSE BELİRLİ BASINÇLARDA PATLAMALARA NEDEN OLUR.  "
atik_lastik.whereaccurs = "Araç ihtiyacının bulunduğu herhangi bir sektörde lastik atıklarının çıkması kaçınılmazdır. Bunun dışında ise üretimi esnasında oluşan ıskarta lastikler de bu kategori altında bulunmaktadır. Ömrünü tamamlamış lastikler ise ikincil kullanım olmak üzere; balık yerleşimleri için uygun ortam yaratan yapay kayalıklarda, oyun parklarında, araç park alanlarında ve iskelelerde gemi tamponu olarak değerlendirilmektedir. Bu yüzden, lastik atıkları bu şekilde de oluşabilir. "
atik_lastik.howunderstand ="Birincil kullanım amacına uygun bir şekilde kullanılamayacak durumda ise atık lastik olduğu söylenebilir. "
atik_lastik.mainname = "ATIK LASTİK"
 
 #atık yağ 
atik_yag = Banner2()
atik_yag.urlname = "Atık Yağ"
atik_yag.whatisit = "Atık yağ orijinal kullanım amacına uygun olmayan ve Atık Yağların Yönetimi Yönetmeliği Ek-1’de atık kodları yer alan madeni yağlardır (Atık Yağların Yönetimi Yönetmeliği, 2019).  "
atik_yag.whyimportant = "Atık yağlar; toprak, kanalizasyon, denizler gibi alıcı ortamlara verilmesi, yakıt olarak kullanılması, uygun olmayan yöntemler ile geri kazandırılması, yakılması ve bertarafı ile çeşitli çevresel sorunlara yol açabilir. Bu doğrultuda “Atık Yağların Yönetimi Yönetmeliği” kapsamında uygun şekilde yönetilmelidir.  "
atik_yag.whereaccurs = "Birçok motor ve mekanizmanın çalışması için madeni yağlara ihtiyaç vardır. Bu yağların yaklaşık yarısı atık yağ olacaktır. Gerisi kullanım sırasında veya sızıntı yoluyla kaybolur. Oluşan atık madeni yağların tümü tehlikeli atık olarak. Aynı zamanda, atık madeni yağların depolandığı ambalajlar da tehlikeli atık olarak gözetilmelidir. "
atik_yag.howunderstand = "Sanayi veya sanayi dışı alanlarda özellikle yağlama ve makinaların çalışması için kullanılan bu yağlar belirli süreden sonra fiziksel veya kimyasal olarak kirlenmesi ile birlikte orijinalliğini kaybetmektedir. Normal kullanım esnasında kir, metal sürtünmeleri, su veya kimyasallar ile kirlenerek rengi koyulaşır ve kullanılamaz duruma gelir. Buna ek olarak, uzun kullanımdan dolayı makinalar veya hangi alanda kullanılıyorsa verimli bir performans elde edilememektedir. Yukarıda belirtildiği üzere, rengi ve performansına bakılarak yağ hakkında yorum yapmak ve buna uygun atığın yönetilmesi mümkündür. "
atik_yag.mainname = "ATIK YAĞ"

#Atık Pil ve Akümülatör
atik_pil = Banner2()
atik_pil.urlname = "Atık Pil ve Akümülator"
atik_pil.whatisit = "Kullanım ömrü dolmuş, son kullanma tarihi geçmiş veya uğramış olduğu fiziksel hasardan dolayı yeniden kullanılabilecek durumda olmayan; evsel atıklardan ayrı olarak toplanması, taşınması ve bertaraf edilmesi gereken atıklar atık pil olarak tanımlanmaktadır."
atik_pil.whyimportant = "Atık pillerin içerisindeki çeşitli kimyasal maddeler vahşi çöp depolama alanlarından sulama sularına ve toprağa karışarak çevre kirliliği yaratabilir. Bu yüzden, çevreye veya çöpe atılmamalı, toprağa gömülmemeli, herhangi bir alıcı su ortamıyla temas ettirilmemeli ve yakılmamalıdır. "
atik_pil.whereaccurs ="Piller primer ve sekonder olmak üzere iki ayrı grupta incelenmektedir. Primer piller veya alkali piller düşük oranda enerji üreten cihazlar için kullanılır.  Sekonder piller ise şarj edilebilen bir pil türüdür ve güç aletleri, aydınlatma vb. aletlerde kullanılmaktadır. Akümülatörler ise otomobillerde ve özellikle endüstriyel amaçlı kullanılmaktadır. "
atik_pil.howunderstand = "İşlevini sürdürememekte, ana görevini yerini getiremeyen ve deforme olmuş her tür pil ve akümülatör atık olarak değerlendirilir. Cihazların çalışması için kullanılan her tür pil ve özellikle endüstri de otomotiv sanayiinde kullanılan akü, batarya gibi enerji depolanmasına yardımcı olan pil kategorileri de işlevlerini yitirdiğinde atık olarak gözetilmektedir. "
atik_pil.mainname = "ATIK PİL VE AKÜMÜLATOR"

#Bitkisel Atık Yağ 
bitkisel_yag = Banner2()
bitkisel_yag.urlname = "Bitkisel Atık Yag"
bitkisel_yag.whatisit = "Bitkisel atık yağ, bitkisel kökenli ve değişik kullanım amaçlarını içererek kullanılan gıda yağlarıdır. Atık Yönetim Yönetmeliğinde yer alan atık tanımına uygun bitkisel yağlar ile kullanılmış kızartmalık yağları kapsamaktadır. Gıda üretimi ve pişirme sonrası da oluşabilen bu yağlar; aynı zamanda son kullanma tarihi geçen ürünleri de içermektedir."
bitkisel_yag.whyimportant = "Bitkisel atık yağlar, eğer doğru yönetilemezse, çevresel sorunlara yol açabilir. Bitkisel atık yağların lavabo, su kaynakları gibi gibi giderlere dökülmesi son derece tehlike arz etmektedir. Bir litre bitkisel atık yağ yaklaşık olarak bir milyon litre içme suyunu kirletmektedir. Yer üstü kaynaklarında suyun üst yüzeyine yayılarak hava girişini engellemekte; yer altı sularında ise içme suyu potansiyelini düşürmektedir. Toprağa dökülmesi ile birlikte toprak yapısını bozmakta ve suda çözünebilen kirleticiler ile yer altı sularına karışabilmektedir. Yakılması durumunda ise hava kirliliğine sebebiyet verir. "
bitkisel_yag.whereaccurs = "Bitkisel atık yağlar, ilgili sektörlerde gıda üretimi veya pişirme sırasında oluşabilir. "
bitkisel_yag.howunderstand = "Zeytin, ayçiçeği, mısır, pamut gibi yağlı bitkilerden özütlenen ve belirli üretim veya pişirme süreçlerinden sonra tekrar kullanılamayacak durumda bulunan her tür yağ bitkisel atık yağ olarak değerlendirilmektedir. Özellikle hazır gıdaların tüketiminin artması ile birlikte kızartmalık yağ alanında ciddi artışlar olmuştur. Kızartma sırasında yağda viskozite artışı veya renk koyulaşması gibi fiziksel değişimler gözlenmektedir. "
bitkisel_yag.mainname = "BİTKİSEL ATIK YAĞ"
#Biyobozunur Atık 
biyobozunur_atik = Banner2()
biyobozunur_atik.urlname = "Biyobozunur Atık"
biyobozunur_atik.whatisit = "Park, bahçe ve evler ile lokantalar, satış noktaları, gıda üretim ve benzeri tesislerden kaynaklanan oksijenli veya oksijensiz ortamda bozunmaya uğrayabilen atıklardır. "
biyobozunur_atik.whyimportant = "Biyobozunur atıklar sebze-meyve kabukları ve artıkları, ziraat atıkları, arıtma çamurları, alg, hayvan gübreleri gibi bir çok türü bulunmaktadır. Biyobozunur atıklar, atık depolama alanlarında tehlikeli sonuçlara neden olabilmektedir. Depolandıkları alanda belirli bir süre sonunda metan gazı salımı yapmaya başlarlar. Bu doğrultuda ise, belirli basınç altında patlamalara sebebiyet verebilir. Ek olarak, metan gazı, karbondioksitten 20 kat daha güçlü bir sera gazı etkisine sahiptir. Eğer doğru yönetilirse, biyobozunur atıklar kompostlanabilir ve bu sayede atık azaltımı da sağlanmış olunur."
biyobozunur_atik.whereaccurs = "Gıda üretimi, kafe, restoran, evsel kaynaklardan oluşmasının yanı sıra; park ve bahçelerden çıkan atıklar da biyobozunur atık kapsamında değerlendirilmektedir. Ek olarak, atıksu arıtımından kaynaklanan çamurlar da bu kategoriye tabii tutulmaktadır."
biyobozunur_atik.howunderstand = "Biyolojik açıdan doğada tamamen çözünebilen ve zamanla yok olan materyaller biyobozunur atık olarak nitelendirilmektedir. Atığın biyobozunur olup olmadığını anlamak için organik bileşiklerden oluşup oluşmadığına bakılabilir. Petrol bileşeni bulunmaması ve doğada kendiliğinden çözünebilmesi biyobozunur atık olduğu konusunda fikir vermektedir. "
biyobozunur_atik.mainname = "BİYOBOZUNUR ATIK "
#ambalaj atık 
ambalaj_atik = Banner2()
ambalaj_atik.urlname = "Ambalaj Atık"
ambalaj_atik.whatisit = "Ambalaj atıkları, ürünün tüketiciye ulaştırılması sırasında ve ürünün kullanılmasından sonra kullanım ömrü dolmuş atıklara denir.  Ambalaj atıkları; metal, kağıt/karton, plastik, cam vb. olabilir. "
ambalaj_atik.whyimportant = "Ambalar atıkları eğer doğru yönetilmezse, kaynak tüketiminde büyük bir alandan sorumludur. Geri dönüştürülmesi ile birçok kaynaktan tasarruf sağlanabilir. "
ambalaj_atik.whereaccurs = "Bir ürünün muhafaza edilmesi için kullanılan kağıt, cam, metal, plastik veya kompozit malzemeden oluşan materyallere ambalaj denmekte ve kullanım ömrü burada son bulduğunda ise ambalaj atıkları oluşmuş olmaktadır. "
ambalaj_atik.mainname = "AMBALAJ ATIK"
#elektrikli atik 
atik_elektrik = Banner2()
atik_elektrik.urlname = "Atık Elektrikli Elektronik Aletler "
atik_elektrik.whatisit = "Kullanım değeri kalmayan ya da kullanılmaz durumda bulunan hasar görmüş, bozuk, kırık veya tamir edilemez olarak görülen elektrikli ve elektronik aletlerin tümüne atık elektrlikli ve elektronik aletler denilmektedir. "
atik_elektrik.whyimportant = "Atık elektrikli elektronik aletlerin çoğu zararlı maddeler içermesi nedeniyle tehlikeli atıklar kapsamında değerlendirilir. Eğer doğru yönetilemezse, insan sağlığının yanı sıra çevre üzerine de zararlı etkileri bulunmaktadır. "
atik_elektrik.whereaccurs = "“Atığın atık elektrikli elektronik aletler olup olmadığını nasıl anlarım?” başlığının altında yer verilen EEE kategorileri adlı tablodadan herhangi bir eşyanın bulunduğu herhangi bir yer de bu tür atıkların oluşması muhtemeldir."
atik_elektrik.howunderstand = "Atık Elektrikli ve Elektronik Eşyaların Yönetmeliğine göre bahsedilen atık türünün kategorilendirilmesi aşağıdaki tabloda mevcuttur. "
atik_elektrik.mainname = "ATIK ELEKTRİKLİ ELEKTRONİK ALETLER"

