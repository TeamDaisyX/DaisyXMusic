# Daisyxmusic (Telegram bot projesi)
# Telif Hakkı (C) 2021 Inukaasith

# Bu program ücretsiz bir yazılımdır: yeniden dağıtabilir ve / veya
# GNU Affero Genel Kamu Lisansı koşulları altında
# Özgür Yazılım Vakfı tarafından yayınlanan
# Lisans veya (sizin tercihinize göre) daha sonraki bir sürüm.

# Bu program faydalı olması umuduyla dağıtılmaktadır,
# HİÇBİR GARANTİ OLMAKSIZIN; zımni garanti bile olmadan
# BELİRLİ BİR AMACA UYGUNLUK veya SATILABİLİRLİK. Bakın
# Daha fazla ayrıntı için GNU Affero Genel Kamu Lisansı.
#
# GNU Affero Genel Kamu Lisansının bir kopyasını almış olmalısınız
# bu programla birlikte. Değilse, <https://www.gnu.org/licenses/> adresine bakın.

 işletim sistemini içe aktar
dan  DaisyXMusic . yapılandırma  içe aktarma  SOURCE_CODE , ASSISTANT_NAME , PROJECT_NAME , SUPPORT_GROUP , UPDATES_CHANNEL
sınıf  Mesajları ():
      START_MSG  =  "** Merhaba 👋 [{}] (tg: // user? İd = {})! ** \ n \ n 🤖 Telegram Grupları ve Kanallarının sesli sohbetlerinde müzik çalmak için oluşturulmuş gelişmiş bir botum. \ n \ n ✅ Daha fazla bilgi için bana / yardıma gönderin. "
      HELP_MSG  = [
        "." ,
f "" "
** Merhaba 👋 { PROJECT_NAME } projesine tekrar hoş geldiniz
⚪️ { PROJECT_NAME } , grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilir
⚪️ Asistan adı >> @ { ASSISTANT_NAME } \ n \ n Talimatlar için İleri'yi tıklayın **
"" " ,

f "" "
** Kurulum **
1) Bot yöneticisi yap (Grup ve cplay kullanıyorsanız kanalda)
2) Sesli sohbet başlatın
3) Bir yönetici tarafından ilk kez [şarkı adını] deneyin / çalın
*) Kullanıcı botu müziğin keyfini çıkarırsa , grubunuza @ { ASSISTANT_NAME } eklemeyin ve yeniden deneyin
** Kanal Müzik Çalma için **
1) Beni kanalınızın yöneticisi yap 
2) Bağlı grupta / userbotjoinchannel gönder
3) Şimdi bağlantılı gruptaki komutları gönderin
** Komutlar **
** = >> Şarkı Çalma 🎧 **
- / play: YouTube müziğini kullanarak şarkı çalın
- / play [yt url]: Verilen yt url'sini oynat
- / play [sesini yanıtla]: Yanıtlanan sesi çal
- / dplay: Şarkıyı deezer ile çal
- / splay: Şarkıyı jio saavn ile çalın
** = >> Oynatma ⏯ **
- / player: Oynatıcının Ayarlar menüsünü açın
- / skip: Geçerli parçayı atlar
- / pause: Parçayı duraklat
- / resume: Duraklatılan parçayı devam ettirir
- / end: Medya oynatmayı durdurur
- / current: Geçerli Çalınan parçayı gösterir
- / playlist: Oynatma listesini gösterir
"" " ,
        
f "" "
** = >> Kanal Müzik Çalma 🛠 **
⚪️ Yalnızca bağlantılı grup yöneticileri için:
- / cplay [şarkı adı] - istediğiniz şarkıyı çalın
- / cdplay [şarkı adı] - deezer aracılığıyla istediğiniz şarkıyı çalın
- / csplay [şarkı adı] - jio saavn aracılığıyla istediğiniz şarkıyı çalın
- / cplaylist - Şimdi çalma listesini göster
- / cccurrent - Şimdi çalan göster
- / cplayer - müzik çalar ayarları panelini aç
- / cpause - şarkı çalmayı duraklatır
- / cresume - şarkı çalmaya devam et
- / cskip - sonraki şarkıyı çal
- / cend - müzik çalmayı durdur
- / userbotjoinchannel - asistanı sohbetinize davet edin
c (/ cplay = / channelplay) yerine kanal da kullanılabilir
⚪️ Bağlantılı grupta oynamayı sevmiyorsanız:
1) Kanal kimliğinizi alın.
2) Başlık ile bir grup oluşturun: Kanal Müziği: kanal_kimliğiniz
3) Tam izinlerle botu Kanal yöneticisi olarak ekleyin
4) @ { ASSISTANT_NAME } kanalına yönetici olarak ekleyin .
5) Grubunuza komutlar göndermeniz yeterlidir.
"" " ,

f "" "
** = >> Daha fazla araç 🧑‍🔧 **
- / admincache: Grubunuzun yönetici bilgilerini günceller. Bot yöneticiyi tanımıyorsa deneyin
- / userbotjoin: @ { ASSISTANT_NAME } Userbot'u sohbetinize davet edin
* Player cmd ve / play, / current ve / playlist dışındaki diğer tüm cmd'ler yalnızca grubun yöneticileri içindir.
"" "
      ]
