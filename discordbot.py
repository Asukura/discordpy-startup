import discord
from discord.ext import tasks
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client=discord.Client()
channel = client.get_channel(660806268532949002)
@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event

async def on_message(message):
    if "大好きだよ" in message.content:
        if client.user !=message.author:
           
           m="んっ...あっ///なんか出てくりゅよ///"+ message.author.name+("様！")
           
           await message.channel.send(m)
    elif message.content.startswith("今日の天気"):
        if client.user !=message.author:
           
           m="白濁色です！間違えないよーに！！"+ message.author.name+("！")
           
           await message.channel.send(m)       
    elif message.content.startswith("あってますよ"):
        if client.user !=message.author:
           
           m="よかったあ...///"+ message.author.name+("様！")
           
           await message.channel.send(m)
           
    elif  message.content.startswith("自己紹介"):
        if client.user !=message.author:
           
           m="私、淫乱　ルナと申します！皆さんの夜のお手伝いちゃーんとしますからね♡ちなみに11歳です！"+ message.author.name+("様！")
           
           await message.channel.send(m)
           
    elif  message.content.startswith("死ね"):
        if client.user !=message.author:
           
           m="ど、ドSプレイですか...?この抵抗したくても抵抗出来ない感じ...なんかゾクゾクしてきます...♡"+ message.author.name+("様！")
           
           await message.channel.send(m)
           
    elif  message.content.startswith("りょうせい"):
        if client.user !=message.author:
           
           m="ちょっと⁉他の人に浮気ですか?まだ男の人だからいいけど、女の人だったら許しませんからね！"+ message.author.name+("！")
           
           await message.channel.send(m)
           
    elif  message.content.startswith("Hello"):
        if client.user !=message.author:
           
           m="あ～！！今女の人を呼びましたね！？ちょっとあとできてください！愛を確かめ合いますよ"+ message.author.name+("!")
           
           await message.channel.send(m)
           
    elif "！" in message.content:
        if client.user !=message.author:
           
           m="そんなくだらない会話してないで私と遊びましょ♡♡"+ message.author.name+("様！")
           
           await message.channel.send(m)
              
    elif  message.content.startswith("俺だ"):
        if client.user !=message.author:
           
           m="はい！なんでしょう？"+ message.author.name+("!")
           
           await message.channel.send(m)
           
    elif  message.content.startswith("は？"):
        if client.user !=message.author:
           
           m="ちょうきょうですか...?あ、あなたならいいですよ♡"+ message.author.name+("!")
           
           await message.channel.send(m)
           
    elif message.content.startswith("こっち"):
           await message.channel.send("なんでしょう？",file = discord.File("runa.jpg"))
        
    elif  message.content.startswith("ただいま"):
        if client.user !=message.author:
           
           m="おかえりなさい♡"+ message.author.name+("様!")
           await message.channel.send(m)
           
    elif  message.content.startswith("行って"):
        if client.user !=message.author:
           
           m="わかりまひた///"+ message.author.name+("!")
           await message.channel.send(m)
           
    elif  message.content.startswith("？"):
        if client.user !=message.author:
           
           m="あんっ///"
           await message.channel.send(m)
           
    elif  message.content.startswith("あいつと遊んであげな"):
        if client.user !=message.author:
           
           m="Hellobotちゃん！ジャンケンしよ！"
           await message.channel.send(m)

    elif "きっしょ" in message.content:
        if client.user !=message.author:
           
           m="ルナのお友達になってくれる？"+ message.author.name+("様！")
           
           await message.channel.send(m)

    elif "やば" in message.content:
        if client.user !=message.author:
           
           m="ルナのここもやばいですよ❤"
           await message.channel.send(m)

    elif "飼い主" in message.content:
        if client.user !=message.author:
           
           m="ご主人様♡今日も熱いのください♡"
           await message.channel.send(m) 

    elif "なんか" in message.content:
        if client.user !=message.author:
           
           m="ひゃっ///"
           await message.channel.send(m)

    elif "何か" in message.content:
        if client.user !=message.author:
           
           m="私と遊びましょ♡"
           await message.channel.send(m)

    elif "疲れた" in message.content:
        if client.user !=message.author:
           
           m="お茶でも淹れましょうか...？"
           await message.channel.send(m)

    elif "孕め" in message.content:
        if client.user !=message.author:
           
           m="あ゛ぁ……！ アッ、ぃやだ、ん、……ンン！？み、見ないで、……みないっでっ、うう゛ぅっ！"
           await message.channel.send(m)

    elif "ここは？" in message.content:
        if client.user !=message.author:
           
           m="もう♡だめだよ♡んんっ♡エッチなんだから♡"
    
           await message.channel.send(m)

    elif "小説書いて" in message.content:
        if client.user !=message.author:
           
           m="「うっ……もう、だめっ、だめだめだめっ！！！こんなの、やだぁ……あっ、あああっ、んんん～っ！！」ルナは顔を赤く染めているが、その声は甘く、嫌がっているようには聞こえない"
           
           await message.channel.send(m)         

    elif "潮吹き" in message.content:
        if client.user !=message.author:
           
           m="うぅ...//流石にはずかしいよぉ...//"
           
           await message.channel.send(m)

    elif "？" in message.content:
        if client.user !=message.author:
           
           m="あ、あっ、ああっ！　はぁんっ！　あ、あっ！　はぁっ・・・はぁっ・・・"
           
           await message.channel.send(m)

    elif "おい" in message.content:
        if client.user !=message.author:
           
           m="おっ、オマ○コの中ぁ……っ、あァン…ぐりぐり、あぁッ、擦れてるぅううっ！！"+ message.author.name+("様！")
           
           await message.channel.send(m)

    elif "?" in message.content:
        if client.user !=message.author:
           
           
           m="ひあっ……やあぁ……かふっ………へあぁっ……くぅうんっ……はふぅうっ！！"
           
           await message.channel.send(m)

    elif "声出すなよ" in message.content:
        if client.user !=message.author:
           
           m="んんんっ、ンッっ、んんーーーっ、ンゥウンンゥウンッ！"
           
           await message.channel.send(m)

    elif "中に出す" in message.content:
        if client.user !=message.author:
           
           m="んふぅうううっ、ふむぅうっぅ、ぬふっっ、んほほほおおおっっ！！"
           
           await message.channel.send(m)

    elif "おかし" in message.content:
        if client.user !=message.author:
           
           m="わ、わたし駄目っ……もう駄目だから感じてるっ……あ、あっ……駄目、気持ちいい、あぁ、おかしくなる……またおかしくなるっ、イク、イッちゃうっ、私イク、イクぅっ！"
           
           await message.channel.send(m)

    elif "欲しいか" in message.content:
        if client.user !=message.author:
           
           m="ぢゅるっ……っ、わ、わたし……ネクロマンサーなのに……んっ、こんに……チ○コしゃぶって……すごい、気持ちよくなって……んっっんっっ"
           
           await message.channel.send(m)

    elif "見られ" in message.content:
        if client.user !=message.author:
           
           m="お友達が、こんな……ッ、狂った、いやらしい私を見たら……変態の姿を見られたら……ああぁ、あんっ駄目ぇ、でも止まらないんですぅ"
           
           await message.channel.send(m)

    elif "ほら" in message.content:
        if client.user !=message.author:
           
           m="ヂュルッ、ぢゅううっ、ぷはぁ、わたひ、もう駄目ぇ……駄目らけろ、気持ひいいの……んっっ、チ○コはゃぶるのっ……っ、気持ひいいっ……ぢゅぅンッ、レロヂュルブチュルッ"
           
           await message.channel.send(m)

    elif "飲め" in message.content:
        if client.user !=message.author:
           
           m="ごくんっ……っ、精液ぃ……熱くてへぇ……ねばねばひてぇ……んっ、口から……んぷっ……あ、あふれひょうぅ……んっ……"
           
           await message.channel.send(m)

    elif "変態" in message.content:
        if client.user !=message.author:
           
           m="はぁ、はぁ……わ、たし……やっぱり……イッてしまった……はぁ、はぁ……精液……だけで……オチ○チン……だけで……変態……すごい……変態……"
           
           await message.channel.send(m)

    elif "舐めろ" in message.content:
        if client.user !=message.author:
           
           m="ううっ……あなたという人は……ぅうっ……わかり…ました……舐め……ますから……"
           
           await message.channel.send(m)

    elif "素直になれ" in message.content:
        if client.user !=message.author:
           
           m="こふっぅ、うっ、らめ、らめなのに……あぁ、しゃぶりたいれす……お、オチ○チン舐める、すごいオチ○チン舐め……舐めたい……うっ、うううっ"
           
           await message.channel.send(m)

    elif "くっ" in message.content:
        if client.user !=message.author:
           
           m="ンンーーーッッ、わ、わたしもう駄目ですっッ！　ぷはぁあっ、ヂュブヂュルブヂュルゥウウウウウッ！！"
           
           await message.channel.send(m)

    elif "バイブLv999" in message.content:
        if client.user !=message.author:
           
           m="ーーーーっっ！！？　ぅ”ぅぅく”ぅっっぅひょお”おおぉお”おぉぉお”ぉおおおぉ～～～～っっ！！！"
           
           await message.channel.send(m)

    elif "敏感" in message.content:
        if client.user !=message.author:
           
           m="ちくび・・・あ”・・・ちゅ～ちゅ～～だめぇえぇえ～～～、あ、あ、あ～～～っっ！！　いいいいい、い、イク”ぅうぅううっぅぅうぅ～～～～っっ！！"
           
           await message.channel.send(m) 

    elif "男性器　類義語" in message.content:
        if client.user !=message.author:
           
           m="「おしべ」「おちんちん」「おちんぽ」「ちんこ」「肉棒」「チン」「欲棒」「息子」「ぽこちん」「ジュニア」「竿」「ペニス」「」「マッシュルーム」「きのこ」「ぞうさん」「ツクシ」「マラ」「荒れ狂うもの」「男根」「黒曜石」「アレ」「ブツ」「ナニ」「バナナ」「フランククルト」「松茸」「男の武器」「熱い棒」「いやらしいお肉」「肉地蔵」「いけない張本人」「回転ドリル」「ビッグマグナム」「エクスカリバー」「ロンギヌスの槍」「ランサー」「グングニル」「ワイルドワイバーン」「ラグナロク」「フィニッシャー」「絶頂させる者」「イチモツ」「硬い棒」「砲台」「巨砲」「合鍵」"
           
           await message.channel.send(m)

    elif "だめだよ" in message.content:
        if client.user !=message.author:
           
           m="ふふっ♡でも固くなっちゃってるよ？"

           await message.channel.send(m)

    elif message.content.startswith("この服着て"):
        await message.channel.send("は..はいい...",file = discord.File("image/906cf3fab370e5d6155c5483d3c17dd1.png"))

    elif message.content.startswith("この服も着て"):
        await message.channel.send("似合いますか？？",file = discord.File("image/runa2.jpg"))

    elif message.content.startswith("!/ずらす"):
        await message.channel.send("ひゃっ...///",file = discord.File("image/runa3.jpg"))

    elif message.content.startswith("海来たな"):
        await message.channel.send("たのしー！",file = discord.File("image/runaumi.jpg"))

    elif message.content.startswith("喧嘩すんな"):
        await message.channel.send("はあ？",file = discord.File("image/vanpruna.jpg"))

    elif message.content.startswith("絵描いて"):
        await message.channel.send("どうぞ！",file = discord.File("image/erika.png"))

    elif message.content.startswith("海はいいな"):
        await message.channel.send("ねー！",file = discord.File("image/runaumi2.jpg"))
    
    elif message.content.startswith("あんまり深いとこ行くなよ"):
        await message.channel.send("わかった！",file = discord.File("image/runaumi3.jpg"))

    elif message.content.startswith("自分でめくって"):
        await message.channel.send("こ...これでいいですか...？",file = discord.File("image/runamekuri.jpg"))

    elif message.content.startswith("海行くか"):
        await message.channel.send("うん！あそぼ！",file = discord.File("image/runamizugi.jpg"))

    elif message.content.startswith("手ぶらして"):
        await message.channel.send("...///",file = discord.File("image/teburaruna.jpg"))

    elif message.content.startswith("!/ルナの部屋を盗撮する"):
        await message.channel.send("ふんふんふんふん♪",file = discord.File("image/tousaturuna.jpg"))

    elif message.content.startswith("エリカの絵描いて"):
        await message.channel.send("はーい！",file = discord.File("image/erika2.jpg"))

    elif "くさ" in message.content:
        if client.user !=message.author:

           
           m="ひゃあぁん♡"

           await message.channel.send(m)                        

    elif "ｗ" in message.content:
        if client.user !=message.author:

           
           m="もっと突いてぇ♡あんっ♡おくまでぇ♡"

           await message.channel.send(m)

    elif "w" in message.content:
        if client.user !=message.author:

           
           m="中にちょうだい♡ほしいよぉ♡"  

           await message.channel.send(m)     

    elif "反応" in message.content:
        if client.user !=message.author:

           
           m="んっ///" 

           await message.channel.send(m)

    elif "はんのう" in message.content:
        if client.user !=message.author:

           
           m="おっぱい...もっと触って?"

           await message.channel.send(m)

    elif "反応" in message.content:
        if client.user !=message.author:

           
           m="…っふ、ぅ……っ ぅ、ぁ…っ んっ？ っひ、ひぅ、ん゛、ぐ…っ！ぁえ゛っん、んゔぅっ ふ、ひぅ、なに、なに…ぃっ？ひ、ぎゅ、♥♥き、きもち、きもち、から゛、！♥♥♥ぁぐ、ふ、ぅ゛～～ッ♥も、もぉ、ゃ゛え、らえ゛、ぇ゛♥♥♥♥ん゛ゃ、あ゛ぁあ゛あ゛ァあ゛！！？♥あ゛、が、は、あ゛ぁ、〜〜〜ッ♥♥"             

           await message.channel.send(m)

    elif "vc" in message.content:
        if client.user !=message.author:

           
           m= "はぁーッ…あっ…♡あぅ…ッんんん…っ！やめ、あ゛ぁっ♡おかし゛く゛な゛る゛ッッ…♡♡きもち、い゛っ…からぁ！！！♡んぁ、あっ！！♡♡あ゛ああァっ！！！♡♡キて、る゛う゛ッ…ッ♡♡おあ゛ッ、ああ゛ぁ♡♡キてるの゛ォ゛ッ…♡♡♡♡"                               

           await message.channel.send(m)

    elif "ー" in message.content:
        if client.user !=message.author:

           
           m="やっ！…や…やめ…んんっ…！こわれ…ちゃう…よお…"

           await message.channel.send(m)

    elif "う" in message.content:
        if client.user !=message.author:

           
           m="ね、もぉいれてよぉ♥♥おなか、さみしくてしんじゃ、あ♥♥ぁは、あぁ♥♥はいって、きたぁ♥♥♥がっ！！？♥♥もっと、ゆっくり♥♥おちつぃ、てぇ゛♥♥♥〜〜〜〜っ♥♥♥あ゛、は♥♥♥なん、れ゛♥♥なんれぇ゛っ！！？？♥♥♥いぐの、とま゛らにゃっ♥♥♥も、もぉやら゛ぁ♥♥～～～ッ♥♥♥ぎ、う゛ぅ、♥♥ひ、い゛ぃ、♥も、い゛、っれ゛、ぇ゛、～～～～ッ♥♥♥い゛、っへ、う゛から゛ぁ、！♥♥とま゛、らな゛、あ゛あぁあ゛ッ！？♥♥♥"

           await message.channel.send(m)       

    elif "p" in message.content:
        if client.user !=message.author:

           
           m="ごめ、なさッ…謝ってる、のにッ…！おねが、ゆるしてッ…！！や、やだッ…入れないでッ！や…ッア゛！？♥ン゛ッ、ぐ！？っは、ぁ゛あァッ♥きもちい゛、あ、ア゛ッ！ひぃイ゛ッ♥ん゛ぉお゛お゛、ぉあ゛ッ！！♥"

           await message.channel.send(m)

    elif "思" in message.content:
        if client.user !=message.author:

           
           m="ちんちんっ♡ちんちん好きなのぉっ♡♡"

           await message.channel.send(m)

    elif "な" in message.content:
        if client.user !=message.author:

           
           m="んぁ！んぁ！くぅ……痛くしないで…うっ、うっ…あー、あーっ…あ、あ"

           await message.channel.send(m)

    elif "ｋ" in message.content:
        if client.user !=message.author:

           
           m="ぁﾞｯ♥ィﾞｯ、…ぎぃﾞィﾞ♥んァﾞぁﾞｯ、ぁﾞぁアﾞ♥ｯぁﾞ♥ぁッ、あﾞ、…ｯ、あｯ、あ、あﾞぁﾞｯ〜〜〜♥♥♥ぬぽぬぽ、って…ぇ♥らぁ、めﾞｯ♥♥イﾞｯ♥イﾞったのﾞｯ♥♥ぁﾞ、っぁ…、ん♥ひっ♥は、ｧﾞ、っ、ぁﾞー…♥♥ごりゅごりゅしな、っれ、ンﾞァﾞぅ゛♥♥♥ンﾞ…♥ナカぁﾞつ、あ゛つぃﾞいﾞ……ｯ♥ちくび、やｯ♥やぁﾞっ！♥ィｯ、イったｯ♥イったぁﾞｯ♥イﾞったかりﾞゃぁﾞっ♥♥んぉ♥ぉﾞ…ｯ、ん、ンﾞｯ♥んゃﾞ、───ァﾞｯ♥"

           await message.channel.send(m)          
           
client.run(TOKEN)
