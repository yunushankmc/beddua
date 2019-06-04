import discord
from discord.ext import commands
import time
import random

class cmd:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context= True)
    async def beddua(self, ctx):
        liste = [
        "Bok kusasınnn inşallahhh !",
        "Yaprak bokuuu sıçmık rezalet bok meraklısı seniiii , bok içinde boğulasın inşşş !",
        "Bok yiyenin sebisi elin ayağın birbirine girsin gözlerin önüne aksın inşallah !",
        "Götünü silecek bez bulamazsın inşallah",
        "Götünden yiyip ağzından sıçasın inşallahhh !",
        "Bağırsaklarınla sokak çocukları ip atlasın inşallah motorun bozulsun !",
        "Ellerin kötürüm kalsın burnundaki sümük ağzına aksın inşallahhh !",
        "Su içtiğin bardak ağzında kırılsın da bağırsaklarınıa kadar insin cam kırıkları sıçıtığın bokta cam olsun inşallah (YIRTILSIN GÖTÜN)",
        "Oyundayken elektiriklerin gitsin  inşallah !",
        "O mouse kablosu burnundan girsin kulağından çıksin inşallah !!",
        "Karakterini yolda giderken kaybedersin inşallahh !! Püğğğghh",
        "İnşallaahh geberirsinn !",
        "Bok yiyen sidiğini yutasın inşallaahh !",
        "Umutlarına sokak köpekleri işesin inşallaahh !",
        "Hasgulgulbedgulaguleyhabedduasılya GEBER inş !",
        "Ayak tırnakların gözüne batsın inş !",
        "Dilini sıçasın inş !",
        "Bilgisiyarın param parça olur inşallahh !",
        "Ekran kartın yansınn inş !",
        "Ban yersin inş !",
        "Sıçtığın bokta yüzesin inş !",
        "Kafandaki saçlar dökülüp ellerinde kıllar çıkar inşallahhh !",
        "Emin misin ?",
        "Çingenem seni yolsun inşallah !",
        "Ütünün üstüne oturasın inşallahh !",
        "Ayak tırnaklarını tornavidayla deşsinler inşallahh !",
        "Matkap kirpiklerini oysun inşallaahh !",
        "Bilek kemiğin yamulurda attığın her adımda hayattan geri kalırsın inşallahh !",
        "Kazıklı volvoda ya yakalanda canlı canlı kazığa otuttursun seni inşallahhhh !!",
        "Açlıktan geberecek gibi olup tuvaletten su içip Bok yiyesinn inşallaahh !!!!",
        "Açlıktan geberecek gibi olup tuvaletten su içip Bok yiyesinn inşallaahh !!!!",
        "Ellerini soyacakla soysunlar inşallaahh !",
        "Bebek bezi yutasın inşallah !",
        "Komşunun boku ağzına düşsün inşallah !",
        "Bebek ağzına kussun inşallaahh !",
        "Burnuna kancayı takıp seni balıklara yem etsinler inşallaahhh !!",
        "Susssss ellerin gözlerine batsın tırnakların içinde kalsın inşallahh !!",
        "Ses tellerin yırtılsın sesin götünden çıksın inşallah boğulursun !",
        "Son paranı da yolda düşürürsün inşallah !",
        "Görüşmeyi çok istediğin insanla bir daha asla görüşemezsin inşallaahh !!!"]
        await self.client.say(random.choice(liste))
    @commands.command(pass_context= True)
    async def bedduaci(self, ctx):
        await self.client.say("<@254783122527354881> Buranın Bedduacısı")

def setup(client):
    client.add_cog(cmd(client))
