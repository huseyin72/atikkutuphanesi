//sistemi kurdum id ve name arraylarını doldurduktan sonra bu iş tamamdır

const select1 = document.querySelector("#drop1");
const select2 = document.querySelector("#drop2");
const codes = document.querySelector(".codes");

var theUl = document.querySelector(".codeUl");
var select1Array = ["01-Madenler","02-Tarım","03-Ahşap işleme","04-Deri işleme","05-Petrol rafinasyon","06-Anorganil kimyasal işlem","07-Organik kimyasal işlem","08-Boya vernik","09-Fotoğraf endüstrisi","10-Isıl işlemler","11-Metal ve diğer kimyasal işlemler","12-Metal plastik fiziki işlemler","13-Atık yağlar","14-organik çözücüler","15-Atık ambalar ve filtre","16-Diğer atıklar","17-İnşaat atıkları","18-Sağlık sektörü","19-Atık yönetim","20-Belediye atıkları"];
var select2Array = [
    ["01-01 Maden kazılarından kaynaklanan atıklar","01-03 Metalik minerallerin fiziki ve kimyasal olarak işlenmesinden kaynaklanan atıklar","01-04 Metalik olmayan minerallerin fiziki ve kimyasal işlemlerinden kaynaklanan atıklar","01-05 Sondaj Çamurları ve Diğer Sondaj Atıkları"],
    ["02-01 Tarım, Bahçıvanlık, Su Ürünleri Üretimi, Ormancılık, Avcılık ve Balıkçılıktan Kaynaklanan Atıklar","02-02 Et, balık ve diğer hayvansal kökenli gıda maddelerinin hazırlanmasından ve işlenmesinden kaynaklanan atıklar","02-03 Meyve, sebze, tahıl, yenilebilir yağlar, kakao, kahve, çay ve tütünün hazırlanmasından ve işlenmesinden; konserve üretiminden, maya ve maya özütü üretiminden, melas hazırlanması ve fermantasyonundan kaynaklanan atıklar","02-04 Şeker üretiminden kaynaklanan atıklar","02-05 Süt ürünleri endüstrisinden kaynaklanan atıklar","02-06 Unlu mamuller ve şekerleme endüstrisinden kaynaklanan atıklar","02-07 Alkollü ve alkolsüz içeceklerin (kahve, çay ve kakao hariç) üretiminden kaynaklanan atıklar"],
    ["03-01 Ağaç İşlemeden ve Sunta ve Mobilya Üretiminden Kaynaklanan Atıklar","03-02 Ahşap Koruma Atıkları","03-03 Kağıt hamuru, kağıt ve kağıt karton üretim ve işlenmesinden kaynaklanan atıklar"],
    ["04-01 Deri ve Kürk Endüstrisinden Kaynaklanan Atıklar","04-02 Tekstil Endüstrisinden Kaynaklanan Atıklar"],
    ["05-01 Petrol Rafinasyon Atıkları","05-06 Kömürün Pirolitik İşlenmesinden Kaynaklanan Atıklar","06-07 Doğal Gaz Saflaştırma ve Nakliyesinde Oluşan Atıklar"],
    ["06-01 Asitlerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-02 Bazların İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-03 Tuzların ve Çözeltilerinin ve Metalik Oksitlerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-04 06 03 Dışındaki Metal İçeren Atıklar","06-05 İşletme Sahası İçerisindeki Atıksu Arıtımından Kaynaklanan Çamurlar","06-06 Kükürtlü Kimyasallardan, Kükürtleyici Kimyasal İşlemlerinin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-07 Halojenlerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) ve Halojenli Kimyasal İşlemlerden Kaynaklanan Atıklar","06-08 Silikon ve Silikon Türevlerinin imalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-09 Fosforlu Kimyasalların İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) ve Fosforlu Kimyasal  İşlenmesinden Kaynaklanan Atıklar","06-10 Gübre Üretimi ve Azotlu Kimyasalların İşlenmesi ve Azot Kimyasalları İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","06-11 Anorganik Pigmentlerin ve Opaklaştırıcıların İmalatından Kaynaklanan Atıklar","06-13 Başka Bir Şekilde Tanımlanmamış Anorganik Kimyasal İşlemlerden Kaynaklanan Atıklar"],
    ["07-01 Temel Organik Kimyasal Maddelerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","07-02 Plastiklerin, Sentetik Kauçuk ve Yapay Elyafların İmalat, Formülasyon, Tedarik ve Kullanımından İFTK Kaynaklanan Atıklar","07-03 Organik Boyaların ve Pigmentlerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar (06 11 dışındaki)","07-04 Organik Bitki Koruma Ürünlerinin (02 01 08 ve 02 01 09 hariç), Ahşap Koruyucu Olarak Kullanılan Maddelerin ( Ajanlarının) (03 02 Hariç) ve Diğer Biyositlerin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","07-05 İlaçların İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","07-06 Yağ, Gres, Sabun, Deterjan, Dezenfektan ve Kozmetiklerin İmalat, Formülasyon, Tedarik ve Kullanımından İFTK Kaynaklanan Atıklar ","07-07 Başka Bir Şekilde Tanımlanmamış Kimyasal ve Kimyasal Ürünlerinin İmalat, Formülasyon, Tedarik ve Kullanımmdan (İFTK) Kaynaklanan Atıklar"],
    ["08-01 Boya ve Verniğin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) ve Sökülmesinden Kaynaklanan Atıklar","08-02 Diğer Kaplama Maddelerinin (Seramik Kaplama Dahil) İmalat, Formülas on, Tedarik ve Kullanımından İFTK Kaynaklanan Atıklar","08-03 Baskı Mürekkeplerinin İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar","08-04 Yapışkanlar ve Yalıtıcıların İmalat, Formülasyon, Tedarik ve Kullanımından (İFTK) Kaynaklanan Atıklar (Su Geçirmeyen Ürünler Dahil)","08-05 08'de Başka Şekilde Tanımlanmamış Atıklar"],
    ["09-01 Fotoğraf Endüstrisi Atıkları"],
    ["10-01 Enerji Santrallerinden ve Diğer Yakma Tesislerinden Kaynaklanan Atıklar (19 Hariç)","10-02 Demir ve Çelik Endüstrisinden Kaynaklanan Atıklar","10-03 Alüminyum Isıl Metalurjisinden Kaynaklanan Atıklar","10-04 Kurşun Isıl Metalurjisinden Kaynaklanan Atıklar","10-05 Çinko Isıl Metalurjisinden Kaynklanan Atıklar","10-06 Bakır Isıl Metalurjisinden Kaynaklanan Atıklar","10-07 Gümüş, Altın ve Platin Isıl Metalurjisinden Kaynaklanan Atıklar","10-08 Demir Dışı Isıl Metalurjisinden Kaynaklanan Atıklar ","10-09 Demir Döküm İşleminden Kaynaklanan Atıklar","10-10 Demir Dışı Döküm Atıkları","10-11 Cam ve Cam Ürünleri Üretim Atıkları","10-12 Seramik Ürünler, Tuğlalar, Fayanslar ve İnşaat Malzemelerinin Üretiminden Kaynaklanan Atıklar","10-13 Çimento, Kireç ve Alçı ve Bunlardan Yapılan Ürünlerin Üretim Atıkları","10-14 Krematoryum Atıkları"],
    ["11-01 Metal ve Diğer Malzemelerin Kimyasal Yüzey İşlemi ve Kaplanmasından Kaynaklanan Atıklar (Örn: Galvanizleme, Çinko Kaplama, Dekapaj, Asitle Sıyırma, Fosfatlama, Alkalin Degradasyonu, Anotlama)","11-02 Demir Dışındaki Madenlerin Hidrometalurjik İşlenmesinin Atıkları","11-03 Tavlama İşlemleri Çamurları ve Katı Maddeleri","11-05 Sıcak Galvanizleme İşlemleri Atıkları"],
    ["12-01 Metallerin ve Plastiklerin Fiziki ve Mekanik Yüzey İşlemlerinden ve Biçimlendirilmesinden Kaynaklanan Atıklar","12-03 Su ve Buhar Yağ Alma İşlemlerinden Kaynaklanan Atıklar (11 Hariç)"],
    ["13-01 Atık Hidrolik Yağlar","13-02 Atık Motor, Şanzıman ve Yağlama Yağları","13-03 Atık Yalıtım ve Isı iletim Yağları","13-04 Sintine Yağları","13-05 Yağ/Su Ayırıcısı İçerikleri","13-07 Sıvı Yakıtların Atıkları","13-08 Başka bir şekilde tanımlanmamış yağ atıkları",],
    ["14-06 Atık Organik Çözücüler, Soğutucular ve Köpük/AerosoI İtici Gazlar"],
    ["15-01 Ambalaj (Belediyenin Ayrı Toplanmış Ambalaj Atıkları Dahil)","15-02 Emiciler, Filtre Malzemeleri, Temizleme Bezleri ve Koruyucu Giysiler"],
    ["16-01 Çeşitli Taşıma Türlerindeki (İş Makineleri Dahil) Ömrünü Tamamlamış Araçlar ve Ömrünü Tamamlamış Araçların Sökülmesi ile Araç Bakımından (13, 14, 16 06 ve 16 08 hariç) Kaynaklanan Atıklar","16-02 Elektrikli ve Elektronik Ekipman Atıkları","16-03 Standart Dışı Gruplar ve Kullanılmamış Ürünler","16-04 Patlayıcı Atıklar ","16-05 Patlayıcı Atıklar ","16-06 Patlayıcı Atıklar ","16-07 Nakliye Tankı, Depolama Tankı ve Varil Temizleme işlemlerinden Kaynaklanan Atıklar (05 ve 13 hariç)","16-08 Bitik Katalizörler","16-09 Oksitleyici Maddeler","16-10 Saha Dışı Arıtmaya Gönderilecek Sulu Sıvı Atıklar","16-11 Atık Astarlar ve Refraktörler"],
    ["17-01 Beton, Tuğla, Kiremit ve Seramik","17-02 Ahşap, Cam ve Plastik","17-03 Bitümlü Karışımlar, Kömür Katranı ve Katranlı Ürünler ","17-04 Metaller (Alaşımları Dahil)","17-05 Toprak (Kirlenmiş Yerlerde Yapılan Hafriyat Dahil), Taşlar ve Dip Tarama Çamurları ","17-06 Yalıtım Malzemeleri ve Asbest İçeren İnşaat Malzemeleri ","17-08 Alçı Bazlı İnşaat Malzemeleri ","17-09 Diğer İnşaat ve Yıkım Atıkları "],
    ["18-01 İnsanlarda Doğum, Teşhis, Tedavi ya da Hastalık Önleme Çalışmalanndan Kaynaklanan Atıklar","18-02 Hayvanlarla İlgili Araştırma, Teşhis, Tedavi ya da Hastahk Önleme Çalışmalarından Kaynaklanan Atıklar"],
    ["19-01 Atık Yakma veya Piroliz'den Kaynaklanan Atıklar","19-02 Atıkların Fiziki/Kimyasal Arıtımından Kaynaklanan Atıklar (Krom Giderme, Siyanür Giderme, Nötralizasyon Dahil) ","19-03 Stabilize Edilmiş/Katılaştırılmış Atıklar (5)","19-04 Vitrifiye Edilmiş Atık ve Vitrifikasyon İşleminden Kaynaklanan Atıklar","19-05 Katı Atıkların Aerobik Arıtımından Kaynaklanan Atıklar","19-06 Atığın Anaerobik Arıtımından Kaynaklanan Atıklar","19-07 Düzenli Depolama Sahası Sızıntı Suları","19-08 Başka Bir Şekilde Tanımlanmamış Atıksu Arıtma Tesisi Atıkları","19-09 İnsan Tüketimi ve Endüstriyel Kullanım İçin Gereken Suyun Hazırlanmasından Kaynaklanan Atıklar","19-10 Metal İçeren Atıkların Parçalanmasından Kaynaklanan Atıklar","19-11 Yağın Yeniden Üretiminden Kaynaklanan Atıklar","19-12 Başka Bir Şekilde Tanımlanmamış Atıkların Mekanik Arıtımından (Örneğin Ayrıştırılması, Ezilmesi, Sıkıştırılması, Topak Haline Getirilmesi) Kaynaklanan Atıklar","19-13 Toprak ve Yeraltı Suyu Islahından Kaynaklanan Atıklar",],
    ["20-01 Ayrı Toplanan Fraksiyonlar (15 01 Hariç)","20-02 Bahçe ve Park Atıkları (Mezarlık Atıkları Dahil)","20-03 Diğer Belediye Atıkları"]
];
var select3Array =[
    [["234234324","33435345345"],["ikinci elemen"],["üçüncü eleman"]],
    [["oldu bu iş"],["oldu iki"]]
];
var selectId =[
    [["1","2"],["3"],["4"]],
    [["5"],["6"]]

];
console.log(select3Array);
    



    

// option maker 
function optionMaker(array,select){
    array.forEach(function(item,index){
        let newOption = document.createElement("option");
        newOption.value = index;
        newOption.innerText = item;
        select.appendChild(newOption);

    });
}

optionMaker(select1Array,select1);


function changeFunc(index){
    ;
    select1.addEventListener("change",function(){
        
        
        select1Array.forEach(function(item,index1){
            
            
            if(select1.value == index1){
                select2.innerHTML = "";
                
               select2Array[index1].forEach(function(item,index){

                    let newoption2 = document.createElement("option");
                    newoption2.value = index;
                    newoption2.innerText = item;
                    select2.appendChild(newoption2);

                    // when first opened its important
                    theUl.innerHTML = "";
                    select3Array[select1.value][select2.value].forEach(function(element,index){

                        let newLi = document.createElement("li");
                        let newA = document.createElement("a");
                        newA.innerHTML = element;
                        newA.setAttribute("href",`${selectId[select1.value][select2.value][index]}`)
                        newLi.appendChild(newA);
                        
                        theUl.appendChild(newLi);
                        
                    })
            
                    
                    
                    
                


               })
                
                
                

            }
            
            

        });
        
        
    })
   
}
// the last code change in drop down menu
function lastcode(){
   

    
    select2.addEventListener("change",function(){
        theUl.innerHTML = "";
       
        select3Array[select1.value][select2.value].forEach(function(element,index){
            let newLi = document.createElement("li");
            let newA = document.createElement("a");
            newA.innerHTML = element;
            newA.setAttribute("href",`${selectId[select1.value][select2.value][index]}`)
            newLi.appendChild(newA);
            
            theUl.appendChild(newLi);
            
        })

       
    })


}
lastcode();
changeFunc();